#!/usr/bin/python3

import inquirer
import requests
import json
from html.parser import HTMLParser


def main():
    Print("Garbage collection agreement lookup for 'Hadeland og Ringerike Avfallsselskap AS'")
    # search for street
    questions = [inquirer.Text("query", message="Enter search string for street")]
    answers = inquirer.prompt(questions)

    # retrieve suggestions for street
    r = requests.get(
        "https://api.hra.no//search/address", params=answers
    )

    data = json.loads(r.text)
    street_choices = []
    for d in data:
        street_choices.append(d["name"])

    # select street
    questions = [
        inquirer.List("name", choices=street_choices, message="Select address")
    ]
    name = inquirer.prompt(questions).get("name")
    for street in data:
        if street["name"] == name:
            agreement=street["agreementGuid"] 

    print("Copy the following statements into your configuration.yaml:\n")
    print("# waste_collection_schedule source configuration")
    print("waste_collection_schedule:")
    print("  sources:")
    print("    - name: hra_no")
    print("      args:")
    print(f"        name: {name}")
    print(f"        agreement: {agreement}")


if __name__ == "__main__":
    main()
