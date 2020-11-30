import pandas as pd
from fuzzywuzzy import fuzz
import pickle
import pytest


class TestNlp:
    @pytest.fixture(autouse=True)
    def get_string(self):
        pickle_in = open("check.pickle","rb")
        ref_string = pickle.load(pickle_in)
        pickle_in.close()
        df = pd.read_csv('data.csv' , sep='\n')
        actual_string = ""
        for index, row in df.iterrows():
            actual_string += str(row[0])
        self.ref_string = ref_string
        self.actual_string = actual_string
        self.df = df
        
    
    def test_answer(self):
        assert self.actual_string == self.ref_string
    

    def test_row(self):
        assert self.df.shape[0] > 50