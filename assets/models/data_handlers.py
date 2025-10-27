import csv
import json
import sqlite3

test = "assets/data/cafe-data.csv"


class DataHandler:
    def __init__(self):
        pass

    def read_csv(self, filepath:str) -> list:
        """Gets data from a CSV file.

        :params str csv_file: a file path to the csv file with the file name.

        :returns list: the row data from the CSV file
        """
        with open(filepath, newline='', encoding='utf-8', mode='r') as file: 
            csv_data = csv.reader(file, delimiter=',')
            data = []
            for row in csv_data:
                data.append(row)
        return data

    def write_csv(self, data:list, filepath:str) -> None:
        """Performs a write operation to a csv file by row.
        
        :params list data: the data in the form of a list for the csv file 
        :params str filepath: the filepath that will store the csvfile to write to.

        """
        with open(filepath, newline='', encoding="utf-8", mode='a') as csv_file:
            form_data = csv.writer(csv_file)
            form_data.writerow(data)


