# Welcome to ETL Project - Extract, Transform, Load

(https://pinnsg.com/wp-content/uploads/bb-plugin/cache/etl-img-768x512-circle.jpg)

## Introduction

This project aims to develop an ETL (Extract, Transform, Load) tool in Python, providing a flexible solution for extracting, transforming, and loading data from various sources. The tool is designed to be modular, declaratively drivable, and usable from the command line. It can also be integrated as a module into third-party applications.

## Virtual Environment

It is highly recommended to use a virtual environment to isolate the project dependencies. To create and activate a virtual environment, use the following commands:

For Windows:

     python -m venv venv
     venv\Scripts\activate

For Mac/Linux:

    python3 -m venv venv
    source venv/bin/activate 

## Installing Dependencies

Once the virtual environment is activated, install the project dependencies using the following commands:

    pip install pandas
    pip install sqlalchemy
    pip install lxml

## Running the Project

To test data conversion, use the `transform.py` script. Specify the input and output file formats with the `--input-format` and `--output-format` options. Here is an example command:

    python transform.py ../in/titanic_50.csv ../out/titanic_50.txt --input-format csv --output-format txt

This command indicates that the CSV file `titanic_50.csv` should be converted to the TXT format with the name `titanic_50.txt`.
