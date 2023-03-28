import snowflake.connector
import pandas as pd

class SnowflakeConnection:
    def __init__(self, user, password, account, warehouse, database, schema):
        self.user = user
        self.password = password
        self.account = account
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.connection = None

    def connect(self):
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
        except snowflake.connector.errors.Error as e:
            print(f"Error connecting to Snowflake: {e}")
    
    def get_dataframe(self, table_name):
        if not self.connection:
            print("Error: You must connect to Snowflake first")
            return
        
        try:
            query = f"SELECT * FROM {table_name}"
            data = pd.read_sql(query, self.connection)
            return data
        except Exception as e:
            print(f"Error getting data from Snowflake: {e}")
            return None

          #example usage
          conn = SnowflakeConnection(
    user='shreshthaeternal',
    password='Eternal@123',
    account='mvwdvom-zi70301',
    warehouse='COMPUTE_WH',
    database='TEST_DB1',
    schema='MY_SCHEMA'
)

conn.connect()
data = conn.get_dataframe('CUSTOMER_DATA')

if data is not None:
    print(data)
