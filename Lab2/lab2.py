import csv
import os

farePerTicket=500

class Train:
    def __init__(self,TrainID,Name,Source,Destination,TotalSeats):
        self.trainID=TrainID
        self.name=Name
        self.source=Source
        self.destination=Destination
        self.totalSeats=int(TotalSeats)
        self.revenue=0
        self.availableSeats=self.totalSeats
    
    def checkAvailability(self,numTickets):
        return numTickets<=self.availableSeats
    
    def bookTickets(self,numTickets):
        if self.checkAvailability(numTickets):
            self.availableSeats -= numTickets
            amount = farePerTicket * numTickets
            self.revenue = amount
            return amount
        else:
            return None


def loadTrainData(filename):
    trains={}
    if os.path.exists(filename):
        with open(filename,'r') as file:
            reader = csv.DictReader(file) #Read CSV Files as Dictionary, taking Key from header and values as rows
            readTrains = [row for row in reader]

            for train in readTrains:
                trainCreate=Train(train['TrainID'],train['Train Name'],train['Source Station'],train['Destination Station'],train['Total Seats'])
                trains[train['TrainID']]=trainCreate
    else:
        print(f"Invalid file name : {filename} while loading train data")
    
    return trains

def loadPassengerData(filename,trains):
    if os.path.exists(filename):
        with open(filename,'r') as file:
            reader = csv.DictReader(file)
            readPassengers = [row for row in reader]
            for passenger in readPassengers:
                trainID = passenger['Train ID']
                numTickets = int(passenger['Number of Tickets'])

                try:
                    amountSpent = trains[trainID].bookTickets(numTickets)
                    if amountSpent != None :
                        print(f"{passenger['Passenger Name']} booked {numTickets} for Train {trainID} and spent {amountSpent}")
                    else:
                        print(f"Insufficient Seats on Train {trainID}, Couldn't Book Tickets for {passenger['Passenger Name']}")
                except KeyError:
                    print(f"Invalid Train : {trainID}")
                
    else:
        print(f"Invalid file name : {filename} while loading passenger data")

def generateReports(trains):
    print("----Report 1----")
    for trainID,train in trains.items():
        print(f"Train ID: {trainID},Name: {train.name},Source: {train.source},Destination: {train.destination},Available Seats: {train.availableSeats}")

    print("----Report 1----")
    for trainID,train in trains.items():
        print(f"Train ID : {trainID}, Revenue Generated : {train.revenue}")

if __name__=="__main__":
    trainData = loadTrainData('trains.csv');
    loadPassengerData('passengers.csv',trainData)
    print("\n\n\n")
    generateReports(trainData)