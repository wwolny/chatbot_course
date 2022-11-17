import json
import pathlib

import streamlit as st
import altair as alt
import pandas as pd


def read_intent_report(path):
    blob = json.loads(path.read_text())
    jsonl = [{**v, 'config': path.parts[1]} for k, v in blob.items() if 'weighted avg' in k]
    # jsonl.append({'accuracy':v, 'config': path.parts[1]} for k,v in blob.items() if 'accuracy' in k)
    return pd.DataFrame(jsonl).drop(columns=['support'])


def read_entity_report(path):
    blob = json.loads(path.read_text())
    jsonl = [{**v, 'config': path.parts[1]} for k, v in blob.items() if 'weighted avg' in k]
    return pd.DataFrame(jsonl).drop(columns=['support'])


def add_zeros(dataf, all_configs):
    for cfg in all_configs:
        if cfg not in list(dataf['config']):
            dataf = pd.concat([dataf, pd.DataFrame({'_precyzja': [0],
                                                    '_czułość': [0],
                                                    'miara-f1': [0],
                                                    'config': cfg})])
    return dataf


def read_pandas(dir_path):
    paths = list(pathlib.Path(dir_path).glob("*/*_report.json"))
    configurations = set([p.parts[1] for p in paths])
    intent_df = pd.concat([read_intent_report(p) for p in paths if 'intent_report' in str(p)])
    paths = list(pathlib.Path(dir_path).glob("*/CRFEntityExtractor_report.json"))
    paths += list(pathlib.Path(dir_path).glob("*/DIETClassifier_report.json"))
    entity_df = pd.concat([read_entity_report(p) for p in paths]).pipe(add_zeros, all_configs=configurations)
    return intent_df, entity_df


st.cache()

intent_df, entity_df = read_pandas("results_updated_test")
intent_df = intent_df.rename(columns={"precision": "_precyzja", "recall": "_czułość", "f1-score": "miara-f1"})
entity_df = entity_df.rename(columns={"precision": "_precyzja", "recall": "_czułość", "f1-score": "miara-f1"})
possible_configs = list(intent_df['config'])

st.markdown("# Porównanie konfiguracji")

st.sidebar.markdown("### Konfiguracje")
selected_config = st.sidebar.multiselect("Wybierze konfiguracje do porównania",
                                         possible_configs,
                                         default=possible_configs)
show_raw_data = st.sidebar.checkbox("Pokaż statystyki")

subset_df = intent_df.loc[lambda d: d['config'].isin(selected_config)].melt('config')

st.markdown("## Podsumowanie wyników intencji")

c = alt.Chart(subset_df).mark_bar().encode(
    y='config:N',
    x='value:Q',
    color='config:N',
    row='variable:N'
)
st.altair_chart(c)

if show_raw_data:
    st.write(intent_df.loc[lambda d: d['config'].isin(selected_config)])

subset_df = entity_df.loc[lambda d: d['config'].isin(selected_config)].melt('config')

st.markdown("## Podsumowanie wyników encji")
c = alt.Chart(subset_df).mark_bar().encode(
    y='config:N',
    x='value:Q',
    color='config:N',
    row='variable:N'
)

st.altair_chart(c)

if show_raw_data:
    st.write(entity_df.loc[lambda d: d['config'].isin(selected_config)])
