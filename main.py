    
import random
import streamlit as st

st.title("Rock Paper Scissors")

a = random.randint(1, 3)

b = st.selectbox("Choose your move", ["Rock", "Paper", "Scissors"])

if st.button("GO"):
    if a == 1:
        computer = "Rock"
    elif a == 2:
        computer = "Paper"
    else:
        computer = "Scissors"
    
    st.write(f"Computer chose: {computer}")

    if b == computer:
        st.write("Tie!")
    elif (b == "Rock" and computer == "Scissors") or \
         (b == "Paper" and computer == "Rock") or \
         (b == "Scissors" and computer == "Paper"):
        st.write("You win!")
    else:
        st.write("You lose!")