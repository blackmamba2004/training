class Tumbochka:

    def __init__(self, *args: int):
        self.boxes = {}
        for arg in args:
            self.boxes[arg] = []

    def add_to_box(self, box_num: int, obj):
        if box_num not in self.boxes.keys():
            print("Введите корректный номер!")
        else:
            self.boxes[box_num].append(obj)

    def add_box(self, box_num: int):
        if box_num not in self.boxes.keys():
            self.boxes[box_num] = []
        else:
            print("Такая коробка уже есть!")

    def remove_from_box(self, box_num: int):
        if box_num not in self.boxes.keys():
            print("Введите корректный номер!")
        else:
            self.boxes[box_num].pop()

    def remove_box(self, box_num: int):
        if box_num in self.boxes.keys():
            del self.boxes[box_num]

    def get_box_nums(self) -> list:
        return list(self.boxes.keys())

    def get_list(self) -> list:
        return list(self.boxes.items())

    def sort(self):
        self.boxes = dict(sorted(self.boxes.items()))

    def __str__(self):
        boxes_items = str({box_num: self.boxes[box_num] for box_num in self.boxes.keys()})
        return boxes_items


tumbochka = Tumbochka(3, 1, 2)
tumbochka.add_to_box(1, 'ножницы')
tumbochka.add_to_box(2, 'карандаш')
tumbochka.add_to_box(3, 'яблоко')
tumbochka.add_to_box(4, 'покемон')
tumbochka.add_box(4)
tumbochka.sort()
print(tumbochka)

tt = tumbochka.get_list()
print(tt)
