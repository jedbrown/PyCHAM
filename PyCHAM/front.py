'''module called on by __main__ to initiate the box model'''

import numpy as np
from ode_gen import ode_gen
import matplotlib.pyplot as plt
import os
import eqn_parser # to parse the .scm file
from init_conc_func import init_conc_func
from pp_intro import pp_intro
from kimt_prep import kimt_prep
from saving import saving
import time # timing how long operations take
import user_input as ui
import pickle # for storing inputs
from volat_calc import volat_calc

def run(testf):
	
	# inputs:
	# testf - test flag, 1 for test mode (called by test_front.py), 2 for test mode 
	# (called by test_PyCHAM.py), 0 for normal mode
	
	if testf==2:
		print('"Run Model" button works fine')
		return()
	if testf==1:
		print('calling user_input.py')
	# module to ask, receive and return required inputs
	[fname, num_sb, lowersize, uppersize, end_sim_time, resfname, tstep_len, 
	tmax, TEMP, PInit, RH, lat, lon, start_sim_time, act_flux_path, save_step, Cw, 
	ChamR, nucv1, nucv2, nucv3, nuc_comp, new_partr, inflectDp, pwl_xpre,  
	pwl_xpro, inflectk, xmlname, init_conc, Comp0, Rader, voli, volP, 
	pconc, std, mean_rad, core_diss, light_stat, light_time, kgwt, testm, 
	dydt_trak, DayOfYear, space_mode, Ct, Compt, injectt, seed_name, 
	const_comp, const_infl, Cinfl, act_wi, act_w, seed_mw, 
	umansysprop_update, core_dens, p_char, e_field, const_infl_t, 
	chem_scheme_markers] = ui.run(0, testf)
	
	if testm == 1:
		print('PyCHAM calls front fine, now returning to PyCHAM.py')
		print('Please select the "Plot Results" button to ensure this works fine')
		return()
	
	if testf==1:
		print('user_input.py called and returned fine')
		print('calling eqn_parser.extract_mechanism')
	
	# obtain gas-phase reaction info
	[rindx, pindx, rstoi, pstoi, reac_coef, spec_list, Pybel_objects, num_eqn, num_speci, 
		RO2_indices, nreac, nprod, prodn, 
		reacn, M_val, N2_val, O2_val, C_H2O, Psat_water, 
		H2O_mw, spec_namelist] = eqn_parser.extract_mechanism(fname, xmlname, 
							TEMP, PInit, testf, RH, start_sim_time, lat, 
							lon, act_flux_path, DayOfYear, chem_scheme_markers)
	
	if testf==1:
		print('eqn_parser.extract_mechanism called and returned fine')
		print('calling init_conc_func')
	# set up initial gas-phase concentration array
	[y, H2Oi, y_mw, num_speci, 
	Cfactor, y_indx_plot, corei, dydt_vst, spec_namelist, 
							inj_indx, Ct, const_compi, 
							const_infli, Cinfl] = init_conc_func(num_speci, Comp0, 
							init_conc, TEMP, RH, M_val, N2_val, O2_val, reac_coef, fname, 
							PInit, start_sim_time, lat, lon, Pybel_objects, testf, pconc,
							act_flux_path, dydt_trak, end_sim_time, save_step, rindx, 
							pindx, num_eqn, nreac, nprod, DayOfYear, C_H2O, H2O_mw, 
							spec_namelist, Compt, Ct, seed_name, const_comp, const_infl, 
							seed_mw, Cinfl)
# 	print(C_H2O/Cfactor)
# 	ipdb.set_trace()
	if testf==1:
		print('init_conc_func called and returned fine')
		print('calling kimt_prep')
	# set up partitioning variables
	[DStar_org, mfp, accom_coeff, therm_sp, surfT, Cw, act_coeff] = kimt_prep(y_mw, TEMP, 
														num_speci, testf, Cw, act_wi, 
														act_w)

	# volatility (molecules/cc (air)) and density (rho, kg/m3) of components
	if testf==1:
		print('kimt_prep called and returned fine')
		print('calling volat_calc.py')
	[Psat, y_dens, Psat_Pa] = volat_calc(spec_list, Pybel_objects, TEMP, H2Oi, num_speci,  
								Psat_water, voli, volP, testf, corei, pconc,
								umansysprop_update, core_dens)

	if testf==1:
		print('volat_calc called and returned fine')
		print('calling wall_prep')
	
	if testf==1:
		print('wall_prep called and returned fine')
		print('calling pp_intro')
	# set up particle phase part
	[y, N_perbin, x, Varr, Vbou, rad0, Vol0, rbou, 
							MV, num_sb, nuc_comp, rbou00, upper_bin_rad_amp] = pp_intro(y, 
							num_speci, Pybel_objects, TEMP, H2Oi, 
							mfp, accom_coeff, y_mw, surfT, DStar_org, 
							RH, num_sb, lowersize, uppersize, pconc, tmax, nuc_comp, 
							voli, volP, testf, std, mean_rad, 
							therm_sp, Cw, y_dens, Psat, core_diss, kgwt, space_mode, 
							corei)
	
	t1 = time.clock() # get wall clock time before call to solver
	if testf==1:
		print('pp_intro called and returned fine')
		print('calling ode_gen')
	
	# call on ode function
	[t_out, y_mat, Nresult_dry, Nresult_wet, x2, dydt_vst] = ode_gen(tstep_len, y, 
				num_speci, num_eqn, 
				rindx, pindx, 
				rstoi, pstoi, H2Oi, TEMP, RO2_indices, 
				num_sb, Psat, mfp, accom_coeff, surfT, y_dens, N_perbin,
				DStar_org, y_mw, x, core_diss, Varr, Vbou, RH, rad0, Vol0,
				end_sim_time, np.array(pconc), save_step, 
				rbou, therm_sp, Cw, light_time, light_stat,
				nreac, nprod, prodn,
				reacn, new_partr, MV, nucv1, nucv2, nucv3, inflectDp, pwl_xpre, 
				pwl_xpro, inflectk, nuc_comp, ChamR, Rader, PInit, testf, kgwt, dydt_vst,
				start_sim_time, lat, lon, act_flux_path, DayOfYear, Ct, injectt, inj_indx,
				corei, const_compi, const_comp, const_infli, Cinfl, act_coeff, p_char, 
				e_field, const_infl_t)
				
	
	t2 = time.clock() # get wall clock time after call to solver
	if testf==0: # in normal mode
		print('time taken=')
		print(t2-t1)
	
		# make new pickle dump to store the indices and names of interesting gas-phase 
		# components along with initial pickle variables
		list_vars = [fname, resfname, y_indx_plot, Comp0]
	if testf==1:
		print('ode_gen called and returned fine')
		print('dumping variables in pickle file')
		# dummy list of variables to dump
		list_vars = ['fnametest','resfnametest', 0, 0]
		with open('test_var_store.pkl','wb') as f:
			pickle.dump(list_vars,f)
	
	if testf==00:
		with open('PyCHAM/var_store.pkl','wb') as f:
			pickle.dump(list_vars,f) 
	
	if testf==1:
		print('dumped successfully')
	# save data
	output_by_sim = saving(fname, y_mat, t_out, Nresult_dry, Nresult_wet, x2, num_sb, 
							y_mw, num_speci, 
							resfname, rbou, Cfactor, MV, testf, dydt_vst, dydt_trak,
							spec_namelist, rbou00, upper_bin_rad_amp)
	if testf==1:
		print('saving called and returned successfully')
	return()