total = 0
barang = []
harga = []
while True:
    print("""Daftar Barang
    1. Roti \t 5000
    2. Kue \t 8000
    3. Cokelat \t 14000
    4. Pulpen \t 4000
    5. Pensil \t 3500
    6. Buku \t 12000""")

    kode = int(input("masukkan kode barang : "))
    if kode == 1:
        barang.append("roti")
        harga.append(5000)
        total += 5000
    elif kode == 2:
        barang.append("kue")
        harga.append(8000)
        total += 8000
    elif kode == 3:
        barang.append("cokelat")
        harga.append(14000)
        total += 14000
    elif kode == 4:
        barang.append("pulpen")
        harga.append(4000)
        total += 4000
    elif kode == 5:
        barang.append("pensil")
        harga.append(3500)
        total += 3500
    elif kode == 6:
        barang.append("Buku")
        harga.append(12000)
        total += 12000
    else:
        print("kode tidak valid")

    lanjut = input("lanjut belanja (y/t) : ")
    if lanjut == "t":
        print("")
        break

    print("barang yang dibeli : ", barang)
    print("harga barangnya : ", harga)
    print("total yang harus dibayar : ", total, "\n")

    uang = int(input("masukkan uang pembayaran : "))
    if uang > total:
        print("kembaliannya : ", uang - total)
    elif uang == total:
        print("uang pas")
    else:
        print("uangnya kurang", uang - total)

    input("nama :")
    input("nohp :")
    input("alamat :")
