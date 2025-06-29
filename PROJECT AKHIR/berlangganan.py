def berlangganan():
    paket = {
        "Mobile": {
            "Resolusi": "480p",
            "Perangkat yang didukung": "Ponsel, Tablet",
            "Tontonan bersamaan": "1 perangkat",
            "Harga bulanan": "Rp. 50.000"
        },
        "Basic": {
            "Resolusi": "720p",
            "Perangkat yang didukung": "Ponsel, Tablet, TV, Komputer",
            "Tontonan bersamaan": "1 perangkat",
            "Harga bulanan": "Rp. 60.000"
        },
        "Standar": {
            "Resolusi": "1080p",
            "Perangkat yang didukung": "Ponsel, Tablet, TV, Komputer",
            "Tontonan bersamaan": "2 perangkat",
            "Harga bulanan": "Rp. 100.000"
        },
        "Premium": {
            "Resolusi": "4K + HDR",
            "Perangkat yang didukung": "Ponsel, Tablet, TV, Komputer",
            "Tontonan bersamaan": "4 perangkat",
            "Harga bulanan": "Rp. 160.000"
        }
    }

    while True:
        print("\n=== Daftar Paket Berlangganan ===")
        for i, nama_paket in enumerate(paket, start=1):
            print(f"{i}. {nama_paket}")
        
        try:
            pilihan = int(input("Pilih paket langganan (1-4): "))
            nama_pilihan = list(paket.keys())[pilihan - 1]
            detail = paket[nama_pilihan]

            print(f"\n--- Detail Paket '{nama_pilihan}' ---")
            for keterangan, isi in detail.items():
                print(f"{keterangan}: {isi}")
            
            konfirmasi = input(f"\nApakah kamu ingin berlangganan paket '{nama_pilihan}'? (YA/TIDAK): ").strip().upper()
            
            if konfirmasi == "YA":
                metode = input("Pilih metode pembayaran (Transfer / Gopay / Dana): ").strip().title()
                print(f"\nMetode pembayaran: {metode}")
                print(f"Selamat, Anda sudah berlangganan paket '{nama_pilihan}'.")
                break  # keluar dari loop setelah sukses
            elif konfirmasi == "TIDAK":
                print("Kembali ke menu paket...")
            else:
                print("Input tidak valid. Mohon ketik YA atau TIDAK.")
        
        except (IndexError, ValueError):
            print("Pilihan tidak valid. Silakan masukkan angka antara 1-4.")

