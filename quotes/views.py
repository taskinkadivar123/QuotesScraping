import csv
import os
from django.conf import settings
from django.shortcuts import render

def quote_list(request):
    quotes = []

    csv_path = os.path.join(settings.BASE_DIR, "quotes.csv")

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            quotes.append({
                "quote": row["quote"],
                "author": row["author"],
                "tags": row["tags"],
                "author_profile": row["author_profile"],
            })

    return render(request, "quotes/quotes_list.html", {"quotes": quotes})
