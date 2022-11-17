## interactive_story_1
* query_entities{"entity_type": "course"}
    - slot{"entity_type": "course"}
    - action_query_entities
    - slot{"entity_type": "course"}
    - slot{"listed_items": ["Programowanie .NET - kurs podstawowy", "Analiza danych tekstowych i języka naturalnego", "Korporacyjna Magistrala Usług na przykładzie Apache ServiceMix", "OpenLayers 3 - Tworzenie interaktywnych map na stronach internetowych", "ISTQB Agile Tester"]}
* query_search{"technology": "python"}
    - slot{"technology": "python"}
    - action_query_search
    - slot{"entity_type": "course"}
    - slot{"listed_items": ["Programowanie sieciowe w języku Python", "Wzorce projektowe w języku Python", "Podstawy analizy danych numerycznych w języku Python", "Warsztat analityka danych w języku Python", "Podstawy uczenia maszynowego w języku Python"]}
* query_attribute{"entity_type": "course", "mention": "czwarty", "attribute": "price"}
    - slot{"attribute": "price"}
    - slot{"entity_type": "course"}
    - slot{"mention": "czwarty"}
    - action_query_attribute
    - slot{"mention": null}
    - slot{"course": "Warsztat analityka danych w języku Python"}
* query_attribute{"attribute": "prerequisites"}
    - slot{"attribute": "prerequisites"}
    - action_query_attribute
    - slot{"mention": null}
    - slot{"course": "Warsztat analityka danych w języku Python"}
* query_attribute{"attribute": "durationInDays"}
    - slot{"attribute": "durationInDays"}
    - action_query_attribute
    - slot{"mention": null}
    - slot{"course": "Warsztat analityka danych w języku Python"}
* bye
    - utter_goodbye
