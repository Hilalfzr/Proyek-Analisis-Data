import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_air_quality.csv")
    df['date'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    return df

data = load_data()

# Sidebar
st.sidebar.title("Air Quality Analysis")
st.sidebar.write("Analisis Perbandingan Kualitas Udara dan Pola Musiman")
station = st.sidebar.selectbox("Pilih Stasiun", data['station'].unique())
filtered_data = data[data['station'] == station]

# Header
st.title("Dashboard Analisis Kualitas Udara")
st.write("Data PM2.5 di Aotizhongxin dan Changping")

# Overview
st.subheader("Overview Data")
st.write(filtered_data.describe())

# Visualisasi Distribusi PM2.5
st.subheader("Distribusi PM2.5")
fig, ax = plt.subplots()
sns.histplot(filtered_data['PM2.5'].dropna(), kde=True, ax=ax)
st.pyplot(fig)

# Perbandingan PM2.5 Antar Stasiun
st.subheader("Perbandingan PM2.5 Antar Stasiun")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='station', y='PM2.5', data=data, ax=ax)
st.pyplot(fig)

# Pola Musiman
st.subheader("Pola Musiman PM2.5")
avg_monthly = data.groupby(['station', 'month'])['PM2.5'].mean().reset_index()
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='month', y='PM2.5', hue='station', data=avg_monthly, marker='o', ax=ax)
st.pyplot(fig)

# Kesimpulan
st.subheader("Kesimpulan")
st.write(
    "1. Aotizhongxin memiliki tingkat PM2.5 yang lebih tinggi dibanding Changping."
    "\n2. Terdapat pola musiman di mana polusi cenderung meningkat pada musim dingin."
)

st.write("Dibuat oleh Hilal Fazri")
