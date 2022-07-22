import unittest
from datetime import date
from dataTypeClasses import queryInput

def userInput():
#Welcome user to program
        print("Welcome to Stock Data Visualizer")

#Ask for ticker, store as a string. 
        ticker = input("Enter the ticker symbol of the company you would like to view:\n$")
#convert string from lowercase to upper
        ticker = ticker.upper() 
        print("The length of the string (ticker symbol) is", end = ' ')
        print(len(ticker))
        if len(ticker) > 7:
            raise Exception ("Please enter correct ticker symbol and length (Max length is 7 characters). Please re-run the program.")


#ask if they would like a bar or line store as bool
        while(True):
            try:
                chartType = int(input("What chart type would you like?\n1. Bar\n2. Line\n"))
                if chartType == 1:
                    chartType = False
                    break
                elif chartType == 2:
                    chartType = True
                    break
                else:
                    raise Exception ("Please enter either 1 or 2")
            except:
                raise Exception ("Please enter either 1 or 2")
     
#ask what time series they would like store as int
        while(True):
            try:
                timeSeries = int(input("What time series would you like?\nPlease Note: If you select intraday you will only be provided the last 1 - 2 months of data.\n1. Interday\n2. Daily\n3. Weekly\n4. Monthly\n"))
                if timeSeries == 1:
                    break
                elif timeSeries == 2:
                    break
                elif timeSeries == 3:
                    break
                elif timeSeries == 4:
                    break
                else:
                    raise Exception ("Please enter numbers 1-4")
            except:
                   raise Exception ("Please enter numbers 1-4")
        
        if timeSeries == 1:
            while(True):
                try:
                    interval = int(input("What time intervals would you like to use?\n1. 1 min\n2. 5 min\n3. 15 min\n4. 30 min\n 5. 1 hour\n"))
                    if interval == 1:
                        break
                    elif interval == 2:
                        break
                    elif interval == 3:
                        break
                    elif interval == 4:
                        break
                    elif interval ==5:
                        break
                    else:
                         raise Exception ("Please enter numbers 1-5")
                except:
                    raise Exception ("Please enter numbers 1-5")
        else:
            interval = 6

#ask for start date as dict
        currentTime = date.today()
        while(True):
            try:
                startYear = int(input("Please enter the year you would like for the data to start:\n"))
                if startYear > currentTime.year:
                    raise Exception ("Invalid year, please try again")
                    
                elif (startYear < currentTime.year - 20):
                    raise Exception ("Our records do not go back that far, please try again.")
                else:
                    break
            except:
                raise Exception ("Invalid input, try again")

        while(True):
            try:
                startMonth = int(input("Please select the Month you would like for the data to start:\n1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n7. July\n8. August\n9. September\n10. October\n11. November\n12. December\n"))
                if startMonth > 12:
                    raise Exception ("Invalid input, try again")
                elif startMonth < 1:
                    raise Exception ("Invalid input, try again")
                elif ((startYear == currentTime.year- 20) and (startMonth < currentTime.month)):
                    raise Exception ("Our records do not go back that far, please try again.")
                elif ((startYear == currentTime.year) and (startMonth > currentTime.month)):
                    raise Exception ("Invalid month, please try again")
                else:
                    break
            except:
                raise Exception ("Invalid input, try again")

        while(True):
            try:
                startDay = int(input("Please enter the day you would like for the data to start:\n"))
                if ((startMonth == 4 or 6 or 9 or 11) and (startDay > 30)):
                    raise Exception ("there are only 30 days in this month, please try again")
                elif ((startMonth == 1 or 3 or 5 or 7 or 8 or 10 or 12) and (startDay > 31)):
                    raise Exception("There are only 31 days in this month, please try again")
                    
                elif ((startYear == currentTime.year- 20) and (startMonth == currentTime.month) and (startDay < currentTime.day)):
                    raise Exception("Our records do not go back that far, please try again.")
                elif ((startYear == currentTime.year) and (startMonth == currentTime.month) and startDay > currentTime.day):
                    raise Exception("invalid day, please try again")
                elif (((startYear % 4 == 0 and startYear % 100 != 0) or (startYear % 400 == 0)) and (startMonth == 2) and (startDay > 29)):
                    raise Exception("You input a leap year, there are only 29 days in this month, please try again")
                elif (((startYear % 4 != 0) or (startYear % 100 == 0 and startYear % 400 != 0)) and (startMonth == 2) and (startDay > 28)):
                    raise Exception("There are only 28 days in this month, please try again")
                elif startDay < 1:
                    raise Exception ("Invalid date, try again")
                else:
                    break
            except:
                raise Exception("Invalid input, try again")

        startDate = {"year": startYear, "month": startMonth, "day": startDay}

#ask for end date store as dict
        while(True):
            try:
                endYear = int(input("Please enter the year you would like for the data to end:\n"))
                if endYear > currentTime.year:
                    raise Exception("Invalid year, please try again")
                elif (endYear < currentTime.year - 20):
                    raise Exception("Our records do not go back that far, please try again.")
                elif (endYear < startDate["year"]):
                    raise Exception("Your data starts after this year, please enter another")
                else:
                    break
            except:
                raise Exception("Invalid input, try again")

        while(True):
            try:
                endMonth = int(input("Please select the Month you would like for the data to end:\n1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n7. July\n8. August\n9. September\n10. October\n11. November\n12. December\n"))
                if endMonth > 12:
                    raise Exception("Invalid input try again")
                elif endMonth < 1:
                    raise Exception("Invalid input try again")
                elif ((endYear == currentTime.year- 20) and (endMonth < currentTime.month)):
                    raise Exception("Our records do not go back that far, please try again.")
                elif ((endYear == currentTime.year) and (endMonth > currentTime.month)):
                    raise Exception("Invalid month please try again")
                elif (endYear == startDate["year"] and endMonth < startDate["month"]):
                    raise Exception("Your data starts after this month, please enter another")
                else:
                    break
            except:
                raise Exception("Invalid input, try again")

        while(True):
            try:
                endDay = int(input("Please enter the day you would like for the data to end:\n"))
                if ((endMonth == 4 or 6 or 9 or 11) and (endDay > 30)):
                    raise Exception("there are only 30 days in this month, please try again")
                elif ((endMonth == 1 or 3 or 5 or 7 or 8 or 10 or 12) and (endDay > 31)):
                    raise Exception("There are only 31 days in this month, please try again")
                elif ((endYear == currentTime.year- 20) and (endMonth == currentTime.month) and (endDay < currentTime.day)):
                    raise Exception("Our records do not go back that far, please try again.")
                elif ((endYear == currentTime.year) and (endMonth == currentTime.month) and endDay > currentTime.day):
                    raise Exception("invalid day, please try again")
                elif (((endYear % 4 == 0 and endYear % 100 != 0) or (endYear % 400 == 0)) and (endMonth == 2) and (endDay > 29)):
                    raise Exception("You input a leap year, there are only 29 days in this month, please try again")
                elif (((endYear % 4 != 0) or (endYear % 100 == 0 and endYear % 400 != 0)) and (endMonth == 2) and (endDay > 28)):
                    raise Exception("There are only 28 days in this month, please try again")
                elif endDay < 1:
                    raise Exception("Invalid date, please try again")
                elif (endYear == startDate["year"] and endMonth == startDate["month"] and endDay < startDate["day"]):
                    raise Exception("Your data starts after this day, please enter another one")
                else:
                    break
            except:
                raise Exception("Invalid input, try again")
        
        endDate = {"year": endYear, "month": endMonth, "day": endDay}
        #initiate a queryinput object with chosen data
        """class queryInput:
            def __init__(self, ticker, chartType, timeSeries, startDate, endDate):
                self.ticker = ticker
                self.chartType = chartType
                self.timeSeries = timeSeries
                self.startDate = startDate
                self.endDate = endDate"""
        inputObject = queryInput(ticker, chartType, timeSeries, interval, startDate, endDate)

        #return queryInput object
        return inputObject

class TestFrontEnd(unittest.TestCase):
    def test_1(self):
        self.assertRaises(Exception, userInput)

    def test_2(self):
        self.assertRaises(Exception, userInput)

    def test_3(self):
        self.assertRaises(Exception, userInput)
    
    def test_4(self):
        self.assertRaises(Exception, userInput)
    
    def test_5(self):
        self.assertRaises(Exception, userInput)

if __name__ == '__main__':
    unittest.main()

