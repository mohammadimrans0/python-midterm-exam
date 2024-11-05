# Task : 1
class Star_Cinema:
    _hall_list = []

    def entry_hall(self, hall):
        self._hall_list.append(hall) 


# Task : 2
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_name):
        super().__init__()
        self._rows = rows    # Task : 9 -> protected attribute            
        self._cols = cols                
        self._hall_name = hall_name          
        self._seats = {}                 
        self._show_list = []               

        # Insert this hall instance into Star_Cinema's hall_list
        self.entry_hall(self)

    # Task : 3
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info) 

        seat_allocation = [["free" for _ in range(self._cols)] for _ in range(self._rows)] 
        self._seats[show_id] = seat_allocation 

    # Task : 4
    def book_seats(self, show_id, seat_list):
        if show_id not in self._seats: 
            print(f"\nShow Id: {show_id} is not correct. Provide a valid Show Id.\n")
            return

        seat_allocation = self._seats[show_id] 

        for row, col in seat_list:
            if 0 <= row < self._rows and 0 <= col < self._cols: 
                if seat_allocation[row][col] == "free":
                    seat_allocation[row][col] = "booked"
                    print(f"\nSeat ({row}, {col}) has been successfully booked.\n")
                else:
                    print(f"Seat ({row}, {col}) is already booked.")
            else:
                print(f"Seat ({row}, {col}) is not available.")

    # Task : 5
    def view_show_lists(self):
        if not self._show_list: 
            print("\nNo shows are currently available. Please, first create/entry a show.\n")
            return

        print("---------------------------------")
        print("Show List :")
        print("Show_Id\t\tName\t\tTime")
        for show_id, movie_name, time in self._show_list:
            print(f"{show_id}\t\t{movie_name}\t\t{time}")
        print("----------------------------------")    


    # Task : 6
    def view_available_seats(self, show_id):
        if show_id not in self._seats: 
            print(f"\nShow Id: {show_id} does not exist. Provide a valid Show Id.\n")
            return

        seat_allocation = self._seats[show_id] 

        print(f"\nAvailable seats for Show ID: {show_id}\n")
        
        # Display all available seats
        for row in range(self._rows):
            row_display = []
            for col in range(self._cols):
                status = "available" if seat_allocation[row][col] == "free" else "booked"
                row_display.append(f"({row},{col})-> {status}")
            print(f"[ {'  '.join(row_display)} ]")

        print()


# Task : 7

 # create a hall
hall1 = Hall(3, 5, "Star_Cineflex")

while True:

    print(f"Welcome {hall1._hall_name} !!\n")
    print("1. Entry Show")
    print("2. View Shows")
    print("3. View Available Seat")
    print("4. Book Seat")
    print("5. Exit")
    
    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        show_id = input("Enter the show ID: ")
        movie_name = input("Enter the name of the movie : ")
        time = input("Enter the show time : ")

        hall1.entry_show(show_id, movie_name, time)
        
    elif choice == 2:
        hall1.view_show_lists()
        
    elif choice == 3:
        show_id = input("Enter the show ID: ")

        hall1.view_available_seats(show_id)

    elif choice == 4:
        show_id = input("Enter the show ID: ")
        num_seats = int(input("Enter the number of seats to book: "))
        seat_list = []
        
        for i in range(num_seats):
            row = int(input(f"Enter row for seat {i + 1}: "))
            col = int(input(f"Enter column for seat {i + 1}: "))
            seat_list.append((row, col))

        hall1.book_seats(show_id, seat_list)

    elif choice == 5:
        break
    else:
        print("Invalid Input")
        