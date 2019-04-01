##Nama  : Ivan Amar
##NIM   : L200170040
##Kelas : B
##Modul : 5

class Mahasiswa(object):
    """Class Manusia yang dibangun dari class manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

class MhsTIF (Mahasiswa):  
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool.')
        
Daftar = [MhsTIF ('Dewi',20,'Sukoharjo', 260000),
MhsTIF('Budianto',71,'Karanganyar', 290000),
MhsTIF('Ahmad Khoirudin',2,'Surakarta', 260000),
MhsTIF('Chandra Kurniawan',18,'Surakarta', 330000),
MhsTIF('Eka Sulistiani',4,'Boyolali', 240000),
MhsTIF('Fandi Fitrianta',32,'Salatiga', 270000),
MhsTIF('Deni Candra',13,'Klaten', 285000),
MhsTIF('Galuh Pratama',5,'Klaten', 245000),
MhsTIF('Yanto',23,'Klaten', 245000),
MhsTIF('Azis',64,'Karanganyar', 270000),
MhsTIF('Khalif',29,'Purwodadi', 265000)]

#====================================== NOMER 1===============================#
def ceknim (d):
    for i in d :
        print (i.NIM)

def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp

def urutnim(d):
    n = len(d)
    for i in range (n -1) :
        for k in range (n-i-1) :
            if d[k].NIM > d[k+1].NIM :
                swap(d,k,k+1)
##cara menampilkan
##urutnim(Daftar)
##ceknim(Daftar)
#======================================= NOMER 2 ==============================#
a = [2,6,7,9,4]
b = [5,8,10,3,1]
c = a + b
 
def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp

def urut(d):
    n = len (d)
    for i in range (n -1) :
        for k in range (n-i-1) :
            if d[k] > d[k+1] :
                swap(d,k,k+1)

urut(c)
print(c)

#======================================= NOMER 3 ==============================#
def swap(A, p, q):
    temp = A[p]
    A[p] = A[q]
    A[q] = temp
    
def cariposisiterkecil(A, darisini, sampaisini):
    posisiterkecil = darisini
    for i in range(darisini + 1, sampaisini):
        if A[1] < A[posisiterkecil]:
            posisiterkecil = 1
    return posisiterkecil

def bubblesort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                
def selectionsort(A):
    n = len(A)
    for i in range(n - 1):
        indexkecil = cariposisiterkecil(A, i, n)
        if indexkecil != i:
            swap(A, i, indexkecil)

def insertionsort(A):
    n = len(A)
    for i in range(1 ,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1 ,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubblesort(u_bub);ak=detak();print('Buble      : %g detik' %(ak-aw));
aw = detak();selectionsort(u_sel);ak=detak();print('Selection  : %g detik' %(ak-aw));
aw = detak();insertionsort(u_ins);ak=detak();print('Insertion  : %g detik' %(ak-aw));
