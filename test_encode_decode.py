import unittest
from EncodeDecode import *


class TestEncodeDecode(unittest.TestCase):
    def test_one_time_pad_encodes_polybius_correctly(self):
        # based on Canvas post: "Assignment 1: Sample input/output"
        # Arrange
        polybius_transformed_values = [22, 54, 43, 44, 52, 00, 00, 00, 22, 2, 52, 52, 5, 00]
        one_time_pad_key = 21

        # Act
        otp_result = oneTimePad(polybius_transformed_values, one_time_pad_key)

        # Assert
        self.assertEqual(otp_result, [3, 35, 62, 57, 33, 21, 21, 21, 3, 23, 33, 33, 16, 21])

    def test_one_time_pad_encodes_string_value_correctly(self):
        # based on https://usu.instructure.com/courses/547987/assignments/2779075
        # Arrange
        polybius_transformed_values = [0, 2, 3, 4, 5]  # 'EZFRM'
        one_time_pad_key = 15

        # Act
        otp_result = oneTimePad(polybius_transformed_values, one_time_pad_key)

        # Assert
        self.assertEqual(otp_result, [15, 13, 12, 11, 10])


if __name__ == '__main__':
    unittest.main()
