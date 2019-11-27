"""
Na (1 pkt.):
Napisz program do sprawdzenia poprawności skompresowanego wyjścia poprzedniej
funkcji.
Funkcja MUSI w swej implementacji korzystać z wyrażeń regularnych.

Funkcja na wejściu przyjmuje nazwę pliku do sprawdzenia, na wyjściu zwraca
dwuelementową tuplę zawierającą liczbę poprawnych wierszy:
- na indeksie 0 płeć F
- na indeksie 1 płeć M
"""
import re

def match_msg(pattern, msg):
    return bool(re.fullmatch(pattern, msg))

def check_animal_list(file_path):
    with open(file_path) as _file:
        lines = _file.readlines()
    
    ms = 0
    fs = 0

    for line in lines:
        line = line.strip()
        ms += match_msg(r'^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}_M_[\d]\.[\d]{3}e[\-\+][\d]{2}$',
        msg=line)
        fs += match_msg(r'^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}_F_[\d]\.[\d]{3}e[\-\+][\d]{2}$',
        msg=line)
        # import ipdb; ipdb.set_trace()   

    return (fs, ms)

if __name__ == '__main__':
    assert check_animal_list('s_animals_sce.txt') == (2, 2)
<<<<<<< HEAD
    assert check_animal_list('animals_sc_corrupted.txt') == (5, 1)
=======
    assert check_animal_list('animals_sc_corrupted.txt') == (5, 0)
>>>>>>> ce8d0bd5c5f2c47511100d6835cdd52b50a31c6f
