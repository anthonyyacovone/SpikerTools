# this is an empty script used for testing, kindly disregard

import json
import spikertools as sp
from matplotlib import pyplot as plt
peth_test = sp.Session("dcmd_example_data\BYB_Recording_2016-07-29_16.29.37.wav", "")
#with open("C:/Users/USER\Desktop/Experiment0708A.json") as f:
#    data = json.load(f)
#    print(data)

#peth_test.plot_peth(0, (-1,1), "2", "1", 20)
#test_vec = [4]*5
#plt.scatter([0,2,3,4,5], test_vec)
#plt.show()
peth_test.plot_overview(show_events=False)