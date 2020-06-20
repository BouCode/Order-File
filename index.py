import re
import os
import numpy as np
import shutil


def created_folders(arr_dir):
    arr_ext = []
    for i in range(len(arr_dir)):
        x, y = os.path.splitext(arr_dir[i])
        if y != '':
            arr_ext.append(y)

    arr_uniq = np.unique(arr_ext)

    for i in arr_uniq:
        os.mkdir(i)


def move_arch(arr_dir, src, dest):
    for i in range(len(arr_dir)):
        x, y = os.path.splitext(arr_dir[i])
        if y != '':
            shutil.copy(f'{src}/{arr_dir[i]}', f'{dest}/{y}')
            # shutil.move f'{src}/{arr_dir[i]}', f'{dest}/{y}')


if __name__ == "__main__":
    source = "/home/empire/Imágenes"
    destination = "/home/empire/Documentos/Python/BorrarImagenes"
    listDir = os.listdir(source)
    created_folders(listDir)
    print(listDir)
    move_arch(listDir, source, destination)
