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


def match_line(pattern, line):
    return bool(re.fullmatch(pattern, line))


def check_animal_list(file_path):
    female_pattern = r'^[a-fA-F\d]{8}\-[a-fA-F\d]{4}\-[a-fA-F\d]{4}\-[a-fA-F\d]{4}\-[a-fA-F\d]{12}_F_[\d]\.[\d]{3}e[\-\+][\d]{2}$'
    male_pattern = r'^[a-fA-F\d]{8}\-[a-fA-F\d]{4}\-[a-fA-F\d]{4}\-[a-fA-F\d]{4}\-[a-fA-F\d]{12}_M_[\d]\.[\d]{3}e[\-\+][\d]{2}$'

    with open(file_path, 'r') as reader_file:
        female_scores = 0
        male_scores = 0
        for line in reader_file:
            female_scores += match_line(female_pattern, line.strip())
            male_scores += match_line(male_pattern, line.strip())

        reader_file.close()

    print(f'{female_scores} {male_scores}')
    return female_scores, male_scores


if __name__ == '__main__':
    assert check_animal_list('s_animals_sce.txt') == (2, 2)
    assert check_animal_list('animals_sc_corrupted.txt') == (6, 0)
