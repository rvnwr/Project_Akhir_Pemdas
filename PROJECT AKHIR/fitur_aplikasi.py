# Global dictionary
daftar_film_lain  = {
    1: {"judul": "Titanic", "genre": "Romance"},
    2: {"judul": "Warkop DkI", "genre": "Komedi"},
    3: {"judul": "Marvel", "genre": "Action"},
    4: {"judul": "Pengabdi Setan", "genre": "Horror"}
}

def rekomendasi_film(): 
    film = ['KKN DESA KEBON', 'TUYUL REBORN', 'SANTRI PILIHAN AYAH', 'CINTA KANDAS DI UBP']
    print("Rekomendasi Film Minggu Ini:")
    for i, judul in enumerate(film, start=1):
        print(f"{i}. {judul}")
    return film

def film_lain():
    return daftar_film_lain  # kembalikan global dict

#Cari film yang di rekomendasikan atau tidak
def cari_film():
    film_rekomendasi = rekomendasi_film()
    daftar_lain = film_lain()
    rekomendasi = input("Apakah anda ingin menonton film yang direkomendasikan? (YA/TIDAK): ").strip().upper()
    
    if rekomendasi == "TIDAK":
        cari = input("Ketik judul film yang ingin kamu cari di sini: ").strip().upper()
        film_atas = [film["judul"].upper() for film in daftar_lain.values()]
        
        if cari in film_atas:
            print("Film sedang disiapkan, mohon tunggu.... dan selamat menonton!")
        else:
            print("Film tidak ada!")
    
    elif rekomendasi == "YA":
        try:
            pilihan = int (input(f"Masukkan nomor film yang ingin kamu tonton (1-{len(film_rekomendasi)}): "))
            if 1 <= pilihan <= len(film_rekomendasi):
                print(f"Anda memilih: {film_rekomendasi[pilihan - 1]}")
                print(f"Film {film_rekomendasi[pilihan - 1]} sedang disiapkan, mohon tunggu.... dan selamat menonton!")
            else:
                print("Nomor film tidak valid!")
        except ValueError:
            print("Input harus berupa angka!")

    else:
        print("Input tidak dikenali. Silakan jawab YA atau TIDAK.")

