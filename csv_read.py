from functii import *
a = 0

while True:
    try:
        if a == 0:
            data = introducere_fisier()
            outlet, ct, data_luna = transformare_ora(data)
            
        timp1 = introducere_ora(outlet, ct, data_luna)
        t1, t2 = cautare_sesiune(data, timp1)
        numar_joc(data, t1, t2)
        nume_joc(data, t1, t2)
        mizaj(data, t1, t2)
        b = int(input("\nIntroduceti 1 pentru a cauta in acest fisier"
                      "\nIntroduceti alt numar pentru a deschide un fisier nou\n"))
        if b = 1:
            a = 1
        else:
            a = 0
    except (ValueError, FileNotFoundError, OSError, IndexError):
        print('SAU INTRODUS DATE GRESITE SAU NU SE GASESC DATELE IN FISIER')
