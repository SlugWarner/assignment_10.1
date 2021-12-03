# Stephen Warner
# Assignment 10.1: Your Own Class
# My own class made to practice writing classes

import random

class Train:
    # Constructor method takes the starting number of passengers and the ticket price
    def __init__(self, num, ticket_price):
        # Initialises private num passengers variable to num
        self.__num_passengers = num
        # Initialises private total profit variable to num * ticket price
        self.__total_profit = ticket_price * num
        # Initialises private station number variable to 0
        self.__station_num = 0
        # Initialises private distance travelled variable to 0
        self.__distance_travelled = 0
        # Initialises ticket price class variable variable to ticket price
        self.ticket_price = ticket_price

    # Returns the number of passengers
    def get_num_passengers(self):
        return self.__num_passengers

    # Returns the distance travelled
    def get_distance_travelled(self):
        return self.__distance_travelled

    # Returns the total profit
    def get_total_profit(self):
        return self.__total_profit

    # Returns the station number
    def get_station_num(self):
        return self.__station_num

    # Sets the number of passengers to the given number
    def set_num_passengers(self, x):
        self.__num_passengers = x
        self.__total_profit = x * self.ticket_price

    # Sets the distance travelled to the given number
    def set_distance_travelled(self, x):
        self.__distance_travelled = x
    
    # Next stop method
    def next_stop(self):
        # There are 10 stops in my loop, so if station number was set to 11 on the last call of this method, it is set back to 0
        if self.__station_num == 11:
            self.__station_num = 0
        else:
            # Increments the station number
            self.__station_num += 1
        # Increases the distance travelled by 3 km for every stop
        self.__distance_travelled += 3
        # Assigns x to be a random integer between 0 and 30
        x = random.randint(0, 30)
        # Removes that random amount from the total passengers
        self.__num_passengers -= x
        print(f"{x} passengers disembarked.")
        # Assigns x to be a random integer between 0 and 30
        x = random.randint(0, 30)
        # Adds that random amount to the total passengers
        self.__num_passengers += x
        print(f"{x} passengers got on the train.")
        # Adds to the total profit the number of passengers that just got on * the ticket price
        self.__total_profit += x * self.ticket_price

    # Changes the ticket price to the given number
    def change_ticket_price(self, x):
        self.ticket_price = x

    # Mayday method
    def mayday(self):
        # Prints a message
        print("ALL PASSENGERS PLEASE EXIT THE TRAIN IN A CONTROLLED MANNER. DO NOT PANIC.")
        # Temporary num_passengers variable
        num_passengers = self.__num_passengers
        # Sets the number of passengers to 0, simulating they got off the train
        self.__num_passengers = 0
        # Removes the number of passengers * the ticket price, simulating that they were refunded their tickets
        self.__total_profit -= num_passengers * self.ticket_price
        if self.__total_profit < 0:
            self.__total_profit = 0

def main():
    train = Train(30, 10)
    print(f"Number of passengers on the train: {train.get_num_passengers()}")
    print(f"Profit: ${train.get_total_profit()}")
    train.next_stop()
    print(f"Number of passengers on the train: {train.get_num_passengers()}")
    print(f"Profit: ${train.get_total_profit()}")
    train.change_ticket_price(25)
    print(f"Station number: {train.get_station_num()}")
    train.next_stop()
    print(f"Number of passengers on the train: {train.get_num_passengers()}")
    print(f"Profit: ${train.get_total_profit()}")
    print(f"Distance Travelled: {train.get_distance_travelled()} km.")
    train.mayday()
    print(f"Number of passengers on the train: {train.get_num_passengers()}")
    print(f"Profit: ${train.get_total_profit()}")

if __name__ == "__main__":
    main()