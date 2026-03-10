

def create_familiars_files(filename: str):
    """Loo fail tuttavad.txt ja lisa sinna vähemalt 6 tuttava perekonna- ja eesnimed
(iga tuttav uuele reale, perekonna- ja eesnimi tühikuga eraldatult).
Koosta programm, mis loeb failist andmed ja väljastab need ekraanile tähestikulises järjekorras.
Mõistlik on ilmselt kasutada järjendit ja sellega seonduvaid võimalusi (järjestamist).
Tähestikulises järjekorras salvestage tuttavate nimed ka uude faili tuttavad1.txt.
    """

    familiars = [
        "Tiit Sukk",
        "Teet Pukk",
        "Peep Nukk",
        "Tina Kukk",
        "Mari Tukk",
        "Sari Lukk",
        ""
    ]

    with open(filename, "w", encoding="utf-8") as f:
        for name in familiars:
            f.write(name + "\n")


def read_names_from(filename: str) -> list[str]:
    result = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            name = line.strip()
            if len(name) > 0:
                result.append(name.strip())
    return result


def sort_names(names):
    names_dict = {}
    for name in names:
        #võta nimest välja perekonnanimi(viimane)
        last_name = name.split()[-1]
        names_dict[(last_name, name)] = name
        #sorteeri
    sorted_keys = sorted(list(names_dict.keys()))
        #tagastada
    return [item[-1] for item in sorted_keys]


if __name__ == '__main__':
    filename = "tuttavad.txt"
    create_familiars_files(filename)
    names_from_file = read_names_from(filename)
    sorted_by_last_name = sort_names(names_from_file)
    for name in sorted_by_last_name:
        print(name)