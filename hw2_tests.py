import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        input1 = data.Point(2,4)
        input2 = data.Point(6,3)
        result = hw2.create_rectangle(input1, input2)
        expected = data.Rectangle(data.Point(2,4), data.Point(6,3))
        self.assertEqual(result, expected)

    def test_create_rectangle_2(self):
        input1 = data.Point(0,0)
        input2 = data.Point(0,0)
        result = hw2.create_rectangle(input1, input2)
        expected = data.Rectangle(data.Point(0,0), data.Point(0,0))
        self.assertEqual(result, expected)

    # Part 2
    def test_shorter_duration_than_1(self):
        input1 = data.Duration(2,4)
        input2 = data.Duration(6,3)
        result = hw2.shorter_duration_than(input1, input2)
        expected = True
        self.assertEqual(result, expected)

    def test_shorter_duration_than_2(self):
        input1 = data.Duration(1,0)
        input2 = data.Duration(0,0)
        result = hw2.shorter_duration_than(input1, input2)
        expected = False
        self.assertEqual(result, expected)

    # Part 3
    def test_song_shorter_than_1(self):
        input1 = [data.Song("John","Song", data.Duration(4,5)),
                  data.Song("Jill","Sad", data.Duration(3,2))]
        input2 = data.Duration(4,1)
        result = hw2.song_shorter_than(input1, input2)
        expected = [data.Song("Jill", "Sad", data.Duration(3,2))]
        self.assertEqual(result, expected)

    def test_song_shorter_than_2(self):
        input1 = [data.Song("John","Song", data.Duration(4,5)),
                  data.Song("Jill","Sad", data.Duration(3,2))]
        input2 = data.Duration(0,0)
        result = hw2.song_shorter_than(input1, input2)
        expected = []
        self.assertEqual(result, expected)

    # Part 4
    def test_running_time_1(self):
        input1 = [data.Song("John","Song", data.Duration(4,5)),
                  data.Song("Jill","Sad", data.Duration(3,2))]
        input2 = [0,1]
        result = hw2.running_time(input1, input2)
        expected = data.Duration(7,7)
        self.assertEqual(result, expected)

    def test_running_time_2(self):
        input1 = [data.Song("John","Song", data.Duration(4,5)),
                  data.Song("Jill","Sad", data.Duration(3,2)),
                  data.Song("Bill", "Happy", data.Duration(5,59))]
        input2 = [0,2]
        result = hw2.running_time(input1, input2)
        expected = data.Duration(10, 4)
        self.assertEqual(result, expected)

    # Part 5
    def test_validate_route_1(self):
        input1 = []
        input2 = ["john"]
        result = hw2.validate_route(input1, input2)
        expected = True
        self.assertEqual(result, expected)

    def test_validate_route_2(self):
        input1 = [
            ["joe", "bob"],
            ["bob", "dylan"]
        ]
        input2 = ["joe", "bob", "dylan"]
        result = hw2.validate_route(input1, input2)
        expected = True
        self.assertEqual(result, expected)

    # Part 6
    def test_longest_repetitions_1(self):
        input1 = []
        result = hw2.longest_repetition(input1)
        expected = None
        self.assertEqual(expected, result)

    def test_longest_repetitions_2(self):
        input1 = [2,1,1,1]
        result = hw2.longest_repetition(input1)
        expected = 1
        self.assertEqual(expected, result)





if __name__ == '__main__':
    unittest.main()
