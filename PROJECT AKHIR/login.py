from welcome import welcome_message


akun_tersedia = {
    "username": "Kemal Korawa",
    "email": "abcd",
    "password": "0123456789"
}

def login():
    print("========= LOGIN YU Streaming =========")
    
    max_verif = 3
    verif = 0
    
    while verif < max_verif:
        email = input("Alamat email: ")
        password = input("Password: ")
        
        if email == akun_tersedia["email"] and password == akun_tersedia["password"]:
            print(f"Login berhasil, Selamat datang {akun_tersedia['username']}!\n")
            welcome_message()  # panggil fungsi welcome_message
            return  # keluar dari fungsi login jika berhasil
        else:
            print("Email atau password salah, silakan coba lagi.\n")
            verif += 1  # tambahkan 1 ke percobaan verifikasi
    
    print("Terlalu banyak percobaan, keluar dari menu login.")
    exit()
