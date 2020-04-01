import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as si
import pandas as pd


# open saved files
output_by_sim = '/Users/Simon_OMeara/Documents/Manchester/postdoc_stuff/box-model/PyCHAM_Gitw/PyCHAM/output/apinene_scheme_MCM/N2O5_test'

# name of file where experiment constants saved (number of size bins and whether wall 
# included)
fname = str(output_by_sim+'/constants')

const_in = open(fname)
const = {} # prepare to create dictionary
for line in const_in.readlines():

	# convert to python list
	dlist = []
	for i in line.split(',')[1::]:
		if str(line.split(',')[0]) == 'num_sb':
			dlist.append(int(i))
		if str(line.split(',')[0]) == 'num_speci':
			dlist.append(int(i))
		if str(line.split(',')[0]) == 'mw' or  str(line.split(',')[0]) == 'mv':
			i = i.strip('\n')
			i = i.strip('[')
			i = i.strip(']')
			i = i.strip(' ')
			dlist.append(float(i))
		if str(line.split(',')[0]) == 'spec_namelist':
			i = i.strip('\n')
			i = i.strip('[')
			i = i.strip(']')
			i = i.strip(' ')
			i = i.strip('\'')
			dlist.append(str(i))
		if str(line.split(',')[0]) == 'Cfactor':
			i = i.strip('\n')
			i = i.strip('[')
			i = i.strip(']')
			i = i.strip(' ')
			i = i.strip('\'')
			dlist.append(float(i))
	const[str(line.split(',')[0])] = dlist

num_sb = const['num_sb'] # number of size bins
num_speci = int((const['num_speci'])[0]) # number of species
y_mw = const['mw']
y_MV = const['mv']
PyCHAM_names = const['spec_namelist']
Cfac = float((const['Cfactor'])[0])


# name of file where concentration (molecules/cc (air)) results saved
fname = str(output_by_sim+'/y')
y = np.loadtxt(fname,delimiter=',',skiprows=1) # skiprows=1 omits header)

# withdraw times (s)
fname = str(output_by_sim+'/t')
t_array = np.loadtxt(fname,delimiter=',',skiprows=1) # skiprows=1 omits header)

plt.semilogy(t_array/3600.0, y[:,4]/Cfac, label='NO3')
plt.semilogy(t_array/3600.0, y[:,6]/Cfac, label='N2O5')
plt.semilogy(t_array/3600.0, y[:,20]/Cfac, label='APINENE')
plt.ylabel('ppb')
plt.xlabel('time (hrs)')
plt.legend()
plt.show()

# name of file with saved reaction rate coefficients
#fname = str(output_by_sim+'/OH_dydt')
#dydt = np.loadtxt(fname,delimiter=',',skiprows=1) # skiprows=1 omits header)




# name of file where concentration (# particles/cc (air)) results saved
# fname = str(output_by_sim+'/N')
# N = np.loadtxt(fname,delimiter=',',skiprows=1) # skiprows=1 omits header)
# 
# 
# name of file where particle size results saved
# fname = str(output_by_sim+'/x')
# x = np.loadtxt(fname,delimiter=',',skiprows=1) # skiprows=1 omits header)
# 
# calculate radius bounds (um) for the number size distribution contour plot 
# (assumes a linear size distribution)
# xbound = x[0, :]+(x[0, 1]-x[0, 0])/2.0
# xbound = np.append(0.0, xbound) # bottom bound
# 
# size bin radius bounds (um) for calculating dN/dlog10D (/cc (air))
# name of file where particle size results saved
# fname = str(output_by_sim+'/sbb')
# sbb = np.loadtxt(fname,delimiter=',',skiprows=1) # skiprows=1 omits header)
# 
# SOAvst = np.zeros((1,len(t_array)))
# ELVOC_O3 = np.zeros((1,len(t_array)))
# ELVOC_oh = np.zeros((1,len(t_array)))
# SVOC_O3 = np.zeros((1,len(t_array)))
# SVOC_oh = np.zeros((1,len(t_array)))
# 
# SVvst = np.zeros((1,len(t_array)))
# 
# sum of organics in condensed-phase at end of simulation (ug/m3 (air))
# for i in range(num_sb-1):
# 	
# 	# to replicate the SMPS results when using 
# 	# low size bin resolution in the model, find the volume of particles, then
# 	# assume a density of 1.25 g/cm3 for AIDA results (based on SMPS M/SMPS V in AIDA
# 	# results (Igor version)
# 	SOAvst[0, :] += np.sum((y[:, ((i+1)*num_speci):((i+2)*num_speci-1)]/si.N_A*(y_MV[0:-1])*1.0e12), axis = 1)
# 	
# 	# all ELVOC HOMs
# 	SVOC_O3[0, :] += (((y[:, ((i+2)*num_speci-4)]/si.N_A)*(y_MV[-4]))*1.0e12)
# 	SVOC_oh[0, :] += (((y[:, ((i+2)*num_speci-2)]/si.N_A)*(y_MV[-2]))*1.0e12)
# 	ELVOC_O3[0, :] += (((y[:, ((i+2)*num_speci-5)]/si.N_A)*(y_MV[-5]))*1.0e12)
# 	ELVOC_oh[0, :] += (((y[:, ((i+2)*num_speci-3)]/si.N_A)*(y_MV[-3]))*1.0e12)
# 	
# only semi-volatile contribution
# SVvst[0, :] = SOAvst-(ELVOC_O3+ELVOC_oh+SVOC_O3+SVOC_oh) 
# wall = np.sum((y[:, ((num_sb)*num_speci):((num_sb+1)*num_speci-2)]/si.N_A*(y_MV[0:-2])*1.25e12), axis = 1)

# open SMPS mass concentration measurements for comparison
# fnamepre = '/Users/Simon_OMeara/Documents/Manchester/postdoc_stuff/box-model/PyCHAM_Gitw/PyCHAM/output/'
# fname = str(fnamepre+'MACobs/SOAmass.xlsx')
# sht_name = str('SOAmass') # sheet name
# SMPSm = pd.read_excel(fname, sheet_name=sht_name)
# SMPSm = (SMPSm.values)[:, 1::] # convert to numpy array from pandas data frame
# # measured O3 time
# fname = str(fnamepre+'MACobs/dndlogDt.xlsx')
# sht_name = str('dndlogDt') # sheet name
# SMPSt = pd.read_excel(fname, sheet_name=sht_name)
# SMPSt = (SMPSt.values)[0::, 1] # convert to numpy array from pandas data frame
# 
# plt.plot(SMPSt, SMPSm, 'y');
# plt.plot(t_array/3600.0, SOAvst[0,:], 'xr')
# plt.plot(t_array/3600.0, SVvst[0,:], '.r')
# plt.plot(t_array/3600.0, ELVOC_O3[0,:], 'b')
# plt.plot(t_array/3600.0, ELVOC_oh[0,:], 'g')
# plt.plot(t_array/3600.0, SVOC_O3[0,:], 'k')
# plt.plot(t_array/3600.0, SVOC_oh[0,:], 'm')
# plt.show()

# plot simulated and measured O3

# measured O3
# fname = str(fnamepre+'MACobs/O3ppb.xlsx')
# sht_name = str('O3ppb') # sheet name
# O3ppb = pd.read_excel(fname, sheet_name=sht_name)
# O3ppbv = (O3ppb.values)[:, 1::] # convert to numpy array from pandas data frame
# # measured O3 time
# fname = str(fnamepre+'MACobs/gastime.xlsx')
# sht_name = str('gastime') # sheet name
# O3ppb = pd.read_excel(fname, sheet_name=sht_name)
# O3ppbt = (O3ppb.values)[:, 1::] # convert to numpy array from pandas data frame
# 
# plt.plot(O3ppbt, O3ppbv,'xr',label='measured')
# plt.plot(t_array/3600.0, y[:,1],'xg',label='simulated')
# plt.ylabel(r'Gas-phase concentration (ppb)', fontsize=18)
# plt.xlabel(r'Time (hours)', fontsize=18)

# measured alpha-pinene gas phase concentration
# fname = str(fnamepre+'MACobs/apineneppb.xlsx')
# sht_name = str('apinene') # sheet name
# appb = pd.read_excel(fname, sheet_name=sht_name)
# appbv = (appb.values)[:, 1::] # convert to numpy array from pandas data frame
# # apinene time
# sht_name = str('time') # sheet name
# appb = pd.read_excel(fname, sheet_name=sht_name)
# appbt = (appb.values)[:, 1::] # convert to numpy array from pandas data frame
# plt.plot(appbt/3600.0, appbv,'xr',label='measured')
# plt.plot(t_array/3600.0, y[:,num_speci-5],'xg',label='simulated')

# plot gas-phase concentrations from simulation
# plt.plot(t_array/3600.0, y[:, 21]*24614933694.758, label='CH4')
# plt.plot(t_array/3600.0, y[:, 10]*24614933694.758, label='CO')
# plt.plot(t_array/3600.0, y[:, 1]*24614933694.758, label='O3')
# plt.plot(t_array/3600.0, y[:, 3]*24614933694.758, label='NO2')
# plt.plot(t_array/3600.0, y[:, 2]*24614933694.758, label='NO')
# plt.plot(t_array/3600.0, y[:, 7]*24614933694.758, label='OH')
# plt.plot(t_array/3600.0, y[:, 8]*24614933694.758, label='HO2')
# plt.plot(t_array/3600.0, y[:, 22]*24614933694.758, label='CH3O2')
# plt.plot(t_array/3600.0, y[:, 0]*24614933694.758, label='O')

# plt.plot(t_array/3600.0, y[:, 1], label='O3')
# plt.plot(t_array/3600.0, y[:, 7], label='OH')
# plt.plot(t_array/3600.0, y[:, 8], label='HO2')
# plt.plot(t_array/3600.0, y[:, 3], label='NO2')
# plt.plot(t_array/3600.0, y[:, 21], label='CH4')
# plt.plot(t_array/3600.0, y[:, 2], label='NO')
# plt.plot(t_array/3600.0, y[:, 10], label='CO')
# 
# plt.title('PyCHAM Output')	
# plt.legend()
# plt.show()