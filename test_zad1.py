import unittest

class hamming():
    def distance(s1,s2):
        if s1=="" and s2=="":
            return 0
        elif len(s1)==1 and len(s2)==1 and s1==s2:
            return 0
        elif len(s1)==1 and len(s2)==1 and s1!=s2:
            return 1
        elif len(s1)==len(s2) and s1==s2:
            return 0
        elif len(s1)==len(s2) and s1!=s2:
            counter=0
            for i in range(0,len(s1)):
                if (s1[i]==s2[i]):
                    continue
                else:
                    counter+=1
                i+=1
            return counter
        elif len(s1)>len(s2):
            raise ValueError("First input is longer than the other!")
        elif len(s1)<len(s2):
            raise ValueError("Second input is longer than the first one!")
        elif s1=="" or s2=="":
            raise ValueError("Input cannot be empty!")
        # return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


class HammingTest(unittest.TestCase):
    # @unittest.skip
    def test_empty_strands(self):
        self.assertEqual(hamming.distance("", ""), 0)

    # @unittest.skip
    def test_single_letter_identical_strands(self):
        self.assertEqual(hamming.distance("A", "A"), 0)

    # @unittest.skip
    def test_single_letter_different_strands(self):
        self.assertEqual(hamming.distance("G", "T"), 1)

    # @unittest.skip
    def test_long_identical_strands(self):
        self.assertEqual(hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)

    # @unittest.skip
    def test_long_different_strands(self):
        self.assertEqual(hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    # @unittest.skip
    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("AATG", "AAA")

    # @unittest.skip
    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("ATA", "AGTG")

    # @unittest.skip
    def test_disallow_left_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("", "G")

    # @unittest.skip
    def test_disallow_right_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            hamming.distance("G", "")

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")