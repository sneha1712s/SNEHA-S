class Seat:
    def __init__(self, seat_id, row):
        self.seat_id = seat_id
        self.row = row
        self.occupied = False

class SeatingPlan:
    def __init__(self, seating_plan_id, rows):
        self.seating_plan_id = seating_plan_id
        self.rows = rows
        self.columns = 15
        self.seats = [[Seat(f"{i+1}-{j}", i) for j in range(self.columns)] for i in range(self.rows)]

    def add_seat(self, seat_id):
        seat = self.get_seat(seat_id)
        if seat:
            if not seat.occupied:
                seat.occupied = True
                print(f"Seat {seat_id} added successfully.")
            else:
                print(f"Seat {seat_id} is already occupied.")
        else:
            print(f"Seat {seat_id} does not exist.")

    def delete_seat(self, seat_id):
        seat = self.get_seat(seat_id)
        if seat:
            if seat.occupied:
                seat.occupied = False
                print(f"Seat {seat_id} deleted successfully.")
            else:
                print(f"Seat {seat_id} is already empty.")
        else:
            print(f"Seat {seat_id} does not exist.")
    
    def update_seat(self, seat_id, new_seating_plan, occupied):
        seat = self.get_seat(seat_id)
        if seat:
            seat.occupied = occupied
            seat.seating_plan = new_seating_plan
            print(f"Seat {seat_id} updated successfully.")
        else:
            print(f"Seat {seat_id} does not exist.")
            
    def get_seat(self, seat_id):
        for row in self.seats:
            for seat in row:
                if seat.seat_id == seat_id:
                    return seat
        return None

class Stadium:
    def __init__(self):
        self.seating_plans = {}

    def add_seating_plan(self, seating_plan):
        self.seating_plans[seating_plan.seating_plan_id] = seating_plan

    def get_seating_plan(self, seating_plan_id):
        return self.seating_plans.get(seating_plan_id)

class SeatingManager:
    def __init__(self, stadium):
        self.stadium = stadium

    def display_menu(self):
        print("\nMenu:")
        print("1. Add Seat")
        print("2. Delete Seat")
        print("3. Get Seat")
        print("4. Update Seat")
        print("5. Exit")
    def run(self):
        output_file = open("seating_output.txt", "w")  # Open the file for writing
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
           # output_file.write("\nMenu:\n1. Add Seat\n2. Delete Seat\n3. Get Seat\n4. Update Seat\n5. Exit\n")
            if choice == "1":
                seating_plan_id = input("Enter seating plan ID(plan1/plan2/plan3): ")
                seat_id = input("Enter seat ID to add(row-col): ")
                seating_plan = self.stadium.get_seating_plan(seating_plan_id)
                if seating_plan:
                    seating_plan.add_seat(seat_id)
                    output_file.write(f"Seat {seat_id} added successfully.\n")
                else:
                    output_file.write("Seating plan not found.\n")

            elif choice == "2":
                seating_plan_id = input("Enter seating plan ID(plan1/plan2/plan3): ")
                seat_id = input("Enter seat ID to delete(row-col): ")
                seating_plan = self.stadium.get_seating_plan(seating_plan_id)
                if seating_plan:
                    seating_plan.delete_seat(seat_id)
                    output_file.write(f"Seat {seat_id} deleted successfully.\n")
                else:
                    output_file.write("Seating plan not found.\n")

            elif choice == "3":
                seating_plan_id = input("Enter seating plan ID(plan1/plan2/plan3): ")
                seat_id = input("Enter seat ID to find(row-col): ")
                seating_plan = self.stadium.get_seating_plan(seating_plan_id)
                if seating_plan:
                    seat = seating_plan.get_seat(seat_id)
                    if seat:
                        output_file.write(f"Seat {seat_id} is {'occupied' if seat.occupied else 'empty'}.\n")
                    else:
                        output_file.write(f"Seat {seat_id} not found.\n")
                else:
                    output_file.write("Seating plan not found.\n")
        
            elif choice == "4":
                seat_id = input("Enter seat ID to update(row-col): ")
                new_seating_plan_id = input("Enter new Seating Plan ID(plan1/plan2/plan3): ")
                occupied = input("Is the seat occupied? (True/False): ").lower() == 'true'
                seating_plan = self.stadium.get_seating_plan(new_seating_plan_id)
                if seating_plan:
                    seating_plan.update_seat(seat_id, new_seating_plan_id, occupied)
                    output_file.write(f"Seat {seat_id} updated successfully.\n")
                else:
                    output_file.write("New seating plan not found.\n")

            elif choice == "5":
                print("Exiting program.")
                output_file.write("Exiting program.\n")
                break

            else:
                print("Invalid choice. Please enter a valid option.")
                output_file.write("Invalid choice. Please enter a valid option.\n")
        output_file.close()  # Close the file after writing

if __name__ == "__main__":
    stadium = Stadium()

    seating_plan1 = SeatingPlan("plan1", 15)
    seating_plan2 = SeatingPlan("plan2", 15)
    seating_plan3 = SeatingPlan("plan3", 15)

    stadium.add_seating_plan(seating_plan1)
    stadium.add_seating_plan(seating_plan2)
    stadium.add_seating_plan(seating_plan3)

    seating_manager = SeatingManager(stadium)
                                                               
    seating_manager.run()
