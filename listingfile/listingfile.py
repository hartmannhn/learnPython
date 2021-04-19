import os

print('listingfile by @hartmannhn')
print('scan target directory and produces list of files and folders contained\n')
baseDir = ''
filename = ''


while(True):
    #==============Nama lokasi yang mau discan====
    print('sample format : D:/Download/')
    print('choose target directory to scan: ')
    baseDir = input()
    #=============================================

    #==============Nama file disimpan=============
    print('sample format : yourFileName')
    print('choose output file name: ')
    filename = input()
    filename = filename + '.txt'
    #=============================================

    #==============Konfirmasi input===============
    print('Confirmation:')
    print('Target directory: %s' %baseDir)
    print('Output filename: %s' %filename)
    print('Input "y" to continue, "n" to reinput:')
    konfirm = input()
    if konfirm == 'y':
        break
    #=============================================

#init empty array for iteration
space = ' '
multiplier = 4

text_file = open(filename, "w", encoding="utf-8")

def listing(folderName,level):
    global text_file
    text_file.write((level-multiplier)*space+"Isi folder %s\n" %folderName)
    with os.scandir(folderName) as entries:
        for entry in entries:
            text_file.write(level*space+"%s\n" %entry.name)
            if not entry.is_file():
                listing(folderName+entry.name+'/',level+multiplier)
        text_file.write("\n")

#start writing in txt file
listing(baseDir,0)
        
text_file.close()
