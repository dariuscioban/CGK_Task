from utils import get_cv_data, format_json_data

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Please access one of the following endpoints: personal, languages, experience, education'

@app.route('/personal')
def personal():
    response = get_cv_data().get('personal', {})
    return response

@app.cli.command('personal')
def personal_cli():
    info = "Personal information:\n"
    info += format_json_data(personal())
    print(info)

@app.route('/languages')
def languages():
    response = get_cv_data().get('languages', {})
    return response

@app.cli.command('languages')
def languages_cli():
    info = "List of known languages:\n"
    info += format_json_data(languages())
    print(info)

@app.route('/experience')
def experience():
    response = get_cv_data().get('experience', {})
    return response

@app.cli.command('experience')
def experience_cli():
    info = "Work experience:\n"
    info += format_json_data(experience())
    print(info)

@app.route('/education')
def education():
    response = get_cv_data().get('education', {})
    return response

@app.cli.command("education")
def education_cli():
    info = 'Education:\n'
    info += format_json_data(education())
    print(info)
