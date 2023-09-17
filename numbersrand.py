
import time; import random
from threading import Timer; from random import randint

## Функция №2: Генерация случайного шестизначного числа
def sixnumber(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)