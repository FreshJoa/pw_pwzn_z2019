"""
Jesteś informatykiem w firmie Noe's Animals Redistribution Center.
Firma ta zajmuje się międzykontynentalnym przewozem zwierząt.
---------
Celem zadania jest przygotowanie funkcji pozwalającej na przetworzenie
pliku wejściowego zawierającego listę zwierząt do trasnportu.
Funkcja ma na celu wybranie par (samiec i samica) z każdego gatunku,
tak by łączny ładunek był jak najlżeszy (najmniejsza masa osobnika
rozpatrywana jest względem gatunku i płci).
---------
Na 1 pkt.
Funkcja ma tworzyć plik wyjściowy zwierający listę wybranych zwierząt
w formacie wejścia (takim samym jak w pliku wejściowym).
Wyjście ma być posortowane alfabetycznie względem gatunku,
a następnie względem nazwy zwierzęcia.
---------
Na +1 pkt.
Funkcja ma opcję zmiany formatu wejścia na:
"<id>_<gender>_<mass>"
(paramter "compressed") gdzie:
- "id" jest kodem zwierzęcia (uuid),
- "gender" to jedna litera (F/M)
- "mass" zapisana jest w kilogramach w notacji wykładniczej
z dokładnością do trzech miejsc po przecinku np. osobnik ważący 456 gramów
ma mieć masę zapisaną w postaci "4.560e-01"
---------
Na +1 pkt.
* Ilość pamięci zajmowanej przez program musi być stałą względem
liczby zwierząt.
* Ilość pamięci może rosnąć liniowo z ilością gatunków.
---------
UWAGA: Możliwe jest wykonanie tylko jednej opcji +1 pkt.
Otrzymuje się wtedy 2 pkt.
UWAGA 2: Wszystkie jednoski masy występują w przykładzie.
"""
from pathlib import Path
from collections import defaultdict


class NestedDict(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


def select_animals(input_path, output_path, compressed=False):
    with open(input_path, 'r') as reader_file:
        headers = reader_file.readline()
        mass_dict_kg = {'mg': 0.000001, 'g': 0.001, 'kg': 1, 'Mg': 1000}
        animal_dict = NestedDict()

        if compressed:
            headers = 'uuid_gender_mass'
            gender_dict = {'male': 'M', 'female': 'F'}
            for line in reader_file:
                row = line.strip().split(',')
                mass = row[1].split()
                mass_kg = float(mass[0]) * mass_dict_kg.get(mass[1])
                animal_dict[row[2]][row[4]][mass_kg] = f"{row[0]}_{gender_dict.get(row[4])}_{format(mass_kg, '.3e')}"
            with open(output_path, 'w') as writer_file:
                writer_file.write(f"{headers}\n")
                for key in sorted(animal_dict.keys()):
                    min_fmale_mass_key = min(animal_dict[key]['female'].keys())
                    writer_file.write(f"{animal_dict[key]['female'][min_fmale_mass_key]}\n")
                    min_male_mass_key = min(animal_dict[key]['male'].keys())
                    writer_file.write(f"{animal_dict[key]['male'][min_male_mass_key]}\n")

        else:
            for line in reader_file:
                # print(line)
                row = line.strip().split(',')
                mass = row[1].split()
                mass_kg = float(mass[0]) * mass_dict_kg.get(mass[1])
                animal_dict[row[2]][row[4]][mass_kg] = line

            with open(output_path, 'w') as writer_file:
                writer_file.write(headers)
                for key in sorted(animal_dict.keys()):
                    min_fmale_mass_key = min(animal_dict[key]['female'].keys())
                    writer_file.write(animal_dict[key]['female'][min_fmale_mass_key])
                    min_male_mass_key = min(animal_dict[key]['male'].keys())
                    writer_file.write(animal_dict[key]['male'][min_male_mass_key])

        writer_file.close()
        reader_file.close()


if __name__ == '__main__':
    input_path = Path('s_animals.txt')
    output_path = Path('s_animals_s.txt')
    select_animals(input_path, output_path)
    with open(output_path) as generated:
        with open('s_animals_se.txt') as expected:
            assert generated.read() == expected.read()

    output_path = Path('s_animals_sc.txt')
    select_animals(input_path, output_path, True)
    with open(output_path) as generated:
        with open('s_animals_sce.txt') as expected:
            assert generated.read() == expected.read()
