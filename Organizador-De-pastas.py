import os
import shutil

path = r'o caminho da pasta' # usar r se quiser , é apenas pro python entender que as contra-barra e um local da pasta
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)
        shutil.move
