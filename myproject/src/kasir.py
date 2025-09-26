# Dapatkan input untuk tiga harga
harga1 = float(input("Masukkan harga barang 1: "))
harga2 = float(input("Masukkan harga barang 2: "))
harga3 = float(input("Masukkan harga barang 3: "))

# Hitung total belanja
total_belanja = harga1 + harga2 + harga3

# Inisialisasi total akhir
total_akhir = total_belanja

print(f"Total belanja Anda: Rp {total_belanja:,.2f}")

# Periksa apakah total belanja memenuhi syarat untuk diskon
if total_belanja >= 100_000:
    diskon = total_belanja * 0.05
    total_akhir = total_belanja - diskon
    print(f"Anda mendapatkan diskon 5%: Rp {diskon:,.2f}")

# Tampilkan total akhir yang harus dibayar
print(f"Total yang harus dibayar: Rp {total_akhir:,.2f}")
