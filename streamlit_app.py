# conda install matplotlib
# https://moran-shemesh-nlp-project-streamlit-app-v9djv3.streamlitapp.com/
import streamlit as st
import time

import pandas as pd

# import matplotlib.pyplot as plt  #fighure out how to use matplotlib
import numpy as np

# kaggle_dir = f"/content/drive/MyDrive/HIT/NLP/Final_Project/cnn_daily_mail_dataset/kaggle/cnn_dailymail"
# dummy_train_df = pd.read_csv('data/validation.csv', nrows=10)
'''
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
st.sidebar.title ("Summ
arization - CNN / Daily Mail")
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

'''
st.subheader('Sir/Mme , YOU need to fill all necessary informations in order    to get a reply to your loan request !')
    st.sidebar.header("Informations about the client :")
    gender_dict = {"Male":1,"Female":2}
    feature_dict = {"No":1,"Yes":2}
    edu={'Graduate':1,'Not Graduate':2}
    prop={'Rural':1,'Urban':2,'Semiurban':3}
    ApplicantIncome=st.sidebar.slider('ApplicantIncome',0,10000,0,)
    CoapplicantIncome=st.sidebar.slider('CoapplicantIncome',0,10000,0,)
    LoanAmount=st.sidebar.slider('LoanAmount in K$',9.0,700.0,200.0)
    Loan_Amount_Term=st.sidebar.selectbox('Loan_Amount_Term',(12.0,36.0,60.0,84.0,120.0,180.0,240.0,300.0,360.0))
    Credit_History=st.sidebar.radio('Credit_History',(0.0,1.0))
    Gender=st.sidebar.radio('Gender',tuple(gender_dict.keys()))
    Married=st.sidebar.radio('Married',tuple(feature_dict.keys()))
    Self_Employed=st.sidebar.radio('Self Employed',tuple(feature_dict.keys()))
    Dependents=st.sidebar.radio('Dependents',options=['0','1' , '2' , '3+'])
    Education=st.sidebar.radio('Education',tuple(edu.keys()))
    Property_Area=st.sidebar.radio('Property_Area',tuple(prop.keys()))


    class_0 , class_3 , class_1,class_2 = 0,0,0,0
    if Dependents == '0':
        class_0 = 1
    elif Dependents == '1':
        class_1 = 1
    elif Dependents == '2' :
        class_2 = 1
    else:
        class_3= 1

    Rural,Urban,Semiurban=0,0,0
    if Property_Area == 'Urban' :
        Urban = 1
    elif Property_Area == 'Semiurban' :
        Semiurban = 1
    else :
        Rural=1
