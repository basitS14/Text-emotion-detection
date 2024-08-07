import streamlit as st
import pickle

model = pickle.load(open('model.pkl' , 'rb'))

st.title("Emotion Detection")

txt_input = st.text_input(label="Enter Message")

emoji = {
        'neutral':'😐', 
        'joy':'😃',
        'sadness' : '🥲',
        'fear' : '😨', 
        'surprise': '😲',
        'anger':'😠',
        'shame':'😳',
        'disgust':'🤢'

}

if st.button("Predict"):
    result = model.predict([txt_input])

    st.header(emoji[result[0]])