import streamlit as st 
view=[300,200,500]
show_raw = st.checkbox('show raw data')
if show_raw == True :
    st.write('# raw data')
    view
st.write('# raw data')
st.write('# table')
st.table(view) 
st.write('# bar graph')
st.bar_chart(view)