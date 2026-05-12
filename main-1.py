import streamlit as st

st.title("My 1st Streamlit App")
st.write("Hello, World!")

st.markdown("This is a streamlit app created by Adam Ahmed **the great**.")
st.markdown("if you click this button below, you are smart.")
if st.button("Click me!"):
    st.write("Just kidding u just clicked a button, you are not smart. Also, I may or may not have downlaoded a **virus on your computer**, so be careful. If u want to delete it **click below**")
    if st.button("Delete virus"):
        st.write("**LOL U CLICKED A BUTTON AGAIN LOL. THERE WAS NO VIRUS IN THE FIRST PLACE, I WAS JUST JOKING.**")
        
st.markdown("Made *without* love by Adam Ahmed.")