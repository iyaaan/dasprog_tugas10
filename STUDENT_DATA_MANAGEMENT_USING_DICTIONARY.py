data_mahasiswa = {}

while True:
    print("\n=== MENU ===")
    print("1. Tambah Data")
    print("2. Tampilkan Semua Data")
    print("3. Cari Data (NIM)")
    print("4. Hapus Data (NIM)")
    print("5. Keluar")

    pilih = input("Pilih (1-5): ")

    if pilih == "1":
        nim = input("NIM: ")
        nama = input("Nama: ")
        jurusan = input("Jurusan: ")
        ipk = input("IPK: ")
        data_mahasiswa[nim] = {"Name": nama, "Major": jurusan, "GPA": ipk}
        print("Data Ditambahkan.")

    elif pilih == "2":
        if not data_mahasiswa:
            print("Data kosong.")
        else:
            for nim, data in data_mahasiswa.items():
                print(f"\nNIM: {nim}")
                print(f"Nama    : {data['Name']}")
                print(f"Jurusan : {data['Major']}")
                print(f"IPK     : {data['GPA']}")

    elif pilih == "3":
        nim = input("Masukkan NIM: ")
        if nim in data_mahasiswa:
            data = data_mahasiswa[nim]
            print(f"\nNama  : {data['Name']}")
            print(f"Jurusan : {data['Major']}")
            print(f"IPK     : {data['GPA']}")
        else:
            print("Data tidak ditemukan.")

    elif pilih == "4":
        nim = input("Masukkan NIM yang ingin dihapus: ")
        if nim in data_mahasiswa:
            del data_mahasiswa[nim]
            print("Data dihapus.")
        else:
            print("Data tidak ditemukan.")

    elif pilih =="5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")