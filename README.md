# AI_PrediksiPekerjaan_Kel2
Diabetes Diagnosis

Daftar Anggota

1. 71210700 Tirsa W Makmara
2. 71210734 Eunike Meilanie
3. 71210784 Icha Patricia N<br>

Penjelasan singkat<br>
Aplikasi Artificial Intelligence (AI) yang kami buat adalah Sistem Rekomendasi Pekerjaan untuk Mahasiswa Informatika UKDW. Aplikasi tersebut menggunakan data primer yang kmai peroleh dari penyebaran g-form. <br>
Eksplorasi data kami visualisasikan dalam bentuk Violin Plot dan Scatter Plot. Selanjutnya, aplikasi diimplementasikan menggunakan Model Klasifikasi dengan algoritma Logistic Regression. Model yang sudah jadi kami evaluasi menggunakan Confusion Matrix. <br><br><br>

Eksplorasi Data<br><br>
4 Parameter/Feature - Input berupa numerik
Profil = Wajib Profil yang dipilih oleh setiap mahasiswa (minimal semester 5) TI UKDW<br>
Nilai = Nilai yang diperoleh pada setiap mata kuliah yang diampu<br>
Skill = Kelebihan atau penunjang untuk profil pilihan<br>
Mata Kuliah = Mata Kuliah<br>
1 Target - Output berupa numerik<br>
Outcome  = Pekerjaan berdasarkan nilai dan skill<br><br><br>

Modelling<br><br>
Production System<br>
Adalah langkah-langkah atau prosedur yang digunakan untuk mengimplementasikan sebuah sistem produksi (production system). Sistem produksi adalah sistem yang mengatur aliran kerja dan proses produksi dalam suatu kerja algoritma, sehingga suatu algoritma nantinya akan menghasilkan output sesuai dengan rules yang ditetapkan.
Dengan algoritma tersebut dihasilkan:<br>
Aturan (rules) yang digunakan sebagai acuan program:<br>
Jika [Nilai PDAP] dan [Nilai DesEk] dan [NilIai DEA] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang UI Designer. <br>
Jika [Nilai PDAP] dan [Nilai DesEk] dan [NilIai DEA] dan [Nilai BPM] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang UI Designer. <br>
Jika [Nilai ML] dan [Nilai JST] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Data Scientist.  <br>
Jika [Nilai IoT] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang IoT Developer.  <br>
Jika [Nilai Abas] dan [Nilai BaDaTer] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Database Administrator.  <br>
Jika [Nilai DW] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Data Warehouse Specialist.  <br>
Jika [Nilai KamBD] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Database Security Analyst.  <br>
Jika [Nilai EN] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Network Administrator.  <br>
Jika [Nilai Cloud] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Cloud Infrastructure Specialist.  <br>
Jika [Nilai PeKamJar] dan [Nilai KamJar] memiliki nilai sama dengan atau lebih dari 80, maka user akan disarankan untuk menjadi seorang Network Security Engineer. <br><br><br>
 

Confusion Matrix<br><br>
Model evaluasi ini memberikan gambaran tentang jumlah diagnosis yang benar dan salah. Confusion Matrix mencakup empat metrik evaluasi utama, yaitu:
Cara menggunakan Program :<br>
1. User diminta untuk memasukkan Profil pilihan dengan menginputkan angka 1 sampai 4 dan jika memilih / menginputkan dua pilihan, pisahkan dengan tanda koma (,)<br>
2. User diminta untuk memilih skill yang dimiliki dan memasukkan nomor skill yang, jika memilih lebih dari satu skill maka pisahkan dengan tanda koma (,)<br>
3. User memasukkan nilai dari setiap mata kuliah dengan skala angka 10 sampai 100<br>
4. Program akan memberikan output berupa pekerjaan yang cocok sesuai nilai dan skill<br>
