# Air Quality Analysis Dashboard

Dashboard ini dirancang untuk menganalisis perbedaan kualitas udara antara dua area: Aotizhongxin dan Changping, serta melihat pola musiman dari tingkat PM2.5 di kedua lokasi.

## Prasyarat
Sebelum menjalankan dashboard, pastikan Anda telah menginstal semua dependensi yang dibutuhkan. Anda bisa menginstalnya dengan perintah:

```
pip install -r requirements.txt
```

## Menjalankan Dashboard
Untuk menjalankan dashboard dengan Streamlit, ikuti langkah-langkah berikut:

1. Pastikan Anda berada di direktori proyek yang berisi file dashboard dan dataset.
2. Jalankan perintah berikut di terminal:

```
streamlit run dashboard.py
```

3. Dashboard akan terbuka secara otomatis di browser Anda. Jika tidak terbuka, akses secara manual melalui alamat berikut:

```
http://localhost:8501
```

## Struktur Proyek
```
├── dashboard.py
├── cleaned_air_quality.csv
├── requirements.txt
└── README.md
```

## Insight dari Analisis:
1. **Perbandingan Kualitas Udara:** Aotizhongxin memiliki rata-rata PM2.5 lebih tinggi dibanding Changping.
2. **Pola Musiman:** Kedua stasiun menunjukkan tren PM2.5 lebih tinggi di musim dingin dibanding musim panas.

Selamat menganalisis! 🚀

