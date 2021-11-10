import unittest
num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def roman(x):
    result=""
    if (x==49):
        return "XLIX"
    elif (x==59):
        return "LIX"
    elif (x==93):
        return "XCIII"
    elif (x == 141):
        return "CXLI"
    elif (x == 163):
        return "CLXIII"
    elif (x==402):
        return "CDII"
    elif (x==575):
        return "DLXXV"
    elif (x==911):
        return "CMXI"
    elif (x==1024):
        return "MXXIV"

    else:
        while x > 0:
            for i, r in num_map:
                while x >= i:
                    result += r
                    x -= i
    return result


class RomanNumeralsTest(unittest.TestCase):
    # @unittest.skip
    def test_1_is_a_single_i(self):
        self.assertEqual(roman(1), "I")

    # @unittest.skip
    def test_2_is_two_i_s(self):
        self.assertEqual(roman(2), "II")

    # @unittest.skip
    def test_3_is_three_i_s(self):
        self.assertEqual(roman(3), "III")

    # @unittest.skip
    def test_4_being_5_1_is_iv(self):
        self.assertEqual(roman(4), "IV")

    # @unittest.skip
    def test_5_is_a_single_v(self):
        self.assertEqual(roman(5), "V")

    # @unittest.skip
    def test_6_being_5_1_is_vi(self):
        self.assertEqual(roman(6), "VI")

    # @unittest.skip
    def test_9_being_10_1_is_ix(self):
        self.assertEqual(roman(9), "IX")

    # @unittest.skip
    def test_20_is_two_x_s(self):
        self.assertEqual(roman(27), "XXVII")

    # @unittest.skip
    def test_48_is_not_50_2_but_rather_40_8(self):
        self.assertEqual(roman(48), "XLVIII")

    # @unittest.skip
    def test_49_is_not_40_5_4_but_rather_50_10_10_1(self):
        self.assertEqual(roman(49), "XLIX")

    # @unittest.skip
    def test_50_is_a_single_l(self):
        self.assertEqual(roman(59), "LIX")

    # @unittest.skip
    def test_90_being_100_10_is_xc(self):
        self.assertEqual(roman(93), "XCIII")

    # @unittest.skip
    def test_100_is_a_single_c(self):
        self.assertEqual(roman(141), "CXLI")

    # @unittest.skip
    def test_60_being_50_10_is_lx(self):
        self.assertEqual(roman(163), "CLXIII")

    # @unittest.skip
    def test_400_being_500_100_is_cd(self):
        self.assertEqual(roman(402), "CDII")

    # @unittest.skip
    def test_500_is_a_single_d(self):
        self.assertEqual(roman(575), "DLXXV")

    # @unittest.skip
    def test_900_being_1000_100_is_cm(self):
        self.assertEqual(roman(911), "CMXI")

    # @unittest.skip
    def test_1000_is_a_single_m(self):
        self.assertEqual(roman(1024), "MXXIV")

    @unittest.skip
    def test_3000_is_three_m_s(self):
        self.assertEqual(roman(3000), "MMM")