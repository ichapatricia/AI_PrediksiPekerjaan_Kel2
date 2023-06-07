profil_uiux = {
    "PDAP": "Pola Desain Antarmuka Pengguna",
    "DesEk": "Desain Eksperimental",
    "DEA": "Desain dan Evaluasi Antarmuka",
    "BPM": "Pemodelan Proses Bisnis",
    "TE": "Tes Engineering",
    "ProgAnd": "Pemrograman Perangkat Bergerak berbasis android",
    "ProgIOS": "Pemrograman Perangkat Bergerak Berbasis iOS",
    "ProgHyb": "Pemrograman Perangkat bergerak Berbasis Hybrid",
    "ProgWL": "Pemrograman Web Lanjut"
}

profil_isd = {
    "IoT": "Internet Of Things",
    "ML": "Machine Learning",
    "JST": "Jaringan Syaraf Tiruan",
    "KBS": "Knowledge-Based System",
    "NLP": "Pemrosesan Bahasa Natural",
    "PCD": "Pemrosesan Citra Digital",
    "PSD": "Pemrosesan Sinyal Digital",
    "GamEng": "Game Engine",
    "ProgAnd": "Pemrograman Perangkat Bergerak berbasis android",
    "ProgIOS": "Pemrograman Perangkat Bergerak Berbasis iOS",
    "ProgHyb": "Pemrograman Perangkat bergerak Berbasis Hybrid",
    "ProgWL": "Pemrograman Web Lanjut"
}

profil_db_admin = {
    "Abas": "Administrator Basis Data",
    "DW": "Data Warehouse",
    "BaDaTer": "Basis Data Terdistribusi",
    "KamBD": "Keamanan Basis Data",
    "AbasNoR": "Administrasi Basis Data Non Relasional",
    "ProgAnd": "Pemrograman Perangkat Bergerak berbasis android",
    "ProgIOS": "Pemrograman Perangkat Bergerak Berbasis iOS",
    "ProgHyb": "Pemrograman Perangkat bergerak Berbasis Hybrid",
    "ProgWL": "Pemrograman Web Lanjut"
}

profil_network_supervisor = {
    "EN": "Enterprise Network",
    "Cloud": "Cloud Infrastructure",
    "PeKamJar": "Pengantar Keamanan Jaringan",
    "JarNir": "Jaringan Nir Kabel",
    "OtoJar": "Otomatis Jaringan",
    "TekWAN": "Teknologi WAN",
    "KamJar": "Keamanan Jaringan",
    "IoT": "Internet of Things"
}

def cari_pekerjaan(profil, nilai, skill):
    if profil == "1":
        pekerjaan_uiux = {
            "UI Designer": nilai["PDAP"] >= 80 and nilai["DesEk"] >= 80 and nilai["DEA"] >= 80,
            "UX Designer": nilai["PDAP"] >= 80 and nilai["DesEk"] >= 80 and nilai["DEA"] >= 80 and nilai["BPM"] >= 80
        }
        return [pekerjaan for pekerjaan, sesuai in pekerjaan_uiux.items() if sesuai and skill in ["1", "2"]]
    elif profil == "2":
        pekerjaan_isd = {
            "Data Scientist": nilai["ML"] >= 80 and nilai["JST"] >= 80,
            "IoT Developer": nilai["IoT"] >= 80,
            "AI Engineer": nilai["ML"] >= 80 and nilai["JST"] >= 80 and nilai["KBS"] >= 80
        }
        return [pekerjaan for pekerjaan, sesuai in pekerjaan_isd.items() if sesuai and skill in ["1", "2", "3"]]
    elif profil == "3":
        pekerjaan_db_admin = {
            "Database Administrator": nilai["Abas"] >= 80 and nilai["BaDaTer"] >= 80,
            "Data Warehouse Specialist": nilai["DW"] >= 80,
            "Database Security Analyst": nilai["KamBD"] >= 80
        }
        return [pekerjaan for pekerjaan, sesuai in pekerjaan_db_admin.items() if sesuai and skill in ["1", "2", "3"]]
    elif profil == "4":
        pekerjaan_network_supervisor = {
            "Network Administrator": nilai["EN"] >= 80,
            "Cloud Infrastructure Specialist": nilai["Cloud"] >= 80,
            "Network Security Engineer": nilai["PeKamJar"] >= 80 and nilai["KamJar"] >= 80
        }
        return [pekerjaan for pekerjaan, sesuai in pekerjaan_network_supervisor.items() if sesuai and skill in ["1", "2", "3"]]
    else:
        return []

def pilih_skill(profil):
    if profil == "1":
        print("Pilihan Skill:")
        print("1. UI Designer")
        print("2. UX Designer")
    elif profil == "2":
        print("Pilihan Skill:")
        print("1. Data Scientist")
        print("2. IoT Developer")
        print("3. AI Engineer")
    elif profil == "3":
        print("Pilihan Skill:")
        print("1. Database Administrator")
        print("2. Data Warehouse Specialist")
        print("3. Database Security Analyst")
    elif profil == "4":
        print("Pilihan Skill:")
        print("1. Network Administrator")
        print("2. Cloud Infrastructure Specialist")
        print("3. Network Security Engineer")

print("Selamat datang di Program Pemilihan Pekerjaan berdasarkan Skill dan Nilai")
print("--------------------------------------------------------------")
print("Pilih Profil:")
print("1. UI/UX")
print("2. ISD")
print("3. Database Administrator")
print("4. Network Service Supervisor")

profil_input = input("Masukkan pilihan Profil (1/2/3/4, pisahkan dengan koma jika lebih dari satu): ")
profil_list = profil_input.split(',')

nilai = {}
skill_list = []

for profil in profil_list:
    profil = profil.strip()
    if profil in ["1", "2", "3", "4"]:
        pilih_skill(profil)
        skill_input = input("Masukkan nomor skill yang Anda miliki (pisahkan dengan koma jika lebih dari satu): ")
        skill_list.extend(skill_input.split(','))
        print("Masukkan Nilai untuk setiap Mata Kuliah:")
        if profil == "1":
            for matakuliah, deskripsi in profil_uiux.items():
                nilai[matakuliah] = int(input(deskripsi + ": "))
        elif profil == "2":
            for matakuliah, deskripsi in profil_isd.items():
                nilai[matakuliah] = int(input(deskripsi + ": "))
        elif profil == "3":
            for matakuliah, deskripsi in profil_db_admin.items():
                nilai[matakuliah] = int(input(deskripsi + ": "))
        elif profil == "4":
            for matakuliah, deskripsi in profil_network_supervisor.items():
                nilai[matakuliah] = int(input(deskripsi + ": "))

pekerjaan = []

for i, profil in enumerate(profil_list):
    profil = profil.strip()
    pekerjaan.extend(cari_pekerjaan(profil, nilai, skill_list[i]))

if len(pekerjaan) > 0:
    print("Pekerjaan yang cocok sesuai nilai dan skill:")
    for job in pekerjaan:
        print(job)
else:
    print("Pekerjaan tidak ditemukan.")
