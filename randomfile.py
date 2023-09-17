import re; import os; import sys
from threading import Timer; from os.path import abspath; from datetime import datetime
from re import search; from os import scandir, getcwd, execl; from random import randint


## Функция №1: Выбор рандомного файла из определенной папки
def pwd(ruta=getcwd()):
        return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]