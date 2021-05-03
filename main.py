x = 10           
Booked_seat = 0
prize_of_ticket = 0
Total_Income = 0
Row = int(input('Enter number of Row - \n'))
Seats = int(input('Enter number of seats in a Row - \n'))
Total_seat = Row*Seats
Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]  #to get peron info who has booked the ticket

class chart:           #letz define class chart

    @staticmethod       #will write a static method
    def chart_maker():       #now letz define a fun chart_maker for creating chart
        seats_chart = {}    #First this will be an empty set
        for i in range(Row):       
            seats_in_row = {}    #total no of seats in the row  will be assigned here
            for j in range(Seats):   
                seats_in_row[str(j+1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart

    @staticmethod
    def find_percentage():         #this fun is to find percentage of seats that are booked
        percentage = (Booked_seat/Total_seat)*100     #calculation
        return percentage        #this will return percentage 

class_call = chart      #now letz call class chart and then fun chart maker
table_of_chart = class_call.chart_maker()     

while x != 0:    #when x is not equal to 0 follwing option will be displayed
    print('1 for Show the seats \n2 for Buy a Ticket \n3 for Statistics ',
          '\n4 for Show booked Tickets User Info \n0 for Exit')
    x = int(input('Select Option - ')) #to select option
    if x == 1:          # when x=1 the following code will display the seats
        if Seats < 10:
            for seat in range(Seats):
                print(seat, end='  ')
            print(Seats)
        else:
            for seat in range(10):
                print(seat, end='  ')
            for seat in range(10, Seats):
                print(seat, end=' ')
            print(Seats)
        if Seats < 10:
            for num in table_of_chart.keys():
                print(int(num)+1, end='  ')
                for no in table_of_chart[num].values():
                    print(no, end='  ')
                print()
        else:
            count_num = 0
            for num in table_of_chart.keys():
                if int(list(table_of_chart.keys())[count_num]) < 9:
                    print(int(num)+1, end='  ')
                else:
                    print(int(num)+1, end=' ')
                count_key = 0
                for no in table_of_chart[num].values():
                    if int(list(table_of_chart[num].keys())[count_key]) <= 10:
                        print(no, end='  ')
                    else:
                        print(no, end='  ')
                    count_key += 1
                count_num += 1
                print()
        print('Vacant Seats = ', Total_seat - Booked_seat) #to find vacant seats
        print()

    elif x == 2:
        Row_number = int(input('Enter Row Number - \n'))
        Column_number = int(input('Enter Column Number - \n'))
        if Row_number in range(1, Row+1) and Column_number in range(1, Seats+1):
            if table_of_chart[str(Row_number-1)][str(Column_number)] == 'S':
                if Row*Seats <= 60:
                    prize_of_ticket = 10
                elif Row_number <= int(Row/2):
                    prize_of_ticket = 10
                else:
                    prize_of_ticket = 8
                print('prize_of_ticket - ', '$', prize_of_ticket)
                conform = input('yes for booking and no for Stop booking - ')
                person_detail = {}
                if conform == 'yes':
                    person_detail['Name'] = input('Enter Name - ')
                    person_detail['Gender'] = input('Enter Gender - ')
                    person_detail['Age'] = input('Enter Age - ')
                    person_detail['Phone_No'] = input('Enter Phone number - ')
                    person_detail['Ticket_prize'] = prize_of_ticket
                    table_of_chart[str(Row_number-1)][str(Column_number)] = 'B'
                    Booked_seat += 1
                    Total_Income += prize_of_ticket
                else:
                    continue
                Booked_ticket_Person[Row_number-1][Column_number-1] = person_detail
                print('Booked Successfully')
            else:
                print('This seat already booked by some one')
        else:
            print()
            print('***  Invalid Input  ***')
        print()

    elif x == 3:
        print('Number of purchased Ticket - ', Booked_seat)
        print('Percentage - ', class_call.find_percentage())
        print('Current  Income - ', '$', prize_of_ticket)
        print('Total Income - ', '$', Total_Income)
        print()

    elif x == 4:
        Enter_row = int(input('Enter Row number - \n'))
        Enter_column = int(input('Enter Column number - \n'))
        if Enter_row in range(1, Row+1) and Enter_column in range(1, Seats+1):
            if table_of_chart[str(Enter_row-1)][str(Enter_column)] == 'B':
                person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
                print('Name - ', person['Name'])
                print('Gender - ', person['Gender'])
                print('Age - ', person['Age'])
                print('Phone number - ', person['Phone_No'])
                print('Ticket Prize - ', '$', person['Ticket_prize'])
            else:
                print()
                print('---**---  Vacant seat  ---**---')
        else:
            print()
            print('***  Invalid Input  ***')
        print()

    else:
        print()
        print('***  Invalid Input  ***')
        print()
