def climbing_leaderboard(scores, alice):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

    Find the current place for alice's scores as she is working up the leaderboard.  Uses dense ranking.

    For example, if the leaderboard scores are [100, 100, 50, 40, 40, 20, 10], and alice has scores of [5, 25, 50, 120],
    she will have the places returned of [6, 4, 2, 1]

    Args:
        scores (list): list of the current high scores
        alice (list): list of alice's scores as she makes attempts to get into the leaderboard

    Returns:
        list: list of alice's rankings from her score submissions
    """
    ranking = []
    scores = sorted(set(scores))
    prev = 0
    for i, alice_score in enumerate(sorted(alice)):
        score_printed = True
        for j in xrange(prev, len(scores)):
            if alice_score < scores[j]:
                score_printed = False
                ranking.append(len(scores) - j + 1)
                prev = j
                break
        if score_printed:
            ranking.append(1)
    return ranking


if __name__ == "__main__":
    s = [100, 100, 50, 40, 40, 20, 10]
    a = [5, 25, 50, 120]
    print climbing_leaderboard(s, a)
