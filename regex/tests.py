import random
import re
import unittest

from regex import validate_string


def random_ab(max_len):
    while True:
        r = random.randint(1, max_len)
        yield "".join(random.choices("ab", k=r))


random_expr = random_ab(10)

pattern = re.compile(r'^a(ab)*b(ab|a)?$')


class RegexTest(unittest.TestCase):

    def test_10_random(self):
        print("\n")
        for _ in range(10):
            input_string = next(random_expr)
            function_result = validate_string(input_string)
            regex_result = bool(re.match(pattern, input_string))
            print(input_string, function_result)
            self.assertEqual(regex_result, function_result)
