import mysql.connector
from mysql.connector import errors
import pandas as pd
import sys

sys.tracebacklimit = 1

#####################################################################################################
# DB Connection

try:
    connection = mysql.connector.connect(user='oskarsja', password='admin', host='127.0.0.1', database='sys')
    if connection.is_connected():

        #####################################################################################################
        # Fetch Data (Data Frame) from initial table

        read_query = ("SELECT * FROM sys.sys_config")
        df = pd.read_sql(read_query, connection)
        df = pd.DataFrame(df, columns = ['set_time', 'variable'])
        #converted_data = df.to_dict('list') # Convert DataFrame to other type of data

        #####################################################################################################
        # !!!OPTIONAL!!! Fetch Data (Data Frame) from initial table

        # #Check selected data (DATA FRAME)
        # print("Given Dataframe:\n", df)
        # #Check selected data (TABLE)
        # print("\nIterating over rows using iterrows() method:\n")
        # #Iterate through each row and select data
        # for ind, row in df.iterrows():
        #     print (row["set_time"], row["variable"])

        #####################################################################################################
        # Insert Data (Data Frame) to target table
        
        cursor = connection.cursor()
        # Insert DataFrame recrds one by one in to table
        insert_query = "INSERT INTO test.sys_config(laiks, variable) VALUES(%s,%s)"
        for i, row in df.iterrows():
            cursor.execute(insert_query, tuple(row))

        # Connection is not autocommitted by default, so we must commit to save our changes
        connection.commit()
# type: ignore
except errors as e:
     print("Error", e)
finally:
     if connection.is_connected():
        cursor.close()
        connection.close()
        print("SUCCESS. MySQL connection is closed")