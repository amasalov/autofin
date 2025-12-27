
import json
import csv
import sys


def main():
    print("---telegram json converter to csv for Family Finance channel---")
    # Opening JSON file
    with open("./result.json") as json_file:
        data = json.load(json_file)
    print(data)


main()