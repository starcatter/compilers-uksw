from collections import defaultdict
from typing import Tuple, DefaultDict

valid_transitions: DefaultDict[Tuple[int, str], int] = defaultdict()
valid_transitions.default_factory = lambda: None
valid_transitions[(0, 'a')] = 1
valid_transitions[(1, 'a')] = 2
valid_transitions[(1, 'b')] = 3
valid_transitions[(2, 'b')] = 1
valid_transitions[(3, 'a')] = 4
valid_transitions[(4, 'b')] = 5

accepting_states: Tuple[int, ...] = (3, 4, 5)


def validate_string(input_string: str) -> bool:
    state = 0
    for char in input_string:
        if (state := valid_transitions[(state, char)]) is None:
            return False
    if state not in accepting_states:
        return False
    return True


if __name__ == "__main__":
    print("Enter text matching a(ab)*b(ab|a)?:", end=" ")
    text = input()
    print("Correct!" if validate_string(text) else "The string doesn't match a(ab)*b(ab|a)?")
