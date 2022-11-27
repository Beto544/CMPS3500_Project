#*****************************************************************/
# NAME: Hunberto Pascual
# ASGT: Class Project
# ORGN: CSUB - CMPS 3500
# FILE: c_project.py
# DATE: 11/08/22
#*****************************************************************/

# import the pandas library
import pandas as pd
import math
import numpy as np
import timeit

global data_file

# default file loading
data_file = pd.read_csv("Airline_data.csv")
# removes the index column
blankIndex = [''] * len(data_file)
data_file.index = blankIndex

# loads user specified file into dataframe
def  loadFile():
    global data_file
    file_name = str(input("Enter the file name to load: "))
    t_0 = timeit.default_timer()
    data_file = pd.read_csv(file_name)
    # removes the index column
    blankIndex = [''] * len(data_file)
    data_file.index = blankIndex
    t_1 = timeit.default_timer()
    print("\nFile: '%s'" % (file_name))
    print("Total Columns Read: %d" % (data_file.shape[1]))
    print("Total Rows Read: %d" % (len(data_file.index)))
    elapsed_time = (t_1 - t_0)
    print(f"File Loaded Succesfully ! Elapsed time: {elapsed_time:.04f} secs")
    
   
    
# contains part 2
class ExploreData:

    def listColumns():
# Lists all columns in the dataset
        t_0 = timeit.default_timer()
    
        try:
            print("\nThe columns are: \n")
            for col in data_file.columns:
                print(col)
            
            print("-----------------------")
            t_1 = timeit.default_timer()
            elapsed_time = (t_1 - t_0)
            print("Printing successful time to print: %.4f secs" % elapsed_time)
            
            
            col_to_drop= ""
            #Prompt user to drop columns
            while col_to_drop  != 'Q':
                    col_to_drop = input("\nEnter a Column you'd like to DROP (q to quit): ").upper()
                    t_0 = timeit.default_timer()
                    if (col_to_drop == 'Q'):
                        break
                    data_file.drop(col_to_drop, axis =1,inplace =True)
                    # print updated columns
                    print("\n Updated Columns :\n")
                    for cols in data_file.columns:
                        print(cols)
                    t_1 = timeit.default_timer()
                    elapsed_time = (t_1 - t_0)
                    print("\nDrop successful time to drop: %.4f secs" % elapsed_time)
            
            ExploreData.exploreDataMenu()
            
        except KeyError:
            print("** Column not found, try again ** ")
            ExploreData.listColumns()
            
    def countDistinctValues():
    # prompt user for column to count distint values
        print("-----------------------")
        col_to_count = ""
        while col_to_count != 'Q':
            try:
                col_to_count= input("\nFor which Column would you like to know the count of DISTINCT VALUES (q to quit): ").upper()
                t_0 = timeit.default_timer()
                if (col_to_count == 'Q'):
                    break
                distinct_val_count = len(pd.unique(data_file[col_to_count]))
                print("\nCount of unique values in %s: %d" % (col_to_count,distinct_val_count))
                
                 # measure running time
                t_1 = timeit.default_timer()
                elapsed_time = (t_1 - t_0)
                print("\nCount successful time to count: %.4f secs" % elapsed_time)
            except:
                print("Column not found, try again")
        ExploreData.exploreDataMenu()
        
    def searchColumn():
        col_to_search = ""
        isNum = "false"
        while col_to_search != 'Q':
            try:
                col_to_search = input("\nEnter the column you'd like to search inside of (q to quit): ").upper()
                if col_to_search == 'Q':
                    break
                value = str((input("Enter the value to find: "))).upper()
                t_0 = timeit.default_timer()
                values_ = data_file[col_to_search].tolist()
                index = 0
                matches = 0
                strings = []
                index_list = []
                # converts column into list of strings
                for element in values_:
                    strings.append(str(element))
               # check list for value
                for i in strings:
                    if i.upper() == value:
                        index_list.append(index)
                        matches +=1
                    index += 1
                    
                # if index_list is not empty
                if index_list:
                    print("'%s' found %d times in %s" % (value, matches, col_to_search))
                    first_six = index_list[0:6]
                    print("First six rows:", first_six)
                     # measure running time
                    t_1 = timeit.default_timer()
                    elapsed_time = (t_1 - t_0)
                    print("\nSearch successful time to search: %.4f secs" % elapsed_time)
                
                else:
                    print("Value not found")
            except:
                print("Searching error")
        ExploreData.exploreDataMenu()
        
    # prompt user for which column to sort (Ascending or descending)
    def sortColumns():
        print("-----------------------")
        col_to_sort = ""
        sorting_method = 1
    #                                      ****** SORTING MULTIPLE COLMUNS SEEMS TO RESORT PREVIOUSOLY SORTED COLUMNS ********** 
        while col_to_sort != 'Q':
            try:
                if col_to_sort == 'Q' :
                    break
                col_to_sort = input("\nEnter a column you'd like to be SORTED (q to quit): ").upper()
                if col_to_sort == 'Q':
                    break
                try:
                    sorting_method = int(input("Enter 1 for Ascending order or 2 for Descending: "))
                    t_0 = timeit.default_timer()
                    if sorting_method == 1:
                        data_file.sort_values(by = col_to_sort, inplace =True)
                        t_1 = timeit.default_timer()
                        elapsed_time = (t_1 - t_0)
                        print("\nSort successful time to sort: %.4f secs" % elapsed_time)
    
                    elif sorting_method == 2:
                        data_file.sort_values(by = col_to_sort,ascending = False, inplace = True)
                        t_1 = timeit.default_timer()
                        elapsed_time = (t_1 - t_0)
                        print("\nSort successful time to sort: %.4f secs" % elapsed_time)
                    else:
                        print("* ERROR PLEASE ENTER 1 or 2 *")
                    #continue
                # ^ SHOULD JUMP BACK TO LINE 69    
                except:
                    print("Invalid Column entered")
            except:
                print("Invalid input please try again") 
        ExploreData.exploreDataMenu()
        
    def printColmuns():
    # Prompt user for a Column to print, and the total number of rows to be printed
        print("-----------------------")
        col_to_print = ""
        num_of_rows = 0
        while col_to_print != 'Q':
            try:
                col_to_print = input("Enter a Column you'd like to be PRINTED (q to quit): ").upper()
                if col_to_print == 'Q':
                    break
                num_of_rows = int(input("                                     How many rows?: "))
                t_0 = timeit.default_timer()
                columns = data_file.columns
                col_index = columns.get_loc(col_to_print)
                print(data_file.iloc[0:num_of_rows,col_index])
                
                # measure run time
                t_1 = timeit.default_timer()
                elapsed_time = (t_1 - t_0)
                print("\nPrint successful time to print: %.4f secs" % elapsed_time)
            except:
                print("Invalid column or num rows, try again")
        ExploreData.exploreDataMenu()

    # Menu for mode 1, part 2 of the project
    def exploreDataMenu():
        print("\nExplore Data")
        print("**************")
        print(" 1. List & Drop columns \n 2. Count distinct values\n 3. Search for any value in a specified column \n 4. Sort columns \n 5. Print Coumns \n 6. Return to main menu")
        operation = str(input("\nSelect an Operation: "))
        if operation == '1':
            ExploreData.listColumns()
        elif operation == '2':
            ExploreData.countDistinctValues()
        elif operation == '3':
            ExploreData.searchColumn()
        elif operation == '4':
            ExploreData.sortColumns()
        elif operation == '5':
            ExploreData.printColmuns()
        elif operation == '6':
            mainMenu()
        else:
            print("Invalid Operation Selected")

# End of Part 2/ exploring the data       
 
class DescribeData:
    def meanColumn(col_to_mean):
        meanSum = 0
        values = data_file[col_to_mean].tolist()
        for i in values:
            meanSum += i
        print("Mean: %.3f " % (meanSum/len(data_file.axes[0])))
    def minColumn(col_to_min):
        lowest = None
        values = data_file[col_to_min].tolist()
        for i in values:
            if lowest == None:
                lowest = i
            elif lowest > i:
                lowest = i 
        print("Min: %.2f" % (lowest))
        
    def maxColumn(col_to_max):
        highest = None
        values = data_file[col_to_max].tolist()
        for i in values:
            if highest == None:
                highest = i
            elif i > highest:
                highest = i 
        print("Max: %.2f" %(highest))
    #will optimize later by removing a number from the entire list after it has been checked
    def modeColumn(col_to_mode):
        modes = []
        mode_count = 0
        values = data_file[col_to_mode].tolist()
        already_checked = []
        
        for numb in values:
            if numb not in already_checked:
                already_checked.append(numb)
                mode_temp = values.count(numb)
                if  mode_temp > mode_count:
                    mode_count = mode_temp
                    modes = [numb]
                elif mode_temp == mode_count and numb not in modes:
                    modes.append(numb)
            

        if len(modes) == 1:
            print("The mode is", str(modes)[1:-1], "and it occurs", mode_count, "time(s).")
        else:
            print("The modes are", str(modes)[1:-1], "and they occur", mode_count, "time(s).")   

    def medianColumn(col_to_median):
        values = data_file[col_to_median].tolist()
        sorted_values = sorted(values)
        median = sorted_values[int(len(sorted_values)/2)]
        median_even = sorted_values[int(len(sorted_values)/2) - 1]
        if len(values) % 2 == 0:
            print("The median is ", int((median_even + median)/2))
        else:
            print("The median is ", median)

    def uniqueColumn(col_to_unique):
        uniques = []
        unique_count = float("inf")
        values = data_file[col_to_unique].tolist()
        already_checked = []
        for numb in values:
                if numb not in already_checked:
                    already_checked.append(numb)
                    unique_temp = values.count(numb)
                    if  unique_temp < unique_count:
                        unique_count = unique_temp
                        uniques = [numb]
                    elif unique_temp == unique_count and numb not in uniques:
                        uniques.append(numb)
        if len(uniques) == 1:
            print("The unique is", str(uniques)[1:-1], "and it occurs", unique_count, "time(s).")
        else:
            print("The uniques are", str(uniques)[1:-1], "and they occur", unique_count, "time(s).")

    def countColumn(col_to_count):
        values = data_file[col_to_count].tolist()

        print("Count: ", len(values))


    def percentile(col_to_percentile):
        values = data_file[col_to_percentile].tolist()
        #Percentile needs a sorted list
        values.sort()
        
        size = len(values)
        #find the index of the value based on its percentile- size of list * percentage /100
        result20 = values[int(math.ceil((size*20) / 100)) -1]
        result40 = values[int(math.ceil((size*40) / 100)) -1]
        result60 = values[int(math.ceil((size*60) / 100)) -1]
        result80 = values[int(math.ceil((size*80) / 100)) -1]
        
        print("20 Percentile (P20): %.3f" % (result20))
        print("40 Percentile (P40): %.3f" % (result40))
        print("60 Percentile (P60): %.3f" % (result60))
        print("80 Percentile (P80): %.3f" % (result80))

    # Menu for part 3
    def describeDataMenu():
        print("\nDescribe Data")
        print("**************")
        try:
            col_to_describe = str(input("\nEnter the column to describe (q to quit): ")).upper()
            
            if (col_to_describe == 'Q'):
                mainMenu()
            # calls the countColumn function
            t_0 = timeit.default_timer()
            DescribeData.countColumn(col_to_describe)
            
             # calls the uniqueColumn function
            DescribeData.uniqueColumn(col_to_describe)
            
             # calls the meanColumn function
            DescribeData.meanColumn(col_to_describe)
            
             # calls the medianColumn function
            DescribeData.medianColumn(col_to_describe)
            
             # calls the modeColumn function
            DescribeData.modeColumn(col_to_describe)
            
             # calls the minColumn function
            DescribeData.minColumn(col_to_describe)
            
             # calls the maxColumn function
            DescribeData.maxColumn(col_to_describe)
            
             # calls the percentile function
            DescribeData.percentile(col_to_describe)
            
             # measure running time
            t_1 = timeit.default_timer()
            elapsed_time = (t_1 - t_0)
            print("\nStats printed successfully time to print: %.4f secs" % elapsed_time)
            
            # returns to main menu
            mainMenu()
        except TypeError:
            print("\n** Error - No numbers in column, could not perform all operations **")
            DescribeData.describeDataMenu()
        except KeyError:
            print("\n**Error - Column not found")
            DescribeData.describeDataMenu()
            
       
# End of Part 3

class Analysis:
    def question1():
        print("1. What was the month of the year in 2019 with most1 delays overall? And how many delays were recorded in that month?")
    
        monthDict = {
            "January ": 0,"Feburary": 0,"March": 0,"April ": 0, "May": 0,
            "June": 0,"July ": 0,"August": 0,"September": 0,"October ": 0,
            "November": 0,"December": 0,
            }

        # Stores the count of delays in each month
        delay_count = []
        
        # A Delay has occured when there is a 1 in the DEP_DEL15 Column
        # creates a new dataframe comprised of only rows with a delay for a given month
        # the number of rows of that dataframe is equal to the total delays for that month
        for i in range (1,13):
            delays_in_month = data_file[(data_file['MONTH'] == i) & (data_file['DEP_DEL15'].isin([1]))]
            delay_count.append(len(delays_in_month.index))
            
        index = 0
        # updates the dictonary with count of delays
        for key in monthDict:
            monthDict[key] = delay_count[index]
            index +=1
            
        # print answer
        month_with_max_delays = max(monthDict, key = monthDict.get)
        count_max_delays = max(monthDict.values())
        print("\n %s had the most delays in 2019 with a total count of: %d delays\n" % (month_with_max_delays,count_max_delays))
        
    def question2():
        print("2. What was the day in 2019 with most delays overall? And how many delays were recorded in that day? ")
        
        weekDict = {
            "Monday": 0,"Tuesday": 0,"Wednesday": 0,"Thursday": 0, "Friday": 0,
            "Saturday": 0,"Sunday ": 0,
            }
        delay_count = []
        
        # A Delay has occured when there is a 1 in the DEP_DEL15 Column
        # creates a new dataframe comprised of only rows with a delay for a given day
        # the number of rows of that dataframe is equal to the total delays for that day
        for i in range (1,8):
            delays_in_week = data_file[(data_file['DAY_OF_WEEK'] == i) & (data_file['DEP_DEL15'].isin([1]))]
            delay_count.append(len(delays_in_week.index))
            
        index = 0
        # updates the dictonary with count of delays
        for key in weekDict:
            weekDict[key] = delay_count[index]
            index +=1
            
        # print answer
        day_with_max_delays = max(weekDict, key = weekDict.get)
        count_max_delays = max(weekDict.values())
        print("\n %s had the most delays in 2019 with a total count of: %d delays\n" % (day_with_max_delays,count_max_delays))
        
    # not finished 
    def question3():
        print("3. What airline carrier experience the most delays in January, July and December ")
        
        # must populate airline names with code, not manually 
        airline_carrier_dict = {
            "American Airlines Inc.": [],
            "SkyWest Airlines Inc.": [],
            "American Eagle Airlines Inc.": [],
            "Southwest Airlines Co.": [], "JetBlue Airways": [],
            "United Air Lines Inc.": [],"Alaska Airlines Inc. ": [],
            "Atlantic Southeast Airlines": [],"Delta Air Lines Inc. ": [],
            "Midwest Airline, Inc. ": [],"Comair Inc. ": [],
            "Endeavor Air Inc.": [],"Frontier Airlines Inc. ": [],
            "Spirit Air Lines": [],"Mesa Airlines Inc.": [],
            "Allegiant Air": []," Hawaiian Airlines Inc.": [],
            
            }
        
        #print(airline_carrier_dict)
        delay_count = []
        months_to_check = (1,7,12)
        
        # A Delay has occured when there is a 1 in the DEP_DEL15 Column
        # creates a new dataframe comprised of only rows with a delay for a given airline
        # the number of rows of that dataframe is equal to the total delays for that day
        for i in airline_carrier_dict:
            for j in months_to_check:
                delays_in_airline = data_file[(data_file['CARRIER_NAME'] == i) & (data_file['DEP_DEL15']== 1) & (data_file['MONTH'] == j)]
                delay_count.append(len(delays_in_airline.index))
                
        index = 0
        # updates the dictonary with count of delays
        for key in airline_carrier_dict:
                airline_carrier_dict[key].append(delay_count[index])
                index +=1
                airline_carrier_dict[key].append(delay_count[index])
                index +=1
                airline_carrier_dict[key].append(delay_count[index])
                index +=1
        
        jan_max_delays = 0
        july_max_delays = 0
        dec_max_delays = 0
        
        # iterates through the number of delays in airline_carrier_dict, finds the max for each month
        for every_list in airline_carrier_dict.values():
            for each_element in every_list:
                each_element = every_list[0]
                element2 = every_list[1]
                element3 = every_list[2]
                jan_max_delays = each_element if each_element > jan_max_delays else jan_max_delays
                july_max_delays = element2 if element2> july_max_delays else july_max_delays
                dec_max_delays = element3 if element3 > dec_max_delays else dec_max_delays
                
            
        #airline_with_max_delays = max(airline_carrier_dict, key = airline_carrier_dict.get)
        count_max_delays = max(airline_carrier_dict.values())
        
        #print(delay_count)
        #print(len(delay_count))
        
        #keys = [k for k, v in airline_carrier_dict.items() if v == jan_max_delays]
        #print(keys)
        
        airline_with_max_delays = (list(airline_carrier_dict.keys())[list(airline_carrier_dict.values()).index(count_max_delays)])
        
        # print answer
        print("\n %s had the most delays in January with a total count of: %d" % (airline_with_max_delays,jan_max_delays))
        print("\n %s had the most delays in July with a total count of: %d" % (airline_with_max_delays,july_max_delays))
        print("\n %s had the most delays in December with a total count of: %d\n" % (airline_with_max_delays,dec_max_delays))

    def question4():
        print("4. What was the average plane age of all planes with delays operated by American Airlines inc.")
        
        # pulls columns with matching data and creates new dataframe with that data       
        american_airline_delays = data_file[(data_file['CARRIER_NAME'] == 'American Airlines Inc.') & (data_file['DEP_DEL15']== 1)]
        # puts plane ages into a list
        plane_ages = american_airline_delays['PLANE_AGE'].tolist()
        # gets number of planes
        total_planes = len(plane_ages)
        # adds up plane ages
        sum_age = sum(plane_ages)
        # calculate average
        average_age = sum_age/total_planes
        # print answer
        print("\nThe average plane age of all planes with delays operated American Airlines is: %.3f\n" % (average_age))
        
    def question5():
        print("5. How many planes were delayed for more than 15 minutes during days with 'heavy snow' (Days when the inches of snow on ground were 15 or more) )? ")
        
        # pulls columns with matching data and creates a new dataframe with that data  
        planes_delayed = data_file[(data_file['SNOW'] >= 15) & (data_file['DEP_DEL15']== 1)]
        
        # total count of delayed planes 
        num_of_planes = len(planes_delayed.index)
        
        # print answer
        print("\n%d planes were delayed for more than 15mins due to heavy snow\n" % (num_of_planes))
        
    def question6():
       print("6. What are the 5 Airports that had the most delays in 2019?")
       
    def question7():
        print("7. How many airlines are included in the data set? Print the first 5 in alphabetical order.")
       
    def question8():
        print("8. How many departing airports are included in the data set? Print the last 5 in alphabetical order.")
    
    def question9():
       print("9. What airline has the oldest plane?")
    
    def question10():
        print("10. What was the greatest delay ever recorded? print the airline and airpots of this event.")
            
    def question11():
       print("11. What was the smallest delay ever recorded? print the airline and airports of this event.")
       
        
    def analysisMenu():
        print("\nAnalysis")
        print("*********")
        t_0 = timeit.default_timer()
        Analysis.question1()
        
        Analysis.question2()
        
        Analysis.question3()
       
        Analysis.question4()
       
        Analysis.question5()
        
        Analysis.question6()
       
        Analysis.question7()
       
        Analysis.question8()
        
        Analysis.question9()
       
        Analysis.question10()
        
        Analysis.question11()
        
        t_1 = timeit.default_timer()
        elapsed_time = (t_1 - t_0)
        print("\nQuestions answered successfully time to answer: %.4f secs" % elapsed_time)
        mainMenu()
        
# everyone should use this Main menu method 
def mainMenu():
    while True:
       try:
           
            print("\nMain Menu")
            print("***********")
            print("1. Load Data\n2. Explore the data \n3. Describe the data")
            print("4. Analysis \n5. Quit")
            mode = str(input("\nSelect a mode: "))
        
            # Begins Part 2 - Exploring the data 
            if mode == '1':
                loadFile()
                
            elif mode == '2':
                ExploreData.exploreDataMenu()
    
            #Begins part 3 - Desribing the data
            elif mode == '3':
                DescribeData.describeDataMenu()
        
            # Begins part 4 - Analysis
            elif mode == '4':
                Analysis.analysisMenu()
            elif mode == '5':
                break
            else:
                print("** Invalid mode selected **")
            
      
       except FileNotFoundError:
           print("** File not Found try again **\n")
           loadFile()
       except NameError as ne:
           print(ne)
        
# starts the program
mainMenu()