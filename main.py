import types

# Задание 1.
class FlatIterator:

    def __init__(self, list_of_list):
        self.main_list = list_of_list

    def __iter__(self):
        self.cursor = 0
        self.cursor2 = -1
        return self

    def __next__(self):
        self.cursor2 += 1
        if self.cursor2 > len(self.main_list[self.cursor])-1:
          self.cursor2 = 0
          self.cursor += 1
          if self.cursor > len(self.main_list) - 1:
            raise StopIteration
        return self.main_list[self.cursor][self.cursor2]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

# Задание 2

def flat_generator(list_of_lists):
    cursor = 0
    cursor2 = 0
    while cursor < len(list_of_lists):
      yield list_of_lists[cursor][cursor2]
      cursor2 +=1
      if cursor2 > len(list_of_lists[cursor])-1:
        cursor += 1
        cursor2 = 0


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_1()
    test_2()