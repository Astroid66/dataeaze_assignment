# dataeaze_assignment
Dataeaze assignment for internship. 

I have submitted two .py files named- file_up.py and file_upload.py.
file_upload.py is runnable i.e. if you input the username and password in the .py file and run it like 
'python3 file_upload.py --inputdir <folder_dir> --destination_table <table_name>' the file will run and the record willl be inserted in the the mysql database and we can perform the queries on it.

In file_up.py, I have tried to implement sending mysql_details via json file, but still there is an error which I am not able to solve.

So the pipeline of the implementation of the python file is :

-> used argparse to take directory of the folder and the destination table name as arguments.
-> defined a function for the process to be done in a file
-> defined a function for the process to be done in folder i.e. to traverse to all the files in it.
-> called the previous function to execute it with proper arguments.

Process to done in a file :

-> connect to the mysql server using the username and password.
-> Creating database
-> Creating table named <destination_table>
-> converting csv into dataframe
-> Inserting the records into the mysql table
