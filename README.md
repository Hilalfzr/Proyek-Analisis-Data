# Air Quality Analysis Dashboard

Dashboard ini dirancang untuk menganalisis perbedaan kualitas udara antara dua area: **Aotizhongxin** dan **Changping**, serta mengidentifikasi pola musiman dari tingkat **PM2.5** di kedua lokasi.

## Prasyarat
Sebelum menjalankan dashboard, pastikan Anda telah menginstal semua dependensi yang dibutuhkan. Anda bisa menginstalnya dengan perintah berikut:

```sh
pip install -r requirements.txt
```

## Menjalankan Dashboard
Untuk menjalankan dashboard dengan **Streamlit**, ikuti langkah-langkah berikut:

1. Pastikan Anda berada di direktori proyek yang berisi file **dashboard.py** dan dataset.
2. Jalankan perintah berikut di terminal:

   ```sh
   streamlit run dashboard.py
   ```

3. Dashboard akan terbuka secara otomatis di browser Anda. Jika tidak terbuka, akses secara manual melalui alamat berikut:

   ```
   http://localhost:8501
   ```

## Struktur Proyek
Struktur direktori proyek adalah sebagai berikut:

```
├── dashboard.py            # File utama untuk menjalankan Streamlit
├── cleaned_air_quality.csv  # Dataset yang telah dibersihkan
├── requirements.txt        # Daftar dependensi yang diperlukan
└── README.md               # Dokumentasi proyek
```

## Insight dari Analisis
Berdasarkan hasil analisis kualitas udara, diperoleh beberapa insight penting:

1. **Perbandingan Kualitas Udara:**
   - **Aotizhongxin** memiliki rata-rata **PM2.5** yang lebih tinggi dibandingkan dengan **Changping**.
   - Kualitas udara di **Aotizhongxin** lebih buruk, yang mungkin dipengaruhi oleh faktor lingkungan dan aktivitas industri.

2. **Pola Musiman:**
   - Tingkat **PM2.5** lebih tinggi di **musim dingin** dibandingkan dengan **musim panas**.
   - Pola ini menunjukkan bahwa faktor cuaca dan musim berperan penting dalam konsentrasi polusi udara.

📊 **Dashboard ini membantu memahami tren kualitas udara dan memberikan wawasan untuk pengambilan keputusan dalam upaya pengurangan polusi udara.**

Selamat menganalisis!
