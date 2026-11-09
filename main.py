import pandas as pd
import numpy as np
import os
import re

#retrieving list of "entered" rq's
ent_lookup = pd.read_excel(r"C:\Users\Schirmer_N\Desktop\PERSONAL\CODE\Python\data_utilities\check_for_unentered_rqs\SMP_DATA TRACKER(test).xlsx")

rq_list = list(ent_lookup['RQ'])
class(ent_lookup)