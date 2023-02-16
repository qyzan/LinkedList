# Binary Search
array = [10,29,34,56,32,67,89,65,76,45]
kiri = 0
kanan = len(array)-1
inputan = 65
while kiri < kanan:
    mid = (kiri + kanan)//2
    if inputan == array[mid]:
        print(f'data {inputan} ditemukan di indek - {mid}')
        break
    elif inputan < array[mid]:
        kanan = mid - 1
    else:
        kiri = mid + 1