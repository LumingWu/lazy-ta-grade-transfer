# lazy-ta-grade-transfer
I was a TA/Grader for an undergraduate class where I had to transfer over 20 columns for above 80 students. So I wrote a Python program to help myself.

This program is for transfering from csv / excel to Blackboard.

The program accepts csv only, so use Excel to convert to csv.

The program will look match students by the column name "Student ID".

Remember file1 is the one we are looking to be filled.

If the first file is not being read correctly, try to uncomment the Blackboard parameters.

Blackboard is just a mess when you first pull the csv.

When filled, open the output file, at first row's first column, delete the extra encode information. Then you are good to upload the output to Blackboard.

