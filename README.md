# AI_PrediksiPekerjaan_Kel2
Diabetes Diagnosis

Daftar Anggota

1. 71210700 Tirsa W Makmara
2. 71210734 Eunike Meilanie
3. 71210784 Icha Patricia N<br>
Penjelasan singkat<br>
Aplikasi Artificial Intelligence (AI) yang kami buat adalah Sistem Rekomendasi Pekerjaan untuk Mahasiswa Informatika UKDW. Aplikasi tersebut menggunakan data primer yang kmai peroleh dari penyebaran g-form. <br>
Eksplorasi data kami visualisasikan dalam bentuk Violin Plot dan Scatter Plot. Selanjutnya, aplikasi diimplementasikan menggunakan Model Klasifikasi dengan algoritma Logistic Regression. Model yang sudah jadi kami evaluasi menggunakan Confusion Matrix. <br>

Eksplorasi Data
4 Parameter/Feature - Input berupa numerik


Profil = Wajib Profil yang dipilih oleh setiap mahasiswa (minimal semester 5) TI UKDW
Nilai = Nilai yang diperoleh pada setiap mata kuliah yang diampu
Skill = Kelebihan atau penunjang untuk profil pilihan
Mata Kuliah = Mata Kuliah
1 Target - Output berupa numerik
Outcome  = 

Modelling
Production System
Adalah langkah-langkah atau prosedur yang digunakan untuk mengimplementasikan sebuah sistem produksi (production system). Sistem produksi adalah sistem yang mengatur aliran kerja dan proses produksi dalam suatu perusahaan atau organisasi.
Dengan algoritma tersebut dihasilkan:

Area Under the Curve (AUC) = mengukur kemampuan prediksi untuk membedakan antara positif dan negatif = 0.818
Classification Accuracy (CA) = mengukur sejauh mana prediksi benar atau tidak = 0.729
F1 Score = mengukur rata-rata antara presisi dan recall = 0.803
Precision = mengukur mana identifikasi positif benar atau belum = 0.752
Confusion Matrix
Model evaluasi ini memberikan gambaran tentang jumlah diagnosis yang benar dan salah. Confusion Matrix mencakup empat metrik evaluasi utama, yaitu:

True Positive (TP) = actual 1, predicted 1 = diabetes dan didiagnosis diabetes = 34
True Negative (TN) = actual 0, predicted 0 = tidak diabetes dan didiagnosis tidak diabetes = 106
False Positive (FP) = actual 0, predicted 1 = tidak diabetes, tetapi didiagnosis diabetes = 17
False Negative (FN) = actual 1, predicted 0 = diabetes, tetapi didiagnosis tidak diabetes = 35
