import unittest
from brace_balancer import are_braces_balanced


class TestBraceBalancer(unittest.TestCase):
    def test_wrong_input_throws(self):
        self.assertRaises(ValueError, are_braces_balanced, [])

    def test_empty_input(self):
        is_balanced = are_braces_balanced('')
        self.assertTrue(is_balanced)

    def test_simple_input(self):
        is_balanced = are_braces_balanced('()')
        self.assertTrue(is_balanced)

    def test_reverse_order_braces(self):
        is_balanced = are_braces_balanced(')(')
        self.assertFalse(is_balanced)

    def test_non_matching_braces(self):
        is_balanced = are_braces_balanced('(]')
        self.assertFalse(is_balanced)

    def test_simple_imbalanced_input(self):
        is_balanced = are_braces_balanced('([]')
        self.assertFalse(is_balanced)

    def test_very_imbalanced_closing_brace_input(self):
        is_balanced = are_braces_balanced('))))))))))))')
        self.assertFalse(is_balanced)

    def test_very_imbalanced_opening_brace_input(self):
        is_balanced = are_braces_balanced('(((((((((((((')
        self.assertFalse(is_balanced)

    def test_complex_input(self):
        is_balanced = are_braces_balanced("""
        Python {is an easy to [learn]}, (powerful programming language. It)
        has efficient high­level [(data structures) and a simple but
        effective approach to object­oriented programming]. Python’s elegant
        syntax and dynamic typing, together with its {interpreted nature,
        make it an ideal language (for) scripting and rapid} application
        development in many areas on most platforms.
        """)
        self.assertTrue(is_balanced)


if __name__ == '__main__':
    unittest.main()
