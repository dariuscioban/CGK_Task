# Cegeka Task

Setup and run guide for the Flask application.

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