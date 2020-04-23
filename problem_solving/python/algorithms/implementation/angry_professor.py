def angry_professor(k, a):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/angry-professor/problem

    A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, he decides to
    cancel class if fewer than some number of students are present when class starts. Arrival times go from on time
    (arrivalTime <= 0) to arrived late (arrivalTime > 0).

    Given the arrival time of each student and a threshold number of attendees, determine if the class is canceled.

    Args:
        k (int): The number of students needed for professor to hold class
        a (list): List of students arrival time passed as integers

    Returns:
        str: YES or NO depending on whether the professor cancels class
    """
    students_present = 0
    for student in sorted(a):
        if student <= 0:
            students_present += 1
        if students_present >= k:
            return "NO"
    return "YES"


if __name__ == "__main__":
    print angry_professor(3, [-1, -3, 4, 2])
    print angry_professor(2, [0, -1, 2, 1])