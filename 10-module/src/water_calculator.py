# water_calculator.py

def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            argument / 10
        except TypeError:
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")

    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage

    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"


if __name__ == "__main__":
    try:
        print(water_left("5", 100, 3))
    except TypeError as err:
        print(err)
    except RuntimeError as err:
        print(err)