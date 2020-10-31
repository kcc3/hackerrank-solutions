def is_balanced(s):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/balanced-brackets/problem

    A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

    Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of
    a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets:
    [], {}, and ().

    A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])}
    is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a
    single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square
    bracket, ].

    By this logic, we say a sequence of brackets is balanced if the following conditions are met:

    - It contains no unmatched brackets.
    - The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.

    Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced,
    return YES. Otherwise, return NO.

    Args:
        s (str): The string to compare

    Returns:
        (str): "YES" or "NO" based on whether the brackets in the string are balanced
    """
    open_closed = {"(": ")", "[": "]", "{": "}"}
    balanced = []
    for i in s:
        if i in open_closed.keys():
            balanced.append(i)
        else:
            # If the stack is empty, we have a closed bracket without any corresponding open bracket so not balanced
            if len(balanced) == 0:
                return "NO"
            # Compare the brackets to see if they correspond, and if not, not balanced
            if i != open_closed[balanced.pop()]:
                return "NO"
    # If the stack is empty, every open bracket has been closed with a corresponding closed bracket
    if not balanced:
        return "YES"
    # If there's still something in the stack, then return NO because it's not balanced
    return "NO"


if __name__ == "__main__":
    assert is_balanced("}}}") == "NO"
    assert is_balanced("{[()]}") == "YES"
    assert is_balanced("{[(])}") == "NO"
    assert is_balanced("{{[[(())]]}}") == "YES"
    assert is_balanced("{{([])}}") == "YES"
    assert is_balanced("{{)[](}}") == "NO"
    assert is_balanced("{(([])[])[]}") == "YES"
    assert is_balanced("{(([])[])[]]}") == "NO"
    assert is_balanced("{(([])[])[]}[]") == "YES"
