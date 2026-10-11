# program python pertama
nama = input ("Masukan nama anda :")
print (f"Halo, {nama} ! Selamat datang di praktikum python")
print ("Semoga sukses")
umur = int(input("Masukkan umur Anda: "))
print(f"Tahun depan umur Anda {umur + 1} tahun.")

import datetime

print("Selamat datang di program Halo!")

# Mengambil tahun saat ini secara otomatis
tahun_sekarang = datetime.datetime.now().year

try:
    # Meminta input dari pengguna dan mengonversinya ke integer
    tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
    
    # Menghitung perkiraan usia
    usia = tahun_sekarang - tahun_lahir
    
    if usia < 0:
        print("Tahun lahir tidak valid (melebihi tahun saat ini).")
    else:
        print(f"Perkiraan usia Anda saat ini adalah {usia} tahun.")

except ValueError:
    # Ditampilkan jika pengguna memasukkan selain angka (seperti teks/huruf)
    print("Error: Harap masukkan tahun lahir dalam bentuk angka/tahun yang valid!")

print("Terima kasih telah menggunakan program ini.")