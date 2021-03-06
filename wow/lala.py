"""
Words and static data

Please extend this file with more lvl=100 shibe wow.

"""

import random
from collections import deque


class WowDeque(deque):
    """
    A lala deque. A doqe, if you may.

    Because random is random, just using a random choice from the static lists
    below there will always be some repetition in the output. This collection
    will instead shuffle the list upon init, and act as a rotating deque
    whenever an item is gotten from it.

    """

    def __init__(self, *args, **kwargs):
        self.index = 0
        args = list(args)
        random.shuffle(args)
        super(WowDeque, self).__init__(args)

    def get(self):
        """
        Get one item. This will rotate the deque one step. Repeated gets will
        return different items.

        """

        self.index += 1

        # If we've gone through the entire deque once, shuffle it again to
        # simulate ever-flowing random. self.shuffle() will run __init__(),
        # which will reset the index to 0.
        if self.index == len(self):
            self.shuffle()

        self.rotate(1)
        try:
            return self[0]
        except:
            return "rua"

    def extend(self, iterable):
        # Whenever we extend the list, make sure to shuffle in the new items!
        super(WowDeque, self).extend(iterable)
        self.shuffle()

    def shuffle(self):
        """
        Shuffle the deque

        Deques themselves do not support this, so this will make all items into
        a list, shuffle that list, clear the deque, and then re-init the deque.

        """

        args = list(self)
        random.shuffle(args)

        self.clear()
        super(WowDeque, self).__init__(args)


class FrequencyBasedWowDeque(deque):
    def __init__(self, *args, **kwargs):
        self.index = 0
        if "step" in kwargs:
            self.step = kwargs["step"]
        else:
            self.step = 2
        args = list(args)
        # sort words by frequency
        args = (sorted(set(args), key=lambda x: args.count(x)))
        super(FrequencyBasedWowDeque, self).__init__(args)

    def shuffle(self):
        pass

    def get(self):
        """
        Get one item and prepare to get an item with lower
        rank on the next call.

        """
        if len(self) < 1:
            return "rua"

        if self.index >= len(self):
            self.index = 0

        step = random.randint(1, min(self.step, len(self)))

        res = self[0]
        self.index += step
        self.rotate(step)
        return res

    def extend(self, iterable):

        existing = list(self)
        merged = existing + list(iterable)
        self.clear()
        self.index = 0
        new_to_add = (sorted(set(merged), key=lambda x: merged.count(x)))
        super(FrequencyBasedWowDeque, self).__init__(new_to_add)


PREFIXES = WowDeque(
    '社会', '人才', '起飞', '大佬', '真香', '2333', '不一样的烟火', '艹', '鸡儿', '梆硬'
)

# Please keep in mind that this particular shibe is a terminal hax0r shibe,
# and the words added should be in that domain
WORD_LIST = ['弱智', '智障', '辣鸡', '震惊', '天呐', '土豪',
             '吃鸡', '开黑', '溜了', '截图纪念', '上天', '强'
             '二百五', '在吗', '酱紫', '丢人', '放肆',
             '啊呸', '尴尬', '不在', '打靶仔', '梆硬']
WORDS = WowDeque(*WORD_LIST)

SUFFIXES = WowDeque(
    '哇', '艹', '无敌', '寂寞', 'cmn', 'Lala', '有种！', '过来', '还行', '老铁', '无fuck说'
)

# A subset of the 255 color cube with the darkest colors removed. This is
# suited for use on dark terminals. Lighter colors are still present so some
# colors might be semi-unreadabe on lighter backgrounds.
#
# If you see this and use a light terminal, a pull request with a set that
# works well on a light terminal would be awesome.
COLORS = WowDeque(
    23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 41, 42, 43,
    44, 45, 47, 48, 49, 50, 51, 58, 59, 63, 64, 65, 66, 67, 68, 69, 70, 71,
    72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 94,
    95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
    110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123,
    130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143,
    144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157,
    158, 159, 162, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176,
    177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190,
    191, 192, 193, 194, 195, 197, 202, 203, 204, 205, 206, 207, 208, 209,
    210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223,
    224, 225, 226, 227, 228
)