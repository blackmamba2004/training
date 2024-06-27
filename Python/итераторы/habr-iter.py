class Tumbochka:
    """Волшебная тумбочка с тремя ящиками для чего угодно"""

    def __init__(self):
        self.boxes = {
            1: [],
            2: [],
            3: []
        }

    def add_to_box(self, obj, box_num):
        if box_num not in {1, 2, 3}:
            print("Вы ввели неправильный номер ящика!")
        else:
            self.boxes[box_num].append(obj)

    def remove_from_box(self, box_num):
        if box_num not in {1, 2, 3}:
            print("Вы ввели неправильный номер ящика!")
        else:
            return self.boxes[box_num].pop()

    def __str__(self):
        boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        return ", ".join(boxes_items)

    def __iter__(self):
        boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        for el in boxes_items:
            yield el


tumb = Tumbochka()
tumb.add_to_box('ножницы', 1)
tumb.add_to_box('карандаш', 2)
tumb.add_to_box('яблоко', 3)
tumb.add_to_box('книга', 1)
print(tumb)
for i in tumb:
    print(i)