"""
Speed and Travel Time Task

Increasing a car's speed reduces the time needed to reach a destination.
But how much time can actually be saved?

Write a program that:
1. asks the user for the travel distance (in kilometers) at the start of the program;
2. repeatedly asks the user for a driving speed (in km/h);
3. calculates and prints:
   - the travel time for the given speed;
   - the difference in travel time compared to the previous speed;
4. stops execution if the user presses Enter without entering a speed.
"""



def ask_user_car_speed() -> int:
    return int(input("Sisestage auto kiirus: "))


def calculate_estimated_travel_time_in_seconds(distance: int, car_speed: int) -> float:
    time_in_hours = distance / car_speed
    return time_in_hours * 3600


def format_time_string (hours: int, minutes: int, seconds: int) -> str:
    result_values = []
    if hours == 1:
        result_values += ["1 tund"]
    elif hours > 1:
        result_values += [f"{hours} tundi"]
    if minutes == 1:
        result_values += ["1 minut"]
    elif minutes > 1:
        result_values += [f"{minutes} minutit"]
    if seconds == 1:
        result_values += ["1 sekund"]
    elif seconds > 1:
        result_values += [f"{seconds} sekundit"]
    match(len(result_values)):
        case 1:
            return result_values[0]
        case 2:
            return f"{result_values[0]} ja {result_values[1]}"
        case 3:
            return f"{result_values[0]}, {result_values[1]} ja {result_values[2]}"
        case _:
            return ", ".join(result_values)


def display_travel_time_difference(previous_travel_time: float, travel_time: float) -> None:
    hours, minutes, seconds = convert_to_hours_mins_secs(travel_time)
    time_string = format_time_string(hours, minutes, seconds)
    print(f"Sõidule kulub {time_string}.")
    if previous_travel_time != -1:
        difference = previous_travel_time - travel_time
        hours, minutes, seconds = convert_to_hours_mins_secs(abs(difference))
        time_string = format_time_string(hours, minutes, seconds)
        if difference > 0:
            print(f"Jõuad kohale {time_string} hiljem.")
        elif difference == 0:
            print(f"Jõuad kohale sama ajaga.")
        else:
            print(f"Jõuad kohale {time_string} varem.")



def convert_to_hours_mins_secs(time_in_seconds: float) -> tuple[int, int, int]:
    time_in_seconds = round(time_in_seconds)
    hours = time_in_seconds // 3600
    remainding_seconds = time_in_seconds % 3600
    minutes = remainding_seconds // 60
    remainding_seconds = remainding_seconds % 60
    return hours, minutes, remainding_seconds


if __name__ == '__main__':
    distance = int(input("Sisestage läbitav vahemaa kilomeetrites: "))
    speed_text = "1"
    previous_travel_time = -1
    while len(speed_text) > 0:
        speed_text = input("Sisestage sõidukiirus: ")
        if speed_text.isdigit():
            speed = int(speed_text)
            travel_time = calculate_estimated_travel_time_in_seconds(distance, speed)
            display_travel_time_difference(previous_travel_time, travel_time)
            previous_travel_time = travel_time