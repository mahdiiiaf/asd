import streamlit as st

import pickle
st.title("body mody")
st.markdown("reoi pj jfri  i  rf lip sum")

g={"a":[23,5,7],"re":"232"}


h=pickle.load(open("g.pkl","rb"))


st.write(h)