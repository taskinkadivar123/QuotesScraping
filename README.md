Project Workflow:
Step 1: Website Scraping
Quotes are scraped from a quotes website using Python.
Each quote includes:
Quote text
Author name
Tags
Author profile link

Step 2: Store Data in CSV
Scraped data is saved into a CSV file (quotes.csv)
This acts as an intermediate, portable data source.
CSV columns:
quote
author
tags
author_profile

Step 3: Store Data in SQLite
A Django Quote model is created.
SQLite is used as the default Django database.

This step enables:
Structured storage
Future querying
Scalabilit
(Currently optional – CSV is used directly for display)

Step 4: Display Data Using Django
Django reads data from the CSV file.
Data is displayed on a webpage using:
Views
URLs
HTML templates

Create & Activate Virtual Environment
python -m venv .venv
.venv\Scripts\activate

Install Required Packages:
pip install django

Run Django Server:
python manage.py runserver

