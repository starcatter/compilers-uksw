import unittest

from arithmetic import evaluate_expression

from test_expressions import text_expressions, expressions_incorrect_python, incorrect_expressions


class TestEvaluation(unittest.TestCase):

    def test_correct(self):
        for text in text_expressions:
            res = evaluate_expression(text)
            res_ref = eval(text.replace("/", "//"))
            self.assertEqual(res_ref, res, msg=text)

    def test_incorrect_python(self):
        for text, reference in expressions_incorrect_python.items():
            res = evaluate_expression(text)
            res_ref = eval(reference.replace("/", "//"))
            self.assertEqual(res_ref, res, msg=text)

    def test_incorrect_parser(self):
        for text in incorrect_expressions:
            res = evaluate_expression(text)
            self.assertEqual(None, res, msg=text)
