class Train:
    def __init__(self,name,fare,seat):
        self.name=name
        self.fare=fare
        self.seat=seat

    def getStatus(self):
         print("***********")
         print(f"name of train is {self.name}")
         print(f"price of the ticket is rs. {self.fare}")
         print(f"seat available are {self.seat}")

    def bookTicket(self):
        if(self.seat>0):
            print(f"your seat is bookes , & your seat no is {self.seat}")
            self.seat=self.seat-1
        
        else:
            print("sorry , Train is booked ")
        
    def cancleTicket(self,seatnum):
       
        self.seatnum=seatnum
        print(f"cancle seat no. is {self.seatnum}")
        list=[1,2,3,4,5,6,7,8,9,10]
        list.append(seatnum)
        self.seat=self.seat+1
       



nrupTrain=Train("Express011",300,10)
nrupTrain.getStatus()
nrupTrain.bookTicket()
print(f"after booking train seat are avaible no. of seat:  {nrupTrain.seat}")
nrupTrain.bookTicket()
nrupTrain.bookTicket()
nrupTrain.bookTicket()
print(f"after booking train seat is avaible is  {nrupTrain.seat}")
nrupTrain.getStatus()
nrupTrain.cancleTicket(8)
nrupTrain.getStatus()
