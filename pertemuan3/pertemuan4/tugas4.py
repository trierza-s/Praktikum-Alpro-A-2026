# 2 custom exception yang diminta
class NamaError(Exception):
    pass
class UmurError(Exception):
    pass

print("=== REGISTRASI PESERTA SEMINAR ===")

try: 
    while True: # tempatnya input dan validasi nama
        try:
            nama = input("Nama Lengkap: ")
            if len(nama) < 3:
                raise NamaError
            break
        except NamaError:
            print(" [ERROR] Nama Terlalu Pendek!! Minimal 3 karakter.")

    while True: # tempatnya input dan validasi umur
        try:
            umur = int(input("Umur: "))
            if umur < 17 or umur > 60:
                raise UmurError
            break
        except ValueError:
            print(" [ERROR] Umur harus angka.")
        except UmurError:
            print(" [ERROR] Umur tidak masuk syarat (17-60 tahun).")

    while True: # tempatnya iput dan validasi email
        try:
            email = input("Email: ")
            if "@" not in email:
                raise ValueError
            break
        except ValueError:
            print(" [ERROR] Email tidak valid boss, harus mengandung '@'.")
    
    while True: # tempatnya input dan validasi no hp
        try:
            no_hp = input("NO HP: ")
            if not no_hp.isdigit() or len(no_hp) < 10 or len(no_hp) > 13:
                raise ValueError
            break
        except ValueError:
            print(" [ERROR] No HP tidak valid! harus 10-13 angka.")

finally:
    print("Proses input SIAPP")

# Tampilan buat Nama Pesertanya
print("\n=== DATA PESERTA ===")
print("Nama    :", nama)
print("Umur    :", umur)
print("Email   :", email)
print("No HP   :", no_hp)
print("Status  : TERDAFTAR")