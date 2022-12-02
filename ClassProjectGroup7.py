# *****************************************************************/
# Course: CMPS 3500
# ASGT: Class Project
# ORGN: CSUB - CMPS 3500
# FILE: ClassProjectGroup7.py
# DATE: 12/02/22
# Student 1: Hunberto Pascual
# Student 2: Kenneth Wood
# Student 3: Nathan Wardinsky
# Description: Implementation Basic Data Analysis Routines
# *****************************************************************/

# import libraries
import pandas as pd
import math
import timeit
import os

global data_file

# default file loading
data_file = pd.read_csv("Airline_data.csv")
# removes the index column
blankIndex = [''] * len(data_file)
data_file.index = blankIndex

# loads user specified file into dataframe
def  loadFile():
    
    print("-----------------------")
    global data_file
    try: 
        # get current directory and print files
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_files = os.listdir(dir_path)
        print("Files in current directory:")
        print("***************************")
        for file in dir_files:
            print(file)
        # get file name for user
        file_name = str(input("\nEnter the file name to load (q to quit): "))
        if file_name == 'q' or file_name == 'Q':
            mainMenu()
        t_0 = timeit.default_timer()
        data_file = pd.read_csv(file_name)
        # removes the index column
        blankIndex = [''] * len(data_file)
        data_file.index = blankIndex
        # remove duplicate rows
        data_file.drop_duplicates()
        t_1 = timeit.default_timer()
        print("\nFile: '%s'" % (file_name))
        print("Total Columns Read: %d" % (data_file.shape[1]))
        print("Total Rows Read: %d" % (len(data_file.index)))
        t_1 = timeit.default_timer()
        elapsed_time = (t_1 - t_0)
        print(f"File Loaded Succesfully! Elapsed time: {elapsed_time:.04f} secs")
    
    except FileNotFoundError:
        print("\n** File not found **")
        loadFile()
        
# contains part 2
class ExploreData:
    
    # Lists all columns in the dataset
    def listColumns():
        print("-----------------------")
        t_0 = timeit.default_timer()
    
        #try:
        print("\nAvailable columns:")
        print("********************")
        for col in data_file.columns:
            print(col)
        
        print("-----------------------")
        t_1 = timeit.default_timer()
        elapsed_time = (t_1 - t_0)
        print("Printing successful time to print: %.4f secs" % elapsed_time)
        
    # drop any column               
    def dropColumns():
        
        try:
            if not KeyError:
                ExploreData.listColumns()
            print("-----------------------")   
            col_to_drop= ""
            while col_to_drop  != 'Q':
                    col_to_drop = input("\nEnter a Column you'd like to DROP"+
                                        " (q to quit): ").upper()
                    t_0 = timeit.default_timer()
                    if (col_to_drop == 'Q'):
                        break
                    
                    data_file.drop(col_to_drop, axis =1,inplace =True)
                    print("\nUpdated Columns:\n")
                    for cols in data_file.columns:
                        print(cols)
                    t_1 = timeit.default_timer()
                    elapsed_time = (t_1 - t_0)
                    print("\n%s droped successfully time to drop: %.4f secs" \
                        % (col_to_drop,elapsed_time))
                    
        except KeyError:
            print("\n** Column not found ** ")
            ExploreData.dropColumns()
        except:
            print("Error occured")             
        ExploreData.exploreDataMenu()
        
    
    # counts distinct values in a given column       
    def countDistinctValues():
    
        col_to_count = ""
        while col_to_count != 'Q':
            try:
                print("-----------------------")
                print("Count distinct values")
                print("*********************")
                # prompt user for column to count distint values
                col_to_count= input("\nFor which Column would you like to know the "+
                                    "count of DISTINCT VALUES (q to quit): ").upper()
                t_0 = timeit.default_timer()
                if (col_to_count == 'Q'):
                    break
                distinct_val_count = len(pd.unique(data_file[col_to_count]))
                print("\nCount of unique values in %s: %d" % (col_to_count,\
                    distinct_val_count))
                
                 # measure running time
                t_1 = timeit.default_timer()
                elapsed_time = (t_1 - t_0)
                print("\nCount successful time to count: %.4f secs" % elapsed_time)
            except:
                print("Column not found ")
        ExploreData.exploreDataMenu()
        
    # searchs for a value in a given column    
    def searchColumn():
        
        col_to_search = ""
        while col_to_search != 'Q':
            try:
                print("-----------------------")
                print("Search Column")
                print("*************")
                col_to_search = input("\nEnter the column you'd like to search" +
                                      " inside of (q to quit): ").upper()
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
                    print("-----------------------")
                    print("'%s' found %d times in %s" % (value, matches, col_to_search))
                    first_six = index_list[0:6]
                    print("First six rows:", first_six)
                     # measure running time
                    t_1 = timeit.default_timer()
                    elapsed_time = (t_1 - t_0)
                    print("\nSearch successful time to search: %.4f secs" %\
                        elapsed_time)
                
                else:
                    print(" %s not found in %s" % (value,col_to_search))
            except:
                print("Searching error - Column and/or Value not found")
        ExploreData.exploreDataMenu()
        
    # sorts specified column   
    def sortColumns():
        
        col_to_sort = ""
        sorting_method = 1
                                      
        while col_to_sort != 'Q':
            try:
                print("-----------------------")
                print("Sort columns")
                print("*************")
                # prompt user for which column to sort (Ascending or descending)
                col_to_sort = input("\nEnter a column you'd like to be SORTED "+
                                    "(q to quit): ").upper()
                if col_to_sort == 'Q':
                    break
                
                sorting_method = str(input("Enter 1 for Ascending order or 2 for" +
                                           " Descending: "))
                t_0 = timeit.default_timer()
                              
                # ascending sort
                if sorting_method == '1':
                    data_file.sort_values(by = col_to_sort, inplace =True)
    
                # decending sort
                elif sorting_method == '2':
                    data_file.sort_values\
                        (by = col_to_sort,ascending = False, inplace = True)
                    
                # start again  
                else:
                    print("* Error enter 1 or 2 *")
                    ExploreData.sortColumns()
                    
                # column indexes to print preview        
                rows = data_file[col_to_sort].tolist()
                num_of_rows= len(rows)
                middle_row = int(num_of_rows/2)    
                print("-----------------------")        
                # prints the first 5, middle 5, and last 5 rows 
                for i in rows[:5]:
                    print(i)
                print("**")
                for k in rows[middle_row:middle_row+5]:
                    print(k)
                print("**")    
                for k in rows[num_of_rows-6:num_of_rows-1]:
                    print(k)
                    
                # calculate run time   
                t_1 = timeit.default_timer()
                elapsed_time = (t_1 - t_0)
                print("\n%s Sorted successfully, time to sort: %.4f secs" % \
                    (col_to_sort,elapsed_time))
               
                   
            except KeyError:
                print("** Column not found **") 
        ExploreData.exploreDataMenu()
        
    # prints specified column   
    def printColumns():
    
        col_to_print = ""
        num_of_rows = 0
        while col_to_print != 'Q':
            try:
                print("-----------------------\n")
                print("Print columns")
                print("*************")
                col_to_print = input("Enter a Column you'd like to be PRINTED "+
                                     "(q to quit): ").upper()
                if col_to_print == 'Q':
                    break
                num_of_rows = int(input("                          "+
                                        "How many rows 100,500, or 5000?: "))
                # start timer
                t_0 = timeit.default_timer()
                # store column in list
                rows = data_file[col_to_print].tolist()
                # ensuring good data
                if num_of_rows <= len(rows):
                    if num_of_rows == 100:
                        rows_2 = rows[:num_of_rows]
                    elif num_of_rows == 500:
                        rows_2 = rows[:num_of_rows]
                    elif num_of_rows == 5000:
                        rows_2 = rows[:num_of_rows]
                    else:
                        print("** Error - enter 100, 500, or 5000")
                        ExploreData.printColumns()
                else:
                    print("Not enough rows in Column")
                    ExploreData.printColumns()
                # header
                print(col_to_print)
                print("***************")
                
                # print rows
                for i in rows[:num_of_rows]:
                    print(i)
                
                # measure run time
                t_1 = timeit.default_timer()
                elapsed_time = (t_1 - t_0)
                print("\n%s printed successfully, time to print: %.4f secs" %\
                    (col_to_print,elapsed_time))
                
                ExploreData.listColumns()
                
            except KeyError:
                print("** Column not found **")
                ExploreData.printColumns()
            except ValueError:
                print("Error - number of rows must be digits")  
        ExploreData.exploreDataMenu()

    # Menu for ExporeData Class
    def exploreDataMenu():
        print("\nExplore Data")
        print("**************")
        print(" 1. List & Drop columns \n 2. Count distinct values\n 3. Search for"+
              " any value in a specified column \n 4. Sort columns \n 5. Print "+
              "Columns \n 6. Return to main menu")
        operation = str(input("\nSelect an Operation: "))
        
        if operation == '1':
            ExploreData.listColumns()
            ExploreData.dropColumns()
        elif operation == '2':
            ExploreData.listColumns()
            ExploreData.countDistinctValues()
        elif operation == '3':
            ExploreData.listColumns()
            ExploreData.searchColumn()
        elif operation == '4':
            ExploreData.listColumns()
            ExploreData.sortColumns()
        elif operation == '5':
            ExploreData.listColumns()
            ExploreData.printColumns()
        elif operation == '6':
            mainMenu()
        else:
            print("Invalid Operation Selected")    
 
class DescribeData:
    
    # calculates the mean of a given column
    def meanColumn(col_to_mean):
        meanSum = 0
        values = data_file[col_to_mean].tolist()
        for i in values:
            meanSum += i
        print("Mean: %.6f " % (meanSum/len(data_file.axes[0])))
        
    # Finds the mininum in a given column
    def minColumn(col_to_min):
        lowest = None
        values = data_file[col_to_min].tolist()
        for i in values:
            if lowest == None:
                lowest = i
            elif lowest > i:
                lowest = i 
        print("Mininum: %.10f" % (lowest))
        
    # Finds the maximum in a given column   
    def maxColumn(col_to_max):
        highest = None
        values = data_file[col_to_max].tolist()
        for i in values:
            if highest == None:
                highest = i
            elif i > highest:
                highest = i 
        print("Maximum: %.10f" %(highest))
        
    # Finds the mode of a given column
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
            print("Mode: ", str(modes)[1:-1], "and it occurs", mode_count, "time(s).")
        else:
            print("Modes:", str(modes)[1:-1], "and they occur", mode_count, "time(s).")   
            
    # Finds the median of a given column
    def medianColumn(col_to_median):
        values = data_file[col_to_median].tolist()
        sorted_values = sorted(values)
        median = sorted_values[int(len(sorted_values)/2)]
        median_even = sorted_values[int(len(sorted_values)/2) - 1]
        if len(values) % 2 == 0:
            print("Median:", float((median_even + median)/2))
        else:
            print("Median: ", median)
            
    # Counts unique values in a given column
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
            print("Unique:", str(uniques)[1:-1], "and it occurs", unique_count, "time(s).")
        else:
            print("Uniques: ", str(uniques)[1:-1], "and they occur", unique_count, "time(s).")

    # Counts number of rows in a given column
    def countColumn(col_to_count):
        values = data_file[col_to_count].tolist()

        print("Count:", len(values))

    # calculates the standard deviation in given column
    def standardDeviation(col_to_deviation):
        meanSum = 0
        values = data_file[col_to_deviation].tolist()
        temp_numb = 0

        for i in values:
            meanSum += i

        mean = meanSum/len(data_file.axes[0])

        for numb in values:
            temp_numb += (numb - mean)**2
        temp_numb_two = (temp_numb / (len(values) - 1))

        final_numb = math.sqrt(temp_numb_two)

        print("Standard Deviation:", final_numb)
        
    # calculates the variance in given column
    def variance(col_to_variance):
        values = data_file[col_to_variance].tolist()
        meanSum = 0
        temp_numb = 0

        for i in values:
            meanSum += i
        
        mean = meanSum/len(data_file.axes[0])

        for numb in values:
            temp_numb += (numb - mean)**2
            final_numb = (temp_numb / (len(values) - 1))

        print("Variance:", final_numb)

    # calculates the percentile(s) of given column
    def percentile(col_to_percentile):
        values = data_file[col_to_percentile].tolist()
        #Percentile needs a sorted list
        values.sort()
        
        size = len(values)
        #find the index of the value based on its percentile
        # size of list * percentage /100
        result20 = values[int(math.ceil((size*20) / 100)) -1]
        result40 = values[int(math.ceil((size*40) / 100)) -1]
        result60 = values[int(math.ceil((size*60) / 100)) -1]
        result80 = values[int(math.ceil((size*80) / 100)) -1]
        
        print("20 Percentile (P20): %.6f" % (result20))
        print("40 Percentile (P40): %.6f" % (result40))
        print("60 Percentile (P60): %.6f" % (result60))
        print("80 Percentile (P80): %.6f" % (result80))

    # Menu for DescibeData Class
    def describeDataMenu():
        
        try:
            ExploreData.listColumns()
            print("-----------------------")
            print("\nDescribe Data")
            print("**************")
            col_to_describe = str(input("\nEnter the column to describe "+
                                        "(q to quit): ")).upper()
            
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

            DescribeData.standardDeviation(col_to_describe)

            DescribeData.variance(col_to_describe)
            
             # calls the percentile function
            DescribeData.percentile(col_to_describe)

            
             # measure running time
            t_1 = timeit.default_timer()
            elapsed_time = (t_1 - t_0)
            print("\nStats printed successfully time to print: %.4f secs" % \
                elapsed_time)
            
            # returns to main menu
            mainMenu()
        except TypeError:
            print("\n** Error - No numbers in column, could not perform all"+
                  " operations **")
        
        except KeyError:
            print("\n** Column not found **")
    
            
class Analysis:
    
     # Solves question 1
    def question1():
        
        print("1. How many airlines are included in the data set? Print the first"+
              " 5 in alphabetical order.")
        print("-----------------------")
        # find unique airlines
        unique_airlines = []
        airlines = data_file['CARRIER_NAME'].tolist()
        for airline in airlines:
           if airline not in unique_airlines:
               unique_airlines.append(airline)

        #sort the list alphabetically
        sorted_list = sorted(unique_airlines)
        amount = len(sorted_list)
        first_five = sorted_list[0:5]
        print("%s Arlines in the data set." % (amount))
        print("\nFive first airlines in alphabetical order:")
        print("***************************************")
        for airline in first_five:
            print(airline)
        print('\n')  
        
    # Solves question 2
    def question2():
        
        print("2. How many departing airports are included in the data set? Print"+
              "the last 5 in alphabetical order.")
        print("-----------------------")
        # find unique airlines
        unique_dep_airports = []
        dep_airports = data_file['DEPARTING_AIRPORT'].tolist()
        for dep_airport in dep_airports:
           if dep_airport not in unique_dep_airports:
               unique_dep_airports.append(dep_airport)

        #sort the list alphabetically
        sorted_list = sorted(unique_dep_airports)
        amount = len(sorted_list)
        last_five = sorted_list[(len(sorted_list)-5):len(sorted_list)]
        print("%d departing airports in the data set." %(amount))
        print("\nLast five departing airports in alphabetical order:")
        print("***************************************************")
        for airline in last_five:
            print(airline)
        print('\n')
        
    # Solves question 3
    def question3():
        
        print("3. What airline has the oldest plane? Print the five airlines with "+
              "the oldest planes recorded")
        print("-----------------------")
        plane_ages = data_file['PLANE_AGE'].tolist()
        unique_planes = []
        
        for plane in plane_ages:
           if plane not in unique_planes:
               unique_planes.append(plane)
        sorted_list = sorted(unique_planes, reverse=True)

        airlines_with_old_planes = []
        for i in sorted_list:
            if data_file.loc[data_file['PLANE_AGE'] == i]['CARRIER_NAME'].values[0]\
                not in airlines_with_old_planes:
                airlines_with_old_planes.append(data_file.loc[data_file\
                    ['PLANE_AGE']== i]['CARRIER_NAME'].values[0])
                if len(airlines_with_old_planes) == 5:
                    break
        print("%s was the airline with oldest plane at: %d years" \
            %(airlines_with_old_planes[0],sorted_list[0]))
        print("\nTop five airlines with oldest planes:")
        print("***************************************")
        for i in airlines_with_old_planes:
            print(i)
        print('\n')
        
    # Solves question 4
    def question4():
        
        print("\n4. What is the airport that averaged the greatest number of "+
              "passengers recorded in 2019? Print the 5 airport that averaged "+
              "the greatest number of passengers in 2019.")
        print("-----------------------")
        passengers = data_file['AVG_MONTHLY_PASS_AIRPORT'].tolist()
        unique_pass = []
        
        for i in passengers:
           if i not in unique_pass:
               unique_pass.append(i)
        sorted_list = sorted(unique_pass, reverse=True)
            
        airport_amounts = []
        for i in sorted_list:
            if data_file.loc[data_file['AVG_MONTHLY_PASS_AIRPORT'] == i]\
                ['DEPARTING_AIRPORT'].values[0] not in airport_amounts:
                airport_amounts.append(data_file.loc[data_file\
                    ['AVG_MONTHLY_PASS_AIRPORT'] == i]['DEPARTING_AIRPORT'].values[0])
                if len(airport_amounts) == 5:
                    break
        print("%s airport had the hihgest average passengers at  %d passengers"\
            %(airport_amounts[0],sorted_list[0]))
        print("\nTop five airports with highest averaged passengers:")
        print("***************************************")
        for i in airport_amounts:
            print(i)
        print('\n')
        
    # Solves question 5
    def question5():
        print("\n5. What is the airline that averaged the greatest number of "+
              "employees (Flight attendants and ground service) in 2019? Print"+
              "the 5 airlines that averaged the greatest number of employees in"+
              " 2019.")
        print("-----------------------")
        employees = data_file['FLT_ATTENDANTS_PER_PASS'].tolist()
        unique_employees = []

        for i in employees:
            if i not in unique_employees:
                unique_employees.append(i)
        
        sorted_list = sorted(unique_employees, reverse = True)

        employee_amounts = []
        for i in sorted_list:
            if data_file.loc[data_file['FLT_ATTENDANTS_PER_PASS'] == i]\
                ['CARRIER_NAME'].values[0] not in employee_amounts:
                employee_amounts.append(data_file.loc[data_file\
                    ['FLT_ATTENDANTS_PER_PASS'] == i]['CARRIER_NAME'].values[0])
                if len(employee_amounts) == 5:
                    break
        print("%s was the airline with the most average employees at %.7f" % \
            (employee_amounts[0], sorted_list[0]))
        print("\nTop five airlines with highest averaged employees:")
        print("**************************************************")
        for i in employee_amounts:
            print(i)
        print('\n')
        
        # Solves questions 6 & 7
    def question6():
        
        print("6. What was the month of the year in 2019 with most delays overall?"+
              " And how many delays were recorded in that month?")
        print("-----------------------")
        month_dict = {
            "January ": 0,"February": 0,"March": 0,"April ": 0, "May": 0,
            "June": 0,"July ": 0,"August": 0,"September": 0,"October ": 0,
            "November": 0,"December": 0,
            }

        # Stores the count of delays in each month
        monthly_delay_count = []
        
        # A Delay has occured when there is a 1 in the DEP_DEL15 Column
        # creates new dataframe of only rows with a delay for a given month
        # number of rows of dataframe = total delays for that month
        for i in range (1,13):
            delays_in_month = data_file[(data_file['MONTH'] == i) & (data_file\
                ['DEP_DEL15'].isin([1]))]
            monthly_delay_count.append(len(delays_in_month.index))
            
        month_index = 0
        # updates the dictonary with count of delays
        for key in month_dict:
            month_dict[key] = monthly_delay_count[month_index]
            month_index +=1
            
        # print answer
        month_with_max_delays = max(month_dict, key = month_dict.get)
        max_count_monthly_delays = max(month_dict.values())
        print("%s had the most delays in 2019 with a total count of: %d delays\n" \
            % (month_with_max_delays,max_count_monthly_delays))
        
        # question 7
        print("7.What was the month of the year in 2019 with most delays overall? "+
              "And how many delays were recorded in that day?")
        print("-----------------------")
        week_dict = {
            "Monday": 0,"Tuesday": 0,"Wednesday": 0,"Thursday": 0, "Friday": 0,
            "Saturday": 0,"Sunday ": 0,
            }
        daily_delay_count = []
        for i in range (1,8):
            delays_in_week = data_file[(data_file['DAY_OF_WEEK'] == i) & (data_file['DEP_DEL15'].isin([1]) & (data_file['MONTH'] == 6))]
            daily_delay_count.append(len(delays_in_week.index))
            
        week_index = 0
        # updates the dictonary with count of delays
        for key in week_dict:
            week_dict[key] = daily_delay_count[week_index]
            week_index +=1
            
        # print answer
        day_with_max_delays = max(week_dict, key = week_dict.get)
        max_count_daily_delays = max(week_dict.values())
        print("from % s , %s had the most delays in 2019 with a total count of: %d delays\n" % \
            (month_with_max_delays,day_with_max_delays,max_count_daily_delays))
        
     
    # Solves question 8
    def question8():
        
        print("8. What airline carrier experience the most delays in January, July"+
              " and December ")
        print("-----------------------")
        unique_airlines = []
        air_lines = data_file['CARRIER_NAME'].tolist()
        
        #creats a list of all airlines
        for airline in air_lines:
           if airline not in unique_airlines:
               unique_airlines.append(airline)
               
       # creates a airline carrier dictionary      
        airline_carrier_dict = {i:[] for i in unique_airlines}
    
        delay_count = []
        months_to_check = (1,7,12)
        
        # A Delay has occured when there is a 1 in the DEP_DEL15 Column
        # creates new dataframe of only rows with a delay for a given airline
        # the number of rows of = total delays for that day
        for i in airline_carrier_dict:
            for j in months_to_check:
                delays_in_airline = data_file[(data_file['CARRIER_NAME'] == i) & \
                    (data_file['DEP_DEL15']== 1) & (data_file['MONTH'] == j)]
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
                
        # stores delays for each month
        jan_max_delays = 0
        july_max_delays = 0
        dec_max_delays = 0
        
        # iterates through the number of delays in airline_carrier_dict
        # finds the max for each month
        for every_list in airline_carrier_dict.values():
            for each_element in every_list:
                each_element = every_list[0]
                element2 = every_list[1]
                element3 = every_list[2]
                jan_max_delays = each_element if each_element > jan_max_delays \
                    else jan_max_delays
                july_max_delays = element2 if element2> july_max_delays \
                    else july_max_delays
                dec_max_delays = element3 if element3 > dec_max_delays \
                    else dec_max_delays
                
        
        airline_with_max_delays = max(airline_carrier_dict, key = \
            airline_carrier_dict.get)
        count_max_delays = max(airline_carrier_dict.values())
        airline_with_max_delays = (list(airline_carrier_dict.keys())\
            [list(airline_carrier_dict.values()).index(count_max_delays)])
        
        # print answer
        print("%s had the most delays in January with a total count of: %d" % \
            (airline_with_max_delays,jan_max_delays))
        print("%s had the most delays in July with a total count of: %d" % \
            (airline_with_max_delays,july_max_delays))
        print("%s had the most delays in December with a total count of: %d\n" % 
              (airline_with_max_delays,dec_max_delays))

    # Solves question 9
    def question9():
        
        print("9. What was the average plane age of all planes with delays operated"+
              " by American Airlines inc.")
        print("-----------------------")
        # pulls columns with matching data and creates new dataframe with that data       
        american_airline_delays = data_file[(data_file['CARRIER_NAME'] ==\
            'American Airlines Inc.') & (data_file['DEP_DEL15']== 1)]
        # puts plane ages into a list
        plane_ages = american_airline_delays['PLANE_AGE'].tolist()
        # gets number of planes
        total_planes = len(plane_ages)
        # adds up plane ages
        sum_age = sum(plane_ages)
        # calculate average
        average_age = sum_age/total_planes
        # print answer
        print("The average plane age of all planes with delays operated American"+
              " Airlines is: %.3f\n" % (average_age))
        
    # Solves question 10
    def question10():
        
        print("10. How many planes were delayed for more than 15 minutes during "+
              "days with 'heavy snow' (Days when the inches of snow on ground"+
              " were 15in or more) )? ")
        print("-----------------------")
        # pulls columns with matching data and creates a new dataframe   
        planes_delayed = data_file[(data_file['SNOW'] >= 15) & (data_file\
            ['DEP_DEL15']== 1)]
        
        
        # total count of delayed planes 
        num_of_planes = len(planes_delayed.index)
        
        # print answer
        print("%d planes were delayed for more than 15mins due to heavy snow\n" % \
            (num_of_planes))
        
    # Solves question 11
    def question11():
        
       print("11. What are the 5 Departing Airports that had the most delays in 2019?")
       print("-----------------------")
       unique_airports = []
       delay_count = []
       air_ports = data_file['DEPARTING_AIRPORT'].tolist()
       
       # creats a list of all the airports
       for airport in air_ports:
           if airport not in unique_airports:
               unique_airports.append(airport)
               
       # creates a airport dictionary      
       airport_dct = dict(zip(unique_airports, [None]*len(unique_airports)))
      
       # counts delays for every airport
       for every in unique_airports:
           delays = data_file[(data_file['DEP_DEL15']== 1) & (data_file\
               ['DEPARTING_AIRPORT'] == every)]
           delay_count.append(len(delays.index))
        
       index = 0
       
      # updates dictioary with delays
       for key in airport_dct:
                airport_dct[key] = delay_count[index]
                index +=1
        
       # gets the top 5 airports with the most delays
       # only accounts for departing airports, not previous airports
       top_five_airports = sorted(airport_dct, key=airport_dct.get, reverse=True)[:5]
       
       print("Top 5 airports with the most delays in 2019:")
       print("***************************************************")
       for every_port in top_five_airports:
           print("%s with %d delays " % (every_port,airport_dct.get(every_port)))
       
       print('\n')
                
    # menu for Analysis Class   
    def analysisMenu():
        
        try:
            print("\nAnalysis")
            print("*********\n")
            t_begin = timeit.default_timer()
            
            # calls all the question functions
            question_order = (1,2,3,4,5,6,8,9,10,11)
            for i in question_order:
                t_1 = timeit.default_timer()
                func_name = "question"+str(i)
                func_to_call = getattr(Analysis,func_name)
                func_to_call()
                t_2 = timeit.default_timer()
                elapsed_time = (t_2 - t_1)
                if i == 6:
                    print("- Questions %d & 7, time to answer: %.6f secs\n\n" % (i,elapsed_time))
                else:
                    print("- Question%d, time to answer: %.6f secs\n\n" % (i,elapsed_time))
                
            # total time taken    
            t_final = timeit.default_timer()
            total_time = (t_final - t_begin)
            print("Total time to answer: %.6f secs" % \
                total_time)
            
            mainMenu()
            
        except KeyError:
           print("** Error - Required Column(s) Missing **")
         
def mainMenu():
    while True:
       try:
            print("\nMain Menu")
            print("***********")
            print("1. Load Data\n2. Explore the data \n3. Describe the data")
            print("4. Analysis \n5. Quit")
            mode = str(input("\nSelect a mode: "))
        
            # Begins - data loading 
            if mode == '1':
                loadFile()
            # Begins Part 2 - Exploring the data 
            elif mode == '2':
                ExploreData.exploreDataMenu()
    
            #Begins part 3 - Desribing the data
            elif mode == '3':
                DescribeData.describeDataMenu()
        
            # Begins part 4 - Analysis
            elif mode == '4':
                Analysis.analysisMenu()
                
            # Ends program
            elif mode == '5':
                raise SystemExit
            
            else:
                print("** Invalid mode selected **")
            
       except FileNotFoundError:
           print("** File not Found **\n")
           loadFile()
       except NameError as ne:
           print(ne)
       
# starts the program
mainMenu()