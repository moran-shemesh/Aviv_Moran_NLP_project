# The main flow should be here
import streamlit as st


# kaggle_dir = f"/content/drive/MyDrive/HIT/NLP/Final_Project/cnn_daily_mail_dataset/kaggle/cnn_dailymail"
# dummy_train_df = pd.read_csv('data/validation.csv', nrows=10)

st.title ("Summarization - CNN / Daily Mail")
st.header("Aviv Lazar & Moran Shemesh")
# st.markdown("this is the header")
# st.subheader("this is the subheader")
# st.caption("this is the caption")
# st.code("x=2021")
# st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# input widgets:
# st.checkbox('yes')
st.button('Start')
# st.radio('Pickc a model',[RankText', 'Bart'])
# st.selectbox('Pick your gender',['Male','Female'])
# st.multiselect('choose a model',['RankText', 'Bart'])
st.select_slider("What's your grade?", ['Bad', 'Good', 'Excellent'])
# st.slider('Pick a number', 0,50)


# st.write(dummy_train_df.head(10))


