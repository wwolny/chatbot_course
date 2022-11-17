import json


def read_database(filename, group, attributes):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    _dict = {}
    for attr in attributes:
        name, paths = attr.split(":")
        paths = paths.split(",")
        _dict[name] = [x[paths] for x in data[group]]
    return data


if __name__ == "__main__":
    file = "training-data.json"
    group_name = "Kursy"
    attribute_paths = ["title:title", "price:price", "prerequisites:prerequisites", "durationInDays:durationInDays", "addressedTo:addressedTo"]
    courses = read_database(file, group_name, attribute_paths)
    print(courses["Kursy"][0]["classifiers"]["tags"])

    _output = ",".join(["", "title", "price", "prerequisites", "durationInDays", "addressedTo"])
    for i in range(len(courses["Kursy"])):
        _output += "\n"
        _output += str(i) + courses["Kursy"]["title"]