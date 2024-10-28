# Task : 1
class Star_Cinema:
    _hall_list = []

    def entry_hall(self, hall):
        self._hall_list.append(hall) 


# Task : 2
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self._rows = rows    # Task : 9 -> protected attribute            
        self._cols = cols                
        self._hall_no = hall_no          
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
            print(f"Your {show_id} is not correct.")
            return

        seat_allocation = self._seats[show_id] 

        for row, col in seat_list:
            if 0 <= row < self._rows and 0 <= col < self._cols: 
                if seat_allocation[row][col] == "free":
                    seat_allocation[row][col] = "booked"
                    print(f"Seat ({row}, {col}) has been successfully booked.")
                else:
                    print(f"Seat ({row}, {col}) is already booked.")
            else:
                print(f"Seat ({row}, {col}) is not available.")

    # Task : 5
    def view_show_list(self):
        if not self._show_list: 
            print("No shows are currently available.")
            return

        for show_id, movie_name, time in self._show_list: 
            print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {time}")


    # Task : 6
    def view_available_seats(self, show_id):
        if show_id not in self._seats: 
            print(f"Your {show_id} does not exist.")
            return

        seat_allocation = self._seats[show_id] 
        available_seats = []
        
        # Display all available seats
        for row in range(self._rows): 
            for col in range(self._cols): 
                if seat_allocation[row][col] == "free":
                    available_seats.append((row, col))

        if available_seats:
            for seat in available_seats:
                print(f"Seat : {seat} is available.")
        else:
            print("No seats available for this show.")


# Task : 7
class Counter:
    def __init__(self, hall):
        self.hall = hall

    def view_shows(self):
        self.hall.view_show_list()

    def view_available_seats(self, show_id):
        self.hall.view_available_seats(show_id)

    def book_tickets(self, show_id, seat_list):
        print(f"Ticket booked successfully for '{show_id}'")
        self.hall.book_seats(show_id, seat_list)


# Create a hall
star_cineflex = Hall(3, 5, "hall_1")

# Create shows
star_cineflex.entry_show("show_1", "Inception", "7:00 PM")
star_cineflex.entry_show("show_2", "Interstellar", "9:00 PM")

# Create a counter for the hall
counter = Counter(star_cineflex)

# View shows
counter.view_shows()

# View available seats for show
counter.view_available_seats("show_1")

# Book some seats for show
counter.book_tickets("show_1", [(0, 0), (1, 1)])

# Show available seats again after bookings
counter.view_available_seats("show_1")