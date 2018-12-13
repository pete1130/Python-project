from datetime import datetime
import numpy as np
import json


class PoolTable:
    def __init__(self,id):
        self.id = id
        self.open =  True
        self.start_time =  None
        self.end_time =  None
        self.num_mins = ""
        self.costs = ""
        
    

    def __repr__(self):
        if (self.open == True):
            status = "Open"
        else:
            status = "Occupied"

        return f"""Table: {self.id} | Status: {status}\n Start Time: {self.start_time} | End Time: {self.end_time}\nMins Played: {self.num_mins} | Costs: {self.costs}\n\n"""

   



class TableManager:
    def __init__(self):
        self.table_manager_array = []
    
        for i in range(12):
            self.table_manager_array.append(PoolTable(i))
    
    def asDictionary(self):
        return self.__dict__


    def menu (self):
        quit_console = input("Enter C to continue. Enter Q to quit.\n ").upper()

        if (quit_console == "Q"):
            return

        initiate_console = input("Enter O to open, X to close, or V to view.\n ").upper()

        if (initiate_console == "O"):
            self.open_table()

        if (initiate_console == "X"):
            self.close_table()

        if (initiate_console == "V"):
            self.view_table()
        

    def open_table (self):
        for table in self.table_manager_array:
            if (table.open == True):
                table.open = False
                
                table.start_time = [datetime.now().hour, datetime.now().minute]
                print(table)
                
                break
                
        
        self.menu()

    
    def close_table (self):
        choice = int(input("Enter a table number to close out.\n"))
        if (self.table_manager_array[choice].open == False):
            self.table_manager_array[choice].open = True
                
            
            #end_time 
            self.table_manager_array[choice].end_time = [datetime.now().hour, datetime.now().minute]
            #minutes played calc
            self.table_manager_array[choice].num_mins = np.subtract(self.table_manager_array[choice].end_time, self.table_manager_array[choice].start_time)
            #costs calc
            if (self.table_manager_array[choice].num_mins[0] != 0 and self.table_manager_array[choice].num_mins[1] != 0):
                self.table_manager_array[choice].costs = self.table_manager_array[choice].num_mins[0]*(30) + self.table_manager_array[choice].num_mins[1]*(1/60*30)
            if (self.table_manager_array[choice].num_mins[0] == 0 and self.table_manager_array[choice].num_mins[1] != 0):
                self.table_manager_array[choice].costs = self.table_manager_array[choice].num_mins[1]*(1/60*30)
            if (self.table_manager_array[choice].num_mins[0] != 0 and self.table_manager_array[choice].num_mins[1] == 0):
                self.table_manager_array[choice].costs = self.table_manager_array[choice].num_mins[0]*(30) 

        
        
        
        self.menu()

    
    def view_table (self):
        print(self.table_manager_array)
        self.menu()
        


class DatetimeEncoder(json.JSONEncoder):
    def default(self, table_manager):
        try:
            return super(DatetimeEncoder, table_manager).default(table_manager)
        except TypeError:
            return str(table_manager)

table_manager = TableManager()
table_manager.menu()

with open("11-22-2017.json","w") as file_object:
    json.dump(table_manager.asDictionary(),file_object,cls=DatetimeEncoder,indent=2)

