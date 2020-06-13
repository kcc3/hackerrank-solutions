def flatland_space_stations(n, c):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/flatland-space-stations/problem

    Flatland is a country with a number of cities, some of which have space stations. Cities are numbered consecutively
    and each has a road of 1km length connecting it to the next city. It is not a circular route, so the first city
    doesn't connect with the last city. Determine the maximum distance from any city to it's nearest space station.

    For example, there are n = 3 cities and m = 1 of them has a space station, city 1. They occur consecutively along a
    route. City 2 is 2 - 1 = 1 unit away and city 3 is 3 - 1 = 2 units away. City 1 is 0 units from its nearest space
    station as one is located there. The maximum distance is 2.

    Args:
        n (int): The number of cities
        c (list): integer array containing the indices of cities having a space station

    Returns:
        int: The maximum distance that an astronaut needs to travel to reach a space station
    """
    max_distance = 0
    c.sort()
    # Check between the cities
    for i in range(1, len(c)):
        if (c[i] - c[i-1]) // 2 > max_distance:
            max_distance = (c[i] - c[i-1]) // 2
    # Now check the outliers - the first city and the last city distance to a space station
    if c[0] > max_distance:
        max_distance = c[0]
    if n - c[-1] - 1 > max_distance:
        max_distance = n - c[-1] - 1
    return max_distance


if __name__ == "__main__":
    assert flatland_space_stations(5, [0, 4]) == 2
    assert flatland_space_stations(6, [0, 1, 2, 4, 3, 5]) == 0
    assert flatland_space_stations(20, [13, 1, 11, 10, 6]) == 6