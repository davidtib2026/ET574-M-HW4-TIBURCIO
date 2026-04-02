# Name: David Tiburcio
# QCC ID: 23699348
# ET574 HW4 Slot Machine Simulator

# test_slotmachine.py
# Unit tests for SlotMachine assignment

import unittest
from main import Reel, SlotMachine

class TestReel(unittest.TestCase):
    def test_spin_within_bounds(self):
        reel = Reel(max_value=9)
        for _ in range(200):
            value = reel.spin()
            self.assertIn(value, range(0, 10))

class TestSlotMachine(unittest.TestCase):
    def setUp(self):
        self.game = SlotMachine()

    def test_evaluate_win(self):
        self.assertEqual(self.game.evaluate_spin(5, 5, 5), "Win")
        self.assertEqual(self.game.evaluate_spin(0, 0, 0), "Win")

    def test_evaluate_lose(self):
        self.assertEqual(self.game.evaluate_spin(0, 3, 4), "Lose")
        self.assertEqual(self.game.evaluate_spin(7, 0, 2), "Lose")

    def test_evaluate_spin_again(self):
        self.assertEqual(self.game.evaluate_spin(1, 2, 3), "Spin Again")
        self.assertEqual(self.game.evaluate_spin(8, 9, 7), "Spin Again")

    def test_play_round_output_structure(self):
        result = self.game.play_round()
        self.assertEqual(len(result), 5)
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], int)
        self.assertIsInstance(result[2], int)
        self.assertIsInstance(result[3], int)
        self.assertIsInstance(result[4], str)

    # --- Students: Add 3 more test cases below ---

    def test_all_match_win(self):
        machine = SlotMachine()
        self.assertEqual(machine.evaluate_spin(3, 3, 3), "Win")

    def test_zero_is_lose(self):
        machine = SlotMachine()
        self.assertEqual(machine.evaluate_spin(0, 5, 7), "Lose")

    def test_spin_again_case(self):
        machine = SlotMachine()
        self.assertEqual(machine.evaluate_spin(2, 4, 6), "Spin Again")

if __name__ == '__main__':
    unittest.main()
