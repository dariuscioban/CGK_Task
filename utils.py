import os
import json
import sys

from flask import abort


dir_name = os.getcwd()
cv_json_path = "cv.json"

def get_cv_data():
    full_path = os.path.join(dir_name, cv_json_path)
    try:
        with open(full_path) as file:
            json_data = json.load(file)
    except IOError:
        print("File {} not found!".format(full_path))
        if "run" in sys.argv:
            abort(500)
        else:
            exit()
    return json_data

def format_json_data(json_data):
    formatted_data = ""
    if isinstance(json_data, dict):
        for key in json_data.keys():
            formatted_data += "\t" + key.capitalize().replace("_", " ") + \
                              ": " + str(json_data[key]) + "\n"
    elif isinstance(json_data, list):
        for elem in json_data:
            formatted_data += format_json_data(elem) + '\n'
    return formatted_data