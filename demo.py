import streamlit as st


st.title('FIRST PAGE')

st.header('Header')

st.subheader("sub-header")

st.write("This is the first page of streamlit application")

st.markdown("""
# h1
## h2
### h3
   
**HELLO**
*HELLO*

:moon:<br>
:sunglasses:
              """,True) 
st.write("Data","Science","Guvi")
st.write("# Data")

st.write(st)

st.write(sum)

d= {
    'name':'guvi',
    'age':11,
    'place':'chennai'

}
st.write(d)                 