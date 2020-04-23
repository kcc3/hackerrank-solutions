def acm_team(topic):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/acm-icpc-team/problem

    There are a number of people who will be attending ACM-ICPC World Finals. Each of them may be well versed in a number
    of topics. Given a list of topics known by each attendee, you must determine the maximum number of topics a 2-person
    team can know. Also find out how many ways a team can be formed to know that many topics. Lists will be in the form
    of bit strings, where each string represents an attendee and each position in that string represents a field of
    knowledge, 1 if its a known field or 0 if not.

    For example, given three attendees' data as follows:

    10101
    11110
    00010

    These are all possible teams that can be formed:

    Members Subjects
    (1,2)   [1,2,3,4,5]
    (1,3)   [1,3,4,5]
    (2,3)   [1,2,3,4]

    In this case, the first team will know all 5 subjects. They are the only team that can be created knowing that many
    subjects.

    Args:
        topic: list of students representing the topics that they knwo

    Returns:
        array: array with element one being the maximum number of topics a pairing can know, and element two being the
            total number of pairings of students that know that maximum number of topics
    """
    topics = []
    max_topics = 0
    pairings_with_max = 0
    # Iterate through the student pairs
    for i in xrange(len(topic)):
        for j in xrange(len(topic)):
            if i < j:
                # Combine the topics of this pairing
                topics_combined = int(topic[i]) + int(topic[j])
                topics.append(topics_combined)
                cur_topics = 0
                # Count the combined topics for this pairing
                for k in str(topics_combined):
                    if k != "0":
                        cur_topics += 1
                # Set new max value if it's the highest combined topics and reset max pairings count
                if cur_topics > max_topics:
                    max_topics = cur_topics
                    pairings_with_max = 0
                # If the cur count is the highest, add one to max pairings count
                if cur_topics == max_topics:
                    pairings_with_max += 1
    # Return the maximum number of topics a pair can know, and the number of pairs of students who know that number
    return [max_topics, pairings_with_max]


if __name__ == "__main__":
    topic_test = ["10101", "11110", "00010"]
    topic2_test = ["10101", "11100", "11010", "00101"]
    print acm_team(topic_test)
    print acm_team(topic2_test)