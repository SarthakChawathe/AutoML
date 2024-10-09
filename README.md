# AutoML

AutoML is a user-friendly application designed to streamline the process of machine learning model development. It empowers users to easily upload datasets, perform exploratory data analysis, and automatically train and evaluate various machine learning models without requiring extensive coding knowledge.


## Key Features

1. Dataset Upload: Simple interface for uploading datasets in CSV format.
2. Exploratory Data Analysis: Automatically generates insightful visualizations and statistics to understand data distributions and relationships.
3. Model Training: Leverages PyCaret to set up and compare multiple regression models with a single click.
4. Model Saving: Save the best-performing model for future use.
5. Interactive UI: Built using Streamlit, providing a smooth and responsive user experience.

## Create a virtual environment
```
pip install virtualenv
python3.10 -m venv venv
source venv/bin/activate
```

## Install the necessary dependencies
`pip install -r requirements.txt`

## Run the Streamlit Application
`python -m streamlit run app.py`
