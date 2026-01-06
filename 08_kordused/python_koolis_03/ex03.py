

"""
Koosta programm, mis aitab lastel treenida liitmist.
Programm peaks pakkuma välja juhuslike arvudega liitmistehteid ning ootama kasutajalt vastust.
Kui vastus on õige, kiitma kasutajat, kui aga vale, andma õige vastuse ja esitama uue tehte.
Järjest esitatavate tehete hulk võib olla programmis ette antud (näiteks 10), samuti võib olla ette antud piirid,
kui suuri arve kasutajalt küsitakse (näiteks 1 kuni 50).
Programm peaks pidama arvestust ka õigete vastuste üle ning väljastama pärast viimast tehet tulemuse.

Täiendusi vabal valikul:

Programm lubab kasutajal alguses sisestada, mitut tehet soovitakse.
Esitatavate arvude piirid saab kasutaja ette anda (maksimum või nii miinimum kui maksimum).
Küsitakse mitte ainult liitmistehteid, vaid ka teisi (lahutamine, korrutamine, jagamine).
Vastavalt lõpptulemusele reageeritakse erinevalt: "Ülihea!", "Olid tubli!", "Korralik keskmine tulemus!",
"Püüad järgmisel korral rohkem." vms.
"""

from random import randint, choice

operations = ["+", "-", "*", "**", "//"]
true_answers_reactions = ["Ülihea!", "Tubli!", "Hea vastus!"]
false_answers_reactions = ["Vale vastus.", "Harjuta rohkem.", "Püüa järgmisel korral rohkem."]

def get_calculation(min_value: int, max_value: int) -> tuple[str, int]:
    num1 = randint(min_value, max_value)
    num2 = randint(min_value, max_value)
    operation = choice(operations)
    if operation == "+":
        correct_answer = num1 + num2
        return f"{num1} + {num2} = ", correct_answer
    elif operation == "-":
        correct_answer = num1 - num2
        return f"{num1} - {num2} = ", correct_answer
    elif operation == "*":
        correct_answer = num1 * num2
        return f"{num1} * {num2} = ", correct_answer
    elif operation == "**":
        correct_answer = num1 ** num2
        return f"{num1} ** {num2} = ", correct_answer
    elif operation == "//":
        correct_answer = num1 // num2
        return f"{num1} // {num2} = ", correct_answer
    return "Tundmatu tehe", 0


def test_user_knowledge(min_value: int, max_value: int) -> tuple[bool, int]:
    calculation, correct_answer = get_calculation(min_value, max_value)
    user_answer = int(input(calculation))
    return user_answer == correct_answer, correct_answer


def practice_addition(count: int, min_value: int, max_value: int) -> None:
    correct_count = 0

    for i in range(count):
        true_answers_reaction = choice(true_answers_reactions)
        false_answers_reaction = choice(false_answers_reactions)
        print(f"Harjutus {i+1}/{count}")
        is_answer_correct, correct_answer = test_user_knowledge(min_value, max_value)
        if is_answer_correct:
            print(f"{true_answers_reaction} Vastasid õigesti.")
            correct_count+=1
        else:
            print(f"{false_answers_reaction} Õige vastus on {correct_answer}.")
    print(f"See oli viimane ülesanne. Kogusid {count}-st punkrist {correct_count}.")


if __name__ == '__main__':
    min_value = int(input("Milline peab olema minimaalne täisarvu väärtus? "))
    max_value = int(input("Milline peab olema maksimaalne täisarvu väärtus? "))
    count = int(input("Mitu korda soovid harjutada? "))
    practice_addition(count, min_value, max_value)

