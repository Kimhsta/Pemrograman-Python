def bmi(berat_kg, tinggi_m):
    nilai = berat_kg/(tinggi_m**2)
    if nilai < 18.5:
        kategori = "kurus"
        elif nilai < 25:
            kategori = "normal"
            elif nilai < 30:
                kategori = " Berat badan berlebih"
                else:
                    kategori = "Obesitas"
                    return nilai, kategori