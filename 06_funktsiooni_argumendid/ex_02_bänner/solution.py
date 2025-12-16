

def banner(reklaamlause: str) -> str:
    """
    Convert text to uppercase

    :param reklaamlause: str
    :return: reklaamlause: str
    """
    return reklaamlause.upper()


if __name__ == '__main__':
    number_of_banners = int(input("Mitu korda soovitakse reklaamlauset kuvada? "))
    banner_message = input("Sisestage oma reklaamlause: \n")
    for i in range (number_of_banners):
        print(banner(banner_message))