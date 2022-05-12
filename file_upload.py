import argparse
import os
import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

parser = argparse.ArgumentParser()
parser.add_argument("--inputdir", help="path to your subdirectory")
parser.add_argument("--destination_table", action = 'store',type = str, help = 'The text to parse.' )

args = parser.parse_args()

def process_file(filename,table):
    df = pd.read_csv(filename, index_col=False, delimiter = ',')
    try:
        conn = msql.connect(host='localhost', user='root',  
                        password='Lluuhhssarp@2321')#give ur username, password
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE mydb")
            print("Database is created")
    except Error as e:
        print("Error while connecting to MySQL", e)

# Creating table

    try:
        conn = msql.connect(host='localhost', database='mydb', user='root', password='Lluuhhssarp@2321')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.execute('DROP TABLE IF EXISTS startup;')
            print('Creating table....')
# in the below line please pass the create table statement which you want #to create
            cursor.execute('''create table {}( Sr_No int primary key, Date char(20), Startup_Name longtext, Industry_Vertical longtext, Subvertical longtext, City longtext, Investors_Name longtext, InvestmentnType longtext, Amount_in_USD char(20), Remarks longtext)'''.format(table))
            print("Table is created....")
        #loop through the data frame
            for i,row in df.iterrows():
                #here %S means string values 
                sql = '''INSERT INTO {} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''.format(table)
                cursor.execute(sql, tuple(row))
                print("Record inserted")
                # the connection is not auto committed by default, so we must commit to save our changes
                conn.commit()
    except Error as e:
            print("Error while connecting to MySQL", e)
    

def process_directory(directory_name,table):
    for filename in os.listdir(directory_name):
        process_file(os.path.join(directory_name, filename),table)

process_directory(args.inputdir,args.destination_table)