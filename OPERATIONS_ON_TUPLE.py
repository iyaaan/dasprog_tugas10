buah = tuple(input(f"Masukkan nama buah ke-{i+1}: ") for i in range(5))

print("\nTuple buah:", buah)

cari_buah = input("\nMasukkan nama buah yang ingin dicari: ")

if cari_buah in buah:
    print(f"Ya, '{cari_buah}' ada dalam tuple.")
else:
    print(f"Tidak, '{cari_buah}' tidak ada dalam tuple.")

print("\nJumlah kemunculan masing-masing buah:")
for b in set(buah):  
    jumlah = buah.count(b)
    print(f"{b}: {jumlah}")