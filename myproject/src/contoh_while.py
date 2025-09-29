aktif = True

while aktif:
    print("Program berjalan baik")
    masukkan = input("Lanjut Test (y/n)? ")
    if (masukkan == "y"):
        aktif = True
    else:
        aktif = False
else:
    print("Program selesai")