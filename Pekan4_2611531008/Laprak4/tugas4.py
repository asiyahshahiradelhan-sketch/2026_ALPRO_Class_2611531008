# tugas4_1008.py
# Sistem Loket Terpadu & Audit Transaksi Ekspedisi Wahana

print("=" * 50)
print("SISTEM LOKET TERPADU WAHANA PETUALANGAN")
print("=" * 50)

# Input data pengunjung
nama_1008 = input("Nama Pengunjung : ").strip()
umur_1008 = int(input("Umur : "))
sim_1008 = input("Memiliki SIM C/Kartu Identitas? (y/t) : ").strip().lower()
jumlah_tiket_1008 = int(input("Jumlah Tiket : "))

# If tunggal
if jumlah_tiket_1008 <= 0:
    print("Peringatan: jumlah tiket tidak valid!")

print("\nPilihan Wahana")
print("1. Safari Rimba        (Rp 50.000)")
print("2. Arung Jeram         (Rp 75.000)")
print("3. Motor ATV Ekstrim   (Rp 120.000)")
print("4. Roller Coaster Kilat(Rp 100.000)")
print("5. All-Access VIP      (Rp 220.000)")

paket_1008 = int(input("Pilih Paket (1-5): "))

nama_paket_1008 = ""
harga_satuan_1008 = 0
paket_valid_1008 = True

# Match Case
match paket_1008:
    case 1:
        nama_paket_1008 = "Wahana Safari Rimba"
        harga_satuan_1008 = 50000

    case 2:
        nama_paket_1008 = "Wahana Arung Jeram"
        harga_satuan_1008 = 75000

    case 3:
        nama_paket_1008 = "Wahana Motor ATV Ekstrim"
        harga_satuan_1008 = 120000

    case 4:
        nama_paket_1008 = "Wahana Roller Coaster Kilat"
        harga_satuan_1008 = 100000

    case 5:
        nama_paket_1008 = "Wahana All-Access VIP"
        harga_satuan_1008 = 220000

    case _:
        print("Paket wahana tidak valid!")
        paket_valid_1008 = False

# Proses hanya jika paket valid
if paket_valid_1008:

    # If-Elif-Else dengan operator logika
    if paket_1008 == 3 and umur_1008 >= 17 and sim_1008 == "y":
        print("\nAnda sudah dewasa dan boleh mengendarai ATV sendiri.")

    elif paket_1008 == 3 and umur_1008 >= 17 and sim_1008 != "y":
        print("\nAnda sudah dewasa tetapi tidak boleh membawa motor ATV (wajib didampingi instruktur).")

    elif paket_1008 == 3 and umur_1008 < 17:
        print("\nAnda belum memenuhi syarat usia untuk ATV.")

    total_awal_1008 = harga_satuan_1008 * jumlah_tiket_1008

    # Multi-if terpisah untuk diskon akumulatif
    diskon_1008 = 0

    if total_awal_1008 >= 200000:
        diskon_1008 += total_awal_1008 * 0.10

    if jumlah_tiket_1008 >= 4:
        diskon_1008 += total_awal_1008 * 0.05

    if umur_1008 >= 60:
        diskon_1008 += total_awal_1008 * 0.05

    total_bayar_1008 = total_awal_1008 - diskon_1008

    # Audit Status Operasional
    status_tiket_1008 = jumlah_tiket_1008 > 0
    status_paket_1008 = paket_valid_1008
    status_pembayaran_1008 = total_bayar_1008 > 0

    print("\n" + "=" * 50)
    print("STRUK TRANSAKSI")
    print("=" * 50)
    print("Nama Pengunjung :", nama_1008)
    print("Umur            :", umur_1008)
    print("Paket           :", nama_paket_1008)
    print("Harga Satuan    : Rp", format(harga_satuan_1008, ","))
    print("Jumlah Tiket    :", jumlah_tiket_1008)
    print("Total Awal      : Rp", format(total_awal_1008, ","))
    print("Diskon          : Rp", format(int(diskon_1008), ","))
    print("Total Bayar     : Rp", format(int(total_bayar_1008), ","))

    print("\nAUDIT STATUS OPERASIONAL")
    print("Status Tiket      :", status_tiket_1008)
    print("Status Paket      :", status_paket_1008)
    print("Status Pembayaran :", status_pembayaran_1008)

    print("=" * 50)
    print("Transaksi selesai.")