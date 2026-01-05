

"""
Ask the user for their name and age.
Print a greeting that says whether the person is between 7 and 18 years old.
"""

def greeting_according_to_age(age: int, name: str)-> str:
    if 7 <= age <= 18:
        return f"Tere, {name}! Olete 7 kuni 18 aastat vana. Edu!"
    return f"Tere, {name}! Te ei ole 7 kuni 18 aastat vana. Ilusat päeva."

if __name__ == '__main__':
    input_name = input("Mis Te nimi on? ")
    input_age = int(input("Kui vana Te olete? "))
    print(greeting_according_to_age(input_age, input_name))