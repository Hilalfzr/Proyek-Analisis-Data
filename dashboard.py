import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive
    
# Load data
@st.cache_data
def load_data():
    drive.mount('/content/drive')
    df = pd.read_csv("/content/drive/MyDrive/DBS/cleaned_air_quality.csv")
    df['date'] = pd.to_datetime(df['datetime'], errors='coerce')
    return df

data = load_data()

# Sidebar - Filter Interaktif
st.sidebar.title("Air Quality Dashboard")
st.sidebar.write("Analisis kualitas udara berdasarkan PM2.5")

station = st.sidebar.selectbox("Pilih Stasiun", data['station'].unique())

min_date = data['date'].min().date()
max_date = data['date'].max().date()
date_range = st.sidebar.date_input("Pilih Rentang Tanggal", [min_date, max_date], min_value=min_date, max_value=max_date)

season_map = {12: "Winter", 1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer", 9: "Fall", 10: "Fall", 11: "Fall"}
data["season"] = data["month"].map(season_map)
selected_season = st.sidebar.multiselect("Pilih Musim", data["season"].dropna().unique(), default=data["season"].dropna().unique())

# Filter data berdasarkan pilihan pengguna
filtered_data = data[(data['station'] == station) & (data['date'].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1]))) & (data["season"].isin(selected_season))]

# Header
st.title("Dashboard Analisis Kualitas Udara")
st.write(f"Menampilkan data PM2.5 untuk **{station}** pada rentang waktu yang dipilih.")

# Overview Data
st.subheader("Ringkasan Data")
st.write(filtered_data.describe())

# Visualisasi Distribusi PM2.5
st.subheader("Distribusi PM2.5")
fig, ax = plt.subplots()
sns.histplot(filtered_data['PM2.5'].dropna(), kde=True, ax=ax)
st.pyplot(fig)

# Perbandingan PM2.5 Antar Stasiun
st.subheader("Perbandingan PM2.5 Antar Stasiun")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(y='PM2.5', data=filtered_data, ax=ax)
st.pyplot(fig)

# Pola Musiman PM2.5
st.subheader("Pola Musiman PM2.5")
avg_monthly = filtered_data.groupby(['month'])['PM2.5'].mean().reset_index()
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='month', y='PM2.5', data=avg_monthly, marker='o', ax=ax)
st.pyplot(fig)

# Kesimpulan
st.subheader("Kesimpulan")
st.write("1. **Aotizhongxin** memiliki tingkat **PM2.5** yang lebih tinggi dibanding **Changping**.")
st.write("2. Terdapat **pola musiman**, di mana polusi cenderung meningkat pada **musim dingin**.")

st.write(" **Dibuat oleh Hilal Fazri**")
