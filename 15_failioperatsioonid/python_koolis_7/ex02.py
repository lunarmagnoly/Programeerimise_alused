"""
Tee uus fail luuletus.txt ning lisa sinna järgmine luuletus:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.

Koosta programm, mis kuvab ekraanile luuletuse read,
kuid lisab nende ette rea järjekorranumbri ja iga rea järele sulgudesse reas asuvate sümbolite arvu e. rea pikkuse.
"""


def read_lines_from_file(filename: str):
    with open(filename, encoding="utf-8") as f:
        line_count = 1
        for line in f:
            char_count = len(line)
            print(f"{line_count} - {line.rstrip()} ({char_count})") #.rstrip() deletes \n in the end
            line_count += 1



def write_lines_from_file(filename: str):
    file_dict = {}

    with open(filename, encoding="utf-8") as f:
        line_count = 1
        for line in f:
            file_dict.update({line_count: line})
            line_count += 1
        return file_dict


if __name__ == '__main__':
    read_lines_from("luuletus.txt")

