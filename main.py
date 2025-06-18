import os
from datetime import datetime
from tabulate import tabulate

os.system("cls")

# Fungsi untuk format Rupiah
def rupiah(nominal):
    return f"Rp. {nominal:,.0f}".replace(",", ".")

# Data dummy awal
stok_atk = {
    "ATKA1": {"nama": "penghapus", "kategori": "alat tulis", "stok": 15, "harga": 1500, "tanggal_masuk": "15-03-2025", "tanggal_update": "17-03-2025"},
    "ATKA2": {"nama": "pulpen biru", "kategori": "alat tulis", "stok": 100, "harga": 2500, "tanggal_masuk": "02-04-2025", "tanggal_update": "05-04-2025"},
    "ATKA3": {"nama": "buku tulis", "kategori": "alat tulis", "stok": 60, "harga": 5000, "tanggal_masuk": "27-05-2025", "tanggal_update": "29-05-2025"},
    "ATKK1": {"nama": "kertas sidu A4", "kategori": "kertas", "stok": 30, "harga": 55000, "tanggal_masuk": "04-06-2025", "tanggal_update": "10-06-2025"},
    "ATKA4": {"nama": "pensil 2B", "kategori": "alat tulis", "stok": 45, "harga": 2000, "tanggal_masuk": "12-04-2025", "tanggal_update": "15-04-2025"},
    "ATKA5": {"nama": "spidol hitam", "kategori": "alat tulis", "stok": 25, "harga": 4000, "tanggal_masuk": "20-05-2025", "tanggal_update": "22-05-2025"},
    "ATKP1": {"nama": "map folder", "kategori": "perlengkapan kantor", "stok": 65, "harga": 3500, "tanggal_masuk": "10-03-2025", "tanggal_update": "12-03-2025"},
    "ATKP2": {"nama": "penggaris 30cm", "kategori": "perlengkapan kantor", "stok": 20, "harga": 3000, "tanggal_masuk": "28-04-2025", "tanggal_update": "30-04-2025"},
    "ATKP3": {"nama": "amplop coklat", "kategori": "perlengkapan kantor", "stok": 40, "harga": 1500, "tanggal_masuk": "01-06-2025", "tanggal_update": "02-06-2025"},
    "ATKA6": {"nama": "stapler mini", "kategori": "alat tulis", "stok": 0, "harga": 12000, "tanggal_masuk": "18-03-2025", "tanggal_update": "20-03-2025"}
}


# Fungsi Membuat Kode Barang Otomatis
def kode_otomatis(kategori):
    ambil_code = "ATK" + kategori[0].upper()
    kode_terbesar = 0
    for key in stok_atk:
        if key.startswith(ambil_code):
            try:
                urutan = int(key[len(ambil_code):])
                if urutan > kode_terbesar:
                    kode_terbesar = urutan
            except:
                pass
    return ambil_code + str(kode_terbesar + 1)

# Membuat Submenu Pada Menu Utama "Tampilkan Stok ATK"
# Meliputi Fungsi Menampilkan Data : Menampilkan Semua Data
#                                    Menampilkan Data Berdasarkan Nama
#                                    Menampilkan Berdasarkan Kategori yang Dipilih
def tampilkan_semua():
    if not stok_atk:
        print(" 📂 Data Stok ATK Belum di Isi !!!\n")
        return
    while True:
        print('''\n=== Menu Tampilkan Data ===
    [1] Lihat Semua Data Stok
    [2] Cari Data berdasarkan Nama
    [3] Lihat Data berdasarkan Kategori
    [4] Kembali ke Menu Utama''')
        pilihan = input("Pilih Menu yang Tersedia [1-4] : ")
        if not pilihan.isdigit():
            print(" ⚠️ Masukkan Angka bukan Huruf !!!\n")
            continue
        if pilihan == '1':
            tampil_semua_data()
        elif pilihan == '2':
            cari_berdasarkan_nama()
        elif pilihan == '3':
            lihat_berdasarkan_kategori()
        elif pilihan == '4':
            break
        else:
            print(" ⚠️ Pilihan Angka Tidak dalam Pilihan !!!\n")

def tampil_semua_data():
    headers = ["Kode", "Nama", "Kategori", "Stok", "Harga", "Masuk", "Update"]
    tabel = [[
        key,
        unit["nama"].title(),
        unit["kategori"].title(),
        "Habis" if unit["stok"] == 0 else unit["stok"],
        rupiah(unit["harga"]),
        unit.get("tanggal_masuk", "-"),
        unit.get("tanggal_update", "-")
    ] for key, unit in stok_atk.items()]
    
    print("\n📋 Data Semua ATK : ")
    print(tabulate(tabel, headers=headers, tablefmt="fancy_grid"))

def cari_berdasarkan_nama():
    keyword = input("Masukkan Nama Barang yang ingin dicari : ").lower()
    hasil = []
    for key, unit in stok_atk.items():
        if keyword in unit['nama']:
            hasil.append([
                key,
                unit["nama"].title(),
                unit["kategori"].title(),
                "Habis" if unit["stok"] == 0 else unit["stok"],
                rupiah(unit["harga"]),
                unit.get("tanggal_masuk", "-"),
                unit.get("tanggal_update", "-")
            ])
    if hasil:
        print("\n🔎 Hasil Pencarian : ")
        print(tabulate(hasil, headers=["Kode", "Nama", "Kategori", "Stok", "Harga", "Masuk", "Update"], tablefmt="fancy_grid"))
    else:
        print(" ⚠️ Tidak Ada Barang dengan Nama Tersebut !!!")

def lihat_berdasarkan_kategori():
    semua_kategori = sorted(set(unit["kategori"] for unit in stok_atk.values()))
    if not semua_kategori:
        print(" ⚠️ Tidak Ada Kategori yang Tersedia !!!")
        return
    print("\n 📋 Kategori yang Tersedia : ")
    for i, kat in enumerate(semua_kategori, 1):
        print(f"{i}. {kat.title()}")
    pilihan = input("Pilih Nomor Kategori yang Tersedia : ")
    if not pilihan.isdigit():
        print(" ⚠️ Masukkan Angka bukan Huruf !!!\n")
        return
    pilihan = int(pilihan)
    if 1 <= pilihan <= len(semua_kategori):
        kategori_pilihan = semua_kategori[pilihan - 1]
        hasil = [
            [key, unit["nama"].title(), unit["kategori"].title(), "Habis" if unit["stok"] == 0 else unit["stok"], rupiah(unit["harga"]), unit.get("tanggal_masuk", "-"), unit.get("tanggal_update", "-")]
            for key, unit in stok_atk.items() if unit["kategori"] == kategori_pilihan
        ]
        if hasil:
            print(f"\n 📋 Data untuk Kategori : {kategori_pilihan.title()}")
            print(tabulate(hasil, headers=["Kode", "Nama", "Kategori", "Stok", "Harga", "Masuk", "Update"], tablefmt="fancy_grid"))
        else:
            print(f" ⚠️ Tidak Ada Data dalam Kategori {kategori_pilihan}.\n")
    else:
        print(" ❌ Pilihan Kategori tidak Valid !!!\n")


# Membuat Fungsi Untuk Menambahkan Stok ATK Baru yang Belum Pernah Diinput Sebelumnya
def tambah_atk():
    nama = input("Masukkan Nama ATK : ").lower()
    kategori = input("Masukkan Kategori ATK : ").lower()
    if not kategori:
        print(" ⚠️ Kategori Tidak Boleh Kosong !!!")
        return
    try:
        stok = int(input("Masukkan Jumlah Stok : "))
        harga = int(input("Masukkan Harga : "))
    except ValueError:
        print(" ⚠️ Stok dan Harga Harus Berupa Angka !!!")
        return
    tanggal_input = input("Masukkan Tanggal Masuk (DD-MM-YYYY) : ")
    try:
        tanggal_masuk = datetime.strptime(tanggal_input, "%d-%m-%Y").strftime("%d-%m-%Y")
    except ValueError:
        print(" ❌ Format Tanggal Salah !!! Gunakan Format DD-MM-YYYY")
        return
    kode = kode_otomatis(kategori)
    stok_atk[kode] = {
        "nama": nama,
        "kategori": kategori,
        "stok": stok,
        "harga": harga,
        "tanggal_masuk": tanggal_masuk,
        "tanggal_update": tanggal_masuk
    }
    print(f"ATK Berhasil Ditambahkan dengan Kode : {kode} ✅\n")

# Membuat Submenu Pada Menu Utama "Update Data Stok ATK"
# Meliputi Fungsi : Mengubah Data ATK yang Sudah Ada
#                   Menambahkan Stok ATK yang Sudah Ada
#                   Mengurangi Stok ATK yang Sudah Ada
def update_data_stok():
    while True:
        print('''\n=== Menu Update Data Stok ===
    [1] Tambah Stok (Barang Masuk)
    [2] Kurangi Stok (Barang Keluar)
    [3] Ubah Data ATK
    [4] Kembali ke Menu Utama''')
        submenu = input("Pilih Menu Update Data Stok [1-4] : ")
        if submenu == '1':
            tambah_stok()
        elif submenu == '2':
            kurangi_stok()
        elif submenu == '3':
            ubah_atk()
        elif submenu == '4':
            break
        else:
            print(" ⚠️ Angka Pilihan Tidak Valid !!!")

def tambah_stok():
    if not stok_atk:
        print(" 📂 Data kosong !!!")
        return
    tampil_semua_data()
    kode = input("Masukkan Kode ATK untuk Tambah Stok : ").upper()
    if kode not in stok_atk:
        print(" ⚠️ Kode tidak ditemukan !!!")
        return
    try:
        tambah = int(input("Jumlah Stok yang Ditambahkan : "))
        if tambah < 0:
            raise ValueError
    except ValueError:
        print(" ⚠️ Masukkan Angka yang Valid !!!")
        return
    tanggal_input = input("Masukkan Tanggal Update Stok (DD-MM-YYYY) : ")
    try:
        tanggal_update = datetime.strptime(tanggal_input, "%d-%m-%Y").strftime("%d-%m-%Y")
    except ValueError:
        print(" ❌ Format Tanggal Salah !!! Gunakan Format DD-MM-YYYY")
        return
    stok_atk[kode]['stok'] += tambah
    stok_atk[kode]['tanggal_update'] = tanggal_update
    print(f"Stok ATK {kode} Sekarang : {stok_atk[kode]['stok']} ✅\n")

def kurangi_stok():
    if not stok_atk:
        print(" 📂 Data kosong !!!")
        return
    tampil_semua_data()
    kode = input("Masukkan Kode ATK untuk Mengurangi Stok : ").upper()
    if kode not in stok_atk:
        print(" ⚠️ Kode Tidak Ditemukan !!!")
        return
    try:
        kurang = int(input("Jumlah Stok yang Dikurangi : "))
        if kurang < 0 or kurang > stok_atk[kode]['stok']:
            raise ValueError
    except ValueError:
        print("Jumlah yang Di Input Melebihi Stok yang Tersedia !!!")
        return
    tanggal_input = input("Masukkan Tanggal Update Stok (DD-MM-YYYY) : ")
    try:
        tanggal_update = datetime.strptime(tanggal_input, "%d-%m-%Y").strftime("%d-%m-%Y")
    except ValueError:
        print(" ❌ Format Tanggal Salah !!! Gunakan Format DD-MM-YYYY")
        return
    stok_atk[kode]['stok'] -= kurang
    stok_atk[kode]['tanggal_update'] = tanggal_update
    print(f"Stok ATK {kode} Sekarang : {stok_atk[kode]['stok']} ✅\n")

def ubah_atk():
    if not stok_atk:
        print(" ⚠️ Data ATK Kosong. Tidak Ada yang Bisa Diubah !!!\n")
        return
    tampil_semua_data()
    kode_lama = input("Masukkan Kode ATK yang Ingin Diubah : ").upper()
    if kode_lama not in stok_atk:
        print(" ⚠️ Kode Tidak Ditemukan !!!\n")
        return

    unit = stok_atk[kode_lama]
    print("\n📝 Data Stok ATK Saat Ini : ")
    print(tabulate([[unit['nama'].title(), unit['kategori'].title(), unit['stok'], rupiah(unit['harga'])]],
                   headers=["Nama", "Kategori", "Stok", "Harga"], tablefmt="fancy_grid"))

    nama = input(f"Masukkan Nama Baru ({unit['nama'].title()}) : ").lower() or unit['nama']
    kategori = input(f"Masukkan Kategori Baru ({unit['kategori'].title()}) : ").lower() or unit['kategori']

    try:
        stok = int(input(f"Masukkan Stok Baru ({unit['stok']}) : ") or unit['stok'])
        harga = int(input(f"Masukkan Harga Baru ({unit['harga']}) : ") or unit['harga'])
    except ValueError:
        print(" ⚠️ Stok dan Harga Harus Berupa Angka !!!")
        return

    # Jika kategori berubah, buat kode baru otomatis
    if kategori != unit['kategori']:
        kode_baru = kode_otomatis(kategori)
        stok_atk[kode_baru] = {
            "nama": nama,
            "kategori": kategori,
            "stok": stok,
            "harga": harga,
            "tanggal_masuk": datetime.now().strftime("%d-%m-%Y"),
            "tanggal_update": datetime.now().strftime("%d-%m-%Y")
        }
        del stok_atk[kode_lama]  # hapus data lama
        print(f" 💾 ATK Berhasil Diubah ke Kode Baru {kode_baru} ✅\n")
    else:
        stok_atk[kode_lama].update({
            "nama": nama,
            "kategori": kategori,
            "stok": stok,
            "harga": harga,
            "tanggal_update": datetime.now().strftime("%d-%m-%Y")
        })
        print(f" 💾 ATK dengan Kode {kode_lama} Berhasil Diubah ✅\n")


# Fungsi Diskon untuk Menjual Barang dengan Diskon Tertentu Berdasarkan Jumlah Stok yang Dibeli dari Barang ATK yang Tersedia
# Data yang ditampilkan merupakan Barang ATK yang Sudah Melebihi 2 Bulan Sejak Barang Masuk di Gudang
# Ketika Membeli Barang Diskon, akan Menampilkan Deskripsi dari Barang Serta Jumlah Diskon yang Didapat dan Jumlah Harga Setelah Diskon
def menu_diskon():
    print("\n===🛒 Barang Diskon ATK 🏷️===")
    if not stok_atk:
        print("Data Kosong !!!")
        return
    hari_ini = datetime.now()
    barang_diskon = []
    for key, unit in stok_atk.items():
        tanggal_str = unit.get("tanggal_masuk")
        if not tanggal_str:
            continue
        try:
            tanggal_masuk = datetime.strptime(tanggal_str, "%d-%m-%Y")
        except:
            continue
        if (hari_ini - tanggal_masuk).days > 60:
            barang_diskon.append([key, unit["nama"].title(), unit["kategori"].title(), "Habis" if unit["stok"] == 0 else unit["stok"], rupiah(unit["harga"]), tanggal_str])
    if not barang_diskon:
        print("Tidak Ada Barang yang Memenuhi Syarat Diskon.\n")
        return
    print("\nBarang di Gudang yang Diskon : ")
    print(tabulate(barang_diskon, headers=["Kode", "Nama", "Kategori", "Stok", "Harga", "Tanggal Masuk"], tablefmt="fancy_grid"))
    kode = input("Masukkan Kode Barang yang Ingin Dibeli : ").upper()
    if kode not in stok_atk:
        print("Kode Tidak Ditemukan !!!")
        return
    try:
        jumlah = int(input("Masukkan Jumlah Pembelian : "))
        if jumlah <= 0 or jumlah > stok_atk[kode]['stok']:
            raise ValueError
    except ValueError:
        print("Jumlah Pembelian Tidak Valid atau Melebihi Stok !!!")
        return
        
    unit = stok_atk[kode]
    harga_awal = unit["harga"] * jumlah
    diskon = 0.30 if jumlah > 5 else 0.10
    potongan = harga_awal * diskon
    total = harga_awal - potongan
    
    print(f"\n🧾 Rincian Pembelian : ")
    print(f"Barang     : {unit['nama'].title()}")
    print(f"Jumlah     : {jumlah}")
    print(f"Harga awal : {rupiah(harga_awal)}")
    print(f"Diskon     : {int(diskon * 100)} %")
    print(f"Potongan   : {rupiah(potongan)}")
    print(f"Total bayar: {rupiah(total)}\n")
    
    print(f"\nTotal Discount yang Anda Dapatkan Adalah {rupiah(potongan)} 🏷️")
    konfirmasi = input("Apakah Anda Yakin Ingin Membeli Barang Ini ? (y/n) : ").lower()
    
    if konfirmasi == 'y':
        stok_atk[kode]["stok"] -= jumlah
        stok_atk[kode]["tanggal_update"] = datetime.now().strftime("%d-%m-%Y")
        print(f" 🛒 Pembelian Berhasil !!! Stok {kode} Sekarang : {stok_atk[kode]['stok']} ✅")
    else:
        print(" ❌ Pembelian Dibatalkan !!!")

# Fungsi Menghapus ATK yang Ada dalam Gudang ATK
def hapus_atk():
    if not stok_atk:
        print(" ⚠️ Data ATK Kosong. Tidak Ada yang Bisa Dihapus !!!\n")
        return
    tampil_semua_data()
    kode = input("Masukkan Kode ATK yang Ingin Dihapus : ").upper()
    if kode not in stok_atk:
        print("Kode Tidak Ditemukan.\n")
        return
    konfirmasi = input(f"Apakah Anda Yakin Ingin Menghapus {kode} - {stok_atk[kode]['nama'].title()} ? (y/n) : ").lower()
    if konfirmasi == 'y':
        del stok_atk[kode]
        print(f"ATK dengan Kode {kode} Berhasil Dihapus 🗑️\n")
    else:
        print(" ⚠️ Penghapusan Dibatalkan !!!\n")

# Fungsi yang Menampilkan Menu Utama dari Program Stok Gudang ATK
def menu():
    while True:
        print('''\n===   Menu Gudang ATK (Alat Tulis Kantor) 📦 ===
    [1] Tampilkan Stok ATK
    [2] Tambahkan ATK Baru
    [3] Update Data Stok ATK
    [4] Menu Diskon
    [5] Hapus ATK
    [6] Keluar dari Program''')
        pilihan = input("Pilih menu [1-6]: ")
        if not pilihan.isdigit():
            print("Masukkan Angka Bukan Huruf !!!\n")
            continue
        if pilihan == '1':
            tampilkan_semua()
        elif pilihan == '2':
            tambah_atk()
        elif pilihan == '3':
            update_data_stok()
        elif pilihan == '4':
            menu_diskon()
        elif pilihan == '5':
            hapus_atk()
        elif pilihan == '6':
            print("Terima Kasih Telah Menggunakan Program Kami !!! Program Akan Ditutup 👋")
            break
        else:
            print("Pilihan Tidak Valid !!! Silahkan Coba Lagi\n")

# Memanggil Menu Utama Sebagai __main__ Pada Program
if __name__ == "__main__":
    menu()
