from bmi_app import bmi
from greet_waktu import greet
from simpan_file import save_last_greet

def main():
    print("=== Program Utama ===")
    nama = input("Masukkan nama: ")
    usia = int(input("Masukkan usia: "))
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (m): "))

    # Panggil greet
    sapaan = greet(nama, usia)
    print(sapaan)

    # Simpan greet ke file
    save_last_greet(sapaan)

    # Hitung BMI
    nilai_bmi, kategori = bmi(berat, tinggi)
    print(f"Nilai BMI kamu: {nilai_bmi:.2f} ({kategori})")

if __name__ == "__main__":
    main()
