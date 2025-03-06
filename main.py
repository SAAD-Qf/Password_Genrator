import streamlit as st
import random
import string

def g_p (len, dig, spe) :
    char = string.ascii_letters

    if dig :
        char += string.digits

        if spe :
            char += string.punctuation

    return ''.join(random.choice(char) for _ in range(len))

st.title('Password Generator')

length = st.slider('Password Length', min_value=8, max_value=32 , value=10)

dig = st.checkbox('Include Digits')

spe = st.checkbox('Include Special Characters')

if st.button('Generate Your Password') :
    password = g_p(length, dig, spe)
    st.write(f'Your generated password is: {password}')

    st.write('Build With 🖤 by Saad Qureshi')