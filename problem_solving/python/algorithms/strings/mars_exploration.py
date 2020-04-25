def mars_exploration(s):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/mars-exploration/problem

    Sami's spaceship crashed on Mars! She sends a series of SOS messages to Earth for help.

    Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received
    by Earth as a string, s, determine how many letters of Sami's SOS have been changed by radiation.

    For example, Earth receives SOSTOT. Sami's original message was SOSSOS. Two of the message characters were changed
    in transit.

    Args:
        s (str): string to compare with SOS message (must be divisible by 3)

    Returns:
        int: the number of characters that differ between the message and "SOS"
    """
    sos = int(len(s)/3) * "SOS"
    return sum(sos[i] != s[i] for i in range(len(s)))


if __name__ == "__main__":
    assert mars_exploration("SOSSPSSQSSOR") == 3