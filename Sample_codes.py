#Inheritance
class Animal:
    def __init__(self,name:str):
        self.name = name
class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"
my_dog = Dog("Buddy")
print(my_dog.bark())

#Composition
class Room:
    def __init__(self, name: str):
        self.name = name
class House:
    def __init__(self):
        self.rooms = [Room("Kitchen"), Room("Bedroom")]
my_house = House()
for room in my_house.rooms:
    print(f"Room created: {room.name}")

#Aggregation
class Book:
    def __init__(self, title: str):
        self.title = title
    def __del__(self):
        print(f"Book object destroyed: '{self.title}'")
class Library:
    def __init__(self, books: list[Book] = None):
        self.books = books if books else []
    def __del__(self):
        print("Library object destroyed.")
book1 = Book("The Hobbit")
book2 = Book("1984")
my_library = Library([book1, book2])
print(f"Library populated with: {[b.title for b in my_library.books]}")
print("\nExecuting: del my_library")
del my_library  
print("\nchecking variable accessibility after container deletion:")
print(f"Still active in memory -> book1: {book1.title}")
print(f"Still active in memory -> book2: {book2.title}")

#Association
class Customer:
    def __init__(self, name: str):
        self.name = name
        self.orders = []
class Order:
    def __init__(self, order_id: int, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        customer.orders.append(self)
alice = Customer("Alice")
order_1 = Order(101, alice)
order_2 = Order(102, alice)
print(f"Customer Profile: {alice.name}")
print("Linked orders tracked inside Customer array:")
for o in alice.orders:
    print(f"  - Order ID: {o.order_id}")
print(f"\nOrder #101 lookup -> Owned by customer: {order_1.customer.name}")

#Dependency
class Printer:
    def print_page(self, text: str):
        print(f"Printing: {text}")
class ReportGenerator:
    def __init__(self, content: str):
        self.content = content
    def output_report(self, printer_device: Printer):
        printer_device.print_page(self.content)
my_printer = Printer()
quarter_report = ReportGenerator("Q1 Academic Performance: Excellent!")
quarter_report.output_report(my_printer)

#Realization/Implementation
from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass
class GCashPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ₱{amount} via GCash.")
        return True
gateway = GCashPayment()
success = gateway.process_payment(250.75)
print(f"Payment Status: {success}")




    
