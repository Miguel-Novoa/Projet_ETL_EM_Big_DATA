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
    pip install requests


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
Open a console in the "etl" folder and enter all the desired commands in the list bellow.

To test the calculation of the median in the project, use the following script. Specify the input file path and format along with the desired field name and "median".

**For example, on Mac:**

    python3 job.py ../in/titanic.csv csv Age median

**And on Windows:**

    python job.py ../in/titanic.csv csv Age median

This command calculate the age median in the `titanic.csv` file and return its value in the console.



To calculate the deviation, use the following script. Specify the input file path and format, the desired field, "deviation", the output path alongside the desired name for the file (do not specify the file format here !) and all the desired outputs formats.

**On Mac:**

    python3 job.py ../in/titanic.csv csv Age deviation ../out/titanic_output csv,json,xml,txt,html

**On Windows:**

    python job.py ../in/titanic.csv csv Age deviation ../out/titanic_output csv,json,xml,txt,html

This command calculate the age deviation in the titanic.csv file, add a column with the deviation value to the dataframe and generate new files containing the new datas in all the requested formats (here : csv, json, xml, txt and html).



To use the segmentDataByMedian method, use the following script. Specify the input file path and format, the desired field, "segmentByMedian", the output path alongside the desired name for the file (do not specify the file format here !) and all the desired outputs formats.

**On Mac:**

    python3 job.py ../in/titanic.csv csv Age segmentByMedian ../out/titanic_output csv,json,xml,txt,html

**On Windows:**

    python job.py ../in/titanic.csv csv Age segmentByMedian ../out/titanic_output csv,json,xml,txt,html

This command launch the segmentDataByMedian method for the age field in the titanic.csv file. This method use the calculateMedian method to get the age median, create a new column to store the groups and assign all the values to groups based on their proximity to the median (groups : 'Below Median', 'Equal To Median' and 'Above Median').



To check empty values and format a json file, use the following script. Specify the input file path and format, "formatJson", the output path alongside the desired name for the file (do not specify the file format here !) and all the desired outputs formats.

**On Mac:**

    python3 job.py ../in/titanic_50_json.json json formatJson ../out/titanic_formatted csv,json,html,xml,txt

**On Windows:**

    python job.py ../in/titanic_50_json.json json formatJson ../out/titanic_formatted csv,json,html,xml,txt

This command check for empty values in the titanic_50_json.json file, then format this file and generate new files with the formatted datas in all the requested formats (here : csv, json, xml, txt and html).



To check empty values and format a csv file, use the following script. Specify the input file path and format, "formatJson", the output path alongside the desired name for the file (do not specify the file format here !) and all the desired outputs formats.

**On Mac:**

    python3 job.py ../in/titanic_50.csv csv formatCsv ../out/titanic_formatted csv,json,html,xml,txt  

**On Windows:**

    python job.py ../in/titanic_50.csv csv formatCsv ../out/titanic_formatted csv,json,html,xml,txt  
   
This command check for empty values in the titanic_50.csv file, then format this file and generate new files with the formatted datas in all the requested formats (here : csv, json, xml, txt and html).



To filter all data by the desired value in the desired field, use the following command. Specify the input file and format, "filterEqual", the desired field, the desired value, the output path alongside the desired name for the file (do not specify the file format here !) and all the desired outputs formats.

**On Mac:**

    python3 job.py ../in/titanic_50.csv csv filterEqual Survived 0 ../out/titanic_formatted csv,json,html,xml,txt 

**On Windows:**

    python job.py ../in/titanic_50.csv csv filterEqual Survived 0 ../out/titanic_formatted csv,json,html,xml,txt

This command filters all data for which the survived field value is 0 in the titanic_50.csv file and generate new files with the filtered data in all the requested formats (here : csv, json, xml, txt and html).



To filter all data above the desired value in the desired field use the following command. Specify the input file and format, "filterGreater", the desired field, the desired value, the output path alongside the desired name for the file (do not specify the file format here !) and all the desired outputs formats.

**On Mac:**

    python3 job.py ../in/titanic_50.csv csv filterGreater Age 18 ../out/titanic_formatted csv,json,html,xml,txt 

**On Windows:**

    python job.py ../in/titanic_50.csv csv filterGreater Age 18 ../out/titanic_formatted csv,json,html,xml,txt 

This command filters all data for which the Age field value is greater than 18 in the titanic_50.csv file and generate new files with the filtered data in all the requested formats (here : csv, json, xml, txt and html).



To filter all data above or equal to the desired value in the desired field use the following command. Specify the input file and format, "filterGreaterOrEqual", the desired field, the desired value, the output path alongside the desired name for the file (do not specify the file format here !) and all the desired outputs formats.

**On Mac:**

    python3 job.py ../in/titanic_50.csv csv filterGreaterOrEqual Age 35 ../out/titanic_formatted csv,json,html,xml,txt

**On Windows:**

    python job.py ../in/titanic_50.csv csv filterGreaterOrEqual Age 35 ../out/titanic_formatted csv,json,html,xml,txt

This command filters all data for which the Age field value is greater or equal to 35 in the titanic_50.csv file and generate new files with the filtered data in all the requested formats (here : csv, json, xml, txt and html).



To filter all data bellow the desired value in the desired field use the following command. Specify the input file and format, "filterLess", the desired field, the desired value, the output path alongside the desired name for the file (do not specify the file format here !) and all the desired outputs formats.

**On Mac:**

    python3 job.py ../in/titanic_50.csv csv filterLess Age 20 ../out/titanic_formatted csv,json,html,xml,txt

**On Windows:**

    python job.py ../in/titanic_50.csv csv filterLess Age 20 ../out/titanic_formatted csv,json,html,xml,txt

This command filters all data for which the Age field value is less than 20 in the titanic_50.csv file and generate new files with the filtered data in all the requested formats (here : csv, json, xml, txt and html).



To filter all data bellow or equal to the desired value in the desired field use the following command. Specify the input file and format, "filterLessOrEqual", the desired field, the desired value, the output path alongside the desired name for the file (do not specify the file format here !) and all the desired outputs formats.

**On Mac:**

    python3 job.py ../in/titanic_50.csv csv filterLessOrEqual Age 18 ../out/titanic_formatted csv,json,html,xml,txt

**On Windows:**

    python job.py ../in/titanic_50.csv csv filterLessOrEqual Age 18 ../out/titanic_formatted csv,json,html,xml,txt

This command filters all data for which the Age field value is less or equal to 18 in the titanic_50.csv file and generate new files with the filtered data in all the requested formats (here : csv, json, xml, txt and html).



To filter all data by the desired fields, use the following command. Specify the input file and format, "filterByFields", the desired fields, the desired value, the output path alongside the desired name for the file (do not specify the file format here !) and all the desired outputs formats.

**On Mac:**

    python3 job.py ../in/titanic_50.csv csv filterByFields Age,Survived,Name ../out/titanic_formatted csv,json,html,xml,txt 

**On Windows:**

    python job.py ../in/titanic_50.csv csv filterByFields Age,Survived,Name ../out/titanic_formatted csv,json,html,xml,txt 

This command filters all data in the titanic_50.csv file and generate new files with only the age, survived and name fields datas, in all the requested formats (here : csv, json, xml, txt and html).



**Using an api url instead of a file:**

To use the above commands with an api url instead of a file, use the sames commands but replace the input file path with the api url and replace the input format with "api".

**Example :**

Use of the formatJson command with the one piece api.

    python job.py https://api.api-onepiece.com/v2/hakis/fr api formatJson ../out/onepiece_formatted csv,json,html 