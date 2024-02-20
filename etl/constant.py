from sqlalchemy import create_engine

# Database connection details --Note: Dont do like this in production code
def connection():
    mydb = create_engine("mysql://root:root@localhost/world")
    return mydb

CITY_COL_DICT={
     "ID": "city_id",
     "Name": "city_name",
     "CountryCode": "country_code",
     "District": "city_district",
     "Population": "city_population"
}
COUNTRY_COL_DICT={
     "Code": "country_code",
     "Name": "country_name",
     "Continent": "continent",
     "Region": "region",
     "SurfaceArea": "surface_area",
     "IndepYear": "independence_year",
     "Population": "country_population",
     "LifeExpectancy": "life_expectancy",
     "GNP": "gross_national_product",
     "GNPOld": "old_gross_national_product",
     "LocalName": "local_name",
     "GovernmentForm": "government_form",
     "HeadOfState": "head_of_state",
     "Capital": "capital",
     "Code2": "country_code_2"
}
COUNTRY_LANGUAGE_COL_DICT={
     "CountryCode": "country_code",
     "Language": "language",
     "IsOfficial": "is_official_language",
     "Percentage": "language_percentage"
}