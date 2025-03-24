from tabulate import tabulate

def menu_utama():
    print("""
    Selamat Datang di Perpustakaan ABC
    List Menu:
    1. Kelola Buku
    2. Kelola Anggota
    3. Kelola Peminjaman
    4. Exit Program""")

def menu_kelola_buku():
    print("""
    Kelola Buku
    List Menu:
    1. Lihat Daftar Buku
    2. Tambah Buku
    3. Hapus Buku    
    4. Kembali ke Menu Utama""")

def tampilkan_daftar_buku(dictBuku):
    headers = ["ID Buku", "Judul", "Penulis", "Tahun Terbit", "Genre", "Stock"]
    table = zip(
        dictBuku["ID Buku"], dictBuku["Judul"], dictBuku["Penulis"], 
        dictBuku["Tahun Terbit"], dictBuku["Genre"], dictBuku["Stock"]
    )
    print(tabulate(table, headers=headers, tablefmt="grid"))

def tambah_buku(dictBuku):
    try:
        id_buku = int(input("ID buku: "))
        if id_buku in dictBuku["ID Buku"]:
            print("ID buku sudah ada! Gunakan ID yang berbeda.")
            return

        judul = input("Judul buku: ").title()
        penulis = input("Penulis: ").title()
        tahun_terbit = int(input("Tahun terbit buku: "))
        genre = input("Genre buku: ").title()
        stock = int(input("Stock buku yang ingin diinput: "))

        dictBuku["ID Buku"].append(id_buku) 
        dictBuku["Judul"].append(judul)
        dictBuku["Penulis"].append(penulis)
        dictBuku["Tahun Terbit"].append(tahun_terbit) 
        dictBuku["Genre"].append(genre)
        dictBuku["Stock"].append(stock)

        print("Buku berhasil ditambahkan!")
        tampilkan_daftar_buku(dictBuku)
    except ValueError:
        print("Input tidak valid! Pastikan ID dan angka lainnya berupa bilangan bulat.")

def hapus_buku(dictBuku):
    id_buku = int(input("Masukkan ID buku yang ingin dihapus: "))
    if id_buku in dictBuku["ID Buku"]:
        index = dictBuku["ID Buku"].index(id_buku)
        for key in dictBuku.keys():
            del dictBuku[key][index]
        print("Buku berhasil dihapus!")
    else:
        print("ID buku tidak ditemukan.")
    tampilkan_daftar_buku(dictBuku)

def menu_kelola_anggota():
    print("""
    Kelola Anggota
    List Menu:
    1. Lihat Daftar Anggota
    2. Tambah Anggota
    3. Hapus Anggota
    4. Kembali ke Menu Utama""")

def tampilkan_anggota(dictAnggota):
    headers = ["ID Anggota", "Nama", "Email", "No Telp", "Alamat"]
    table = zip(
        dictAnggota["ID Anggota"], dictAnggota["Nama"], dictAnggota["Email"], 
        dictAnggota["No Telp"], dictAnggota["Alamat"]
    )
    print(tabulate(table, headers=headers, tablefmt="grid"))

def tambah_anggota(dictAnggota):
    try:
        id_anggota = int(input("Masukkan ID Anggota Anda: "))
        if id_anggota in dictAnggota["ID Anggota"]:
            print("ID anggota sudah ada! Gunakan ID yang berbeda.")
            return

        nama_anggota = input("Masukkan Nama Anda: ").title()
        email = input("Masukkan Email Anda: ").strip()
        telp = input("Masukkan No Telp Anda: ").strip()
        alamat = input("Masukkan Alamat Anda: ").title()

        dictAnggota["ID Anggota"].append(id_anggota) 
        dictAnggota["Nama"].append(nama_anggota)
        dictAnggota["Email"].append(email)
        dictAnggota["No Telp"].append(telp) 
        dictAnggota["Alamat"].append(alamat)

        print("Anggota berhasil ditambahkan!")
        tampilkan_anggota(dictAnggota)
    except ValueError:
        print("Input tidak valid! Pastikan ID berupa bilangan bulat.")

def hapus_anggota(dictAnggota):
    id_anggota = int(input("Masukkan ID anggota yang ingin dihapus: "))
    if id_anggota in dictAnggota["ID Anggota"]:
        index = dictAnggota["ID Anggota"].index(id_anggota)
        for key in dictAnggota.keys():
            del dictAnggota[key][index]
        print("Anggota berhasil dihapus!")
    else:
        print("ID anggota tidak ditemukan.")
    tampilkan_anggota(dictAnggota)

def pinjam_buku():
    print("""
    Peminjaman Buku\n
    List Menu:
    1. Lihat Daftar Peminjaman
    2. Tambah Peminjaman
    3. Perbarui Status Peminjaman
    4. Hapus Data Peminjaman
    5. Kembali ke Menu Utama""")

def daftar_peminjam(dictPeminjaman):
    headers = ["ID Peminjaman", "ID Anggota", "ID Buku", "Tanggal Peminjaman", "Tanggal Pengembalian", "Status"]
    table = zip(
        dictPeminjaman["ID Peminjaman"], dictPeminjaman["ID Anggota"], dictPeminjaman["ID Buku"],
        dictPeminjaman["Tanggal Peminjaman"], dictPeminjaman["Tanggal Pengembalian"], dictPeminjaman["Status"]
    )
    print(tabulate(table, headers=headers, tablefmt="grid"))

def tambah_peminjam(dictPeminjaman):
    try:
        id_peminjam = int(input("Masukkan ID Peminjaman: "))
        if id_peminjam in dictPeminjaman["ID Peminjaman"]:
            print("ID peminjaman sudah ada! Gunakan ID yang berbeda.")
            return

        id_anggota = int(input("Masukkan ID Anggota Anda: "))
        id_buku = int(input("ID buku: "))
        tgl_peminjaman = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD): ").strip()
        tgl_pengembalian = input("Masukkan Tanggal Pengembalian (YYYY-MM-DD): ").strip()
        status = input("Status (Dipinjam/Dikembalikan): ").title()

        if status not in ["Dipinjam", "Dikembalikan"]:
            print("Status tidak valid! Pilih antara 'Dipinjam' atau 'Dikembalikan'.")
            return

        dictPeminjaman["ID Peminjaman"].append(id_peminjam)
        dictPeminjaman["ID Anggota"].append(id_anggota)
        dictPeminjaman["ID Buku"].append(id_buku)
        dictPeminjaman["Tanggal Peminjaman"].append(tgl_peminjaman)
        dictPeminjaman["Tanggal Pengembalian"].append(tgl_pengembalian)
        dictPeminjaman["Status"].append(status)

        print("Peminjaman berhasil ditambahkan!")
        daftar_peminjam(dictPeminjaman)
    except ValueError:
        print("Input tidak valid! Pastikan ID berupa bilangan bulat.")

def status_peminjam(dictPeminjaman):
    print("\nPerbarui Status Peminjaman")
    id_peminjaman = int(input("Masukkan ID Peminjaman yang ingin diperbarui: "))

    # Cek apakah ID Peminjaman ada dalam dictionary
    if id_peminjaman in dictPeminjaman["ID Peminjaman"]:
        index = dictPeminjaman["ID Peminjaman"].index(id_peminjaman)  # Cari index berdasarkan ID

        print(f"Status saat ini: {dictPeminjaman['Status'][index]}")
        status_baru = input("Masukkan status baru (Dipinjam/Dikembalikan): ").strip().title()

        # Validasi status baru
        if status_baru in ["Dipinjam", "Dikembalikan"]:
            dictPeminjaman["Status"][index] = status_baru
            print("Status peminjaman berhasil diperbarui!")
        else:
            print("Status tidak valid. Harus 'Dipinjam' atau 'Dikembalikan'.")
    else:
        print("ID Peminjaman tidak ditemukan.")

    daftar_peminjam(dictPeminjaman)

def hapus_peminjam(dictPeminjaman):
    id_peminjam = int(input("Masukkan ID peminjam yang ingin dihapus: "))
    if id_peminjam in dictPeminjaman["ID Peminjaman"]:  
        index = dictPeminjaman["ID Peminjaman"].index(id_peminjam)
        for key in dictPeminjaman.keys():
            del dictPeminjaman[key][index]
        print("Peminjaman berhasil dihapus!")
    else:
        print("ID peminjam tidak ditemukan.")
    daftar_peminjam(dictPeminjaman)

def main():
    dictBuku = {
        "ID Buku": [101, 102, 103, 104, 105],
        "Judul": ["Laskar Pelangi", "Sapiens", "Bumi", "Harry Potter", "Atomic Habits"],
        "Penulis": ["Andrea Hirata", "Yuval Noah Harari", "Tere Liye", "J.K. Rowling", "James Clear"],
        "Tahun Terbit": [2005, 2011, 2014, 1997, 2018],
        "Genre": ["Fiksi", "Nonfiksi", "Fantasi", "Fantasi", "Nonfiksi"],
        "Stock": [2, 1, 3, 1, 2]
    }
    
    dictAnggota = {
        "ID Anggota": [200, 201, 202, 203],
        "Nama": ["Andi", "Putri", "Baskara", "Dinda"],
        "Email": ["andi00@gmail.com", "putriii@gmail.com", "b4skar4@gmail.com", "dinda@gmail.com"],
        "No Telp": ["+6281234567890", "+6289876543210", "+6281122334455", "+6285566778899"],
        "Alamat": ["Jakarta", "Bekasi", "Tangerang", "Bekasi"]
    }

    dictPeminjaman = {
        "ID Peminjaman": [301, 302, 303, 304],
        "ID Anggota": [200, 201, 202, 203],
        "ID Buku": [101, 103, 104, 105],
        "Tanggal Peminjaman": ["2025-03-10", "2025-03-12", "2025-03-15", "2025-03-18"],
        "Tanggal Pengembalian": ["2025-03-17", "2025-03-19", "2025-03-22", "2025-03-25"],
        "Status": ["Dikembalikan", "Dipinjam", "Dipinjam", "Dikembalikan"]
    }

    while True:
        menu_utama()
        menu = int(input("Masukkan angka menu yang ingin dijalankan: "))
        
        if menu == 1:
            while True:
                menu_kelola_buku()
                pilihan = int(input("Pilih menu: "))
                if pilihan == 1:
                    tampilkan_daftar_buku(dictBuku)
                elif pilihan == 2:
                    tambah_buku(dictBuku)
                elif pilihan == 3:
                    hapus_buku(dictBuku)
                elif pilihan == 4:
                    break
                else:
                    print("Pilihan tidak valid!")
                    
        elif menu == 2:
            while True:
                menu_kelola_anggota()
                pilihan = int(input("Pilih menu: "))
                if pilihan == 1:
                    tampilkan_anggota(dictAnggota)
                elif pilihan == 2:
                    tambah_anggota(dictAnggota)
                elif pilihan == 3:
                    hapus_anggota(dictAnggota)
                elif pilihan == 4:
                    break
                else:
                    print("Pilihan tidak valid!")
        
        elif menu == 3:
            while True:
                pinjam_buku()
                pilihan = int(input("Pilih menu: "))
                if pilihan == 1:
                    daftar_peminjam(dictPeminjaman)
                elif pilihan == 2:
                    tambah_peminjam(dictPeminjaman)
                elif pilihan == 3:
                    status_peminjam(dictPeminjaman)
                elif pilihan == 4:
                    hapus_peminjam(dictPeminjaman)
                elif pilihan == 5:
                    break
                else:
                    print("Pilihan tidak valid!")
                    
        elif menu == 4:
            print("Terima kasih telah menggunakan sistem perpustakaan ABC!")
            break
        else:
            print("Menu tidak tersedia, silakan pilih menu yang sesuai!")

if __name__ == "__main__":
    main()