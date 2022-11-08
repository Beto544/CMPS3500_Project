Group 7: 


Kenneth Wood
Hunberto Pascual
Nathan Wardinsky    

This is our data processing final project for Programming Languages. By the end of the project it will be able to: 

Data Loading: Your program should read data from csv files, Note that the input list will have up to 30 columns and ~4.5 million rows and could be unordered and contain repeated, missing, incorrect and or misleading values. Test your loading function with the following data sets:
InputDataSample.csv
Boston_Lyft_Uber_Data.csv

Exploring the Data: Your program should be able to perform the following asks:
Load the csv file and stored into an array or data frame
list all columns in the dataset and offer the user the possibility of drop any of them
Count distinct values of any column selected by the user
Search any value in any column as input by the user
Sort any columns (Ascending or descending) as selected by the user
Print the first 100, 1000 or 5000 rows of the dataset as selected by the user

Describing the data: Your program should have the ability of performing statistical analysis per column functions (Mean, Max, minimum, Standard Deviation, and Count) must be implemented by the team, pre-designed libraries like the ones included in pandas and numpy (Python) are not allowed. The following statistical functions are required:
 Count
 Unique
 Mean
 Median
 Mode
 Standard Deviation (SD)
 Variance
 Minimum
 Maximum
 20 Percentile (P20)
 40 Percentile (P40)
 50 Percentile (P50)
 60 Percentile (P60)
 80 Percentile (P80)

Analysis: Your job is to implement the necessary functions and methods to answer questions like the questions listed below.
What was the month of the year in 2019 with most delays overall? And how many delays were recorded in that month?
What was the month of the year in 2019 with most delays overall? And how many delays were recorded in that day?
What airline carrier experience the most delays in January, July and December
What was the average plane age of all planes with delays operated by American Airlines inc.
How many planes were delayed for more than 15 minutes during days with "heavy snow" (Days when the inches of snow on ground were 15 or more) )?
What are the 5 Airports that had the most delays in 2019?

Measuring running Times: Please implement all necessary functions or methods to measure running times as your script runs to allow the user to see the effectiveness of your code. Your scripts will be run and measured in Odin.

Interface: A textual menu should be implemented in a way that the user could load , explore and analyze this dataset.