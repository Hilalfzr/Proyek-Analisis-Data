import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================
# Load Data
# ==========================
@st.cache_data
def load_data():
    data_path = '/mnt/data/cleaned_air_quality.csv'
    df = pd.read_csv(data_path)
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

df = load_data()

# ==========================
# Sidebar
# ==========================
st.sidebar.title('Air Quality Analysis')
station_filter = st.sidebar.multiselect('Select Station', df['station'].unique(), default=df['station'].unique())
filtered_df = df[df['station'].isin(station_filter)]

# ==========================
# Dashboard Title
# ==========================
st.title('Air Quality Dashboard')
st.write('Dashboard to analyze air quality data from Aotizhongxin and Changping stations.')

# ==========================
# Data Overview
# ==========================
st.header('Data Overview')
st.write(filtered_df.describe())

# ==========================
# PM2.5 Distribution
# ==========================
st.header('PM2.5 Distribution')
fig, ax = plt.subplots()
sns.histplot(filtered_df['PM2.5'], kde=True, ax=ax)
st.pyplot(fig)

# ==========================
# Comparison Between Stations
# ==========================
st.header('PM2.5 Comparison Between Stations')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='station', y='PM2.5', data=filtered_df, ax=ax)
st.pyplot(fig)

# ==========================
# Seasonal Pattern
# ==========================
st.header('Seasonal Pattern of PM2.5')
filtered_df['month'] = filtered_df['datetime'].dt.month
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='month', y='PM2.5', hue='station', data=filtered_df, ax=ax)
st.pyplot(fig)

# ==========================
# Conclusion
# ==========================
st.header('Conclusion')
st.write('1. Perbandingan Kualitas Udara: Aotizhongxin memiliki rata-rata PM2.5 lebih tinggi dibanding Changping.')
st.write('2. Pola Musiman: Kedua stasiun menunjukkan tren PM2.5 lebih tinggi di musim dingin dibanding musim panas.')

st.write('Analysis Completed!')
