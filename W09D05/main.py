class bookMyMovie:
    def __init__(self):
        self.row = int(input('Enter the number of rows\n'))
        self.col = int(input('Enter the number of seats in each row\n'))
        self.no_of_seats = self.row * self.col
        self.matrix = []
        self.seat_count = 0 # no of purchased tickets
        self.current_income = 0
        self.total_income = 0
        self.total_revenue()
        self.u_details = {}
        
        for i in range(self.row):
            a = []
            for j in range(self.col):
                a.append('S')
            self.matrix.append(a)
    
    def show_seats(self):
        print('\nCinema:')
        print(end="  ")
        for j in range(1, self.col+1):
            print(j, end = " ")
        print()
        a = 0
        for i in self.matrix:
            a = a+1
            print(a,end=" ")
            print(" ".join(i), sep=",")
    
    def buy(self):
        a = int(input('Enter the row you want to book\n'))
        b = int(input('Enter the column you want to book\n'))
        if self.matrix[a-1][b-1] == 'B':
            print('This seat is already booked')
            return
        elif self.no_of_seats < 60:
            current_price = 10
            print('Ticket per person is $10, do you want to proceed ahead? Press Y/y')
        elif a < self.row//2:
            current_price = 10
            print('Ticket per person is $10, do you want to proceed ahead? Press Y/y')
        elif a > self.row//2:
            current_price = 8
            print('Ticket per person is $8, do you want to proceed ahead? Press Y/y')
            
        self.pr = input()
        
        if self.pr == "Y" or self.pr == 'y':
            u_dict = {}
            Uname = input('For Booking, Enter your name\n')
            Ugen = input('Enter the gender\n')
            UAge = input('Enter your age\n')
            Ucn = input('Enter your contact Number\n')
            current_row = a-1
            current_col = b-1
            self.matrix[current_row][current_col] = "B"
            self.seat_count += 1
            self.current_income += current_price
            u_dict[a,b] = [Uname,Ugen,UAge,Ucn,current_price]
            self.u_details.update(u_dict)
            print('Booked Successfully !!\n')
        else:
            print("Booking could't be proccessed!\n")
    
    def total_revenue(self):
        if self.no_of_seats < 60:
            self.total_income = self.no_of_seats * 10
        elif self.no_of_seats >= 60:
            income_from_front = (self.row//2)*self.col*10
            income_from_back = (self.row - (self.row//2))*self.col*8
            self.total_income = income_from_front + income_from_back
    
    def stats(self):
        print("Number of purchased tickets: ",self.seat_count)
        self.percentage = (self.seat_count/self.no_of_seats)*100
        print("Percentage of Tickets Booked:","{:.2f}".format(self.percentage),"%")
        print("Current Income : $",self.current_income)
        print("Total Income : $",self.total_income)
        
    def info(self):
        self.check_a = int(input('Enter the row you booked\n'))
        self.check_b = int(input('Enter the column you booked\n'))
        if self.matrix[self.check_a-1][self.check_b-1] == "B":
            ticket_info = self.u_details[(self.check_a,self.check_b)]
            print('Name:',ticket_info[0])
            print('Gender:',ticket_info[1])
            print('Age:',ticket_info[2])
            print('Phone No:',ticket_info[3])
            print('Ticket Price',ticket_info[4])
        else:
            print('This seat is not booked yet!')
            
    def menu(self):
        ans = True
        while ans:
            print('\n Enter the number corresponding to what you want to choose:')
            self.choice = int(input("\n1. Show the seats\n2. Buy a Ticket\n3. Statistics\n4. Show booked ticket User Info\n0. Exit\n"))
            if self.choice == 1:
                self.show_seats()
            elif self.choice == 2:
                self.buy()
            elif self.choice == 3:
                self.stats()
            elif self.choice == 4:
                self.info()
            elif self.choice == 0:
                ans = False
            else:
                print('\n Not a Valid Choice Try Again!!')
obj = bookMyMovie()
obj.menu()