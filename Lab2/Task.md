# LAB Assignment 2: Railway Ticket Reservation System

You are tasked with developing a railway ticket reservation system for a busy rail network. The system
should handle ticket booking, seat availability, and generate reports for the railway administration. Your
task is to implement a Python program that provides the following functionalities:

Load Train Data: The program should read the train data from a CSV file named "trains.csv." Each row in
the CSV file represents a train with the following information:

- Train ID (a unique alphanumeric code)
- Train Name
- Source Station
- Destination Station
- Total Seats (total number of seats available on the train)

Load Passenger Data: The program should read the passenger data from a CSV file named
"passengers.csv." Each row in the CSV file represents a passenger with the following information:

- Passenger Name
- Train ID (the ID of the train the passenger wants to book a ticket on)
- Number of Tickets (the number of tickets the passenger wants to book)

Check Seat Availability: Given the train ID and the number of tickets requested by a passenger, the
program should check if there are enough seats available on the specified train for booking. If seats are
available, the booking should be confirmed, and the total fare for the booking should be calculated as per
the fare rules (you can define fare rules based on distance, class, etc.).

Update Seat Availability: After confirming the booking, the program should update the seat availability
for the corresponding train.

Generate Reports:

Report 1: The program should generate a report showing the details of all the trains, including their
names, source stations, destination stations, and the total number of seats available on each train.

Report 2: The program should generate a report showing the total revenue earned from each train based
on the total number of confirmed bookings and their respective fares.

Handle Errors: The program should handle various types of errors gracefully, such as invalid train IDs,
invalid passenger names, insufficient seats, etc., and provide appropriate error messages.

Note:

You can assume that the passenger data in "passengers.csv" will not exceed the available seats on any
train.

You can design the fare rules based on your preference and mention them clearly in the program.

Write the Python program to implement the above functionalities for the railway ticket reservation
system. Use comments to explain each step of your implementation and provide sample CSV files
("trains.csv" and "passengers.csv") for testing the program