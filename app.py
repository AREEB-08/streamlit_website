import streamlit as st
import  pandas as pd
import numpy as np
import time

st.title('MY DASHBOARD')
st.header('Hello there in the stramlit ')

st.subheader("WElCOME here in the  website")
st.write("here it is the stram lit ")

st.markdown(
"""
### NOUMAN
## aabid
### faizan
- volleybol
- cricket
"""
)
st.code("""
def number_square(x):
    return x**2
    
sqaure=number(9)
print(square)    
""")

df=pd.DataFrame({
    'name':['mahir',"nouman","aadil"],
    'Package':[23,56,21],
    'MARKS':[89,98,67]
})
st.dataframe(df)
st.latex(r'x^2 + y^2 = 2xy')

st.write("The formula to calculate the distance between two points is:")

st.latex(r'\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}')
st.metric("revenue",'$ 3lak ','-4')

st.header("JSON details is here ")
st.json({
    'name':['mahir',"nouman","aadil"],
    'Package':[23,56,21],
    'MARKS':[89,    98,67]
})


st.image('streamlit_website/images.jpg')

st.video('streamlit_website/p5.mkv')

st.sidebar.title("SIDE BAR PREVIEW")

col1,col2,col3=st.columns(3)

st.sidebar.title("SIDE BAR PREVIEW")


with col1:
    st.image('streamlit_website/20240406_180105.jpg')

with col2:
    st.image('streamlit_website/20240406_180511.jpg')

with col3:
    st.image('streamlit_website/20240407_172749.jpg')

st.error("unable to show")
st.success("congrats  ")



file = st.file_uploader("Enter the CSV file here", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())









email=st.text_input("enter the email ")

age=st.number_input("enter your age ")
date=st.date_input("enter your DOB ")
gender=st.selectbox("SELECT GENDER",['MALE','FEMALE',"OTHERS"])

btn=st.button("Login ")

if btn:
    if email=='mahir@gmail.com' and age==23:
        st.balloons()
        st.write(gender)



# st.write("wait it will take only few seconds")
# bar=st.progress(0)
# for i in range(1,101):
#     time.sleep(0.01)
#     bar.progress(i )