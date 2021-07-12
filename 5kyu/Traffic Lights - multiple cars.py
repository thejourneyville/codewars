light_sequence = "G" * 5 + "O" + "R" * 5


def convert(light_state, car_state):
    state = ""
    for idx, position in enumerate(light_state):
        if car_state[idx]:
            state += "C"
        elif str(position).isdecimal() and position >= 0:
            state += light_sequence[position]
        elif position == -1:
            state += "."

    return state


def traffic_lights(road, time_units):

    # light_timer_idx = len(light_sequence)

    history = []
    streetlight_idx, cars = [], []
    for position in road:
        if position == "G":
            streetlight_idx.append(0), cars.append(False)
        elif position == "O":
            streetlight_idx.append(6), cars.append(False)
        elif position == "R":
            streetlight_idx.append(7), cars.append(False)
        elif position == "C":
            streetlight_idx.append(-1), cars.append(True)
        else:
            streetlight_idx.append(-1), cars.append(False)

    history.append(convert(streetlight_idx, cars))

    current_time_unit = 1
    while current_time_unit <= time_units:

        current_state = []
        for idx in range(len(road) - 1, -1, -1):
            if streetlight_idx[idx] >= 0:
                streetlight_idx[idx] = (streetlight_idx[idx] + 1) % 11

        for idx in range(len(road) - 1, -1, -1):
            if idx == len(road) - 1:
                if cars[idx]:
                    cars[idx] = False
            else:
                if cars[idx]:

                    if streetlight_idx[idx + 1] >= 5:
                        pass

                    if not cars[idx + 1]:

                        if streetlight_idx[idx + 1] == -1:
                            cars[idx + 1] = True
                            cars[idx] = False
                        elif streetlight_idx[idx + 1] == 0:
                            cars[idx + 1] = True
                            cars[idx] = False

                    if cars[idx + 1]:
                        pass
                        # if streetlight_idx[idx + 1] == -1:
                        #     cars[idx + 1] = True
                        #     cars[idx] = False
                        # elif streetlight_idx[idx + 1] >= 0:
                        #     pass



        history.append(convert(streetlight_idx, cars))
        current_time_unit += 1

    return history









for i in (traffic_lights('CC....G........R...', 23)):
    print(i)
