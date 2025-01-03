from operator import index
import streamlit as st
import plotly.express as px
# from pycaret.regression import setup, compare_models, pull, save_model, load_model
# from pycaret.classification import setup, compare_models, pull, save_model, load_model
# import pandas_profiling
import pandas as pd
# from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport
import os


if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

with st.sidebar: 
    st.image("Artificial-Intelligence-AI-scaled.jpg")
    st.title("AutoML")
    choice = st.radio("Navigation", ["Upload","Profiling","Modelling", "Download"])
    st.info("This project application helps you build and explore your data.")


if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

# if choice == "Profiling": 
#     st.title("Exploratory Data Analysis")
#     if 'df' in globals():
#         profile = ProfileReport(df, explorative=True)
#         profile_html = profile.to_html() 
#         st.components.v1.html(profile_html, height=1000, scrolling=True) 
#     else:
#         st.error("Please upload a dataset first.")

if choice == "Profiling":
    st.title("Exploratory Data Analysis")
    
    if 'df' in globals():
        profile = ProfileReport(df, explorative=True)
        profile_html = profile.to_html() 
        st.components.v1.html(profile_html, height=1000, scrolling=True)
        
        if st.button("Export report as HTML"):
            html_output = "profile_report.html"
            with open(html_output, "w") as f:
                f.write(profile_html)
            
            st.success(f"HTML report saved as {html_output}")
            st.download_button("Download HTML", data=open(html_output, "r").read(), file_name=html_output)
    else:
        st.error("Please upload a dataset first.")

# if choice == "Modelling": 
#     chosen_target = st.selectbox('Choose the Target Column', df.columns)
#     if st.button('Run Modelling'): 
#         setup(df, target=chosen_target)
#         setup_df = pull()
#         st.dataframe(setup_df)
#         best_model = compare_models()
#         compare_df = pull()
#         st.dataframe(compare_df)
#         save_model(best_model, 'best_model')

if choice == "Modelling": 
    st.title("Select the Type of Analysis")
    task_type = st.radio("Choose the type of dataset:", ["Regression", "Classification"])
    
    if 'df' in globals():
        chosen_target = st.selectbox('Choose the Target Column', df.columns)
        
        if st.button('Run Modelling'): 
            if task_type == "Classification":
                from pycaret.classification import setup, compare_models, pull, save_model
                setup(df, target=chosen_target)
            elif task_type == "Regression":
                from pycaret.regression import setup, compare_models, pull, save_model
                setup(df, target=chosen_target)
            
            setup_df = pull()
            st.dataframe(setup_df)
            
            best_model = compare_models()
            compare_df = pull()
            st.dataframe(compare_df)
            
            save_model(best_model, 'best_model')
    else:
        st.error("Please upload a dataset first.")

if choice == "Download": 
    st.title("Download the Best Model")
    with open('best_model.pkl', 'rb') as f: 
        st.download_button('Download Model', f, file_name="best_model.pkl")