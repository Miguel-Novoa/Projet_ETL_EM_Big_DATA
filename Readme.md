# Welcome to ETL Project - Extract, Transform, Load

![enter image description here](https://pinnsg.com/wp-content/uploads/bb-plugin/cache/etl-img-768x512-circle.jpg)

## Introduction

This project aims to develop an ETL (Extract, Transform, Load) tool in Python, providing a flexible solution for extracting, transforming, and loading data from various sources. The tool is designed to be modular, declaratively drivable, and usable from the command line. It can also be integrated as a module into third-party applications.

## Virtual Environment

It is highly recommended to use a virtual environment to isolate the project dependencies. To create and activate a virtual environment, use the following commands:

**For Windows:**

     python -m venv venv
     venv\Scripts\activate

**For Mac/Linux:**

    python3 -m venv venv
    source venv/bin/activate

## Installing Dependencies

Once the virtual environment is activated, install the project dependencies using the following commands:

    pip install pandas
    pip install sqlalchemy
    pip install lxml
    pip install xml
    pip install lxml beautifulsoup4 sqlalchemy

## Initalize the database

To perform the database creation, you need `mySQL` installed on your computer.

Create an .env file at the root of the project with your mySQL credentials, for example:

```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=password
```

You can run the following command at the root of the project to initialize the database that will store the transformed data :

```
python etl/init_db.py
```

## ## Running the Project

To test the transformation in the project, use the `transform.py` script. Specify the input and output file formats along with the desired transformation types.

**For example, on Mac:**

    python3 transform.py ../in/titanic_50_html.html json,xml,csv html

**And on Windows:**

    python transform.py ../in/titanic_50_html.html json,xml,csv html

This command transforms the `titanic_50_html.html` file into `JSON`, `XML`, and `CSV` formats.

For a more general use case, execute the following command:

**On Mac:**

    python3 transform.py ../in/name_files type(s)_of_files_desired_for_transformation type_of_file_entered

**On Windows:**

    python transform.py ../in/name_files type(s)_of_files_desired_for_transformation type_of_file_entered

This command tests the transformation project on a specified file, transformation types, and the entered file format.
