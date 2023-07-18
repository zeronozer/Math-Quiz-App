import unittest
from quiz import generate_problem, calculate_score

MAX_SCORE = 100
WRONG_ANSWER_PENALTY = 10
TIME_PENALTY_FACTOR = 0.5

class TestProject(unittest.TestCase):

    def test_generate_problem(self):
        expr, answer = generate_problem()
        self.assertIsInstance(expr, str)
        self.assertIsInstance(answer, int)
    
    def test_calculate_score(self):
        wrong_answers = 5
        time = 60
        
        expected = MAX_SCORE - (wrong_answers * WRONG_ANSWER_PENALTY) - (time * TIME_PENALTY_FACTOR)

        score = calculate_score(wrong_answers, time)
      
        self.assertEqual(score, expected)
        
if __name__ == '__main__':
    unittest.main()