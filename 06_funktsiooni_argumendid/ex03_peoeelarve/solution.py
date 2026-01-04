

def eelarve(number_of_invited_people:int) -> int:
    """
    Calculate party budget depending on number of invited people
    food: 10 EUR per person
    venue: 55 EUR fixed price

    :param number_of_invited_people: int
    :return: party_budget: int
    """
    return number_of_invited_people * 10 + 55

if __name__ == '__main__':
    number_of_invited_guests = int(input("Mitu inimest on peole kutsutud? "))
    number_of_guests_confirmed = int(input("Mitu inimest tuleb? "))
    maximum_party_budget = eelarve(number_of_invited_guests)
    minimum_party_budget = eelarve(number_of_guests_confirmed)
    print(f"Maksimaalne eelarve on {maximum_party_budget} eurot \n"
          f"Minimaalne eelarve on {minimum_party_budget} eurot")