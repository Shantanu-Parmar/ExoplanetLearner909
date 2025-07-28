# Disk dictionary for SMA HNC sample that includes basic geometric details

disk_dict = {}
disk_dict['V4046Sgr'] = { 'name'                   : 'V4046 Sgr',
		                  'SpT'                    : 'K5+K7', 
                          'RA'                     : '18h14m10.48s',
                          'Dec'                    : '-32.47.35.88',
                          'distance'               : 71.316, 		         # pc, Gaia DR3, Bailer-Jones et al. (2021)
                          'incl'                   : 34.69, 		         # deg, Flaherty et al. (2020)
                          'PA'                     : 75.7, 		             # deg, Flaherty et al. (2020)
                          'PA_gofish'              : 75.7 + 180.0, 	         # deg, corrected for gofish tool
                          'L_star'                 : 0.86, 		             # solar luminosities, Rosenfeld et al. (2012)
                          'M_star'                 : 1.75, 		             # solar masses,binary,0.9+0.9,Flaherty etal (2020)              
                          'M_star_err_pos'         : 0.09,                   # +pos err, solar masses, Rosenfeld et al. (2012)     
                          'M_star_err_neg'         : 0.06,		             # -neg err, solar masses, Rosenfeld et al. (2012)     
                          'Mass_Source'            : 'dynamical',            # type of mass calc., Rosenfeld et al. (2012) 
                          'v_sys'                  : 2.857, 		         # LSR systemic velocity [km/s]; Flaherty et al. (2020)
		                  'x0'                     : -0.47,                  # arcsec, continuum fit 
		                  'y0'                     : -0.45, 		         # arcsec, continuum fit
		                  'rmax_Keplerian'         : 3.0,                    # based on HCN data, SMA and Bergner et al. (2019) 
                          'target_res'             : 4.0,
                          'dV0'                    : 500.0,
                          'dVq'                    : -0.5,
                          'zr'                     : 0.0,
                          'mm_dust_cavity'         : 31,                     # in au

}

disk_dict['J1604'] = {    'name'                       : 'RXJ1604.3−2130 A',
                          'SpT'                       : 'K3',
                          'RA'                        : '16h04m21.655s',
                          'Dec'                       : '-21.30.28.55',
                          'distance'                  : 144.6,               # source distance in pc, from Gaia Collaboration 2023,
                          'incl'                      : 6.0,                 # inclination in degrees, Dong et al. (2017)
                          'PA'                        : 258.75,              # position angle in degrees, Stadler et al. 2023
                          'PA_gofish'                 : 258.75 + 0.0,        # position angle in degrees, corrected for gofish
                          'L_star'                    : 0.0,                 # stellar luminosity in solar luminosities,
                          'M_star'                    : 1.220,               # stellar mass in solar masses, Stadler et al. 2023
                          'Mass_Source'               : 'dynamical',         # type of mass calc., Teague et al. (2021)
                          'logMdot'                   : -8.1,                # stellar accretion rate, solar masses/yr (GM Aur is variable!), Ingleby et al. 2013
                          'v_sys'                     : 4.6172,              # LSR systemic velocity [km/s]; Stadler et al. (2023)
                          'x0'                        : 0.43,                # arcsec, continuum fit
                          'y0'                        : -0.45,               # arcsec, continuum fit
                          'rmax_Keplerian'            : 3.0,                 # based on HCN data, SMA and Bergner et al. (2019)
                          'target_res'                : 5.0,
                          'dV0'                       : 500.0,
                          'dVq'                       : -0.5,
                          'zr'                        : 0.0,
                          'mm_dust_cavity'            : 87,                  # in au, Stadler et al. (2023)

}


disk_dict['GMAur'] = {    'name'                      : 'GM Aur',
                          'RA'                        : '04h55m11.0s',
                          'Dec'                       : '+30.21.59.0',
                          'SpT'                       : 'K6',
                          'distance'                  : 159,                 # source distance in pc, from Gaia Collaboration 2018,
                          'incl'                      : -53.21,              # inclination in degrees, Huang et al. (2020)
                          'PA'                        : 57.17,               # position angle in degrees, Huang et al. (2020)
                          'PA_gofish'                 : 57.17 + 0.0,         # position angle in degrees, corrected for gofish
                          'L_star'                    : 1.2,                 # stellar luminosity in solar luminosities, Macias et al. 2018
                          'M_star'                    : 1.1,                 # stellar mass in solar masses, Macias et al. 2018
                          'Mass_Source'               : 'dynamical',         # type of mass calc., Teague et al. (2021)
                          'logMdot'                   : -8.1,                # stellar accretion rate, solar masses/yr (GM Aur is variable!), Ingleby et al. 2013
                          'v_sys'                     : 5.61,                # LSR systemic velocity [km/s]; Huang et al. (2020)
                          'x0'                        : -0.26,               # arcsec, continuum fit
                          'y0'                        : -0.20,               # arcsec, continuum fit
                          'rmax_Keplerian'            : 3.0,                 # based on HCN data, SMA and Bergner et al. (2019)
                          'target_res'                : 5.0,
                          'dV0'                       : 500.0,
                          'dVq'                       : -0.5,
                          'zr'                        : 0.0,
                          'mm_dust_cavity'            : 40,                  # in au, Huang et al. (2020)

}


disk_dict['LkCa15'] = {   'name'                   : 'LkCa 15',
                          'RA'                     : '04h39m17.8s',
                          'Dec'                    : '+22.21.03.1',
                          'SpT'                    : 'K5',		             # Luhman et al. (2010)
                          'distance'               : 156.5, 		         # pc, Gaia DR3, Bailer-Jones et al. (2021)
                          'incl'                   : -50.16,     	         # degrees, Facchini et al. (2020)
                          'PA'                     : 61.92,    	             # degrees, Facchini et al. (2020)
                          'PA_gofish'            : 61.92 + 0.0,  	         # degrees, corrected for disksurf
                          'L_star'                 : 1.05, 		             # solar luminosities, Donati et al. 2019
                          'M_star'                 : 1.20, 		             # solar masses, Law et al. 2023      
                          'M_star_err_pos'         : 0.07, 	                 # +pos err, solar masses, Law et al. (2023)     
                          'M_star_err_neg'         : 0.07, 		             # -neg err, solar masses, Law et al. (2023)     
                          'Mass_Source'            : 'dynamical',            # type of mass calc., Law et al. (2023) 
                          'v_sys'                  : 6.28, 	                 # LSR systemic velocity [km/s]
                          'x0'                     : 0.0,
                          'y0'                     : 0.0,
		                  'rmax_Keplerian'         : 4.5, 
                          'target_res'             : 0.5,
                          'dV0'                    : 500.0,
                          'dVq'                    : -0.5,
                          'zr'                     : 0.0,

}

disk_dict['GGTau'] = {    'name'                   : 'GG Tau',
		                  'SpT'                       : 'K7 + M0', 
                          'RA'                       : '04h32m30.34s',
                          'Dec'                      : '17.31.40.59',        # degrees
                          'distance'                 : 147.673996, 	         # pc, Gaia DR3, Bailer-Jones et al. (2021)
                          'incl'                     : 143, 		         # deg, Guilloteau et al. (1999)- referenced by other people
                          'PA'                       : 7.8, 		         # deg, Tang et al. 2023
                          'PA_gofish'                : 7.8, 	             # deg, corrected for gofish tool
                          'L_star'                   : 0.67,		         # solar luminosities, Keppler et al. (2020)
                          'M_star'                   : 1.41, 		         # solar masses, Phuong et al. 2020
                          'M_star_err_pos'           : 0.08,                 # +pos err, solar masses,  Phuong et al. 2020  
                          'M_star_err_neg'           : 0.08,	             # -neg err, solar masses, Phuong et al. 2020     
                          'Mass_Source'              : 'dynamical',          # type of mass calc., Phuong et al. 2020
                          'v_sys'                    : 6.5,	                 # LSR systemic velocity [km/s] 
		                  'x0'                       : 0,                    # arcsec, continuum fit 
		                  'y0'                       : 0,                    # arcsec, continuum fit
		                  'rmax_Keplerian'           : 4.0,                  # Keppler et al. (2020) 
                          'target_res'             	 : 2.6,                  # arcsec
                          'dV0'                   	 : 500,                  # defaults- not much resolution
                          'dVq'                   	 :-0.5,                  # default
                          'zr'                    	 : 0,
                          'mm_dust_cavity'           : 224,                  # in au
}
