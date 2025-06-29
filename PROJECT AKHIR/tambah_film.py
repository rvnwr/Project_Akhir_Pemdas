from fitur_aplikasi import film_lain

def tambah_film():
    daftar = film_lain()  # akses global dictionary
    judul = input("Masukkan judul film: ")
    genre = input("Masukkan genre film: ")
    id_baru = max(daftar.keys(), default=0) + 1
    daftar[id_baru] = {"judul": judul, "genre": genre}
    print("✅ Film berhasil ditambahkan!")