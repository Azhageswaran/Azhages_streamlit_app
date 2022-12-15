import re
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

def get_db():

    with my_cnx.cursor() as my_cur:

        my_cur.execute("Select Database_name from SNOWFLAKE.INFORMATION_SCHEMA.DATABASES;")

        return my_cur.fetchall();



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

my_data_row = get_db()

my_cnx.close()

streamlit.dataframe(my_data_row)



option = streamlit.selectbox(

'select ',

 (my_data_row))

selectval = re.findall(r"'(.*?)'", str(option), re.DOTALL)
streamlit.write(selectval)
query = "select DISTINCT table_schema from SNOWFLAKE.INFORMATION_SCHEMA.TABLE_STORAGE_METRICS where table_catalog = '"+str(selectval[0])+"';"
streamlit.write(query)
# def get_schema(query):
#     with my_cnx.cursor() as my_cur:
#         my_cur.execute(query)

#         return my_cur.fetchall();

# my_cnx1 = snowflake.connector.connect(**streamlit.secrets["snowflake"])

# my_data_row1 = get_db()

# my_cnx1.close()

# streamlit.dataframe(my_data_row1)
