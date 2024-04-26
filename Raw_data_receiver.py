import numpy as np
import pandas as pd

""" data columns = <date> <open> <high> <low> <close> """

class rawdatareceiver ():
    def __init__ (self):
        self.preferred_col_names = ["date", "open", "high", "low", "close"]
        self.col_selection = None
        self.default_choice = [0,2,3,4,1]

    def receive_data_file (self, filename, data_name):
        readfile = pd.read_csv(filename)
        self.dataname = data_name
        print(f"read file with header as follows \n\n{readfile.head()}\n\n")
        self.rawdata = self.sort_columns(readfile)
        self.rawdata.columns = self.preferred_col_names
        return self.rawdata.copy()

    def get_column_selection (self,data):
        if self.col_selection : return self.col_selection
        self.colname_number = {i.lower():k for k,i in enumerate(data.columns)}

        msg1 = f"choose the order which data columns is sorted. \n\n "
        msg2 = f"data should be in order of {self.preferred_col_names} \n\n"
        msg3 = f"read data columns are : \n{self.colname_number}\n\n" # list(self.colname_number.keys())
        msg4 = f"write your selection as index starting from 0 , put space between indexes: \n"
        msg5 = f"if nothing wrote the default selection is performed with indexes as below\n"
        msg6 = str(self.default_choice) + "\n"
        chosen_order = input(msg1+msg2+msg3+msg4+msg5+msg6)

        if chosen_order == '' : chosen_order = self.default_choice
        else :
            chosen_order = chosen_order.split(" ")
            chosen_order = [int(i) for i in chosen_order]
        self.col_selection = chosen_order

        return self.col_selection

    def sort_columns (self,data):
        col_selection = self.get_column_selection(data)
        return data[np.array(data.columns)[col_selection]]
