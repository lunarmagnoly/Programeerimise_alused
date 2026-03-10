"""
Palindroomiks nimetatakse sõna (ka sõnaühendit), mis on nii vasakult paremale kui paremalt vasakule lugedes täpselt ühesugunem
(näit. "kook", "kuulilennuteetunneliluuk" jne).
Loo programm, mis trükib ekraanile välja kõik tekstifailis olevad sõnad, mis on palindroomid.
Alustekstiks võid kasutada suvalist teksti, kuid katsetada tasuks ka sõnaloenditega, kus iga sõna asub eraldi real
(näit. eesti keele sõnade algvormid e. lemmad veebilehelt http://www.eki.ee/tarkvara/wordlist/).
"""

#def sise lähem sõna slaisime ja vaatame kas esimene jf viimane tähemd on samad teine ja eelvimmane jne.
def palindrome_check(word: str):
    lenght = len(word)
    for i in range(0, 1, lenght):
        for j in range (-1, -1, lenght):
            if i == j:
                return True
    return False


#loeme kõik sõnad failist ja kontrollime mis võivad olla palindroomiks, kuvada neid ekranile

def print_palindrome(filename: str):
    with open(filename, encoding="utf-8") as f:
        for word in f:
            if palindrome_check(word):
                print(word)


if __name__ == '__main__':
    print_palindrome("palindrome_check.txt")