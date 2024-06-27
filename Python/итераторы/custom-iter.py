class Tumbochka:

    def __init__(self, *args: int):
        self.boxes = {}
        for arg in sorted(set(args)):
            self.boxes[arg] = []

    def add_to_box(self, box_num: int, obj: str):
        if box_num not in self.boxes.keys():
            print("Введите корректный номер!")
        else:
            self.boxes[box_num].append(obj)

    def add_box(self, box_num: int):
        if box_num not in self.boxes.keys():
            self.boxes[box_num] = []
            self.sort()
        else:
            raise
            # print("Такая коробка уже есть!")

    def remove_from_box(self, box_num: int, thing_num: int = 0):
        if box_num not in self.boxes.keys():
            print("Введите корректный номер!")
        else:
            self.boxes[box_num].pop(thing_num)

    def remove_box(self, box_num: int):
        if box_num in self.boxes.keys():
            del self.boxes[box_num]

    def clear_box(self):
        self.boxes.clear()

    def get_box_nums(self) -> list:
        return list(self.boxes.keys())

    def get_list(self) -> list:
        return list(self.boxes.items())

    def sort(self):
        self.boxes = dict(sorted(self.boxes.items()))

    def __str__(self):
        return ", ".join(item for box in self.boxes.values() for item in box)

    def __iter__(self):
        box_items = str([value for value in self.boxes.values()])
        box_items = self.boxes.values()
        for el in box_items:
            yield el


class TumbochkaIterator:
    def __init__(self, some_objects):
        self.some_objects = some_objects
        self.current = 0

    def __next__(self):
        if self.current < len(self.some_objects):
            result = self.some_objects[self.current]
            self.current += 1
            return result

    def __iter__(self):
        return TumbochkaIterator()


tumbochka = Tumbochka(3, 1, 2)
tumbochka.add_to_box(1, 'ножницы')
tumbochka.add_to_box(2, 'карандаш')
tumbochka.add_to_box(3, 'яблоко')
tumbochka.add_box(4)
tumbochka.add_to_box(4, 'покемон')
tumbochka.add_to_box(2, 'шампунь')
tumbochka.sort()

print(tumbochka)
it = iter(tumbochka)
print(next(it))

for i in tumbochka:
    print(i)
