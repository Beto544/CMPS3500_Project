#*****************************************************************/
# NAME: Hunberto Pascual
# ASGT: Class Project
# ORGN: CSUB - CMPS 3500
# FILE: c_project.py
# DATE:10/29/22
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
        while col_to_drop  != 'q':
                col_to_drop = input("\nEnter a Column you'd like to DROP (q to quit): ").upper()
                if (col_to_drop == 'Q') or (col_to_drop == 'q'):
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
        while col_to_count != 'q':
            try:
                col_to_count= input("\nFor which Column would you like to know the count of DISTINCT VALUES (q to quit): ").upper()
                if (col_to_count == 'q') or (col_to_count == 'Q'):
                    break
                distinct_val_count = len(pd.unique(airline_data[col_to_count]))
                print("\nCount of unique values in %s: %d" % (col_to_count,distinct_val_count))
            except:
                print("Invalid column please try again")
        ExploreData.exploreDataMenu()

    # prompt user for which column to sort (Ascending or descending)
    def sortColumns():
        print("-----------------------")
        col_to_sort = ""
        sorting_method = 1
    #                                      ****** SORTING MULTIPLE COLMUNS SEEMS TO RESORT PREVIOUSOLY SORTED COLUMNS ********** 
        while col_to_sort != 'q':
            try:
                if col_to_sort == 'q' or col_to_sort == 'Q':
                    break
                col_to_sort = input("\nEnter a column you'd like to be SORTED (q to quit): ").upper()
                if col_to_sort == 'q' or col_to_sort == 'Q':
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
                    print("Invalid input")
            except:
                print("Invalid input please try again") 
        ExploreData.exploreDataMenu()
        
    def printColmuns():
    # Prompt user for a Column to print, and the total number of rows to be printed
        print("-----------------------")
        col_to_print = ""
        num_of_rows = 0
        while col_to_print != 'q':
            try:
                col_to_print = input("Enter a Column You'd like to be PRINTED (q to quit): ").upper()
                if col_to_print == 'q' or col_to_print == 'Q':
                    #print("Q entered")
                    break
                num_of_rows = int(input("                                     How many rows?: "))
                #or num_of_rows == 'q' or num_of_rows == 'Q'
            except:
                print("Invalid input please try again")

    # prints the selected number of rows from the selected column
    #                      [start_row:end_row,column_Index]
        print(airline_data.iloc[0:num_of_rows,0])
        #print(airline_data.columns.get_loc(col_to_print))#
        ExploreData.exploreDataMenu()

    # Menu for mode 1, part 2 of the project
    def exploreDataMenu():
        print("\n* Exploring the data *\n")
        print(" 1. List & Drop columns \n 2. Count distinct values \n 3. Sort columns \n 4. Print Coumns \n 5. Return to main menu")
        operation = int(input("\nSelect an Operation: "))
        if operation == 1:
            ExploreData.listColumns()
        elif operation == 2:
            ExploreData.countDistinctValues()
        elif operation == 3:
            ExploreData.sortColumns()
        elif operation == 4:
            ExploreData.printColmuns()
        elif operation == 5:
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
        col_to_min =  input("\nEnter the column you'd like to find the minimum of").upper()
        lowest = None
        values = airline_data[col_to_min].tolist()
        for i in values:
            if lowest == None:
                lowest = i
            elif lowest > i:
                lowest = i 
        #print(lowest)4
        
    def maxColumn():
        col_to_max =  input("\nEnter the column you'd like to find the maximum of").upper()
        highest = None
        values = airline_data[col_to_max].tolist()
        for i in values:
            if highest == None:
                highest = i
            elif i > highest:
                highest = i 
        print(highest)
        
    # Menu for part 3
    def describeDataMenu():
        print("\n* Describing the data *\n")
        print(" 1. Mean \n 2. Min \n 3. Max \n 4. Return to main menu")
        operation = int(input("\nSelect an Operation: "))
        if operation == 1:
            DescribeData.meanColumn()
        elif operation == 2:
            DescribeData.minColumn()
        elif operation == 3:
            DescribeData.maxColumn()
        elif operation == 4:
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