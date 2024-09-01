def findSmallest(arr):
    #Mengeset nilai array terkecil dimulai dari index pertama
    smallest = arr[0]
    #Mengeset index array
    smallest_index = 0

    #Perulangan mulai dari 1 sampai dengan panjang array
    for i in range(1, len(arr)):
        #Jika array yang dipilih/aktif lebih kecil dari nilai smallest
        if arr[i] < smallest:
            #Maka nilai smallest akan digantikan dengan nilai array yang aktif saat ini
            smallest = arr[i]
            #Juga nilai index array akan digantikan dengan nilai array yang aktif saat ini
            smallest_index = i
    #Mengembalikan nilai index array 
    return smallest_index

def selectionSort(arr):
    #Set array baru
    newArr = []
    #Perulangan i sebanyak panjang array
    for i in range(len(arr)):
        #Set nilai terkecil dengan memanggil fungsi findSmallest
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    #Mengembalikan nilai newArr
    return newArr

#Memuculkan hasil
print(selectionSort([5,3,6,2,10,110,5818,41999,144,1,8]))
