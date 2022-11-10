#*****************************************************************/
# NAME: Hunberto Pascual
# ASGT: Class Project
# ORGN: CSUB - CMPS 3500
# FILE: c_project.py
# DATE: 11/08/22
#*****************************************************************/

# import the pandas library
import pandas as pd

# load the csv file into a data frame
airline_data = pd.read_csv('Airline_data.csv')

# removes the index column
blankIndex = [''] * len(airline_data)
airline_data.index = blankIndex

# contains part 2
class ExploreData:

    def listColumns():
# Lists all columns in the dataset
        print("\nThe columns are: \n")
        for col in airline_data.columns:
            print(col)
            
        print("-----------------------")
        col_to_drop= ""
        
     #Prompt user to drop columns
        while col_to_drop  != 'Q':
                col_to_drop = input("\nEnter a Column you'd like to DROP (q to quit): ").upper()
                if (col_to_drop == 'Q'):
                    break
                airline_data.drop(col_to_drop, axis =1,inplace =True)
                # print updated columns
                print("\n Updated Columns :\n")
                for cols in airline_data.columns:
                    print(cols)
                    
        ExploreData.exploreDataMenu()
    
    def countDistinctValues():
    # prompt user for column to count distint values
        print("-----------------------")
        col_to_count = ""
        while col_to_count != 'Q':
            try:
                col_to_count= input("\nFor which Column would you like to know the count of DISTINCT VALUES (q to quit): ").upper()
                if (col_to_count == 'Q'):
                    break
                distinct_val_count = len(pd.unique(airline_data[col_to_count]))
                print("\nCount of unique values in %s: %d" % (col_to_count,distinct_val_count))
            except:
                print("Invalid column please try again")
        ExploreData.exploreDataMenu()
        
    # not finished 
    def searchColumn():
        col_to_search = ""
        while col_to_search != 'Q':
            try:
                col_to_search = input("Enter the column you'd like to search inside of (q to quit): ").upper()
                if col_to_search == 'Q':
                    break
                value = input("Enter the value to find: ")
                #print(airline_data[col_to_search].where(airline_data==[value]))
                #print(airline_data.where(airline_data.col_to_search == airline_data))
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
                    if sorting_method == 1:
                        airline_data.sort_values(by = col_to_sort, inplace =True)
    
                    elif sorting_method == 2:
                        airline_data.sort_values(by = col_to_sort,ascending = False, inplace = True)
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
                columns = airline_data.columns
                col_index = columns.get_loc(col_to_print)
                print(airline_data.iloc[0:num_of_rows,col_index])
            except:
                print("Invalid column or num rows, try again")
        ExploreData.exploreDataMenu()

    # Menu for mode 1, part 2 of the project
    def exploreDataMenu():
        print("\n* Exploring the data *\n")
        print(" 1. List & Drop columns \n 2. Count distinct values\n 3. Search for any value in a specified column \n 4. Sort columns \n 5. Print Coumns \n 6. Return to main menu")
        operation = int(input("\nSelect an Operation: "))
        if operation == 1:
            ExploreData.listColumns()
        elif operation == 2:
            ExploreData.countDistinctValues()
        elif operation == 3:
            ExploreData.searchColumn()
        elif operation == 4:
            ExploreData.sortColumns()
        elif operation == 5:
            ExploreData.printColmuns()
        elif operation == 6:
            mainMenu()
        else:
            print("Invalid Operation Selected")

# End of Part 2/ exploring the data       
 
class DescribeData:
    def meanColumn():
        col_to_mean = input("\nEnter the column you'd like to be be averaged: ").upper()
        meanSum = 0
        values = airline_data[col_to_mean].tolist()
        for i in values:
            meanSum += i

        print(meanSum/len(airline_data.axes[0]))
    def minColumn():
        col_to_min =  input("\nEnter the column you'd like to find the minimum of ").upper()
        lowest = None
        values = airline_data[col_to_min].tolist()
        for i in values:
            if lowest == None:
                lowest = i
            elif lowest > i:
                lowest = i 
        print(lowest)
        
    def maxColumn():
        col_to_max =  input("\nEnter the column you'd like to find the maximum of ").upper()
        highest = None
        values = airline_data[col_to_max].tolist()
        for i in values:
            if highest == None:
                highest = i
            elif i > highest:
                highest = i 
        print(highest)
    #will optimize later by removing a number from the entire list after it has been checked
    def modeColumn():
        col_to_mode = input("\nEnter the column you'd like to find the mode(s) of ").upper()
        modes = []
        mode_count = 0
        values = airline_data[col_to_mode].tolist()
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

    def medianColumn():
        col_to_median = input("\nEnter the column you'd like to find the median of ").upper()
        values = airline_data[col_to_median].tolist()
        sorted_values = sorted(values)
        median = sorted_values[int(len(sorted_values)/2)]
        median_even = sorted_values[int(len(sorted_values)/2) - 1]
        if len(values) % 2 == 0:
            print("The median is ", int((median_even + median)/2))
        else:
            print("The median is ", median)

    def uniqueColumn():
        col_to_unique = input("\nEnter the column you'd like to find the unique(s) of ").upper()
        uniques = []
        unique_count = float("inf")
        values = airline_data[col_to_unique].tolist()
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
        
    # Menu for part 3
    def describeDataMenu():
        print("\n* Describing the data *\n")
        print(" 1. Mean \n 2. Min \n 3. Max \n 4. Mode \n 5. Median \n 6. Unique\n 7. Return to main menu")
        operation = int(input("\nSelect an Operation: "))
        if operation == 1:
            DescribeData.meanColumn()
        elif operation == 2:
            DescribeData.minColumn()
        elif operation == 3:
            DescribeData.maxColumn()
        elif operation == 4:
            DescribeData.modeColumn()
        elif operation == 5:
            DescribeData.medianColumn()
        elif operation == 6:
            DescribeData.uniqueColumn()
        elif operation == 7:
            mainMenu()
        else:
            print("Invalid Operation Selected")

# End of Part 3

# everyone should use this Main menu method 
def mainMenu():
    try:
        print("Main Menu\n")
        print("1. Explore the data \n2. Describe the data \n3. Analysis")
        mode = int(input("\nSelect a mode: "))
        
        # Begins Part 2 - Exploring the data 
        if mode == 1:
            ExploreData.exploreDataMenu()
        
        # Begins part 3 - Desribing the data
        elif mode == 2:
            junk = 0    # <= useless code 
            # example 
            DescribeData.describeDataMenu()
        
        # Begins part 4 - Analysis
        elif mode == 3:
            junk = 1   # <= useless code
            # example
            # Analysis.analysisMenu()
        else:
            print("Invalid mode selected")
      
    except:
        print("Invalid input entered")
        
# starts the program
mainMenu()