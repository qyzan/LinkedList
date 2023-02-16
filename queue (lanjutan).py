import time #delay untuk setiap inputan
#Operasi Create
s = []
total_per_hari = 0
#Operasi is Empety
def isEmpty (s):
    if len(s) <= 0 :
        return True
    else : 
        return False
#Operasi isFull
def isFull (s):
    if total_per_hari >= 10:
        return True
    else :
        return False

#Operasi Enqueue
def tambah_antrian(s,plat_motor,tipe_motor,jenis_motor):
    global total_per_hari
    total_per_hari = total_per_hari + 1
    x = {'motor_plat':plat_motor, 'no_antrian':total_per_hari, 'motor_tipe':tipe_motor, 'motor_jenis':jenis_motor}
    s.append(x)
    print('>> No. Antrian Baru Telah Tersimpan \nNo. Antrian --> %s'%(x['no_antrian']))

#Operasi Dequeue    
def panggil_antrian (s):
    matic = 'Rp. 55.000'
    bebek = 'Rp. 50.000'
    sport = 'Rp. 70.000'
    if isEmpty(s) :
        return print('Antrian Masih Kosong \nHarap Masukkan Antrian Terlebih Dahulu')
    else :
        p = (s.pop(0))
        if p['motor_jenis'] == 'Matic':
            return print('\tMemanggil Antrian \nNo.Antrian\t: {satu}\nPlat Motor\t: {dua}\nTipe Motor\t: {tiga}\nJenis Motor\t: {empat}\nHarga Service\t: {lima}'
            .format(
                satu = str(p['no_antrian']),
                dua = str(p['motor_plat']),
                tiga = str(p['motor_tipe']),
                empat = str(p['motor_jenis']),
                lima = matic
            )
        )
        elif p['motor_jenis'] == 'Bebek':
            return print('\tMemanggil Antrian \nNo.Antrian\t: {satu}\nPlat Motor\t: {dua}\nTipe Motor\t: {tiga}\nJenis Motor\t: {empat}\nHarga Service\t: {lima}'
            .format(
                satu = str(p['no_antrian']),
                dua = str(p['motor_plat']),
                tiga = str(p['motor_tipe']),
                empat = str(p['motor_jenis']),
                lima = bebek
            )
        )
        elif p['motor_jenis'] == 'Sport' :
            return print('\tMemanggil Antrian \nNo.Antrian\t: {satu}\nPlat Motor\t: {dua}\nTipe Motor\t: {tiga}\nJenis Motor\t: {empat}\nHarga Service\t: {lima}'
            .format(
                satu = str(p['no_antrian']),
                dua = str(p['motor_plat']),
                tiga = str(p['motor_tipe']),
                empat = str(p['motor_jenis']),
                lima = sport
            )
        )
def Tampil_Semua(s) :
    if (len(s) == 0):
        print("Data Antrian Masih Kosong. \nSilahkan Masukkan Data Antrian Terlebih Dahulu.")
    else:
        print ("\t- Ada %s Antrian Motor Untuk Diservice -"%(len(s)))
        for i in s: 
            time.sleep(0.2)
            print (">",'No. Antrian\t:',i['no_antrian'], '\nNo. Plat Motor\t:', i['motor_plat'],'\nTipe Motor\t:', i['motor_tipe'],'\nJenis Motor\t:', i['motor_jenis'])
            print('-'*36)

def contdown(w):
    while w:
        menit,detik = divmod(w,60)
        format_waktu = '{:02d}:{:02d} '.format(menit,detik)
        print(format_waktu,end="\r")
        time.sleep(1)
        w -= 1

while True:
    try :
        print('\t[-Program Antrian Pasien-] \n[1] {satu}\n[2] {dua}\n[3] {tiga}\n[4] {empat}'
            .format(
                satu = 'Tambah Antrian',
                dua = 'Panggil Pelanggan',
                tiga = 'Tampil Daftar Antrian',
                empat = 'Keluar'
            )
            
        )
        inputan = int(input("Silahkan Pilih : "))
        print ('-'*36)
        if (inputan == 1):
            if (isFull(s) == True):
                print ('Kapasitas Antrian Sudah Mencapai Batas Hari Ini')
                print('No. Antrian Akan Diriset Ulang')
                contdown(5)
                print('-Terima Kasih-')
                total_per_hari = 0
            else:
                pushinput = input("No. Plat Motor\t\t\t:").upper()
                pushinput1 = input('Tipe Motor\t\t\t:').title()
                pushinput2 = input('Jenis Motor(Bebek, Matic, Sport):').title() 
                if (pushinput2 == 'Bebek' or pushinput2 == 'Matic' or pushinput2 == 'Sport'):
                    tambah_antrian(s,pushinput,pushinput1,pushinput2)
                else :
                    print('-'*36)
                    print ('Salah Input Dibagian Jenis Motor \nHarap Masukkan Jenis Motor Yang Sudah Disediakan')
                    print('-'*36)
                    time.sleep(0.6)
                    continue

        elif (inputan == 3):
            Tampil_Semua(s)
            x = input("Continue? (yes/no) : ").lower()
            if (x == 'yes'):
                print("-"*36)
                continue
            elif (x == 'no'):
                print ('Terima Kasih')
                break
            elif(x != 'yes' or x != 'no'):
                print('-'*36)
                print('Salah Input\n')
                break

        elif (inputan == 2):
            panggil_antrian(s)
        elif (inputan == 4):
            print("> Terima Kasih")
            break
        else:
            print ("Masukkan angka sesuai Menu")
        print("\n")
        time.sleep(0.6)

    except:
        time.sleep(0.5) 
        print ('\n-Pilih dengan angka bukan huruf-\n-Jika Ingin Berhenti Ketik "4"-\n')
        continue      