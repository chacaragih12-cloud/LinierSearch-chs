def linear_search(names, target):
    for i in range(len(names)):
        if names[i] == target:
            return i # Mengembalikan indeks tempat target ditemukan
    return -1 # Jika tidak ditemukan

# Daftar nama
names = ['Ali', 'Budi', 'Charlie', 'Dian', 'Eva']
target = 'Dian'
result = linear_search(names, target)

if result!= -1:
    print(f'{target} ditemukan pada indeks {result}')
else:
    print(f'{target} tidak ditemukan dalam daftar.')

    