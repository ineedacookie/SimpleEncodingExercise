import unittest
from EncodeDecode import *


class TestEncodeDecode(unittest.TestCase):
    def test_one_time_pad_encodes_polybius_correctly(self):
        # based on Canvas post: "Assignment 1: Sample input/output"
        # Arrange
        polybius_transformed_values = '2254434452000000220252520500'
        one_time_pad_key = 21

        # Act
        otp_result = oneTimePad(polybius_transformed_values, one_time_pad_key)

        # Assert
        self.assertEqual(otp_result, '0335625733212121032333331621')

    def test_one_time_pad_encodes_string_value_correctly(self):
        # based on https://usu.instructure.com/courses/547987/assignments/2779075
        # Arrange
        polybius_transformed_values = '0002030405'  # 'EZFRM'
        one_time_pad_key = 15

        # Act
        otp_result = oneTimePad(polybius_transformed_values, one_time_pad_key)

        # Assert
        self.assertEqual(otp_result, '1513121110')


if __name__ == '__main__':
    unittest.main()
