from datetime import datetime

def greet(name, usia):
    waktu = datetime.now().strftime("%H:%H:%S")
    return f"Hai, {name}. Usia kamu {usia} tahun! Sekarang pukul {waktu}"