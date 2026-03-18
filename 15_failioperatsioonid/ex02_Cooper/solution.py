"""
Ülesanne. Cooperi test

Cooper testis mõõdetakse, kui palju suudab inimene joosta 12 minutiga. On määratud erinevad hindenormid meestele ja naistele.
Koostada funktsioon, mis võtab argumentideks meetrite arvu ja jooksja soo ning tagastab:
•	Sõne „väga hea“, kui meetreid on meeste puhul vähemalt 2800 ja naiste puhul 2600 vähem
•	Sõne „nõrk“, kui meetreid on meeste puhul vähem kui 2000 ja naistel alla 1800
•	Sõne „rahuldav“ muudel juhtudel
•	Tulemused, mis jäävad alla „väga hea“, peavad lisaks teatama, mitu meetrit jäi järgmisest hindest puudu

Koostada programm, mis küsib kasutajalt:

•	failinime,
Programm peab:
•	lugema failist jooksutulemused (täisarvud) ja jooksjate sood (M või N);
•	funktsiooniga arvutama hinded ja väljastama need ekraanile
•	arvutama ja väljastama ekraanile sugude kaupa kõikide tulemuste täisarvuni ümardatud keskmised ning funktsiooni abil keskmised hinded.

Näide funktsiooni rakendamisest
#>>> hinda(1800,’N’)
’rahuldav, järgmisest hindest puudu 800 m’
#>>> hinda(1799,’N’)
’nõrk, järgmisest hindest puudu 1m’
#>>> hinda(2600,’N’)
’väga hea’
Näide programmi tööst
Faili cooper.txt sisu:
1900 N
1800 M
2700 M
2600 N
1400 M
3801 N
1500 N
1800 N

Programmi töö:

Sisestage failinimi: cooper.txt
N 1900 m, rahuldav, järgmisest hindest puudu 700 m
M 1800 m, nõrk, järgmisest hindest puudu 200 m
M 2700 m, rahuldav, järgmisest hindest puudu 100 m
N 2600 m, väga hea
M 1400 m, nõrk, järgmisest hindest puudu 600 m
N 3801 m, väga hea
N 1500 m, nõrk, järgmisest hindest puudu 300 m
N 1800 m, rahuldav, järgmisest hindest puudu 800 m
Keskmised:
M 1967 m, nõrk, järgmisest hindest puudu 33 m
N 2320 m, rahuldav, järgmisest hindest puudu 280 m
"""


def read_from_file(filename: str)-> list:
    list_from_file_data = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            distance, gender = line.split(" ")
            list_from_file_data.append((int(distance), gender))
    return list_from_file_data


def evaluate(distance: int, gender: str) -> str:
    good_result_male  = 2800
    acceptable_result_male = 2000
    good_result_female = 2600
    acceptable_result_female = 1800
    if (gender == 'M' and distance >= good_result_male) or (gender == 'N' and distance >= good_result_female):
        evaluation = "väga hea"
    elif (gender == 'M' and distance < acceptable_result_male) or (gender == 'N' and distance < acceptable_result_female):
        if gender == 'M':
            evaluation = f"nõrk, järgmisest hindest puudu {acceptable_result_male - distance}"
        else:
            evaluation = f"nõrk, järgmisest hindest puudu {acceptable_result_female - distance}"
    else:
        if gender == 'M':
            evaluation = f"rahuldav, järgmisest hindest puudu {good_result_male - distance}"
        else:
            evaluation = f"rahuldav, järgmisest hindest puudu {good_result_female - distance}"
    return evaluation


def average_distance(filename)-> str:
