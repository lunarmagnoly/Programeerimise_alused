"""
Koosta programm, mis küsib kasutajalt rea, mille järele ta soovib failis luuletus.txt uut rida lisada
ning seejärel lisab kasutaja poolt sisestatud rea nt:

Sisesta rida, mille järele soovid uut rida lisada:
>> Padja, teki viskan maha,
Sisesta rida, mida soovid lisada:
>> üles ärgata ma ei taha,
Tulemus failis luuletus.txt:

Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
üles ärgata ma ei taha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.
"""
import ex02

#find if line exists in file



#add new line after the found line.
if __name__ == '__main__':
    line = input("Sisesta rida, mille järele soovid uut rida lisada:")
    filename = input("Sisestage faili nimi: ")
    read_lines_from_file(line, filename)
