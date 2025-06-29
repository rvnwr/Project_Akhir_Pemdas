from fitur_aplikasi import film_lain

def lihat_wishlist():
    daftar = film_lain()
    if not daftar:
        print("🎬 Daftar film kosong.")
    else:
        print("🎞️ Daftar Film Tonton Nanti:")
        for id, info in daftar.items():
            print(f"{id}. {info['judul']} - Genre: {info['genre']}")
