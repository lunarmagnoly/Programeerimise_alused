

def elektrihind(electricity_price_in_s_kwh:float) -> float:
    """
    Convert electricity price from cents per kilowatt-hour (s/kWh)
    to euros per megawatt-hour (€/MWh)

    :param electricity_price_in_s_kwh: float
    :return: electricity_price_in_eur_mwh: float
    """
    return electricity_price_in_s_kwh * 10


if __name__ == '__main__':
    electricity_price_in_s_kwh = float(input("Sisesta elektrihind sentides kilovatt-tunni kohta: "))
    print(f"{electricity_price_in_s_kwh} s/kWh on {elektrihind(electricity_price_in_s_kwh)} €/MWh")
