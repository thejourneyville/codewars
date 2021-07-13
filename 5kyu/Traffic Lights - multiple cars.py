def convert(light_state, car_state):
    """
    :param light_state: list containing index numbers of current light state to reference light_sequence
    :param car_state: list containing booleans of car exists or not in arbitrary position of the current state
    :return: state: string showing current state of traffic lights and car positions
    """

    light_sequence = "G" * 5 + "O" + "R" * 5  # 11 total states of the traffic light cycle
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
    """
    :param road: string of initial car/traffic-light state
    :param time_units: number of time units to iterate through
    :return: history: a list of strings showing each time unit iteration of car/traffic-lights
    """

    history = [road]
    streetlight_idx, cars = [], []
    # creates 2 lists (streetlight_idx, cars) to separately track traffic state and car position state
    for position in road:
        if position == "G":
            streetlight_idx.append(0), cars.append(False)
        elif position == "O":
            streetlight_idx.append(5), cars.append(False)
        elif position == "R":
            streetlight_idx.append(6), cars.append(False)
        elif position == "C":
            streetlight_idx.append(-1), cars.append(True)
        else:
            streetlight_idx.append(-1), cars.append(False)

    current_time_unit = 1
    while current_time_unit <= time_units:

        for idx in range(len(road) - 1, -1, -1):  # from right to left, updates traffic light state
            if streetlight_idx[idx] >= 0:
                streetlight_idx[idx] = (streetlight_idx[idx] + 1) % 11

            if idx == len(road) - 1:  # car drops off end
                if cars[idx]:
                    cars[idx] = False

            else:

                if cars[idx]:  # if car in current index

                    if cars[idx + 1]:  # if car in right adjacent index
                        continue

                    else:

                        if streetlight_idx[idx + 1] > -1:  # if traffic light exists adjacent right

                            try:
                                if not cars[idx + 2]:  # if passageway is clear of intersection

                                    if streetlight_idx[idx + 1] <= 4:  # if light is green move to right
                                        cars[idx + 1] = True
                                        cars[idx] = False

                            except IndexError:  # index error prevented at end of road when checking idx + 2
                                if streetlight_idx[idx + 1] <= 4:
                                    cars[idx + 1] = True
                                    cars[idx] = False

                        elif streetlight_idx[idx + 1] == -1:  # if no traffic light exists adjacent right move to right
                            cars[idx + 1] = True
                            cars[idx] = False

        history.append(convert(streetlight_idx, cars))  # append history using helper function for formatting
        current_time_unit += 1

    return history


for i in (traffic_lights('CCC.G', 6)):
    print(i)
