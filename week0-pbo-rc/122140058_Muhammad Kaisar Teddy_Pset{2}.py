kamus_nilai_siswa = dict()

n = int(input('Enter the number of students: '))
print("Enter the name and the student's grade.")
for i in range(n):
    name = input(str(i+1) + '. ''Name: ')
    grade = int(input('Grade: '))
    kamus_nilai_siswa[name] = grade

print('grade = ', kamus_nilai_siswa)