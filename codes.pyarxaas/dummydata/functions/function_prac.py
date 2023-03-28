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


from snowflake.connector.pandas_tools import write_pandas
# Connect to Snowflake
connect = snowflake.connector.connect(
        user='shreshthaeternal',
        password='Eternal@123',
        account='mvwdvom-zi70301',
        warehouse='COMPUTE_WH',
        database='TEST_DB1',
        schema='MY_SCHEMA'
    )

# Define table name and target columns
table_name = 'ANONYMIZED_DATA'
""" target_cols = ['NAME','GENDER','EMAIL','AMOUNT_SPENT','ZIPCODE','AGE']

# Create a cursor object
cur = connect.cursor()

# Execute COPY command to upload data to Snowflake
cur.execute(f"COPY INTO {table_name} ({', '.join(target_cols)}) FROM (SELECT * FROM VALUES {','.join(map(str, anon.to_records(index=False)))})")

# Commit the transaction
connect.commit() """

# Close the cursor and connection objects
""" cur.close() """
database='TEST_DB1'
schema='MY_SCHEMA'

