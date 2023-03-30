import snowflake.connector
import pandas as pd
from pyarxaas import ARXaaS
from pyarxaas.privacy_models import KAnonymity
from pyarxaas import AttributeType
from pyarxaas import Dataset
import time
import pyarxaas
from pyarxaas import ARXaaS
from pyarxaas.hierarchy import IntervalHierarchyBuilder, OrderHierarchyBuilder,RedactionHierarchyBuilder
from pyarxaas import AttributeType
from pyarxaas.privacy_models import KAnonymity
from pyarxaas import Dataset
import pandas as pd
import pandas as pd

def set_hierarchy(data=pd.DataFrame):   
    dataset = Dataset.from_pandas(data)
    arxaas = ARXaaS("http://localhost:8080/")

    Name = pd.read_csv("./hierarchies/namehier.csv")
    Age = pd.read_csv("./hierarchies/agehier.csv")
    Email = pd.read_csv("./hierarchies/emailhier.csv")
    Zipcode = pd.read_csv("./hierarchies/zipcode.csv")
    Amount_spent = pd.read_csv("./hierarchies/amountspend.hier.csv")
    
    dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'AGE', 'ZIPCODE', 'AMOUNT_SPENT')
    dataset.set_attribute_type(AttributeType.INSENSITIVE,'GENDER','NAME','EMAIL')
    
    for column in ['AGE', 'ZIPCODE', 'AMOUNT_SPENT']:
        if column not in data.columns:
            raise ValueError(f"{column} column not found in data")
        elif column == 'AGE':
            dataset.set_hierarchy('AGE', Age)
        elif column == 'ZIPCODE':
            dataset.set_hierarchy('ZIPCODE', Zipcode)
        elif column=="AMOUNT_SPENT":
            dataset.set_hierarchy("AMOUNT_SPENT",Amount_spent)
    
    kanon = KAnonymity(2)
    anonymize_result = arxaas.anonymize(dataset, [kanon])
    anonymized_dataset = anonymize_result.dataset
    anon_dataframe = anonymized_dataset.to_dataframe()

    return anon_dataframe


""" data=pd.read_csv("./customer_data.csv")
anon_data=set_hierarchy(data) """
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
anon=set_hierarchy(data)
print(anon)
anon.to_csv('anonymized_data.csv')


from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine,types
from sqlalchemy.types import Integer, String
from snowflake.sqlalchemy import (  # import Snowflake-specific types
    DOUBLE,
    FLOAT,
    INTEGER,
    NUMBER,
    TEXT,
)

# Set up Snowflake connection
snowflake_user = 'shreshthaeternal'
snowflake_password = 'Eternal@123'
snowflake_account = 'mvwdvom-zi70301'
snowflake_database = 'TEST_DB1'
snowflake_schema = 'MY_SCHEMA'

snowflake_url = URL(
    account=snowflake_account,
    user=snowflake_user,
    password=snowflake_password,
    database=snowflake_database,
    schema=snowflake_schema,
)

engine = create_engine(snowflake_url)

# Name of the Snowflake table to load data into
table_name = 'ANONYMIZED_DATA'
df_name = anon
df_name['AMOUNT_SPENT']=df_name['AMOUNT_SPENT'].astype(str)
df_name['ZIPCODE']=df_name['ZIPCODE'].astype(str)
df_name['AGE']=df_name['AGE'].astype(str)
# Define column types for Snowflake table

with engine.connect() as con:
   
    anon.to_sql(table_name, con=con, if_exists='append', index=False)

""" with engine.connect() as conn:
    # Alter table to change datatype of amount_spent column
    alter_table_query = f"ALTER TABLE {table_name} MODIFY COLUMN amount_spent {column_types['AMOUNT_SPENT','ZIPCODE']}"
    conn.execute(alter_table_query)
    
    # Load data into table
    df_name.to_sql(table_name, con=conn, if_exists='append', index=False, dtype=column_types) """
""" try:
# Load data from Pandas DataFrame to Snowflake table
   with engine.connect() as conn:
       anon.to_sql(table_name, con=conn, if_exists='append', index=False)
except snowflake.connector.errors.Error as e:
    print(f"Error connecting to Snowflake: {e}")
 """
