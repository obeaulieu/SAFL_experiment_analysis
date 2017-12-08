import numpy as np
import matplotlib.pyplot as plt

data = np.load('/home/olivia/Documents/SAFL_Data/Fluvial_2016_Time_Stamp/NetCDF_files/BL_25mmhr.npy')

for i in range(len(f_not_reworked_list)):
    plt.plot(time_list[i] - time_list[i][0], f_not_reworked_list[i], 'k,')
plt.show()

