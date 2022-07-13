# https://moran-shemesh-nlp-project-streamlit-app-v9djv3.streamlitapp.com/
# https://www.datacamp.com/tutorial/streamlit
# /home/appuser/venv/bin/python -m pip install --upgrade pip
# pip install --upgrade -r requirements.txt
import streamlit as st
# import time
import numpy as np
# from transformers import BartForConditionalGeneration
from huggingface_hub import from_pretrained_fastai
from fastai.text.all import *

from blurr.text import *

# model = BartForConditionalGeneration.from_pretrained("Moran/Moran_Aviv_Bart",from_tf=True)

# inf_learn = load_learner(fname='Moran/Moran_Aviv_Bart')
# import torch
# from google.colab import drive
# drive.mount('/content/drive')

# url = ' google drive sharing link'
# path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]


# @st.cache(allow_output_mutation=True)
# kaggle_dir = f"/content/drive/MyDrive/HIT/NLP/Final_Project/cnn_daily_mail_dataset/kaggle/cnn_dailymail"
repo_id = "Aviv/Moran_Aviv_Bart"
inf_learn = from_pretrained_fastai(repo_id)


st.title ("Text Summarization") 
model_type = st.radio('Pick a model',['RankText', 'Bart'])
text = st.text_area('Enter or paste your text')
st.button('Summarize')

# summary = inf_learn.blurr_summarize(text)
# st.title(summary)

st.title(inf_lear_summarize(text))


grade = st.select_slider(
     'What do you think about the summary?',
     options=['Bad', 'Good', 'Excellent'],
     value=('Good'))


st.header(" © Aviv Lazar & Moran Shemesh")
# url = 'https://drive.google.com/file/d/16XYO5xFM16hXMBshK4orssiTDkhggo98/view?usp=sharing'
# filename = url.split('/')[-1]

# urllib.request.urlretrieve(url, filename)


# st.markdown(
#      """
#      <style>
#      [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
#          width: 450px;
#        }
#        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
#            width: 500px;
#            margin-left: -500px;
#         }
#         </style>
  
#         """,
#         unsafe_allow_html=True)
# container = st.container()






# st.markdown("this is the header")
# st.subheader("this is the subheader")
# st.caption("this is the caption")
# st.code("x=2021")
# st.latex(r'' a+a r^1+a r^2+a r^3 '')
# input widgets:
# st.checkbox('yes')

# sidebar:

# st.selectbox('Pick your gender',['Male','Female'])
# st.multiselect('choose a model',['RankText', 'Bart'])


# st.slider('Pick a number', 0,50)

# progress bar:
# st.progress(10)
# with st.spinner('Working on it...'):
#     time.sleep(10)
# grade = st.select_slider("What do you think about the summarization?", ['Bad', 'Good', 'Excellent'])





#st.sidebar.success("You did it !")

# st.write(dummy_train_df.head(10))



# df= pd.DataFrame(
#     np.random.randn(10, 2),
#     columns=['x', 'y'])
# st.line_chart(df)


# st.header(df['article'][0])
# rand=np.random.normal(1, 2, size=20)
# fig, ax = plt.subplots()
# ax.hist(rand, bins=15)
# st.pyplot(fig)

# loaded_model = torch.load(path, 'rb')

# inf_learn = load_learner(fname='ft_cnndm_export.pkl')
# inf_learn.blurr_summarize(test_article)


