import netCDF4
import numpy as np
import matplotlib.pyplot as plt

nc = netCDF4.Dataset('/home/olivia/Documents/SAFL_Data/Fluvial_2016_Time_Stamp/NetCDF_files/25mmhr/25mmhr_photos.nc', 'r')

ts_min = 1054
ts_max = 2049 # max time step
npix = 1700. * 3500.

time_list = []
f_not_reworked_list = []
#channel_maps = np.sum(nc.variables['channel_map'][400:1400,:,ts_min:ts_max], axis=2)
channel_maps = nc.variables['channel_map'][480:1280,:,ts_min:ts_max]

for i in range(ts_min, ts_max):
    print i
    time_list.append(nc.variables['time'][i:ts_max] - nc.variables['time'][i]) # Time lags relative to the selected starting time step
    reworked = np.cumsum(channel_maps[:,:,i-ts_min:], axis=2) > 0
    n_reworked = np.sum(reworked, axis=(0,1))
    f_not_reworked = 1 - n_reworked / npix
    f_not_reworked_list.append(f_not_reworked)

np.save('/home/olivia/Documents/SAFL_Data/Fluvial_2016_Time_Stamp/NetCDF_files/transition_25mmhr', (time_list, f_not_reworked_list))
