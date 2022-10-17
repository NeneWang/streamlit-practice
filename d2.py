import streamlit as st
import time

st.write("""
# Introduction
Hello World!
""")

buttonToggled=False

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')