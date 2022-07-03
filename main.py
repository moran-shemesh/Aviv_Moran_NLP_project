# The main flow should be here
import streamlit as st
import mymodel as m

st.write("hello world")
window = st.slider("Forecast Window")
st.write(m.run(window=window))
