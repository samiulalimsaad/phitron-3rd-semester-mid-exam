class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows: list, cols: list, hall_no: int) -> None:
        self.seats = {}
        self.show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        super().entry_hall(self)

    def entry_show(self, id: str, movie_name: str, time: str):
        tpl = (id, movie_name, time)
        self.show_list.append(tpl)
        self.seats[id] = [[0] * self.__cols for _ in range(self.__rows)]

    def book_seats(self, id: str, row: int, col: int):
        if id not in self.seats:
            print("\n#########################")
            print(f"{id} not found")
            print("#########################\n")
            return
        elif row > self.__rows:
            print("\n#########################")
            print(f"invalid row {row}")
            print("#########################\n")
            return
        elif col > self.__cols:
            print("\n#########################")
            print(f"invalid col {col}")
            print("#########################\n")
            return
        elif self.seats[id][row][col] == 1:
            print("\n#########################")
            print(f"seat already booked")
            print("#########################\n")
            return

        self.seats[id][row][col] = 1

    def view_show_list(self):
        for id, name, time in self.show_list:
            print(f"id: {id}, movie_name: {name}, time: {time}")

    def view_available_seats(self, id):
        if id not in self.seats:
            return print(f"{id} not found")

        for s in self.seats[id]:
            print(s)
        print()


hall1 = Hall(5, 5, 1)
hall2 = Hall(6, 6, 2)

hall1.entry_show("111", "Movie A", "1/2/3")
hall2.entry_show("222", "Movie B", "4/5/6")


def view_all_show_today():
    print("\n#########################")
    for hall in Star_Cinema.hall_list:
        hall.view_show_list()
    print("#########################\n")


def view_available_seats():
    found = False
    show_id = input("Enter show id: ")
    for hall in Star_Cinema.hall_list:
        for show in hall.show_list:
            if show[0] == show_id:
                print("\n#########################\n")
                hall.view_available_seats(show_id)
                print("#########################\n")
                found = True
    if found == False:
        print("\n#########################")
        print(f"Show not found")
        print("#########################\n")


def book_ticket():
    show_id = input("Enter show id: ")
    hallIns = None
    for hall in Star_Cinema.hall_list:
        for show in hall.show_list:
            if show[0] == show_id:
                hallIns = hall

    if hallIns == None:
        print("\n#########################")
        print(f"Show not found")
        print("#########################\n")
        return

    tickets = int(input("Number of tickets: "))

    for _ in range(tickets):
        row = int(input("Enter seat row: "))
        col = int(input("Enter seat col: "))
        hallIns.book_seats(show_id, row, col)


while True:
    txt = "------------------------------\n1. VIEW ALL SHOW TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\n4. EXIT\n------------------------------\n: "

    op = int(input(txt))

    if op == 1:
        view_all_show_today()
    elif op == 2:
        view_available_seats()
    elif op == 3:
        book_ticket()
    elif op == 4:
        print("...EXIT...")
        break
    else:
        print("___invalid option___")
