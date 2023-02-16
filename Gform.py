from selenium import webdriver
import time

     
def countdown(detik): 

    while detik: 
        menit, detik = divmod(detik, 60) 
        waktu = '{:02d}:{:02d}'.format(menit, detik) 
        print (end='\r')
        print(waktu)
        time.sleep(1) 
        detik -= 1
    print('Buka chrome!!') 

detik = 5

countdown(int(detik))


print('\n')
lokasi = 'D:\chromedriver.exe'
chrome = webdriver.Chrome(lokasi)
chrome.get ('https://docs.google.com/forms/d/e/1FAIpQLSccjkIfuzP5gIH398GyM_06W5u7bldK90GAEWh64SxAdZ-uuA/viewform?fbzx=3436350974529355520')

time.sleep(2)
Nama = 'Khairul'
ketik = chrome.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
ketik.send_keys(Nama)

time.sleep(1)
Kelas = chrome.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div')
Kelas.click()

time.sleep(1)
nim = '4332101010'
nomor = chrome.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
nomor.send_keys(nim)

time.sleep(1)
kirim = chrome.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
kirim.click()

text = chrome.find_element_by_class_name('freebirdFormviewerViewResponseConfirmationMessage')
file = text.text
print(file)

if (file == 'Jawaban Anda telah direkam.'):
    print('Berhasil dikirim')
else :
    print('Tidak berhasil mengirim')


time.sleep(4)
chrome.back()
chrome.close()
print ('\n')
print('Chrome berhasil di close')