# Pei Jun Yu, 210939L, IT2852-01
from datetime import datetime

import colorama
from colorama import init, Fore, Style
from tabulate import tabulate
import re as r

colorama.init(autoreset=True)


class Car:
    count = 0

    def __init__(self, CarEngineNo, CarBrand, CarType, Mileage, RegYear):
        self.CarEngineNo = CarEngineNo
        self.CarBrand = CarBrand
        self.CarType = CarType
        self.Mileage = int(Mileage)
        self.RegYear = int(RegYear)
        Car.count += 1

    #   Accessor & Mutator methods

    def get_CarEngineNo(self):
        return self.CarEngineNo

    def get_CarBrand(self):
        return self.CarBrand

    def get_CarType(self):
        return self.CarType

    def get_Mileage(self):
        return self.Mileage

    def get_RegYear(self):
        return self.RegYear

    def get_count(self):
        return self.count

    def set_CarEngineNo(self, CarEngineNo):
        self.CarEngineNo = CarEngineNo

    def set_CarBrand(self, CarBrand):
        self.CarBrand = CarBrand

    def set_CarType(self, CarType):
        self.CarType = CarType

    def set_Mileage(self, Mileage):
        self.Mileage = Mileage

    def set_RegYear(self, RegYear):
        self.RegYear = RegYear

    def set_count(self, count):
        self.count = count


def display_car_details():
    table_data = []
    for v, car_item in enumerate(car_list, start=1):
        car_item.set_count(v)
        table_data.append([
            v,
            car_item.get_CarEngineNo(),
            car_item.get_CarBrand(),
            car_item.get_CarType(),
            car_item.get_Mileage(),
            car_item.get_RegYear()
        ])

    headers = [
        "Record Count",
        "Car Engine No",
        "Car Brand",
        "Car Type",
        "Mileage",
        "Registration Year"
    ]

    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


def display_stats():
    mileage_list = [int(car.get_Mileage()) for car in car_list]
    mileage_list.sort()
    total_cars = len(car_list)
    mean = sum(mileage_list) / total_cars
    median = mileage_list[total_cars // 2]
    max_mileage = max(mileage_list)
    min_mileage = min(mileage_list)
    q1 = mileage_list[total_cars // 4]
    q3 = mileage_list[(total_cars // 4) * 3]
    IQR = q3 - q1

    print(Fore.GREEN + "\nMileage Statistics:")
    print(f"Total Cars: {total_cars}")
    print(f"Mean Mileage: {mean}")
    print(f"Median Mileage: {median}")
    print(f"Maximum Mileage: {max_mileage}")
    print(f"Minimum Mileage: {min_mileage}")
    print(f"75th Percentile Mileage: {q3}")
    print(f"25th Percentile Mileage: {q1}")
    print(f"Interquartile Range: {IQR}")


car_list = [
    Car("112251654254", "KIA", "SUV", '71000', '2021'),
    Car("569325487515", "BMW", "SEDAN", '20000', '2023'),
    Car("A09821295", "CHEVROLET", "SUV", '123190', '2011'),
    Car("K12393195", "FORD", "VAN", '92281', '2009'),
    Car("AA22119977", "AUDI", "MINIVAN", '100902', '2021'),
    Car("A13A230982", "EICHER", "SEDAN", '99293', ' 1999'),
    Car("A13A230900", "AUDI", "SEDAN", '100000', '1999'),
    Car("A13A231910", "AUDI", "VAN", '100280', '1999')
]

acceptable_years_range = range(1900, 2024)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index].get_RegYear() < right[right_index].get_RegYear():
            merged.append(left[left_index])
            left_index += 1
        elif left[left_index].get_RegYear() > right[right_index].get_RegYear():
            merged.append(right[right_index])
            right_index += 1
        else:
            if left[left_index].get_CarEngineNo() < right[right_index].get_CarEngineNo():
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


class Customer:
    cust_count = 0

    def __init__(self, customer_id, name, email, tier, points):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.tier = tier
        self.points = points
        Customer.cust_count += 1

    def get_customer_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_tier(self):
        return self.tier

    def get_points(self):
        return self.points

    def get_cust_count(self):
        return self.cust_count

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_tier(self, tier):
        self.tier = tier

    def set_points(self, points):
        self.points = points

    def set_cust_count(self, cust_count):
        self.cust_count = cust_count


class CustomerRequest(Customer):
    def __init__(self, customer, request, time):
        super().__init__(
            customer.get_customer_id(),
            customer.get_name(),
            customer.get_email(),
            customer.get_tier(),
            customer.get_points()
        )
        self.request = request
        self.time = time

    def get_request(self):
        return self.request

    def set_request(self, request):
        self.request = request

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time


# Implementation of the Queue ADT using a Python list.
class Queue:
    # Creates an empty queue.
    def __init__(self):
        self._qlist = list()

    # Returns True if the queue is empty.
    def isEmpty(self):
        return len(self._qlist) == 0

    # Returns the number of items in the queue.
    def __len__(self):
        return len(self._qlist)

    def enqueue(self, item):
        self._qlist.append(item)

    def dequeue(self):
        assert not self.isEmpty(), \
            "Cannot dequeue from an empty queue"
        return self._qlist.pop(0)


def add_customer_request():
    while True:
        try:
            customer_id = input(Fore.YELLOW + "Enter Customer ID: ").upper()
            if sequential_search(customer_id, customer_list):
                while True:
                    try:
                        customer_request = input(Fore.YELLOW + "Enter Customer's Request: ").replace(' ', '')
                        if len(customer_request) == 0:
                            raise ValueError
                        customer = get_customer(customer_id)
                        realtime = get_real_time()
                        customer_request_obj = CustomerRequest(customer, customer_request, realtime)
                        queue.enqueue(customer_request_obj)
                        customer_request_list.append(customer_request_obj)
                        print(Fore.GREEN + "Customer request added successfully.")
                        print(Fore.GREEN + "=" * 60)
                        break
                    except ValueError:
                        print(Fore.RED + "Invalid Request!" + Fore.CYAN + " Please enter a valid request!")
            else:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Invalid input. " + Fore.CYAN + "Please try again.")


def sequential_search(customer_id, customer_list):
    for customer in customer_list:
        if customer.get_customer_id() == customer_id:
            return True
    return False


def get_customer(customer_id):
    for customer in customer_list:
        if customer.get_customer_id() == customer_id:
            return customer
    return None


def get_real_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time


def view_number_of_requests():
    print(Fore.GREEN + "=" * 60)
    print(Fore.CYAN + "Number of customer requests in the queue:", queue.__len__())
    print(Fore.GREEN + "=" * 60)


def process_next_request():
    if not queue.isEmpty():
        customer_request = queue.dequeue()
        customer_id = customer_request.get_customer_id()
        customer_name = customer_request.get_name()
        customer_email = customer_request.get_email()
        customer_tier = customer_request.get_tier()
        customer_points = customer_request.get_points()
        request = customer_request.get_request()
        time = customer_request.get_time()

        print(Fore.GREEN + "=" * 60)
        print(Fore.CYAN + "Processing Customer ID:", customer_id)
        print(Fore.CYAN + "Name: ", customer_name)
        print(Fore.CYAN + "Email: ", customer_email)
        print(Fore.CYAN + "Tier: ", customer_tier)
        print(Fore.CYAN + "Points: ", customer_points)
        print(Fore.GREEN + "=" * 60)
        print(Fore.CYAN + "Time of Request: ", time)
        print(Fore.CYAN + "Request: ", request)
        print(Fore.GREEN + "=" * 60)
        print("")
        print(Fore.CYAN + "Remaining Requests: ", queue.__len__())
    else:
        print(Fore.RED + "No customer requests in the queue.")


queue = Queue()

customer_list = [
    Customer('S001', 'John Doe', 'john.doe@example.com', 'C', 100),
    Customer('S002', 'Jane Smith', 'jane.smith@example.com', 'A', 250),
    Customer('S003', 'Michael Johnson', 'michael.johnson@example.com', 'C', 50),
    Customer('S004', 'Emily Davis', 'emily.davis@example.com', 'B', 500),
    Customer('S005', 'David Wilson', 'david.wilson@example.com', 'A', 300),
    Customer('S012', 'Sarah Thompson', 'sarah.thompson@example.com', 'B', 200),
    Customer('S007', 'Matthew Anderson', 'matthew.anderson@example.com', 'C', 75),
    Customer('S020', 'Olivia Taylor', 'olivia.taylor@example.com', 'A', 350),
    Customer('S019', 'Daniel Brown', 'daniel.brown@example.com', 'B', 250),
    Customer('S010', 'Sophia Martinez', 'sophia.martinez@example.com', 'C', 100),
    Customer('S222', 'Mary Jane', 'maryjane@gmail.com', 'B', 250),
    Customer('S393', 'Kiseki', 'Daisukiseki@gmail.com', 'A', 600),
    Customer('S011', 'Jordan lee', 'jdlee@gmaiol.com', 'A', 200)

]

customer_request_list = [
    CustomerRequest(Customer('S222', 'Mary Jane', 'maryjane@gmail.com', 'B', 250), 'Great Service!',
                    '2023-07-03 18:21:26'),
    CustomerRequest(Customer('S393', 'Kiseki', 'daisukiseki@gmail.com', 'A', 600), 'More seats please',
                    '2023-07-06 05:02:10')
]
for cust in customer_request_list:
    queue.enqueue(cust)


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high].customer_id

    for j in range(low, high):
        if arr[j].customer_id <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and (
            arr[i].get_tier() < arr[left].get_tier()
            or (arr[i].get_tier() == arr[left].get_tier() and arr[i].get_points() > arr[left].get_points())
    ):
        largest = left

    if right < n and (
            arr[largest].get_tier() < arr[right].get_tier()
            or (arr[largest].get_tier() == arr[right].get_tier() and arr[largest].get_points() > arr[
        right].get_points())
    ):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


# Making a regular expression to validate an Email
regexp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(the_email):
    if (r.fullmatch(regexp, the_email)):
        return True

    else:
        return False

def validate_integer(input_string):
    try:
        last_3_digits = int(input_string[-3:])
        return True
    except ValueError:
        return False


def add_customer():
    while True:
        try:
            customer_id = input(Fore.YELLOW + "Customer ID (Must begin with S and 3 digits): ").upper().replace(" ", '')
            if len(customer_id) != 4 or not customer_id.startswith('S') or not customer_id[1:].isdigit():
                raise ValueError("Invalid format. Customer ID must begin with 'S' and have 3 digits.")

            if any(l.get_customer_id() == customer_id for l in customer_list):
                print(Fore.RED + "Duplicated Entry! " + Fore.WHITE + "Please enter again.")
                continue

            break
        except ValueError as ve:
            print(Fore.RED + str(ve) + Fore.CYAN + " Please try again.")

    while True:
        try:
            customer_name = input(Fore.YELLOW + "Name: ")
            if not customer_name.replace(" ", "").isalpha():
                raise ValueError("Invalid input. Name can only contain letters.")
            break
        except ValueError as ve:
            print(Fore.RED + str(ve) + Fore.CYAN + " Please try again.")

    while True:
        try:
            customer_email = input(Fore.YELLOW + 'Email: ')
            if not check(customer_email):
                raise ValueError("Invalid input. Please enter a valid email address.")
            break
        except ValueError as ve:
            print(Fore.RED + str(ve) + Fore.CYAN + " Please try again.")

    customer_tier = 'C'
    print(Fore.CYAN + 'Default Customer Tier is C')
    customer_points = 100
    print(Fore.CYAN + 'Default Points when added is 100')

    newCustomer = Customer(customer_id, customer_name, customer_email, customer_tier, customer_points)
    customer_list.append(newCustomer)
    print(Fore.GREEN + 'Customer Added Successfully')


def customerpage():
    while True:
        print("\n==== Customer Page ====")
        print(Fore.GREEN + "1." + Fore.CYAN + " View Customers")
        print(Fore.GREEN + "2." + Fore.CYAN + " Sort Customers by Tiers & Points using Heap Sort")
        print(Fore.GREEN + "3." + Fore.CYAN + " Add Customer")
        print(Fore.GREEN + "0." + Fore.CYAN + " Back to Customer Request Menu")

        cust_opt = input(Fore.YELLOW + "Enter your choice: ")

        if cust_opt == "1":
            print(Fore.GREEN + '\nDisplaying Customer Records in Alphanumeric Order')
            quick_sort(customer_list, 0, len(customer_list) - 1)
            display_customer_details()

        elif cust_opt == "2":
            print(Fore.GREEN + '\nSorted Customers by Tiers & Points using Heap Sort')
            heap_sort(customer_list)
            display_customer_details()

        elif cust_opt == "3":
            print(Fore.GREEN + "\nEnter Customer Details")
            print(Fore.GREEN + '===================================================')
            add_customer()

        elif cust_opt == "0":
            break

        else:
            print(Fore.RED + "Invalid choice. " + Fore.CYAN + "Please try again.")


def display_customer_details():
    table_data = []
    for cust, customer_item in enumerate(customer_list, start=1):
        customer_item.set_cust_count(cust)
        table_data.append([
            cust,
            customer_item.get_customer_id(),
            customer_item.get_name(),
            customer_item.get_email(),
            customer_item.get_tier(),
            customer_item.get_points()
        ])

    headers = [
        "Customer Count",
        "Customer ID",
        "Name",
        "Email",
        "Tier",
        "Points"
    ]

    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


if __name__ == '__main__':

    def display_menu():
        car = [
            Fore.YELLOW + "        ______",
            Fore.YELLOW + "    ___/|____|\___",
            Fore.GREEN + "   /     SING     \\",
            Fore.GREEN + "  |   o  CAR   o  |",
            Fore.YELLOW + "   \_____________/"
        ]

        car_width = len(car[0])
        menu_width = 60  # Adjust this value to set the desired menu width

        max_line_width = max(len(line) for line in car)
        left_margin = (menu_width - max_line_width) // 2

        print("\n".join(" " * left_margin + line for line in car))
        print("\nWelcome! Thanks for using SINGCAR! How can we help you?")
        print(Fore.GREEN + "1. " + Fore.CYAN + "Display all cars records in Alphanumeric order")
        print(
            Fore.GREEN + "2. " + Fore.CYAN + "Sort cars by CarBrand in ascending order using Bubble Sort and display the outcome")
        print(
            Fore.GREEN + "3. " + Fore.CYAN + "Sort cars by Mileage in descending order using Insertion Sort and display the outcome")
        print(Fore.GREEN + "4. " + Fore.CYAN + "Sort cars by Registration Year in ascending order")
        print(Fore.GREEN + "5. " + Fore.CYAN + "Sort cars by Registration Year in descending order")
        print(Fore.GREEN + "6. " + Fore.CYAN + "Sort cars by Car Types in ascending order using selection sort")
        print(
            Fore.GREEN + "7. " + Fore.CYAN + "Sort cars using Merge sort to arrange cars in ascending order,first by Registration Year and then by Car Engine Number.")
        print(Fore.GREEN + "=" * menu_width)
        print(Fore.GREEN + "8. " + Fore.CYAN + "Add a new car record")
        print(Fore.GREEN + "9. " + Fore.YELLOW + "Update" + Fore.CYAN + " a car record")
        print(Fore.GREEN + "10. " + Fore.RED + "Delete " + Fore.CYAN + "a car record")
        print(Fore.GREEN + "11. " + Fore.BLUE + "Search " + Fore.CYAN + "a car record")
        print(Fore.GREEN + "=" * menu_width)
        print(Fore.GREEN + "12. " + Fore.CYAN + "Display Mileage Statistics")
        print(Fore.GREEN + "13. " + Fore.CYAN + "Manage Customer Request")
        print(Fore.GREEN + "0. " + Fore.CYAN + "Exit the program")


    while True:
        try:
            display_menu()
            choice = int(input(Fore.YELLOW + "Please enter your choice: "))

            if choice == 1:  # display all the car records using insertion sort in increasing order
                print(Fore.GREEN + '\nDisplaying Records and Car Details in Alphanumeric Order')

                for i in range(1, len(car_list)):
                    current_car = car_list[i]
                    j = i - 1

                    while j >= 0 and car_list[j].CarEngineNo > current_car.CarEngineNo:
                        car_list[j + 1] = car_list[j]
                        j -= 1

                    car_list[j + 1] = current_car

                display_car_details()

            elif choice == 2:  # sort cars by car brand in ascending order using bubble sort
                n = len(car_list)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if car_list[j].CarBrand > car_list[j + 1].CarBrand:
                            car_list[j], car_list[j + 1] = car_list[j + 1], car_list[j]

                print(Fore.GREEN + "\nCars sorted by CarBrand in ascending order:")

                display_car_details()

            elif choice == 3:  # sort cars by mileage in descending order using insertion sort
                for i in range(1, len(car_list)):
                    key = car_list[i]
                    j = i - 1
                    while j >= 0 and key.Mileage > car_list[j].Mileage:
                        car_list[j + 1] = car_list[j]
                        j -= 1
                    car_list[j + 1] = key

                print(Fore.GREEN + "\nCars sorted by Mileage in descending order:")
                display_car_details()

            elif choice == 4:  # display years in ascending order
                for i in range(1, len(car_list)):
                    current_car = car_list[i]
                    j = i - 1

                    while j >= 0 and car_list[j].RegYear > current_car.RegYear:
                        car_list[j + 1] = car_list[j]
                        j -= 1

                    car_list[j + 1] = current_car
                print(Fore.GREEN + "\nCars sorted by Registration Year in ascending order:")

                display_car_details()

            elif choice == 5:  # display years in descending order
                for i in range(1, len(car_list)):
                    key = car_list[i]
                    j = i - 1
                    while j >= 0 and key.RegYear > car_list[j].RegYear:
                        car_list[j + 1] = car_list[j]
                        j -= 1
                    car_list[j + 1] = key

                print(Fore.GREEN + "\nCars sorted by Registration Year in descending order:")
                display_car_details()


            elif choice == 6:  # use Selection sort to arrange the car Types in ascending order
                n = len(car_list)
                for i in range(n - 1):
                    min_index = i
                    for j in range(i + 1, n):
                        if car_list[j].get_CarType() < car_list[min_index].get_CarType():
                            min_index = j
                    car_list[i], car_list[min_index] = car_list[min_index], car_list[i]

                print(Fore.GREEN + "\nCars sorted by Car Types in ascending order:")
                display_car_details()


            elif choice == 7:  # use Merge sort to arrange the cars in ascending order, first by Registration Year and then by Car Engine Number
                car_list = merge_sort(car_list)

                print(Fore.GREEN + "\nCars sorted by Registration Year and Car Engine Number in ascending order:")
                display_car_details()

            elif choice == 8:  # add a new car record
                while True:
                    try:
                        CarEngineNo = str(input("Enter Car Engine No: ")).replace(' ', '').upper()
                        if len(CarEngineNo) < 9 or len(CarEngineNo) >= 13:
                            raise ValueError
                        if not CarEngineNo.isalnum():
                            raise ValueError
                        # Check if engine number is duplicated
                        for x in car_list:
                            if x.get_CarEngineNo() == CarEngineNo:
                                print(Fore.RED + "Duplicated Entry! " + Fore.WHITE + "Please enter again.")
                                break
                        else:
                            break
                    except ValueError:
                        print(
                            Fore.RED + "Invalid input. " + Fore.WHITE + "Please enter a valid alphanumeric entry with 9 - 12 characters for Car "
                                                                        "Engine No.")

                while True:
                    try:
                        CarBrand = str(input("Enter Car Brand: ")).upper().replace(' ', '')
                        if not CarBrand.isalnum():
                            raise ValueError
                        if len(CarBrand) == 0:
                            raise ValueError
                        break
                    except ValueError:
                        print(
                            Fore.RED + "Invalid input. " + Fore.WHITE + "Please enter a valid alphanumeric entry for Car Brand.")

                while True:
                    try:
                        CarType = str(input("Enter Car Type: ")).upper().replace(' ', '')
                        if len(CarType) == 0:
                            raise ValueError
                        if not CarType.isalnum():
                            raise ValueError
                        break
                    except ValueError:
                        print(
                            Fore.RED + "Invalid input. " + Fore.WHITE + "Please enter a valid alphanumeric entry for Car Type.")

                while True:
                    try:
                        Mileage = int(input("Enter Mileage: "))
                        if Mileage <= 0:
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print(Fore.RED + "Invalid input. " + Fore.WHITE + "Please enter a valid integer for Mileage.")

                while True:
                    try:
                        # used datetime format to find the current year
                        current_year = datetime.now().year
                        RegYear = int(input("Enter Registration Year: "))
                        if 1900 <= RegYear <= current_year:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print(Fore.RED +
                              "Invalid input. " + Fore.WHITE + f'Please enter a valid four-digit integer for Registration Year (1900 - '
                                                               f'{current_year}).')

                # store the details into the list
                newCar = Car(CarEngineNo, CarBrand, CarType, Mileage, RegYear)
                car_list.append(newCar)
                print(Fore.GREEN + "\nNew Car record has been successfully added!")



            elif choice == 9:  # Update the car record

                print(Fore.GREEN + "===================================================")

                display_car_details()

                while True:

                    try:

                        input_engine = input(
                            Fore.YELLOW + "Please enter the Car Engine No that you want to update: ").replace(" ",
                                                                                                              "").upper()

                        if not input_engine.isalnum() or not 9 <= len(input_engine) <= 12:
                            raise ValueError(

                                Fore.RED + "Invalid input." + Fore.WHITE + "Please enter a valid alphanumeric entry with 9 - 12 characters for Car Engine No.")

                        found_car = next((car for car in car_list if input_engine == car.get_CarEngineNo()), None)

                        if not found_car:
                            print(

                                Fore.RED + "Invalid input. " + Fore.WHITE + "No car record found with the given Car Engine No.")

                            continue

                        print(Fore.YELLOW + "Please enter the updated details")

                        break


                    except ValueError:

                        print(

                            Fore.RED + "Invalid input. " + Fore.WHITE + "Please enter a valid alphanumeric entry with 9 - 12 characters for Car Engine No.")

                while True:
                    try:
                        cb_option = input(Fore.YELLOW + "Do you want to update your Car Brand? (Y/N) ").upper()

                        if cb_option not in ["Y", "N"]:
                            raise ValueError

                        if cb_option == "Y":
                            while True:
                                try:
                                    updated_carbrand = str(
                                        input(Fore.YELLOW + "Enter your updated Car Brand: ").upper().replace(" ", ""))

                                    if not updated_carbrand.isalnum() or len(updated_carbrand) == 0:
                                        raise ValueError
                                    found_car.set_CarBrand(updated_carbrand)
                                    break
                                except ValueError:

                                    print(
                                        Fore.RED + "Invalid input. " + Fore.WHITE + "Please enter a valid alphanumeric entry for Car Brand.")

                        # Ask for subsequent updates regardless of the choice to update car brand

                        while True:
                            try:
                                updated_cartype = input(
                                    Fore.YELLOW + "Do you want to update your Car Type? (Y/N) ").upper()

                                if updated_cartype not in ["Y", "N"]:
                                    raise ValueError

                                if updated_cartype == "Y":
                                    while True:
                                        try:
                                            updated_cartype_input = input(
                                                Fore.YELLOW + "Enter your updated Car Type: ").upper().replace(" ", "")
                                            if not updated_cartype_input.isalnum() or len(updated_cartype_input) == 0:
                                                raise ValueError
                                            found_car.set_CarType(updated_cartype_input)
                                            break

                                        except ValueError:
                                            print(
                                                Fore.RED + "Invalid input. " + Fore.WHITE + "Please enter a valid alphanumeric entry for Car Type.")
                                break  # Exit the loop for car type update

                            except ValueError:
                                print(Fore.RED + "Invalid Input. " + Fore.WHITE + "Please enter either 'Y' or 'N'.")

                        while True:
                            try:
                                updated_mileage = input(
                                    Fore.YELLOW + "Do you want to update your Mileage? (Y/N) ").upper()

                                if updated_mileage not in ["Y", "N"]:
                                    raise ValueError

                                if updated_mileage == "Y":
                                    while True:
                                        try:
                                            updated_mileage_input = int(
                                                input(Fore.YELLOW + "Enter your updated Mileage: "))
                                            if updated_mileage_input <= 0:
                                                raise ValueError
                                            found_car.set_Mileage(updated_mileage_input)
                                            break

                                        except ValueError:
                                            print(
                                                Fore.RED + "Invalid input. " + Fore.WHITE + "Please enter a valid integer for Mileage.")

                                break  # Exit the loop for mileage update
                            except ValueError:
                                print(Fore.RED + "Invalid Input. " + Fore.WHITE + "Please enter either 'Y' or 'N'.")

                        while True:
                            try:
                                updated_regyear = input(
                                    Fore.YELLOW + "Do you want to update your Registration Year? (Y/N) ").upper()

                                if updated_regyear not in ["Y", "N"]:
                                    raise ValueError

                                if updated_regyear == "Y":
                                    while True:
                                        try:
                                            # used datetime format to find the current year
                                            current_year = datetime.datetime.now().year
                                            updated_registrationYear = int(
                                                input(Fore.YELLOW + "Enter your updated Registration Year: "))

                                            if 1900 <= updated_registrationYear <= current_year:
                                                found_car.set_RegYear(updated_registrationYear)
                                                break
                                            else:
                                                raise ValueError
                                        except ValueError:
                                            print(
                                                Fore.RED + "Invalid input. " + Fore.WHITE + f'Please enter a valid four-digit integer for Registration Year (1900 - {current_year}).')
                                break  # Exit the loop for registration year update

                            except ValueError:
                                print(Fore.RED + "Invalid Input. " + Fore.WHITE + "Please enter either 'Y' or 'N'.")
                        print(Fore.GREEN + "Car record updated successfully.")
                        break

                    except ValueError:
                        print(Fore.RED + "Invalid Input. " + Fore.WHITE + "Please enter either 'Y' or 'N'.")

            elif choice == 10:  # Delete a car record
                print(Fore.GREEN + "===================================================")
                display_car_details()
                while True:
                    try:
                        input_engine = input(
                            Fore.YELLOW + "Please enter the Car Engine No that you want to delete: ").replace(" ",
                                                                                                              "").upper()
                        if not input_engine.isalnum() or not 9 <= len(input_engine) <= 12:
                            raise ValueError(
                                Fore.RED + "Invalid input. " + Fore.WHITE + "Please enter a valid alphanumeric entry with 9 - 12 characters for Car Engine No.")

                        found_car = next((car for car in car_list if input_engine == car.get_CarEngineNo()), None)

                        if not found_car:
                            print(
                                Fore.RED + "Invalid input. " + Fore.WHITE + "No car record found with the given Car Engine No.")
                            continue

                        car_list.remove(found_car)
                        print(Fore.GREEN + "Car record deleted successfully.")
                        break

                    except ValueError:
                        print(
                            Fore.RED + "Invalid input. " + Fore.WHITE + "Please enter a valid alphanumeric entry with 9 - 12 characters for Car Engine No.")

            elif choice == 11:  # search by Car Engine No
                while True:
                    try:
                        input_engine = input(
                            Fore.YELLOW + "Please enter the Car Engine No that you want to search: ").replace(" ",
                                                                                                              "").upper()

                        if not input_engine.isalnum() or not 9 <= len(input_engine) <= 12:
                            raise ValueError(
                                Fore.RED + "Invalid input." + Fore.WHITE + "Please enter a valid alphanumeric entry with 9 - 12 characters for Car Engine No.")

                        found_car = next((car for car in car_list if input_engine == car.get_CarEngineNo()), None)

                        if not found_car:
                            print(
                                Fore.RED + "Invalid input. " + Fore.WHITE + "No car record found with the given Car Engine No.")
                            continue

                        print(Fore.GREEN + "===================================================")
                        print(Fore.GREEN + "Car Engine No. searched successfully.")
                        table_data = []
                        c = 1
                        for x in car_list:
                            if x.get_CarEngineNo() == input_engine:
                                table_data.append([
                                    c,
                                    x.get_CarEngineNo(),
                                    x.get_CarBrand(),
                                    x.get_CarType(),
                                    x.get_Mileage(),
                                    x.get_RegYear()
                                ])

                                headers = [
                                    "Record Count",
                                    "Car Engine No",
                                    "Car Brand",
                                    "Car Type",
                                    "Mileage",
                                    "Registration Year"
                                ]

                        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
                        break

                    except ValueError:
                        print(
                            Fore.RED + "Invalid input. " + Fore.WHITE + "Please enter a valid alphanumeric entry with "
                                                                        "9 - 12 characters for Car Engine No.")

            elif choice == 12:  # Mileage Statistics
                display_stats()

            elif choice == 13:  # Manage Customer Request menu function to manage customer request
                while True:
                    print("\n==== Customer Requests Page ====")
                    print(Fore.GREEN + "1." + Fore.CYAN + " Customers Page")
                    print(Fore.GREEN + "2." + Fore.CYAN + " Input customer request")
                    print(Fore.GREEN + "3." + Fore.CYAN + " View number of customer requests")
                    print(Fore.GREEN + "4." + Fore.CYAN + " Service next request in Queue")
                    print(Fore.GREEN + "0." + Fore.CYAN + " Go back to Main Menu")

                    choice = input(Fore.YELLOW + "Enter your choice: ")

                    if choice == "1":
                        customerpage()

                    elif choice == "2":
                        add_customer_request()
                    elif choice == "3":
                        view_number_of_requests()
                    elif choice == "4":
                        process_next_request()
                    elif choice == "0":
                        break
                    else:
                        print(Fore.RED + "Invalid choice. " + Fore.CYAN + "Please try again.")

            elif choice == 0:  # exit the program
                print('\nSee You Again!')
                break

            else:  # if invalid input
                print(Fore.RED + '\nPlease try again.')

        except ValueError:
            print(Fore.RED + '\nPlease try again.')
