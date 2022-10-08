import streamlit
import pandas
import snowflake.connector

#top heading banner
streamlit.title("Zena's Amazing Athleisure Catalog")

#get the snowflake data
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT COLOR_OR_STYLE FROM ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")
my_catalog = my_cur.fetchall()

#create dropdown list
df = pandas.DataFrame(my_catalog)
color_list = df[0].values.tolist()
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

#add caption
product_caption = 'Our warm, comfortable, '+ option +' sweatsuit!'

#use the option to retrieve additional data from snowflake
my_cur.execute("select DIRECT_URL, PRICE, SIZE_LIST, UPSELL_PRODUCT_DESC FROM ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE WHERE COLOR_OR_STYLE = '"+ option +"';")
df2 = my_cur.fetchone()

streamlit.image(
    df2[0],
    width=400,
    caption=product_caption
)
streamlit.write('Price: ', df2[1])
streamlit.write('Sizes Available: ',df2[2])
streamlit.write(df2[3])
