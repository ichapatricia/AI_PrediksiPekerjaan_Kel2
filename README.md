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


Profil = Wajib Profil yang dipilih oleh setiap mahasiswa (minimal semester 5) TI UKDW<br>
Nilai = Nilai yang diperoleh pada setiap mata kuliah yang diampu<br>
Skill = Kelebihan atau penunjang untuk profil pilihan<br>
Mata Kuliah = Mata Kuliah<br>
1 Target - Output berupa numerik<br>
Outcome  = 

Modelling
Production System
Adalah langkah-langkah atau prosedur yang digunakan untuk mengimplementasikan sebuah sistem produksi (production system). Sistem produksi adalah sistem yang mengatur aliran kerja dan proses produksi dalam suatu kerja algoritma, sehingga suatu algoritma nantinya akan menghasilkan output sesuai dengan rules yang ditetapkan.
Dengan algoritma tersebut dihasilkan:

Aturan (rules) yang digunakan sebagai acuan program; 
Jika [Nilai PDAP] dan [Nilai DesEk] dan [NilIai DEA] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang UI Designer. 
Jika [Nilai PDAP] dan [Nilai DesEk] dan [NilIai DEA] dan [Nilai BPM] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang UI Designer. 
Jika [Nilai ML] dan [Nilai JST] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Data Scientist.  
Jika [Nilai IoT] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang IoT Developer.  
Jika [Nilai Abas] dan [Nilai BaDaTer] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Database Administrator.  
Jika [Nilai DW] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Data Warehouse Specialist.  
Jika [Nilai KamBD] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Database Security Analyst.  
Jika [Nilai EN] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Network Administrator.  
Jika [Nilai Cloud] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Cloud Infrastructure Specialist.  
Jika [Nilai PeKamJar] dan [Nilai KamJar] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Network Security Engineer. 
 

Confusion Matrix
Model evaluasi ini memberikan gambaran tentang jumlah diagnosis yang benar dan salah. Confusion Matrix mencakup empat metrik evaluasi utama, yaitu:

True Positive (TP) = actual 1, predicted 1 = diabetes dan didiagnosis diabetes = 34
True Negative (TN) = actual 0, predicted 0 = tidak diabetes dan didiagnosis tidak diabetes = 106
False Positive (FP) = actual 0, predicted 1 = tidak diabetes, tetapi didiagnosis diabetes = 17
False Negative (FN) = actual 1, predicted 0 = diabetes, tetapi didiagnosis tidak diabetes = 35
