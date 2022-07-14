# https://moran-shemesh-nlp-project-streamlit-app-v9djv3.streamlitapp.com/
# https://www.datacamp.com/tutorial/streamlit

import streamlit as st
import time
from huggingface_hub import from_pretrained_fastai
import gensim
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
# textRank
def textrank(corpus, ratio=0.2):    
  if type(corpus) is str:        
      corpus = [corpus]    
  summaries = [gensim.summarization.summarize(txt, ratio=ratio) for txt in corpus]    
  return summaries

# @st.cache(allow_output_mutation=True)
# kaggle_dir = f"/content/drive/MyDrive/HIT/NLP/Final_Project/cnn_daily_mail_dataset/kaggle/cnn_dailymail"

# inf_learn = from_pretrained_fastai(repo_id)


with st.spinner('Please wait...'):
    time.sleep(10)

st.title ("Text Summarization") 
model_type = st.radio('Pick a model',['RankText', 'Bart'])
text = st.text_area('Enter or paste your text')

def start_summarize(long_text, model):
    if model=="RankText":
      summary = textrank(long_text)[0]
      if summary=="":
        summary = long_text
    else:
      if model=="Bart":
        summary = "Sorry, we don't support Bart here. Please try summarize with Bart at the following link: https://huggingface.co/spaces/Moran/Aviv_Moran_Summarization For more details aboute the model visit the model's card https://huggingface.co/Aviv/Moran_Aviv_Bart"
    # repo_id = "Aviv/Moran_Aviv_Bart"
    # inf_learn = from_pretrained_fastai(repo_id)    
    st.success(summary)
    time.sleep(10)
    grade = st.select_slider('What do you think about the summary?', options=['Bad', 'Good', 'Excellent'], value=('Good'))

  
st.button('Summarize', on_click=start_summarize, args=(text, model_type, ) )
# increment = st.button('Increment', on_click=increment_counter,
#     args=(increment_value, ))


# try:
#   print(x)
# except:
#   print("An exception occurred")

#   try run the model one of the next code:
# inf_learn.blurr_generate([text])
# summary = inf_learn.blurr_summarize(text)

# st.title(text)

# st.title(inf_learn.blurr_summarize(text))




st.caption(" © Aviv Lazar & Moran Shemesh")
# url = 'https://drive.google.com/file/d/16XYO5xFM16hXMBshK4orssiTDkhggo98/view?usp=sharing'
# filename = url.split('/')[-1]


# We will not use bart here because loading the model crosses streamlits limit. We get the same error as described here: https://discuss.streamlit.io/t/error-deploying-app-error-checking-streamlit-healthz-connection-refused/9063

