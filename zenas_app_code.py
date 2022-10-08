import streamlit
import pandas
import snowflake.connector

#top heading banner
streamlit.title("Zena's Amazing Athleisure Catalog")

#get the snowflake data
def get_sweats_info():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select COLOR_OR_STYLE from ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")
         return my_cur.fetchall()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_catalog = get_sweats_info()
my_cnx.close()

#create dropdown list
df = pandas.DataFrame(my_catalog)
color_list = df[0].values.tolist()
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

#add caption
product_caption = 'Our warm, comfortable, '+ option +' sweatsuit!
