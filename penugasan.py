#Program Konversi Uang Indonesia
while True: 
    print('='*37)
    print("Program Konversi Uang Indonesia (IDR)")
    print('='*37)

    #Pemilihan Konversi IDR
    print('(1). IDR to USD')
    print('(2). IDR to EUR')
    print('(3). IDR to JPY')
    print('(4). IDR to KRW')
    print('(5). IDR to GBP')

    #Pendeklarasian Variabel Pemilihan
    pilih_konversi = int(input('Pilih Konversi Uang (1/2/3/4/5): '))

    #Pemilihan Konversi IDR If-Elif-Else
    if pilih_konversi == 1:
        #Pendeklarasian Variabel Nominal
        nominal_idr = float(input("Masukkan Nominal Awal Anda(IDR): "))
        nominal_usd=nominal_idr/15436.00
        print("Nominal Anda Sekarang (USD): $", round(nominal_usd, 3))
    elif pilih_konversi == 2:
        #Pendeklarasian Variabel Nominal
        nominal_idr = float(input("Masukkan Nominal Awal Anda(IDR): "))
        nominal_eur=nominal_idr/17017.40
        print("Nominal Anda Sekarang (EUR): €", round(nominal_eur, 3))
    elif pilih_konversi == 3:
        #Pendeklarasian Variabel Nominal
        nominal_idr = float(input("Masukkan Nominal Awal Anda (IDR): "))
        nominal_jpy=nominal_idr/108.15
        print("Nominal Anda Sekarang (JPY): ¥", round(nominal_jpy, 3))
    elif pilih_konversi == 4:
        #Pendeklarasian Variabel Nominal
        nominal_idr = float(input("Masukkan Nominal Awal Anda (IDR): "))
        nominal_krw=nominal_idr/11.50
        print("Nominal Anda Sekarang (KRW): ₩", round(nominal_krw, 3))
    elif pilih_konversi == 5:
        #Pendeklarasian Variabel Nominal
        nominal_idr = float(input("Masukkan Nominal Awal Anda (IDR): "))
        nominal_gbp=nominal_idr/20147.00
        print("Nominal Anda Sekarang (GBP): £", round(nominal_gbp, 3))
    else :
        #Jika Pemilihan Konversi 
        print('Konversi Belum Tersedia!!')

print("Program Telah Selesai")
print("Terimakasih")

