import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('My New Hello World App')
st.write('Hello world!')

df = pd.DataFrame(np.random.randn(15, 3), columns=(["A", "B", "C"]))
my_data_element = st.bar_chart(df)

for tick in range(10):
    time.sleep(1)
    add_df = pd.DataFrame(np.random.randn(1, 3), columns=(["A", "B", "C"]))
    my_data_element.delete_rows(df)
    my_data_element.add_rows(add_df)

st.button("Regenerate")
