import argparse
import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup


def main(filename: str):
    courses = []
    with open(filename, newline="\n") as f:
        csvreader = csv.DictReader(f, delimiter=";", quotechar='"')
        for row in csvreader:
            courses.append(row)
    df_courses = pd.DataFrame(courses)
    additional_info = []
    for c_id, course in enumerate(df_courses.to_dict(orient='records')):
        html_site = requests.get(course["Link"])
        soup = BeautifulSoup(html_site.text, 'html.parser')
        course_info_title = [el.text for el in soup.find_all(class_="about_training_box_title")]
        course_info_desc = [". ".join([text_val.text for text_val in el.ul.contents]) for el in
                            soup.find_all(class_="about_training_box_description")]
        course_info = dict(zip(course_info_title, course_info_desc))
        course_dict = {"prerequisites": course_info["Wymagania"] if "Wymagania" in course_info else "",
                       "addressedTo": course_info["Dla kogo?"] if "Dla kogo?" in course_info else ""}
        additional_info.append(course_dict)
    joint_df = df_courses.join(pd.DataFrame(additional_info))
    joint_df.to_csv("scrapped_course.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Path to the filename with courses.")
    args = parser.parse_args()
    main(args.filename)
