# https://moran-shemesh-nlp-project-streamlit-app-v9djv3.streamlitapp.com/
# https://www.datacamp.com/tutorial/streamlit

import streamlit as st
import time
from huggingface_hub import from_pretrained_fastai
import gensim
import nltk
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize
# container_main = st.container()
# container_summarization = st.container()
# textRank
def textrank(corpus, ratio=0.2):    
  if type(corpus) is str:        
      corpus = [corpus]    
  summaries = [gensim.summarization.summarize(txt, ratio=ratio) for txt in corpus]    
  return summaries

# @st.cache(allow_output_mutation=True)
# kaggle_dir = f"/content/drive/MyDrive/HIT/NLP/Final_Project/cnn_daily_mail_dataset/kaggle/cnn_dailymail"

# inf_learn = from_pretrained_fastai(repo_id)
long_text = "What is Lorem Ipsum? Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsu"
repo_id = "Aviv/Moran_Aviv_Bart"
inf_learn = from_pretrained_fastai(repo_id)  
summary = inf_learn.blurr_generate([long_text])[0]['generated_texts']  
st.success(summary)


# summary = ""
# st.caption(" © Aviv Lazar & Moran Shemesh")

# with st.spinner('Please wait...'):
#     time.sleep(10)

# container_main.title ("Text Summarization") 
# model_type = container_main.radio('Pick a model',['RankText', 'Bart'])
# user_text = container_main.text_area('Enter or paste text to summarize')

# def start_summarize(long_text, model):
#   num_of_sentences = len(sent_tokenize(long_text))
#   if num_of_sentences > 4:
#     if model=="RankText":
#       summary = textrank(long_text)[0]
#       # if summary=="":
#       # summary = long_text
#     else:
#       if model=="Bart":
#         summary = "Sorry, we don't support Bart here. Please try summarize with Bart at the following link: https://huggingface.co/spaces/Moran/Aviv_Moran_Summarization . For more details aboute the model visit the model's card https://huggingface.co/Aviv/Moran_Aviv_Bart"
# #       streamlit limits are pass while running it, so we will write the code as comments:
# #         repo_id = "Aviv/Moran_Aviv_Bart"
# #         inf_learn = from_pretrained_fastai(repo_id)  
# #         summary = inf_learn.blurr_generate([long_text])[0]['generated_texts']  
#   else:
#     summary = long_text
#   container_summarization.markdown("Summary")
#   container_summarization.success(summary)
#   time.sleep(9)
#   grade = container_summarization.select_slider('What do you think about the summary?', options=['Bad', 'Good', 'Excellent'], value=('Good'))


  
# container_main.button('Summarize', on_click=start_summarize, args=(user_text, model_type, ) )
# ######################
