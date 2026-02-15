class Provinsi:
    def __init__(this, ibukota, kabupaten, kecamatan):
        this.ibukota = ibukota
        this.kabupaten = kabupaten
        this.kecamatan = kecamatan
    def ubah_ibukota(this, ibukota_baru):
        this.ibukota = ibukota_baru

    def ubah_kabupaten(this, kabupaten_baru):
        this.kabupaten = kabupaten_baru
p1 = Provinsi("Pekanbaru", "Bengkalis", "Batsol")
p2 = Provinsi("Medan", "Labura", "marbau")
p3 = Provinsi("Padang", "Agam", "KamangBaru")

p1.ubah_ibukota("Palembang")
p1.ubah_kabupaten("Rohil")
print(p1.ibukota)
print(p1.kabupaten)    