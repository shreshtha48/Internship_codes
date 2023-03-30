#this code has functions to connect to a snowflake database and fetch the data
#importing the neccessary libraries
import snowflake.connector
import pandas as pd
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
#creating a class with functions to help upload the data and upload the anonymized data after connection
class SnowflakeConnector:
    #initializing
    def __init__(self, user, password, account, warehouse, database, schema):
        self.user = user
        self.password = password
        self.account = account
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.connection = None
        self.engine = None
#this function lets you connect to the snowflake table
    def connect(self):
        """Connect to Snowflake"""
        try:
            self.connection = snowflake.connector.connect(
                user=self.user,
                password=self.password,
                account=self.account,
                warehouse=self.warehouse,
                database=self.database,
                schema=self.schema
            )
            print("Successfully connected to Snowflake")
            #exception handling
        except snowflake.connector.errors.Error as e:
            print(f"Error connecting to Snowflake: {e}")
#fetching the data from a snowflake table to anonymize it
    def get_dataframe(self, table_name):
        """Get dataframe from a table in Snowflake"""
        #error handling
        if not self.connection:
            print("Not connected to Snowflake. Please connect first.")
            return None
        try:
            data = pd.read_sql(f"SELECT * FROM {table_name}", self.connection)
            print(f"Successfully fetched data from {table_name}")
            return data
        except snowflake.connector.errors.Error as e:
            print(f"Error fetching data from {table_name}: {e}")
            return None
#code for uploading the anonymized data to snowflake
    def upload_dataframe(self, table_name, df):
        """Upload a dataframe to a table in Snowflake"""
        if not self.engine:
            self.engine = create_engine(self.get_snowflake_url())
        try:
            df.to_sql(table_name, con=self.engine, if_exists='append', index=False)
            print(f"Successfully uploaded data to {table_name}")
        except Exception as e:
            print(f"Error uploading data to {table_name}: {e}")
#building the engine connection for snowflake
    def get_snowflake_url(self):
        """Return the Snowflake URL"""
        return URL(
            account=self.account,
            user=self.user,
            password=self.password,
            database=self.database,
            schema=self.schema,
        )


