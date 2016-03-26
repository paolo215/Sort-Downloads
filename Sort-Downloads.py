#!/usr/bin/python env
import os
import shutil
import config

DOWNLOADS_PATH = config.DOWNLOADS_PATH

def main():
    extensions = []
    files = os.listdir(DOWNLOADS_PATH)
    for i in files:
        ext = os.path.splitext(i)[1]
        if ext not in extensions:
            extensions.append(ext)

    for i in extensions:
        if i == "":
            if not os.path.exists(DOWNLOADS_PATH + "\_ETC"):
                os.mkdir(DOWNLOADS_PATH + "\_ETC")
        if not os.path.exists(DOWNLOADS_PATH + "\\" + i):
            os.mkdir(DOWNLOADS_PATH + "\\" + i.upper())

    for i in files:
        ext = os.path.splitext(i)[1].upper()
        if ext == "" and i[0] != ".":
            shutil.move(DOWNLOADS_PATH + "/" + i, DOWNLOADS_PATH + "/_ETC/" + i)
        else:
            shutil.move(DOWNLOADS_PATH + "/" + i, DOWNLOADS_PATH  +"/" + ext.upper() + "/" + i)

if __main__ == "__name__":
    main()
