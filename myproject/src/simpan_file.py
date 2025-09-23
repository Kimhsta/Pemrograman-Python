def save_last_greet(pesan):
    with open("last_greet.txt", "w", encoding="utf-8") as f:
        f.write(pesan)