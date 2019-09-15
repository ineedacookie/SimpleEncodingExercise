import unittest
from EncodeDecode import *


class TestEncodeDecode(unittest.TestCase):
    def test_one_time_pad_encodes_string_value_correctly(self):
        # based on https://usu.instructure.com/courses/547987/assignments/2779075
        # Arrange
        polybius_transformed_values = 'ERFZM'
        one_time_pad_key = 15

        # Act
        otp_result = oneTimePadEncode(polybius_transformed_values, one_time_pad_key)

        # Assert
        self.assertEqual(otp_result, '1513121110')


    def test_one_time_pad_decodes_encoded_string_correctly(self):
        # based on https://usu.instructure.com/courses/547987/assignments/2779075
        # Arrange
        polybius_transformed_values = '1513121110'
        one_time_pad_key = 15

        # Act
        otp_result = oneTimePadDecode(polybius_transformed_values, one_time_pad_key)

        # Assert
        self.assertEqual(otp_result, 'ERFZM')


if __name__ == '__main__':
    unittest.main()
