import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
df = pd.read_excel(
    io= 'supermarkt_sales.xlsx',
    engine='openpyxl',
    sheet_name= 'Sales',
    skiprows= 3,
    usecols= 'B:R',
    nrows= 1000,
)

print(df)

# st.dataframe(df)

st.sidebar.header("Filter Here:")
city= st.sidebar.multiselect(
    "Select City:",
    options=df["City"].unique(),
)

customer_type= st.sidebar.multiselect(
    "Select Customer Type:",
    options=df["Customer_type"].unique(),
)

gender= st.sidebar.multiselect(
    "Select Gender:",
    options=df["Gender"].unique(),
)

df_selection= df.query(
    "City == @city & Customer_type == @customer_type & Gender==@gender"
)

# st.dataframe(df_selection)

st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

total_sales= int(df_selection["Total"].sum())
average_rating= round(df_selection["Rating"].mean(),1)
# star_rating= ":star:" * int(round(average_rating,0))
average_sale_by_transaction = round(df_selection["Total"].mean(),2)

left_column, middle_column,right_column= st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US ${total_sales}")

with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} ")

with right_column:
    st.subheader("Average Sales Per Transaction")
    st.subheader(f"US ${average_sale_by_transaction}")

st.markdown("---")

sales_by_product_line= (
    df_selection.groupby(by= ["Product line"]).sum()[["Total"]].sort_values(by="Total")
)

fig_product_sales= px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="Sales by product line",
    color_discrete_sequence=[' #00b140']* len(sales_by_product_line),
    template="plotly_white"

)
st.plotly_chart(fig_product_sales)