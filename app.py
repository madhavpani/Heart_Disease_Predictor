# Importing Libraries
import streamlit as st
import tensorflow as tf
import keras
import pandas as pd
import numpy as np

# Loading Model
model = keras.models.load_model('model.keras')

# Creating the Page

# Container for Heading
with st.container():

    # columns for image and title
    img_col, title_col = st.columns([.5,2], vertical_alignment='top')

    # Image Column
    with img_col:
        st.image('Images/logo.png', width=100)

    # Title Column
    with title_col:
        st.write('# :red[Heart🫀 Disease Predictor]')

# Container for About the Project
with st.container():

    # an expander for about project section
    with st.expander('**:blue[WHAT IS THIS ?]**', expanded=True):

        st.write('**:green[Heart🫀 Disease Predictor] is a supervised DL model 👍🏻dignosing👎🏻 :green[Heart🫀 diseases].**')
        st.write('**An Artificial Neural Network (ANN) is working behind the model.**')

# Container for Patients Details
with st.container():

    # Output container
    with st.container(border=False):
        output = st.empty()
 
    # age, sex, cp columns
    age_col, sex_col, cp_col = st.columns(3)
        
    with age_col:
        age = st.text_input('**:blue[AGE]**', placeholder='Enter Age here..')
        if age:
            age = np.int64(age)
        
    with sex_col:
        sex = st.selectbox('**:blue[GENDER]**', options=['Male', 'Female'])
        if sex == 'Male':
            sex = 1
        else: 
            sex = 0
        
    with cp_col:
        cp = st.selectbox('**:blue[CP]**', options=[0,1,2,3,4])
        
    # trestbps, chol, fbs columns
    trestbps_col, chol_col, fbs_col = st.columns(3)

    with trestbps_col:
        trestbps = st.text_input('**:blue[TRESTBPS]**', placeholder='Enter between 94 to 200')
        if trestbps:
            trestbps = np.int64(trestbps)
        
    with chol_col:
        chol = st.text_input('**:blue[CHOL]**', placeholder='Enter between 126 to 564')
        if chol:
            chol = np.int64(chol) 
        
    with fbs_col:
        fbs = st.selectbox('**:blue[FBS]**', options=[True, False])
        if fbs == True:
            fbs = 1
        else:
            fbs = 0

    # restecg, thalach, exang columns
    restecg_col, thalach_col, exang_col = st.columns(3)

    with restecg_col:
        restecg = st.selectbox('**:blue[RESTECG]**', options=[0, 1, 2])

    with thalach_col:
        thalach = st.text_input('**:blue[THALACH]**', placeholder='Enter between 71 to 202')
        if thalach:
            thalach = np.int64(thalach)

    with exang_col:
        exang = st.selectbox('**:blue[EXANG]**', options=['Yes', 'No'])
        if exang == 'Yes':
            exang = 1
        else:
            exang = 0

    # oldpeak, slope, ca columns
    oldpeak_col, slope_col, ca_col = st.columns(3)

    with oldpeak_col:
        oldpeak = st.text_input('**:blue[OLDPEAK]**', placeholder='Enter between 0.1 to 6.2')
        if oldpeak:
            oldpeak = np.float32(oldpeak)

    with slope_col:
        slope = st.selectbox('**:blue[SLOPE]**', options=[1,2,3])

    with ca_col:
        ca = st.selectbox('**:blue[CA]**', options=[0,1,2,3])
        
    # thal column
    thal_col, submit_col = st.columns([1,2])

    with thal_col:
        thal = st.selectbox('**:blue[THAL]**', options=['1','2','fixed', 'normal', 'reversible'])
        
    sample = {
            "age": age, "sex": sex, "cp": cp, "trestbps": trestbps, "chol": chol, "fbs": fbs, "restecg": restecg, "thalach": thalach, "exang": exang, 
            "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal
            }
    if age and trestbps and chol and thalach and oldpeak:
        input_dict = {name: tf.convert_to_tensor([value]) for name, value in sample.items()}
        predictions = model.predict(input_dict)
        output.info(f'**PERCENTAGE OF HEART🫀 DISEASE IS :blue[{100 * predictions[0][0]:.2f} %]**')

# Container for sharing contents
with st.container():
     # five more cols for linking app with other platforms
    youtube_col, hfspace_col, madee_col, repo_col, linkedIn_col = st.columns([1,1.2,1.08,1,1], gap='small')

    # Youtube link
    with youtube_col:
        st.link_button('**VIDEO**', icon=':material/slideshow:', url='https://youtu.be/IDHr9Z4Q4iY', help='YOUTUBE')
    
    # Hugging Face Space link
    with hfspace_col:
        st.link_button('**HF SPACE**', icon=':material/sentiment_satisfied:', url='https://huggingface.co/spaces/madhav-pani/Heart_Disease_Predictor/tree/main', help='HUGGING FACE SPACE')

    # Madee Link
    with madee_col:
        st.button('**MADEE**', icon=':material/flight:', disabled=True, help='MADEE')

    # Repository Link
    with repo_col:
        st.link_button('**REPO**', icon=':material/code_blocks:', url='https://github.com/madhavpani/Heart_Disease_Predictor', help='GITHUB REPOSITORY')

    # LinkedIn link
    with linkedIn_col:
        st.link_button('**CONNECT**', icon=':material/connect_without_contact:', url='https://www.linkedin.com/in/madhavpani', help='LINKEDIN')