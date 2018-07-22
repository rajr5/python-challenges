import unittest
from brace_balancer import BraceBalancer

class TestBraceBalancer(unittest.TestCase):
    def test_empty_input(self):
        balancer = BraceBalancer()
        is_balanced = balancer.is_balanced('')
        self.assertTrue(is_balanced)

    def test_simple_input(self):
        balancer = BraceBalancer()
        is_balanced = balancer.is_balanced('()')
        self.assertTrue(is_balanced)

    def test_simple_imbalanced_input(self):
        balancer = BraceBalancer()
        is_balanced = balancer.is_balanced('([]')
        self.assertFalse(is_balanced)

    def test_very_imbalanced_closing_brace_input(self):
        balancer = BraceBalancer()
        is_balanced = balancer.is_balanced('))))))))))))')
        self.assertFalse(is_balanced)

    def test_very_imbalanced_opening_brace_input(self):
        balancer = BraceBalancer()
        is_balanced = balancer.is_balanced('(((((((((((((')
        self.assertFalse(is_balanced)


    def test_complex_input(self):
        balancer = BraceBalancer()
        is_balanced = balancer.is_balanced("""
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