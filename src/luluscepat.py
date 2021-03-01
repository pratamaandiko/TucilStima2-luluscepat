# read dari file.txt
with open('file.txt') as f:
    lines = f.read().splitlines()
# print logo lulus cepat
print(' __               __                           ______                              __     ')
print('|  \             |  \                         /      \                            |  \    ')
print('| $$     __    __| $$__    __  _______       |  $$$$$$\ ______   ______   ______ _| $$_   ')
print('| $$    |  \  |  | $|  \  |  \/       \      | $$   \$$/      \ /      \ |      |   $$ \  ')
print('| $$    | $$  | $| $| $$  | $|  $$$$$$$      | $$     |  $$$$$$|  $$$$$$\ \$$$$$$\$$$$$$  ')
print('| $$    | $$  | $| $| $$  | $$\$$    \       | $$   __| $$    $| $$  | $$/      $$| $$ __ ')
print('| $$____| $$__/ $| $| $$__/ $$_\$$$$$$\      | $$__/  | $$$$$$$| $$__/ $|  $$$$$$$| $$|   '+chr(92))
print('| $$     \$$    $| $$\$$    $|       $$       \$$    $$\$$     | $$    $$\$$    $$ \$$  $$')
print(' \$$$$$$$$\$$$$$$ \$$ \$$$$$$ \$$$$$$$         \$$$$$$  \$$$$$$| $$$$$$$  \$$$$$$$  \$$$$ ')
print('                                                               | $$                       ')
print('                                                               | $$                       ')
print('                                                                \$$                       ')
print('Jangan leyeh-leyeh terus boy...\n')

print(',-----,-----,-----,-----,-----,-----,-----,-----,-----,-----,-----,-----,-----,-----.')
print("'-----'-----'-----'-----'-----'-----'-----'-----'-----'-----'-----'-----'-----'-----'")

# print apa yang dibaca dari file.txt
print("Daftar kode mata kuliah(input dari file.txt):")
for line in lines:
    print(line)

# apa yang dibaca di file.txt dijadikan array dan disimpan pada variabel daftarmatkul
daftarmatkul =[]
for line in lines:
    daftarmatkul.append(line[:-1].split(', '))

# fungsi untuk mencari mata kuliah yang tidak memiliki prerequisit bukan prerequisit dari mata kuliah lain lalu mereturnkanya
def matkulnotprerec(daftarmatkul):
    notpreq = [] 
    for i in range(len(daftarmatkul)):
    # melakukan pencarian apakah pada array daftarmatkul ada yang panjangnya 1(berarti dia tidak memiliki prerequisit)
        if (len(daftarmatkul[i]) == 1):
            isprec = False
            for j in range(len(daftarmatkul)):
                # skip jika yang di cek elemen dirinya sendiri
                if (j == i):
                    continue
                else:
                    # jika elemen tersebut terdapat pada elemen lain, berarti adalah prerequisit dari mata kuliah lain
                    if daftarmatkul[i][0] in daftarmatkul[j]:
                        isprec = True
            # jika tidak memmiliki prerequisit dan juga bukan prerequisit dari mata kuliah lain, maka akan disimpan di array
            if (isprec == False):
                notpreq.append(daftarmatkul[i][0])
    return notpreq

# menyimpan list mata kuliah bukan prerequisit ke variabel notpreq dan menghapusnya dari array daftarmatakul
notpreq = matkulnotprerec(daftarmatkul)              
for i in notpreq:
    daftarmatkul.remove([i])

# fungsi rekursif untuk menentukan urutan pengambilan mata kuliah berdasarkan prerequisit
def luluscepat(daftarmatkul,ordering):
    # basis
    if(len(daftarmatkul) == 0):
        return
    # rekursif
    # pencarian apakah pada array daftarmatkul ada yang panjangnya 1(tidak memiliki prerequisit), jika ada dimasukan pada variabel ordering
    temp = []
    for mat in daftarmatkul:
        if(len(mat) == 1):
            temp.append(mat[0])
    ordering.append(temp)

    # menghapus matkul tersebut dari array daftarmatkul
    for l in temp:
        daftarmatkul.remove([l])

    # menghapus matkul tersebut dalam list prerequisit mata kuliah lain
    for i in range(len(daftarmatkul)):
        for z in temp:
            if z in daftarmatkul[i] :
                daftarmatkul[i].remove(z)
    luluscepat(daftarmatkul,ordering)


ordering = []
luluscepat(daftarmatkul,ordering)

print("\n               HASIL PENJADWALAN BERDASARKAN PREREQUISIT SETIAP MATA KULIAH\n")
# print mata kuliah yang bisa diambil sesuai semester
for i in range (len(ordering)):
    print("Semester " + str(i+1)+" : ", end="")
    for j in range(len(ordering[i])):
        if (j < len(ordering[i]) - 1):
            print(ordering[i][j]+', ', end="")
        else:
            print(ordering[i][j], end="")
    print()

# print mata kuliah yang tidak memiliki pre requisit, dan bisa diambil di semester berapapun
if len(notpreq) != 0:
    print("Mata kuliah yang bisa diambil di semester berapapun(tidak memiliki prerequisit dan bukan mata kuliah prerequisit):", end=" ")
    for i in range(len(notpreq)):
        if (i < len(notpreq) -1):
            print(notpreq[i] + ', ', end='')
        else:
            print(notpreq[i])

print(',-----,-----,-----,-----,-----,-----,-----,-----,-----,-----,-----,-----,-----,-----.')
print("'-----'-----'-----'-----'-----'-----'-----'-----'-----'-----'-----'-----'-----'-----'")


