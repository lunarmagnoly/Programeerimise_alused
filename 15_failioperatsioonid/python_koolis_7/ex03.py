"""
Tee programm, mis väljastab failist luuletus.txt kasutaja poolt soovitud rea nt:

Mitmendat rida soovid kuvada:
>> 7
Error tuleb ette siis,
NB! Faili avamiseks ja rea väljastamiseks koosta eraldi alamprogramm (ehk funktsioon).
"""

import ex02

def read_specific_line(line_count, filename):
    file_dict = ex02.write_lines_from_file(filename)
    for key, value in file_dict.items():
        if key == line_count:
            print(value)


if __name__ == '__main__':
    line_count = int(input("Sisestage rida numbri: ").strip())
    filename = input("Sisestage faili nimi: ")
    read_specific_line(line_count, filename)

