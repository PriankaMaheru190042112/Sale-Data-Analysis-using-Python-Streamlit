import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
from query import view_data

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.subheader("Analytics")
st.markdown("##")

result= view_data()
df=pd.DataFrame(result,columns=["Invoice_ID","Branch","City"])
st.dataframe(df)

# st.sidebar.header("Please Filter")
# gender = st.sidebar.multiselect(
#     "Select Gender",
#     option= df["Gender"].unique()
# )

