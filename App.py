import streamlit as st
import pandas as pd
import numpy as np
#import cyborg as cy
#import matplotlib as plt

dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0) )

df_colombia_inversion_original = pd.read_html('https://datosmacro.expansion.com/estado/gasto/colombia')
df_datos = pd.DataFrame(df_colombia_inversion_original[0])

st.write(df_datos)


chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c'])

st.line_chart(chart_data)



map_data=pd.DataFrame(
    np.random.randn(10,2) / [50,50] + [37.76, -122.4],
    columns=['lat','lon'])

st.map(map_data)


map_data=pd.DataFrame(
    np.random.randn(10,2) / [50,50] + [2.2476, 0.99],
    columns=['lat','lon'])

st.map(map_data)




x = st.slider('x')
st.write(x, 'squared is', x * x)