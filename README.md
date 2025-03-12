# Air Quality Analysis Dashboard

Dashboard ini dibuat dengan menggunakan Streamlit untuk menganalisis dan membandingkan kualitas udara antara dua area, yaitu Aotizhongxin (urban) dan Changping (suburban), dengan fokus utama pada polutan PM2.5.

## Struktur Proyek

1. Gathering Data: Mengambil data dari Google Drive.
2. Assessing Data: Memeriksa informasi dasar, missing values, dan duplikasi.
3. Cleaning Data: Menangani missing values dan duplikasi, serta menambahkan kolom stasiun.
4. Exploratory Data Analysis (EDA): Visualisasi distribusi PM2.5, perbandingan antar stasiun, dan pola musiman.
5. Dashboard: Menyediakan visualisasi interaktif untuk mendukung analisis.
6. Kesimpulan: Menyajikan ringkasan dari hasil analisis.

## Cara Menjalankan Dashboard

1. Pastikan Python dan Streamlit sudah terinstall:
> pip install streamlit pandas matplotlib seaborn
2. Jalankan aplikasi Streamlit:
>streamlit run air_quality_dashboard.py

## Insight Utama

- **Perbandingan Kualitas Udara**: Aotizhongxin memiliki konsentrasi PM2.5 yang lebih tinggi dibanding Changping.
- **Pola Musiman: Tingkat polusi**: cenderung lebih tinggi pada musim dingin di kedua lokasi.

## File Penting

- air_quality_dashboard.py: Kode utama untuk menjalankan dashboard.
- cleaned_air_quality.csv: Dataset hasil pembersihan.
