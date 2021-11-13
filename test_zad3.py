import unittest
versesList=['On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.', 'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.','On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.']



class PrintSong():

    def printSingleVerse(n):
        toPrint=''
        if type(n) is not int or n=="undefined":
            raise ValueError("Please insert a number!")
        if n>13 or n<1:
            raise ValueError("Inserted value must be between 1 and 13!")
        else:
            toPrint=(versesList[n-1])
            print(toPrint)
            return toPrint

    def printManyVerses(start,end):
        toPrint=[]
        if start=="undefined" or end=="undefined":
            raise ValueError("Please insert both start and end verse!")
        if type(start) is not int or type(end) is not int:
            raise ValueError("Please insert a number!")
        if start>13 or start<1 or end>13 or end<1:
            raise ValueError("Inserted values must be between 1 and 13!")
        else:
            for i in range (start-1, end):
                toPrint.append(versesList[i])
                print(versesList[i])
            return toPrint

    def printWholeSong():
        toPrint=[]
        for i in range(0, len(versesList)):
            toPrint.append(versesList[i])
            print(versesList[i])
        return toPrint


class PrintingSongTest(unittest.TestCase):
    def test_get_first(self):
        self.assertEqual(PrintSong.printSingleVerse(1), 'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.')

    def test_get_from_3_to_7(self):
        self.assertEqual(PrintSong.printManyVerses(3,7),
                         ['On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.','On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            ])
    def test_get_whole_song(self):
        self.assertEqual(PrintSong.printWholeSong(),versesList)
    def test_not_a_number_single(self):
        with self.assertRaisesWithMessage(ValueError):
            PrintSong.printSingleVerse('osiem')
    def test_not_a_number_start(self):
        with self.assertRaisesWithMessage(ValueError):
            PrintSong.printManyVerses('osiem',2)
    def test_not_a_number_end(self):
        with self.assertRaisesWithMessage(ValueError):
            PrintSong.printManyVerses(3,'osiem')

    def test_wrong_number_single(self):
        with self.assertRaisesWithMessage(ValueError):
            PrintSong.printSingleVerse(87)

    def test_wrong_number_start(self):
        with self.assertRaisesWithMessage(ValueError):
            PrintSong.printManyVerses(-87, 2)

    def test_wrong_number_end(self):
        with self.assertRaisesWithMessage(ValueError):
            PrintSong.printManyVerses(3, 87)
    def test_wrong_both_start_end(self):
        with self.assertRaisesWithMessage(ValueError):
            PrintSong.printManyVerses(-3, 87)
    def test_wrong_both_start_end_send_list(self):
        with self.assertRaisesWithMessage(ValueError):
            PrintSong.printManyVerses([-3, 87],0)
    def test_no_number_single(self):
        with self.assertRaisesWithMessage(ValueError):
            PrintSong.printSingleVerse('')

    def test_no_number_start(self):
        with self.assertRaisesWithMessage(ValueError):
            PrintSong.printManyVerses('',2)

    def test_no_number_end(self):
        with self.assertRaisesWithMessage(ValueError):
            PrintSong.printManyVerses(3,'')
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

