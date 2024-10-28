class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

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

    
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)

        seat_allocation = [["free" for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[show_id] = seat_allocation


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

    
    def view_show_list(self):
        if not self.show_list:
            print("No shows are currently avaiable.")
            return

        print(f"Shows running in Hall {self.hall_no}:")
        for show_id, movie_name, time in self.show_list:
            print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {time}")