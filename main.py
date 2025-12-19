from checkin_checkout import check_in, check_out
from report_generator import generate_daily_report
from visualize import visualize_productivity

def menu():
    while True:
        print("\n1. Check-In\n2. Check-Out\n3. Generate Daily Report\n4. Visualize Productivity\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            check_in(emp_id, name)

        elif choice == '2':
            emp_id = input("Enter Employee ID: ")
            check_out(emp_id)

        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            generate_daily_report(date)

        elif choice == '4':
            date = input("Enter date (YYYY-MM-DD): ")
            visualize_productivity(date)

        elif choice == '5':
            break
        else:
            print("[!] Invalid choice.")

if __name__ == '__main__':
    menu()