# conda install matplotlib
# https://moran-shemesh-nlp-project-streamlit-app-v9djv3.streamlitapp.com/
# https://www.datacamp.com/tutorial/streamlit
import streamlit as st
import time

import pandas as pd

# import matplotlib.pyplot as plt  #fighure out how to use matplotlib
import numpy as np

# kaggle_dir = f"/content/drive/MyDrive/HIT/NLP/Final_Project/cnn_daily_mail_dataset/kaggle/cnn_dailymail"
# dummy_train_df = pd.read_csv('data/validation.csv', nrows=10)

st.markdown(
     """
     <style>
     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
         width: 450px;
       }
       [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
           width: 500px;
           margin-left: -500px;
        }
        </style>
        """,
        unsafe_allow_html=True)
container = st.container()
st.sidebar.title ("Text Summarization") 
st.sidebar.header("Aviv Lazar & Moran Shemesh")
# st.markdown("this is the header")
# st.subheader("this is the subheader")
# st.caption("this is the caption")
# st.code("x=2021")
# st.latex(r'' a+a r^1+a r^2+a r^3 '')

# input widgets:
# st.checkbox('yes')
st.sidebar.text_area('Enter text to summarize')
st.sidebar.radio('Pick a model',['RankText', 'Bart'])
# st.selectbox('Pick your gender',['Male','Female'])
# st.multiselect('choose a model',['RankText', 'Bart'])
st.sidebar.button('Start')
st.sidebar.select_slider("What do you think about the summarization?", ['Bad', 'Good', 'Excellent'])
# st.slider('Pick a number', 0,50)

# progress bar:
# st.progress(10)
# with st.spinner('Working on it...'):
#     time.sleep(10)

st.sidebar.success("You did it !")
# st.write(dummy_train_df.head(10))

df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.line_chart(df)


# rand=np.random.normal(1, 2, size=20)
# fig, ax = plt.subplots()
# ax.hist(rand, bins=15)
# st.pyplot(fig)

