

def pronksikarva_summa(coins_list: list[int])-> int:
    """
    Returns the sum of bronze coins (1, 2 and 5 cents) in the given list.
    """
    coins_sum = 0
    for coin in coins_list:
        if coin in {1, 2, 5}:
            coins_sum+=coin
    return coins_sum

if __name__ == '__main__':
    ask_file_name = input("Mis failis on müntide nimikiri? ")
    coin_list_file = open(ask_file_name)
    coins = []
    for line in coin_list_file:
        coins.append(int(line.strip()))
    coin_list_file.close()

