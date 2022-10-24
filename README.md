# Cegeka Task

Setup and run guide for the Flask application.

## Requirement

Please write a Python Flask application that presents your CV data:

- As a JSON REST API with endpoints GET /personal, GET /experience, GET /education, ...
- As a Flask CLI command that prints the data to the console
The CV data can be hard-coded in the code or read from disk. You do not need to integrate with any database. Please include a README file on how to start the REST API and how to execute the CLI command.

It’s not a problem if you do not manage to get to a working version. Just send us the code you’ve written and describe the issue that is blocking you.

## Setup

### Using Anaconda

Run from the root of this repository:
```
conda env update -f environment.yml
conda active CGK_task
```

### Using pip

Run from the root of this repository:

```
pip install -r requirements.txt
```

## Run

### Flask app

In order to  run the app, use the following command:

```flask run```

The app runs on http://127.0.0.1:5000 by default, and the available
endpoints are listed on the index page.

### CLI commands

In order to print the CV information, use the following CLI commands:

```flask personal``` for personal information.

```flask experience``` for experience information.

```flask education``` for education information.

```flask languages``` for languages information.