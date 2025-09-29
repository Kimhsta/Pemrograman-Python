#game Cluenya berputar(arah jarum jam 12 jam)
#ada 2 inputan ditambahkan
# ada lanjut y/t
#jika benar,good job

# Game jam berputar 12 jam

def hitung_jam(a, b):
    total = (a + b) % 12
    return 12 if total == 0 else total

while True:
    print("cluenya berputar")
    a = int(input("Masukkan angka 1: "))
    b = int(input("Masukkan angka 2: "))
    jawab = int(input("Jawaban Anda: "))

    if jawab == hitung_jam(a, b):
        print("Benar, Good job!")
    else:
        print("Salah, jawabannya:", hitung_jam(a, b))

    ulang = input("Lanjut? (y/t): ").lower()
    if ulang != 'y':
        print("Terima kasih sudah main!")
        break