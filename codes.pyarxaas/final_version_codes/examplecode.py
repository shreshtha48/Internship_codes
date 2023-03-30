#importing the class to get the data from snowflake
from database_connections import SnowflakeConnector
#creating a connection
connector = SnowflakeConnector(
    user='shreshthaeternal',
    password='Eternal@123',
    account='mvwdvom-zi70301',
    warehouse='COMPUTE_WH',
    database='TEST_DB1',
    schema='MY_SCHEMA'
)

connector.connect()

# Get dataframe from a CSV table in Snowflake
csv_table_name = 'CUSTOMER_DATA'
data = connector.get_dataframe(csv_table_name)
print(data)


from Anonymize_data import Anonymizer

Danonymized_df=Anonymizer.set_hierarchy(data=data)
print(Danonymized_df)