# Task : 1
class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

# Task : 2
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self.rows = rows                 
        self.cols = cols                  
        self.hall_no = hall_no         
        self.seats = {}                   
        self.show_list = []              

        # insert this hall instance into Star_Cinema's hall_list
        self.entry_hall(self)

    
    # Task : 3
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)

        seat_allocation = [["free" for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[show_id] = seat_allocation


    # Task : 4
    def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            print(f"Your {show_id} is not correct.")
            return

        seat_allocation = self.seats[show_id]

        for row, col in seat_list:
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if seat_allocation[row][col] == "free":
                    seat_allocation[row][col] = "booked"
                    print(f"Seat ({row}, {col}) has been successfully booked.")
                else:
                    print(f"Seat ({row}, {col}) is already booked.")
            else:
                print(f"Seat ({row}, {col}) is not available.")

    # Task : 5
    def view_show_list(self):
        if not self.show_list:
            print("No shows are currently avaiable.")
            return

        for show_id, movie_name, time in self.show_list:
            print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {time}")


    # Task : 6
    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print(f"Your {show_id} does not exist.")
            return

        seat_allocation = self.seats[show_id]
        available_seats = []
        
        # display all available seats
        for row in range(self.rows):
            for col in range(self.cols):
                if seat_allocation[row][col] == "free":
                    available_seats.append((row, col))

        if available_seats:
            for seat in available_seats:
                print(f"Seat : {seat} is available.")
        else:
            print("No seats available for this show.")


# created a hall instance
star_cineflex = Hall(3, 5, "hall_1")

# creating show
star_cineflex.entry_show("show_1", "Inception", "7:00 PM")
star_cineflex.entry_show("show_2", "Interstellar", "9:00 PM")

# booking seat
star_cineflex.book_seats("show_1", [(0, 0), (1, 1), (2, 2)])

# showing available seats
star_cineflex.view_available_seats("show_1")