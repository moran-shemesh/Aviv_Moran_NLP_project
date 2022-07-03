# The main flow should be here

conda install matplotlib

import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

# kaggle_dir = f"/content/drive/MyDrive/HIT/NLP/Final_Project/cnn_daily_mail_dataset/kaggle/cnn_dailymail"
# dummy_train_df = pd.read_csv('data/validation.csv', nrows=10)


container = st.container()

st.sidebar.title ("Summarization - CNN / Daily Mail")
st.sidebar.header("Aviv Lazar & Moran Shemesh")
# st.markdown("this is the header")
# st.subheader("this is the subheader")
# st.caption("this is the caption")
# st.code("x=2021")
# st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# input widgets:
# st.checkbox('yes')
st.sidebar.button('Start')
st.sidebar.radio('Pickc a model',['RankText', 'Bart'])
# st.selectbox('Pick your gender',['Male','Female'])
# st.multiselect('choose a model',['RankText', 'Bart'])
st.sidebar.select_slider("What's your grade?", ['Bad', 'Good', 'Excellent'])
# st.slider('Pick a number', 0,50)

# progress bar:
# st.progress(10)
# with st.spinner('Working on it...'):
#     time.sleep(10)

st.sidebar.success("You did it !")
# st.write(dummy_train_df.head(10))


rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
