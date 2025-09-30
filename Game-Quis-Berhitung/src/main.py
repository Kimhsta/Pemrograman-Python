aktif = True

# Kamus satuan dan puluhan
satuan = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen"
]

puluhan = [
    "", "", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
]

while aktif:
    print("\n=== Game Quis Kelompok 5 ===")
    print("----------------------------")
    print("Cluenya adalah: \"BERHITUNG\"")

    a = input("\nInputkan angka pertama : ")
    b = input("Inputkan angka kedua   : ")

    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)

        if 0 <= a <= 9999 and 0 <= b <= 9999:
            hasil = a + b

            # Ubah hasil ke ejaan
            angka = hasil
            ejaan = ""

            if angka < 20:
                ejaan = satuan[angka]
            elif angka < 100:
                p = angka // 10
                s = angka % 10
                if s == 0:
                    ejaan = puluhan[p]
                else:
                    ejaan = puluhan[p] + " " + satuan[s]
            elif angka < 1000:
                r = angka // 100
                sisa = angka % 100
                if sisa == 0:
                    ejaan = satuan[r] + " hundred"
                else:
                    if sisa < 20:
                        ejaan = satuan[r] + " hundred " + satuan[sisa]
                    else:
                        p = sisa // 10
                        s = sisa % 10
                        if s == 0:
                            ejaan = satuan[r] + " hundred " + puluhan[p]
                        else:
                            ejaan = satuan[r] + " hundred " + puluhan[p] + " " + satuan[s]
            elif angka <= 9999:
                ribu = angka // 1000
                sisa = angka % 1000
                bagian = ""

                if sisa == 0:
                    ejaan = satuan[ribu] + " thousand"
                else:
                    r = sisa // 100
                    sisa2 = sisa % 100

                    if r > 0:
                        bagian = satuan[r] + " hundred"

                    if sisa2 > 0:
                        if sisa2 < 20:
                            if bagian != "":
                                bagian += " " + satuan[sisa2]
                            else:
                                bagian = satuan[sisa2]
                        else:
                            p = sisa2 // 10
                            s = sisa2 % 10
                            if s == 0:
                                if bagian != "":
                                    bagian += " " + puluhan[p]
                                else:
                                    bagian = puluhan[p]
                            else:
                                if bagian != "":
                                    bagian += " " + puluhan[p] + " " + satuan[s]
                                else:
                                    bagian = puluhan[p] + " " + satuan[s]

                    ejaan = satuan[ribu] + " thousand " + bagian

            # Hitung 
            huruf = ""
            for karakter in ejaan:
                if karakter.isalpha():
                    huruf += karakter

            jumlah_huruf = len(huruf)

            # Jawaban
            print(f"\n{a} + {b} = Berapa?")
            jawab = input("Jawaban: ")

            if jawab.isdigit():
                if int(jawab) == jumlah_huruf:
                    print("\n✅  Benar, Good job!")
                else:
                    print("\n❌ Salah, Inget cluenya: 'berhitung' ya dek... 😏")

    lanjut = input("\nLanjut? (y/t): ")
    if lanjut.lower() == "y":
        aktif = True
    else:
        aktif = False
else:
    print("Program Kesel")
