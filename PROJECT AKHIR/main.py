from welcome import welcome_message
from login import login
from fitur_aplikasi import rekomendasi_film
from fitur_aplikasi import cari_film
from tambah_film import tambah_film
from hapus_film import hapus_film
from berlangganan import berlangganan
from lihat_wishlist import lihat_wishlist  # import fungsi barumu

welcome_message()
print("***** Silahkan Login *******")
login()
def main():
    while True:
        print("\n=== MENU STREAMING FILM ===")
        print("1. Mulai Berlangganan")
        print("2. Tonton Film")
        print("3. Tambah Film ke tonton nanti")
        print("4. Hapus Film dari wishlist")
        print("5. Lihat Daftar Tonton Nanti")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            berlangganan()
        elif pilihan == "2":
            cari_film()
        elif pilihan == "3":
            tambah_film()
        elif pilihan == "4":
            hapus_film()
        elif pilihan == "5":
            lihat_wishlist()
            input("\nTekan ENTER untuk kembali ke menu...")
        elif pilihan == "6":
            print("👋 Terima kasih sudah menggunakan aplikasi!")
            break
        else:
            print("❌ Pilihan tidak valid. Coba lagi.")

# Jalankan program
main()