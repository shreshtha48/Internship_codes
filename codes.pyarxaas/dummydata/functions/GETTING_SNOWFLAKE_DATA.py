#getting the neccesary libraries
import snowflake.connector
import pandas as pd
import numpy as np
# Authenticate with Snowflake
#connecting to the snowflake account using the snowflake connector
try:
    connect = snowflake.connector.connect(
        user='shreshthaeternal',
        password='Eternal@123',
        account='mvwdvom-zi70301',
        warehouse='COMPUTE_WH',
        database='TEST_DB1',
        schema='MY_SCHEMA'
    )
    print("Successfully connected to Snowflake")
except snowflake.connector.errors.Error as e:
    print(f"Error connecting to Snowflake: {e}")

# Get dataframe from a CSV table in Snowflake
csv_table_name = 'CUSTOMER_DATA'
#the dataframe is now ready to be used
data = pd.read_sql(f"SELECT * FROM {csv_table_name}", connect) 
print(data)
from function_prac import set_hierarchy
anon=set_hierarchy(data)


