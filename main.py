nama = 'fitrianingsih'
program = 'gaya gesek'

print(f'program {program} oleh {nama}')

def hitung_gayagesek(koefisiengesek, gayanormal):
    gayagesek = koefisiengesek * gayanormal
    print(f'koefisien gesekan per satuan satuan gayanormal = N')
    print(f'sehingga gayagesek {gayagesek} newton')
    return(gayagesek)

# koefisiengesek = 5
# gayanormal = 10
gayagesek = hitung_gayagesek(5, 10)

def hitung_gayaberat(massabenda, grafitasibumi):
    gayaberat = massabenda * grafitasibumi
    print(f'massabenda kg {massabenda} kg per satuan percepatan = m/s**2')
    print(f'sehingga gayaberat = {gayaberat} Newton')
    return(gayaberat)

# massabenda = 5000
# grafitasibumi = 9.8
gayaberat = hitung_gayaberat(5000, 9.8)

def hitung_hukum2newton(massa, percepatan):
    hukum2newton = massa * percepatan
    print(f'massa kg {massa} kg per satuan percepatan = m/s**2')
    print(f'sehingga hukum2newton = {hukum2newton} Newton')
    return hukum2newton

# massa = 500
# percepatan 70
hukum2newton = hitung_hukum2newton(500, 70)
hukum2newton = hitung_hukum2newton(1000,80)
