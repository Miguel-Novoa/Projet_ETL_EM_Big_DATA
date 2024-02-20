from sqlalchemy import create_engine

# Database connection details --Note: Dont do like this in production code
def connection():
    mydb = create_engine("mysql://root:root@localhost/world")
    return mydb