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