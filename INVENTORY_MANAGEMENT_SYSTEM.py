inventaris = {}

while True:
    print("\n=== MENU ===")
    print("1. Tambah Item")
    print("2. Tampilkan Semua Item")
    print("3. Cari Item")
    print("4. Update Stok")
    print("5. Hapus Item")
    print("6. Analisis")
    print("7. Keluar")

    pilih = input("Pilih (1-7): ")

    if pilih == "1":
        nama = input("Nama item: ")
        harga = float(input("Harga: "))
        stok = int(input("Stok: "))
        inventaris[nama] = (harga, stok)

    elif pilih == "2":
        for item, data in inventaris.items():
            print(f"{item}: Harga = {data[0]}, Stok = {data[1]}")

    elif pilih == "3":
        nama = input("Cari item: ")
        if nama in inventaris:
            print(f"{nama}: Harga = {inventaris[nama][0]}, Stok = {inventaris[nama][1]}")
        else:
            print("Item tidak ditemukan.")

    elif pilih == "4":
        nama = input("Nama item: ")
        if nama in inventaris:
            stok_baru = int(input("Stok baru: "))
            inventaris[nama] = (inventaris[nama][0], stok_baru)
        else:
            print("Item tidak ditemukan.")

    elif pilih == "5":
        nama = input("Hapus item: ")
        if nama in inventaris:
            del inventaris[nama]
        else:
            print("Item tidak ditemukan")

    elif pilih == "6":
        if inventaris:
            termahal = max(inventaris.item(), key=lambda x: x[1][0])
            termurah = min(inventaris.item(), key=lambda x: x[1][0])
            total = sum(h * s for h, s in inventaris.values())
            print(f"Termahal: {termahal[0]} ({termahal[1][0]})")
            print(f"Termurah: {termurah[0]} ({termurah[1][0]})")
            print(f"Total nilai stok: {total}")
        else :
            print("Inventaris kosong.")
    elif pilih == "7":
        break

    else:
        print("Pilihan tidak valid")