class Error(Exception):
    pass


class SourceNameError(Error):
    pass


class DestinationNameError(Error):
    pass


class SamePlaceError(Error):
    pass


class PlaceNameError(Error):
    pass


class Train:
    def __init__(self):
        self.source = ["mumbai", "bangalore", "delhi", "chennai", "kolkata"]
        self.destination = ["mumbai", "bangalore",
                            "delhi", "chennai", "kolkata"]
        self.sourcee = ''
        self.destinationn = ''
        self.train_no = ''
        self.train_ari = ''
        self.train_dep = ''
        self.ticket_fare = ''

    def fare_calculator(self, source, destination):

        train_no = {
            'mumbai-bangalore': 1, 'mumbai-delhi': 2, 'mumbai-chennai': 3, 'mumbai-kolkata': 4,
            'bangalore-mumbai': 5, 'bangalore-delhi': 6, 'bangalore-chennai': 7, 'bangalore-kolkata': 8,
            'delhi-mumbai': 9, 'delhi-bangalore': 10, 'delhi-chennai': 11, 'delhi-kolkata': 12,
            'chennai-mumbai': 13, 'chennai-bangalore': 14, 'chennai-delhi': 15, 'chennai-kolkata': 16,
            'kolkata-mumbai': 17, 'kolkata-bangalore': 18, 'kolkata-delhi': 19, 'kolkata-chennai': 20
        }

        train_ari = {
            'mumbai-bangalore': '9pm', 'mumbai-delhi': '10pm', 'mumbai-chennai': '12am', 'mumbai-kolkata': '1pm',
            'bangalore-mumbai': '9pm', 'bangalore-delhi': '10pm', 'bangalore-chennai': '12am', 'bangalore-kolkata': '1pm',
            'delhi-mumbai': '9pm', 'delhi-bangalore': '10pm', 'delhi-chennai': '12am', 'delhi-kolkata': '1pm',
            'chennai-mumbai': '9pm', 'chennai-bangalore': '10pm', 'chennai-delhi': '12am', 'chennai-kolkata': '1pm',
            'kolkata-mumbai': '9pm', 'kolkata-bangalore': '10pm', 'kolkata-delhi': '12am', 'kolkata-chennai': '1pm'
        }

        train_dep = {
            'mumbai-bangalore': '9am', 'mumbai-delhi': '10am', 'mumbai-chennai': '12pm', 'mumbai-kolkata': '11pm',
            'bangalore-mumbai': '9am', 'bangalore-delhi': '10am', 'bangalore-chennai': '12pm', 'bangalore-kolkata': '11pm',
            'delhi-mumbai': '9am', 'delhi-bangalore': '10am', 'delhi-chennai': '12pm', 'delhi-kolkata': '11pm',
            'chennai-mumbai': '9am', 'chennai-bangalore': '10am', 'chennai-delhi': '12pm', 'chennai-kolkata': '11pm',
            'kolkata-mumbai': '9am', 'kolkata-bangalore': '10am', 'kolkata-delhi': '12pm', 'kolkata-chennai': '11pm'
        }

        train_fare = {
            'mumbai-bangalore': 1000, 'mumbai-delhi': 2000, 'mumbai-chennai': 3000, 'mumbai-kolkata': 4000,
            'bangalore-mumbai': 1000, 'bangalore-delhi': 2000, 'bangalore-chennai': 3000, 'bangalore-kolkata': 4000,
            'delhi-mumbai': 1000, 'delhi-bangalore': 2000, 'delhi-chennai': 3000, 'delhi-kolkata': 4000,
            'chennai-mumbai': 1000, 'chennai-bangalore': 2000, 'chennai-delhi': 3000, 'chennai-kolkata': 4000,
            'kolkata-mumbai': 1000, 'kolkata-bangalore': 2000, 'kolkata-delhi': 3000, 'kolkata-chennai': 4000
        }
        self.ticket_fare = train_fare[source+'-'+destination]
        self.train_ari = train_ari[source+'-'+destination]
        self.train_dep = train_dep[source+'-'+destination]
        self.train_no = train_no[source+'-'+destination]
        self.sourcee = source
        self.destinationn = destination


class Customer(Train):

    def __init__(self, cust_id, cust_name):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.counter = 0
        super().__init__()

    def book_ticket(self):
        print(' \t Location : mumbai bangalore delhi chennai kolkata ')
        source = input('enter your source ')
        source = source.lower()
        destination = input('enter your destination ')
        destination = destination.lower()
        try:
            if source in self.source and destination in self.destination:
                if source == destination:
                    raise SamePlaceError
                else:
                    Train.fare_calculator(self, source, destination)
                    self.counter = 1

            elif source not in self.source and destination in self.destination:
                raise SourceNameError
            elif source in self.source and destination not in self.destination:
                raise DestinationNameError
            elif source not in self.source and destination not in self.destination:
                raise PlaceNameError

        except SamePlaceError:
            print('\nBoth the source and destination are same ')
        except SourceNameError:
            print('\nwrite the correct source name')
        except DestinationNameError:
            print('\nwrite the correct destination name')
        except PlaceNameError:
            print('\nwrite correct source and destination ')

    def display(self):
        print(
            f"\ndear {self.cust_name} your ticket details \nFrom {self.sourcee} to {self.destinationn} is :")
        print(f"Train no : {self.train_no} \nTrain arriving at : {self.train_ari} \
        \nTrain departuring at : {self.train_dep} \nTrain Fare : {self.ticket_fare}")

    def confirm_booking(self):
        while True:
            pd = int(input('enter amount of Ticket Fare '))
            if pd == self.ticket_fare:
                print('\nYour ticket has been successfully Booked')
                print(f'\nName : {self.cust_name} Id: {self.cust_id} \nTrain no:{self.train_no} From {self.sourcee} to {self.destinationn}\
                \nTrain arriving Time:{self.train_ari} Train departuring Time:{self.train_dep}\
                \nTrain Fare:{self.ticket_fare} Paid')
                print('\n\nHave a Nice Day')
                break
            elif pd != self.ticket_fare:
                print(
                    '!!!\nentered ticket fare is not equal to the ticket fare mentioned!!!')
                ch = input('press any key to pay again or n to exit')
                if ch.lower() == 'n':
                    print('\nBye Have a nice day')
                    break
                else:
                    pass


cust_id = input("Customer ID ")
cust_name = input("Name ")
train = Customer(cust_id, cust_name)
train.book_ticket()
print(train.counter)
if train.counter == 1:
    train.display()
    while True:
        ch = input("Do u want to book the ticket Y or N ? ")
        if ch.lower() == 'y':
            train.confirm_booking()
            break
        elif ch.lower() == 'n':
            print('Bye Have a nice day !!!')
            break
        else:
            print('wrong input enter again')

print("\n program terminated")
