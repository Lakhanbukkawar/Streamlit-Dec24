import streamlit as st

st.title("Learning Steamlit!!")
st.header("First streamlit App.")
st.write("learning streamlit for the first time")

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")


genre = st.radio("What's your favorite movie genre?",
                 ["Comedy", "Drama", "Documentary"])


if genre == "Comedy":
    st.write("You are funny.. HaHa.")
elif genre == 'Drama':
    st.write("Dramatic Fellow")
else:
    st.write("Documentary Nice!!")