def jumping_on_clouds(c, k):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

    Cloud hopping game where you start at 100 energy, and jump through the clouds of step size k until you get back
    to the original cloud at position array 0.  Each time you jump, you expend 1 energy, and each time you land on a
    thunderstorm cloud, you spend an additional 2 energy.  Thunderstorm clouds are denoted by a 1 in the cloud array, with
    regular or cumulus clouds denoted as a 0.

    Args:
        c (list): array of cloud types
        k (int): step size each time you jump

    Returns:
        energy (int): the energy remaining after jumping through the clouds
    """
    energy = 100
    steps = 0
    cloud = None
    while cloud != 0:
        steps += 1
        energy -= 1
        cloud = (steps * k) % len(c)
        if c[cloud]:
            energy -= 2
    return energy


if __name__ == "__main__":
    c = [0, 0, 1, 0, 0, 1, 1, 0]
    k = 2
    print jumping_on_clouds(c, k)