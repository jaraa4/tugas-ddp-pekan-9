#buatlah sebuah fungsi bernama celcius_ke_fahreinheit
print('## nomor 1 ##')
def celcius_ke_fahreinheit(celcius):
    fahreinheit=(celcius*9/5)+32
    return fahreinheit

suhu_celcius1 = 0
suhu_celcius2 = 100
suhu_fahreinheit1 = celcius_ke_fahreinheit(suhu_celcius1)
suhu_fahreinheit2 = celcius_ke_fahreinheit(suhu_celcius2)
print('suhu celcius', suhu_celcius1,'sama dengan',suhu_fahreinheit1)
print('suhu celcius', suhu_celcius2,'sama dengan',suhu_fahreinheit2)

#cetak 100 celcius ke 212 fahreinheit
suhu_fahreinheit = celcius_ke_fahreinheit(suhu_celcius2)
print('suhu celcius', suhu_celcius2, 'sama dengan', suhu_fahreinheit2)

print()
print('## Nomor 2##')
def genap_ganjil(bilangan):
    hitung = bilangan % 2 == 0 # menentukan bilangan ganjil atau genap
    return hitung #mengembalikan nilai hitung

angka = 4
hasil = genap_ganjil(angka)
print(f"Bilangan {angka} bernilai {hasil}")

angka2 = 7
hasil2 = genap_ganjil(angka2)
print(f"Bilangan {angka2} bernilai {hasil2}")

print()
print('## nomor 3 ##')

def cek_kelulusan(nilai):
    if nilai >=60:
        return 'lulus'
    else:
        return 'gagal'

nilai_kamu = 80
status = cek_kelulusan(nilai_kamu)
print(f"nilai: {nilai_kamu}, status: {status}")

nilai_kamu2 = 50
status2 = cek_kelulusan(nilai_kamu2)
print(f"nilai: {nilai_kamu2}, status: {status2}")

