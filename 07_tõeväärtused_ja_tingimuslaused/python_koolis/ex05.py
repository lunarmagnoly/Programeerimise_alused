

"""
Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides ja väljastab tulemuse Fahrenheiti kraadides.
Kuidas muuta programmi nii, et võimalik oleks teisendamine nii üht- kui teistpidi? Proovi.
"""

def convert_temperature_from_c_to_f (temperature_in_c: float) -> str:
    return f"{temperature_in_c * 1.8 + 32} °F"


def convert_temperature_from_f_to_c (temperature_in_f: float) -> str:
    return f"{(temperature_in_f - 32) / 1.8} °C"


if __name__ == '__main__':
    choose_conversion = input("Vali teisendamise suund: \n\n 1 – Celsius → Fahrenheit\n 2 – Fahrenheit → Celsius\n\n")
    convert_temperature_input = float(input("Sisesta temperatuur: "))
    conversion_result = ""
    if choose_conversion.strip() == "1":
        conversion_result = convert_temperature_from_c_to_f(convert_temperature_input)
        print(f"Tulemus on {conversion_result}")
    elif choose_conversion.strip() == "2":
        conversion_result = convert_temperature_from_f_to_c(convert_temperature_input)
        print(f"Tulemus on {conversion_result}")
    else:
        print("Valikud on ainul 1 ja 2")