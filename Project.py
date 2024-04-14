import random
import string

class SeatBookingSystem:
    """
    This class represents a seat booking system for an airline, managing both seat states
    and customer data associated with each booking.
    """

    def __init__(self):
        # Initialize the seat map. 'F' denotes free; occupied seats will hold their booking reference.
        # We simplify the seating configuration with a 3x6 layout, avoiding complexities of aisles or storage areas for this example.
        self.seats = [['F' for _ in range(6)] for _ in range(3)]
        self.customer_db = {}  # Simulates a database of customer details indexed by booking references.
        self.generated_references = set()  # Ensures unique booking references.

    def generate_unique_reference(self):
        """
        Generates a unique booking reference consisting of exactly eight alphanumeric characters.
        """
        while True:
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if reference not in self.generated_references:
                self.generated_references.add(reference)
                return reference

    def book_seat(self, row, col, passport, first_name, last_name):
        """
        Books a seat if it is available and stores customer data in the 'database'.
        """
        if self.seats[row][col] == 'F':
            reference = self.generate_unique_reference()
            self.seats[row][col] = reference
            self.customer_db[reference] = {'passport': passport, 'first_name': first_name, 'last_name': last_name}
            print(f"Seat at row {row+1} column {col+1} has been booked with reference {reference}.")
        else:
            print(f"Seat at row {row+1} column {col+1} is not available for booking.")

    def free_seat(self, row, col):
        """
        Frees a seat if it was previously booked and removes associated customer data.
        """
        if self.seats[row][col] != 'F':
            reference = self.seats[row][col]
            self.seats[row][col] = 'F'
            del self.customer_db[reference]  # Remove customer data from the 'database'.
            print(f"Seat at row {row+1} column {col+1} has been freed.")
        else:
            print(f"Seat at row {row+1} column {col+1} is already free.")

    def display_seats(self):
        """
        Displays the current booking state of all seats.
        """
        for row in self.seats:
            print(' '.join(row))
        print()

def main():
    system = SeatBookingSystem()
    system.book_seat(0, 0, "123456789", "John", "Doe")
    system.display_seats()
    system.free_seat(0, 0)
    system.display_seats()

main()
