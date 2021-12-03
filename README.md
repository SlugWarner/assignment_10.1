# assignment_10.1

The purpose of the Train class is to keep track of the total profit the train has made for the day and how far it has travelled. It is a much simpler version of what a train station might use to determine if any
given train is still profitable. It includes variables and methods that stay updated through every stop throughout the train's journey.

The class variable self.ticket_price is a variable that is initialised when the train object is created. It keeps
track of the current price of the ticket that each passenger has to buy before they get on the train.

The data variable self.__num_passengers is initialised when the train object is created, which keeps track
of the number of passengers on the train.

The data variable self.__total_profit is initialised to how many passengers are initialised when the object is
created times the ticket price that is initalised. This is updated at each station when passengers buy
tickets and get on the train.

The data variable self.__station_num is initialised to 0. This keeps track of which station the train is on
in its loop.

The data variable self.__distance_travelled is initialised to 0, and keeps track of how far the train has
travelled in kilometers.

The get_num_passengers method has no arguments and returns the number of passengers on the train

The get_distance_travelled method has no arguments and returns the distance travelled

The get_total_profit method has no arguments and returns the total profit of the train for the day

The get_station_num method has no arguments and returns the number of the station the train is at

The set_distance_travelled method has 1 argument and sets the distance travelled to the given number

The set_num_passengers method has 1 argument and sets the number of passengers to the given number

The change_ticket_price method takes 1 argument and sets the ticket price to the given number

The next_stop method has no arguments. It increments the station number the train is at and the distance the train
has travelled. It then uses the random module to remove a random amount of passengers between 0 and 30 from the
train and adds a random amount of passengers between 0 and 30. It calculates the price of a ticket * the number
of passengers that embarked and adds that to the total profit of the train for the day

The mayday method takes no arguments. It prints a warning message, then sets the number of passengers to 0.
It then takes the amount of passengers that were on the train * the ticket price and removes that number from the 
total profit, simulating that all passengers were refunded their ticket.



In my demo program, first a train object is created with 30 passengers and a ticket price of $10. The number of
passengers and the total profit is printed. Then, the next_stop method is used to advance the train. The number
of passengers and the total profit is printed, then the ticket price is changed to 25. The station number is
printed, then the next_stop method is used to advance the train. The distance travelled is then printed. Finally,
the mayday method is used and the number of passengers and the total profit is printed one last time.
This demo method is run by simply running the program in the terminal.
