"""
Create four lists for a dictionary (numbers, Estonian, English, Italian) containing:
numbers – 1, 2, 3, 4
Estonian – üks, kaks, kolm, neli
English – one, two, three, four
Italian – uno, due, tre, quattro

Print all elements in a table format on the screen:
1 – üks – one – uno
2 – kaks – two – due
...

Add two more elements to the numbers and Estonian lists.
Check whether the Italian words list contains the element "tre".
Print the elements of all four lists in alphabetical order.

"""


numbers = [1, 2, 3, 4]
estonian_numbers = ["üks", "kaks", "kolm", "neli"]
english_numbers = ["one", "two", "three", "four"]
italian_numbers = ["uno", "due", "tre", "quattro"]
for i in range(len(numbers)):
    print(f"{numbers[i]} - {english_numbers[i]:^4} - {english_numbers:^5} - {italian_numbers:^7}")
if "tre" in italian_numbers:
    print("'tre' eksisteerib itaalia järjendis.")

print("Numbrid sorteeritud:")
numbers.sort()
for number in numbers:
    print(number)

all_languages = sorted(estonian_numbers)
all_languages += sorted(english_numbers)
all_languages += sorted(italian_numbers)

print("Iga keel eraldi sorteeritud: ")
for value in all_languages:
    print(value)

all_languages.sort()
print("Kõik keeled korraga sorteeritud:")
for value in all_languages:
    print(value)
