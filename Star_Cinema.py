class Hall:
    def __init__(self, rows: list, cols: list, hall_no: int) -> None:
        self.__seats = {}  # which is an dictionary of seats information
        self.__show_list = []  # which is an list of tuples
        self.__rows = rows  # which is the row of the seats in that hall
        self.__cols = cols  # which is the column of the seats in that hall
        self.__hall_no = hall_no  # which is the unique no. of that hall

    def entry_show(self, id: str, movie_name: str, time: str):
        self.__show_list.append(tuple([id, movie_name, time]))
        self.__seats[id] = [[0 for _ in range(self.__rows)] for _ in range(self.__cols)]

    def book_seats(self, id: str, row: int, col: int):
        if id not in self.__seats:
            return print(f"{id} not found")
        elif row > self.__rows:
            return print(f"invalid row {row}")
        elif col > self.__cols:
            return print(f"invalid col {col}")

        self.__seats[id][row][col] = 1

    def view_show_list(self):
        for show in self.__show_list:
            print(f"id: {show[0]}, movie_name: {show[1]}, time: {show[2]}")

    def view_available_seats(self, id):
        if id not in self.__seats:
            return print(f"{id} not found")

        for s in self.__seats[id]:
            print(s)
        print()


class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall: Hall):
        self.hall_list.append(hall)


a = Hall(5, 5, 555)
a.entry_show("111", "aaa", "1/2/3")
a.entry_show("222", "bbb", "4/5/6")

total = 5
for i in range(total):
    # a.view_show_list()
    id = f"{i}{i}{i}"
    a.view_available_seats(id)
    a.book_seats(id, i, i)
    a.view_available_seats(id)
