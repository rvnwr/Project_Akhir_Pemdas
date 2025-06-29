from fitur_aplikasi import film_lain 

def hapus_film():
    daftar = film_lain()  # ✅ ini dictionary dari fungsi film_lain()

    if not daftar:
        print("🎞️ Tidak ada film di wishlist.")
        return

    print("📋 Daftar Film Saat Ini:")
    for id, info in daftar.items():
        print(f"{id}. {info['judul']} - {info['genre']}")

    try:
        hapus = int(input("Masukkan ID film yang ingin dihapus: "))
        if hapus in daftar:
            print(f"🗑️  Menghapus film: {daftar[hapus]['judul']}")
            del daftar[hapus]
            print("✅ Film berhasil dihapus.")
        else:
            print("❌ ID tidak ditemukan.")
    except ValueError:
        print("❌ Masukkan angka yang valid.")
