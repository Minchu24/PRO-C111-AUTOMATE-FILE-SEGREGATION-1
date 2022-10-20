import os
import shutil
#print(dir(os))
file=os.getcwd()
print("my current working directry is "+file)
#os.mkdir('abc')
#source=input('enter the source path')
source='C:/Users/minchu/Desktop/older'
#destination=input('enter the source path')
destination='C:/Users/minchu/Desktop/C111'

   
#shiftfiles=shutil.move(source,destination)
#print(os.listdir(shiftfiles))
path='C:/Users/minchu/Desktop/trex'
listoffiles=os.listdir(path)
print(listoffiles)
for file in listoffiles:
 root,extension=os.path.splitext(path)
print('root of the path',root)
print('extension of the path',extension)