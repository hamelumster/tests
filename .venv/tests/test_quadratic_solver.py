import unittest
from quadratic_solver import solve_quadratic_equation


class TestQuadraticEquationSolver(unittest.TestCase):

    def test_two_real_roots(self):
        root1, root2 = solve_quadratic_equation(1, -3, 2)
        self.assertAlmostEqual(root1, 2)
        self.assertAlmostEqual(root2, 1)

    def test_one_real_root(self):
        root, _ = solve_quadratic_equation(1, 2, 1)
        self.assertAlmostEqual(root, -1)

    def test_no_real_roots(self):
        root1, root2 = solve_quadratic_equation(1, 0, 1)
        self.assertIsNone(root1)
        self.assertIsNone(root2)

    def test_complex_case(self):
        root1, root2 = solve_quadratic_equation(1, 1, -6)
        self.assertAlmostEqual(root1, 2)
        self.assertAlmostEqual(root2, -3)


if __name__ == '__main__':
    unittest.main()

