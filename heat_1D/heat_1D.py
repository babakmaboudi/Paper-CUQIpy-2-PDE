#!/usr/bin/env python

#%%
### Not to be included in the paper ###
import numpy as np
import matplotlib.pyplot as plt
from math import floor
import sys
import cuqi
cuqi.__version__
import os
import time
import pickle
import copy


global_Ns = 50000*3#1000000
use_global_Ns = True
data_folder = './data2_cont6/'

cases = []

case_name = 'paper_case1'
# We increased the number of samples to 50000
# 
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
sampler_choice = 'MetropolisHastings'
domain_dim = N
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 50000 # Number of samples
scale = 0.001
dg = 'Continuous1D'
cov = 0.05**2
mean = np.zeros(domain_dim)
x0=np.zeros(domain_dim)*0.1
noise_level = 0.01
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='ExpSin'
adapt = True
prior_obj = None
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})



case_name = 'paper_case2'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.05
scale[1] = 0.1
scale[2] = 0.2
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='ExpSin'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})

case_name = 'paper_case2_b'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.5
scale[1] = 1
scale[2] = 1
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='two_peaks'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case2_b2'
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.5
scale[1] = 1
scale[2] = 1
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='two_peaks'
adapt = True
prior_obj = None
decay = 1.5 # (but not stored in the case, can be accessed from the geometry object)
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case2_b3'
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.5
scale[1] = 1
scale[2] = 1
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='two_peaks'
adapt = True
prior_obj = None
decay = 1.3
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case2_b4'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.5
scale[1] = 1
scale[2] = 1
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='two_peaks'
adapt = True
prior_obj = None
decay = 1.4
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case2_b3_1'
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[:5] = [0.16743717, 0.34472453, 0.36497482, 0.39897863, 0.61114392]
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='two_peaks'
adapt = True
prior_obj = None
decay = 1.3
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})

case_name = 'paper_case2_b3_2'
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.5
scale[1] = 1
scale[2] = 1
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='two_peaks'
adapt = True
prior_obj = None
decay = 1.3
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case2_b3_3'
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.5
scale[1] = 1
scale[2] = 1
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.05
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='two_peaks'
adapt = True
prior_obj = None
decay = 1.3
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case2_b3_4'
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.5
scale[1] = 1
scale[2] = 1
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = 0
obs_grid_rl = int(N/2)
exact_func ='two_peaks'
adapt = True
prior_obj = None
decay = 1.3
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})

case_name = 'paper_case2_b3_5'
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.5
scale[1] = 1
scale[2] = 1
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.05
obs_grid_ll = 0
obs_grid_rl = int(N/2)
exact_func ='two_peaks'
adapt = True
prior_obj = None
decay = 1.3
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case2_b5'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.5
scale[1] = 1
scale[2] = 1
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.005
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='two_peaks'
adapt = True
prior_obj = None
decay = 1.1
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case2_b6'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.5
scale[1] = 1
scale[2] = 1
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.001
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='two_peaks'
adapt = True
prior_obj = None
decay = 1.5
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})

case_name = 'paper_case2_b6_2'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.5
scale[1] = 1
scale[2] = 1
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.001
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='two_peaks'
adapt = True
prior_obj = None
decay = 1.3
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case3'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.05
scale[1] = 0.1
scale[2] = 0.2
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='Prior_sample'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case3_b'
# 
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.04 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)*1.1
scale[0] = 0.02
scale[1] = 0.1
scale[2] = 0.7
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='Prior_sample'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})

case_name = 'paper_case3_c'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.02 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.05
scale[1] = 0.1
scale[2] = 0.2
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='Prior_sample'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case3_d'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.03 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.05
scale[1] = 0.1
scale[2] = 0.2
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='Prior_sample'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})

case_name = 'paper_case9'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.05
scale[1] = 0.1
scale[2] = 0.2
noise_level = 0.02
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='ExpSin'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case10'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.05
scale[1] = 0.1
scale[2] = 0.2
noise_level = 0.05
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
obs_grid_ll = 0
obs_grid_rl = N
exact_func ='ExpSin'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case11'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.05
scale[1] = 0.1
scale[2] = 0.2
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = int(N/3)
obs_grid_rl = N
exact_func ='ExpSin'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})

case_name = 'paper_case12'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.05
scale[1] = 0.1
scale[2] = 0.2
noise_level = 0.02
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
obs_grid_ll = int(N/3)
obs_grid_rl = N
exact_func ='ExpSin'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False


cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case13'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.05
scale[1] = 0.1
scale[2] = 0.2
noise_level = 0.05
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
obs_grid_ll = int(N/3)
obs_grid_rl = N
exact_func ='ExpSin'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case14'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.05
scale[1] = 0.1
scale[2] = 0.2
# Added later
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
noise_level = 0.01
obs_grid_ll = int(2*N/3)
obs_grid_rl = N
exact_func ='ExpSin'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})

case_name = 'paper_case15'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.05
scale[1] = 0.1
scale[2] = 0.2
noise_level = 0.02
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
obs_grid_ll = int(2*N/3)
obs_grid_rl = N
exact_func ='ExpSin'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case16'
# Very Good results, min ESS ~60, I will use this case for the paper
# unless we decide to increase the final time. Can display 50% CI
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 20
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = np.ones(domain_dim)
scale[0] = 0.05
scale[1] = 0.1
scale[2] = 0.2
noise_level = 0.05
dg = 'KL'
cov = 1
mean = np.zeros(domain_dim)
x0=None
obs_grid_ll = int(2*N/3)
obs_grid_rl = N
exact_func ='ExpSin'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case17'
# 
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 3
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = 1
noise_level = 0.01
dg = 'Step'
cov = 1
mean = np.zeros(domain_dim)
x0=None
obs_grid_ll = 0
obs_grid_rl = N
exact_func = 'Step'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case17_b'
# 
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 3
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = 1
noise_level = 0.05
dg = 'Step'
cov = 1
mean = np.zeros(domain_dim)
x0=None
obs_grid_ll = 0
obs_grid_rl = N
exact_func = 'Step'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case17_c'
# 
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = N
sampler_choice = 'MetropolisHastings'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = 0.03
noise_level = 0.01
dg = 'Continuous1D'
cov = 1
mean = np.zeros(domain_dim)
x0=np.ones(domain_dim)*0.5
obs_grid_ll = 0
obs_grid_rl = N
exact_func = 'Step'
adapt = True
#prior_obj = cuqi.distribution.Cauchy_diff(np.zeros(domain_dim), 0.002, 'neumann')
#prior_obj =  cuqi.distribution.Laplace_diff(location=np.zeros(domain_dim), scale=0.01)

prior_obj = cuqi.distribution.LMRF(np.zeros(domain_dim), 100, domain_dim, 1, 'neumann')
decay = 1.7
enable_FD = False


cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})


case_name = 'paper_case19'
# 
# Prepare PDE form
N = 100   # Number of solution nodes
L = 1.0  # Length of the domain
T = 0.01 # Final time
dx = L/(N+1)   # Space step size
cfl = 5/11 # The cfl condition to have a stable solution
dt_approx = cfl*dx**2 # Defining approximate time step size
num_time_steps = int(T/dt_approx)+1 # Number of time steps
domain_dim = 2
sampler_choice = 'CWMH'
Ns_factor = domain_dim if sampler_choice == 'CWMH' else 1
Ns =  int(global_Ns/Ns_factor) if use_global_Ns  else 1000 # Number of samples
scale = 1
noise_level = 0.01
dg = 'GaussianPulse'
cov = np.array([0.2, 0.1])
mean = np.array([0.5, 0.2])
x0=None
obs_grid_ll = 0
obs_grid_rl = N
exact_func = 'GaussianPulse'
adapt = True
prior_obj = None
decay = 1.7
enable_FD = False

cases.append({'case_name':case_name, 'N':N, 'L':L, 'T':T, 'dx':dx, 'cfl':cfl, 'dt_approx':dt_approx, 'num_time_steps':num_time_steps, 'Ns':Ns, 'domain_dim':domain_dim, 'scale':scale, 'dg':dg, 'cov':cov, 'x0':x0, 'sampler_choice':sampler_choice, 'noise_level':noise_level, 'obs_grid_ll':obs_grid_ll, 'exact_func':exact_func, 'mean':mean, 'adapt':adapt, 'prior_obj':prior_obj, 'decay':decay, 'obs_grid_rl':obs_grid_rl, 'enable_FD':enable_FD})

case_name = 'paper_case20'
for case in cases:
    if case['case_name'] == 'paper_case2_b6_2':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['decay'] = 1.7
cases.append(case_copy)

case_name = 'paper_case21'
for case in cases:
    if case['case_name'] == 'paper_case2_b3_2':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['decay'] = 1.7
cases.append(case_copy)

case_name = 'paper_case22'
for case in cases:
    if case['case_name'] == 'paper_case2_b3_3':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['decay'] = 1.7
cases.append(case_copy)

case_name = 'paper_case23'
for case in cases:
    if case['case_name'] == 'paper_case2_b3_5':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['decay'] = 1.7
cases.append(case_copy)

case_name = 'paper_case24'
for case in cases:
    if case['case_name'] == 'paper_case2_b6':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
cases.append(case_copy)

case_name = 'paper_case25'
for case in cases:
    if case['case_name'] == 'paper_case2_b6':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['noise_level'] = 0.01
cases.append(case_copy)

case_name = 'paper_case26'
for case in cases:
    if case['case_name'] == 'paper_case2_b6':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['noise_level'] = 0.05
cases.append(case_copy)

case_name = 'paper_case27'
for case in cases:
    if case['case_name'] == 'paper_case2_b6':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['noise_level'] = 0.05
case_copy['obs_grid_rl']= int(case_copy['N']/2)
cases.append(case_copy)

case_name = 'paper_case28'
for case in cases:
    if case['case_name'] == 'paper_case2_b6':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['noise_level'] = 0.05
case_copy['obs_grid_rl']= int(case_copy['N']*2/3)
cases.append(case_copy)


case_name = 'paper_case29'
for case in cases:
    if case['case_name'] == 'paper_case2_b6':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['noise_level'] = 0.05
case_copy['obs_grid_rl']= int(case_copy['N']/2)
case_copy['Ns'] = case_copy['Ns']*2 
cases.append(case_copy)


#case_name = 'paper_case30'
#for case in cases:
#    if case['case_name'] == 'paper_case2_b6':
#        case_copy = copy.deepcopy(case)
#        break
#case_copy['case_name'] = case_name
#case_copy['sampler_choice'] = 'ULA'
#case_copy['enable_FD'] = True
#case_copy['scale'] = 1/(20)
#cases.append(case_copy)
#
#
#case_name = 'paper_case31'
#for case in cases:
#    if case['case_name'] == 'paper_case2_b6':
#        case_copy = copy.deepcopy(case)
#        break
#case_copy['case_name'] = case_name
#case_copy['sampler_choice'] = 'ULA'
#case_copy['enable_FD'] = True
#case_copy['noise_level'] = 0.01
#case_copy['scale'] = 1/(20)
#cases.append(case_copy)
#
#
#case_name = 'paper_case32'
#for case in cases:
#    if case['case_name'] == 'paper_case2_b6':
#        case_copy = copy.deepcopy(case)
#        break
#case_copy['case_name'] = case_name
#case_copy['sampler_choice'] = 'ULA'
#case_copy['enable_FD'] = True
#case_copy['noise_level'] = 0.05
#case_copy['scale'] = 1/(20)
#cases.append(case_copy)
#
#
#case_name = 'paper_case33'
#for case in cases:
#    if case['case_name'] == 'paper_case2_b6':
#        case_copy = copy.deepcopy(case)
#        break
#case_copy['case_name'] = case_name
#case_copy['sampler_choice'] = 'ULA'
#case_copy['enable_FD'] = True
#case_copy['noise_level'] = 0.05
#case_copy['obs_grid_rl']= int(case_copy['N']/2)
#case_copy['scale'] = 1/(20)
#cases.append(case_copy)

#selected_case_names = ['paper_case20', 'paper_case21', 'paper_case22', 'paper_case23']
#selected_case_names = ['paper_case24', 'paper_case25', 'paper_case26', 'paper_case27']

#selected_case_names = ['paper_case28', 'paper_case29']#, 'paper_case30', 'paper_case31', 'paper_case32', 'paper_case33']


case_name = 'paper_case34'
for case in cases:
    if case['case_name'] == 'paper_case2_b6':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['noise_level'] = 0.05
case_copy['normalizer'] = 10
cases.append(case_copy)

case_name = 'paper_case35'
for case in cases:
    if case['case_name'] == 'paper_case24':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['normalizer'] = 10
cases.append(case_copy)

case_name = 'paper_case36'
for case in cases:
    if case['case_name'] == 'paper_case25':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['normalizer'] = 10
cases.append(case_copy)

case_name = 'paper_case37'
for case in cases:
    if case['case_name'] == 'paper_case26':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['normalizer'] = 10
cases.append(case_copy)

case_name = 'paper_case38'
for case in cases:
    if case['case_name'] == 'paper_case29':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['normalizer'] = 10
case_copy['Ns'] = int(case_copy['Ns']/2)
cases.append(case_copy)

case_name = 'paper_case39'
for case in cases:
    if case['case_name'] == 'paper_case17':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['T'] = 0.02
case_copy['num_time_steps'] = case_copy['num_time_steps']*2 
cases.append(case_copy)

case_name = 'paper_case40'
for case in cases:
    if case['case_name'] == 'paper_case17_b':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['num_time_steps'] = case_copy['num_time_steps']*2
case_copy['T'] = 0.02
cases.append(case_copy)

case_name = 'paper_case41'
for case in cases:
    if case['case_name'] == 'paper_case17':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['T'] = 0.04
case_copy['num_time_steps'] = case_copy['num_time_steps']*4 
cases.append(case_copy)

case_name = 'paper_case42'
for case in cases:
    if case['case_name'] == 'paper_case17_b':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['num_time_steps'] = case_copy['num_time_steps']*4
case_copy['T'] = 0.04
cases.append(case_copy)

case_name = 'paper_case43'
for case in cases:
    if case['case_name'] == 'paper_case17':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['T'] = 0.02
case_copy['noise_level'] = 0.05
case_copy['scale'] = 0.0001
case_copy['num_time_steps'] = case_copy['num_time_steps']*2 
case_copy['sampler_choice'] = 'MALA'
case_copy['enable_FD'] = True
cases.append(case_copy)

case_name = 'paper_case44'
for case in cases:
    if case['case_name'] == 'paper_case17_b':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['num_time_steps'] = case_copy['num_time_steps']*2
case_copy['T'] = 0.02
case_copy['noise_level'] = 0.1
case_copy['scale'] = 0.0001
case_copy['sampler_choice'] = 'MALA'
case_copy['enable_FD'] = True
cases.append(case_copy)

case_name = 'paper_case45'
for case in cases:
    if case['case_name'] == 'paper_case17':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['T'] = 0.02
case_copy['noise_level'] = 0.05
case_copy['num_time_steps'] = case_copy['num_time_steps']*2 
cases.append(case_copy)

case_name = 'paper_case46'
for case in cases:
    if case['case_name'] == 'paper_case17_b':
        case_copy = copy.deepcopy(case)
        break
case_copy['case_name'] = case_name
case_copy['T'] = 0.02
case_copy['noise_level'] = 0.1
case_copy['num_time_steps'] = case_copy['num_time_steps']*2
cases.append(case_copy)


#selected_case_names = ['paper_case39','paper_case40'] 
#selected_case_names = ['paper_case41','paper_case42']
selected_case_names = ['paper_case45','paper_case46']

selected_cases = [case for case in cases if case['case_name'] in selected_case_names]
for case in selected_cases:
    # Create the results folder if it does not exist


    print("Sampling for case", case['case_name'])
    print(case)
    case_name = case['case_name']
    N = case['N']
    L = case['L']
    T = case['T']
    dx = case['dx']
    cfl = case['cfl']
    dt_approx = case['dt_approx']
    num_time_steps = case['num_time_steps']
    Ns = case['Ns']
    domain_dim = case['domain_dim']
    scale = case['scale']
    dg = case['dg']
    cov = case['cov']
    x0 = case['x0']
    sampler_choice = case['sampler_choice']
    noise_level = case['noise_level']
    obs_grid_ll = case['obs_grid_ll']
    obs_grid_rl = case['obs_grid_rl']
    exact_func = case['exact_func']
    mean = case['mean']
    adapt = case['adapt']
    prior_obj = case['prior_obj']
    decay = case['decay']
    enable_FD = case['enable_FD']
    if 'normalizer' in case.keys():
        normalizer = case['normalizer']
    else:
        normalizer = 12
    

    print("###"+data_folder+case_name)
    if not os.path.exists(data_folder+case_name):
        os.makedirs(data_folder+case_name)
        print("Created folder for case", case['case_name'])
    else:
        print("The folder already exists for case "+case["case_name"]+". Please delete the folder or change the case name.")
        break  

    # Grid for the heat model
    grid = np.linspace(dx, L, N, endpoint=False)
    grid_obs = grid[obs_grid_ll:obs_grid_rl]
    
    # Time steps
    time_steps = np.linspace(0, T, num_time_steps, endpoint=True)
    
    # FD diffusion operator
    Dxx = (np.diag(-2*np.ones(N)) + np.diag(np.ones(N-1), -1)
           + np.diag(np.ones(N-1), 1))/dx**2  
    
    
    # PDE form (diff_op, IC, time_steps)
    if dg == 'GaussianPulse':
        domain_map = lambda x0, a, grid: a*np.exp( -50 * ( (grid - x0)/L)**2 )
        domain_map_grid = lambda x: domain_map(x[0], x[1], grid) 
        def PDE_form(initial_condition, t): return (Dxx, np.zeros(N),
                                                domain_map_grid(initial_condition))
    else:
        def PDE_form(initial_condition, t): return (Dxx, np.zeros(N),
                                                initial_condition)
    
    PDE = cuqi.pde.TimeDependentLinearPDE(
        PDE_form, time_steps, grid_sol=grid, grid_obs=grid_obs)
    

    
    # Set up geometries for model
    if (dg == 'KL'): # (paper) remove the options
        domain_geometry = cuqi.geometry.KLExpansion(grid, decay_rate=decay,
                                                normalizer=normalizer, 
                                                num_modes=domain_dim)
    elif (dg == 'Continuous1D'):
        domain_geometry = cuqi.geometry.Continuous1D(grid)

    elif (dg == 'Step'):
        domain_geometry = cuqi.geometry.StepExpansion(grid, n_steps=domain_dim)

    elif (dg == 'GaussianPulse'):
        domain_geometry = cuqi.geometry.Discrete(['x0', 'a'])
    
    range_geometry = cuqi.geometry.Continuous1D(grid_obs)
    
    # Prepare model
    model = cuqi.model.PDEModel(PDE, range_geometry, domain_geometry)
    
    # Create the prior distribution
    if prior_obj == None:
        x = cuqi.distribution.Gaussian(mean=mean, cov=cov,
                                   geometry=domain_geometry)
    else:
        x = prior_obj
        x.geometry = domain_geometry
        x.name = 'x'
    
    
    # Now samples from the prior will look like:
    
    ### Not to be included in the paper ###
    try:
        prior_samples = x.sample(20) 
    except:
        prior_samples = cuqi.samples.Samples(np.zeros((model.domain_dim, 20)), geometry=domain_geometry)

    plt.figure()
    for s in prior_samples:
        domain_geometry.plot(s, is_par=True)
    
    # True parameters that we want to infer
    x_exact_raw = None
    if exact_func == "ExpSin":
        x_exact_raw = grid*np.exp(-2*grid)*np.sin(L-grid)
    elif exact_func == "two_peaks":
        x_exact_raw =1/30*(1-np.cos(2*np.pi*(L-grid)/(L)))\
                    +1/30*np.exp(-2*(10*(grid-0.5))**2)+\
                     1/30*np.exp(-2*(10*(grid-0.8))**2)
    elif exact_func == "Step":
        n_steps = 3 #model.domain_dim
        n_steps_values = [0,1,.5]
        x_exact_raw = np.zeros(N)
        
        start_idx=0
        for i in range(n_steps):
            end_idx = floor((i+1)*N/n_steps)+1
            x_exact_raw[start_idx:end_idx] = n_steps_values[i]
            start_idx = end_idx
    elif exact_func == "GaussianPulse":
        x_exact_raw = domain_map_grid([.3, .15])

    elif exact_func == 'Prior_sample':
        np.random.seed(0)
        x_exact = x.sample()

    if x_exact_raw is not None:
        x_exact = cuqi.array.CUQIarray(x_exact_raw, is_par=False,
                                     geometry=domain_geometry)


    # Generate the exact data
    y_exact = model.forward(x_exact)
    

    
    ### Not to be included in the paper ###
    sigma =1.0/np.sqrt(N)* noise_level*np.linalg.norm(y_exact)
    

    
    # Create the data distribution
    y = cuqi.distribution.Gaussian(model(x),
                                   sigma**2*np.eye(model.range_dim),
                                   geometry=range_geometry)

    # Generate noisy data
    data = y(x = x_exact).sample()

    plt.figure()
    legend_list = []
    if dg != 'GaussianPulse':
        x_exact.plot()
        legend_list.append('exact solution')
    y_exact.plot()
    legend_list.append('exact data')
    data.plot()
    legend_list.append('noisy data')
    plt.legend(legend_list);

    
    
    #plt.plot(data-y_exact)
    print(np.linalg.norm(data-y_exact))
    print(np.linalg.norm(y_exact))
    print(np.linalg.norm(data-y_exact)/np.linalg.norm(y_exact))
    
    
    
    # Bayesian model
    joint_distribution = cuqi.distribution.JointDistribution(x, y)
    posterior = joint_distribution(y = data) 
    

    if (sampler_choice == 'MetropolisHastings'):
        MySampler = cuqi.sampler.MetropolisHastings(posterior, scale = scale, x0=x0)
    elif (sampler_choice == 'CWMH'):
        MySampler = cuqi.sampler.CWMH(posterior, scale = scale, x0=x0)
    elif (sampler_choice == 'pCN'):
        MySampler = cuqi.sampler.pCN(posterior, scale = scale, x0=x0)
    elif (sampler_choice == 'ULA'):
        if enable_FD:
            posterior.enable_FD()
        MySampler = cuqi.sampler.ULA(posterior, scale = scale, x0=x0)
    elif (sampler_choice == 'MALA'):
        if enable_FD:
            posterior.enable_FD()
        MySampler = cuqi.sampler.MALA(posterior, scale = scale, x0=x0)
    elif (sampler_choice == 'NUTS'):
        if enable_FD:
            posterior.enable_FD()
        MySampler = cuqi.sampler.NUTS(posterior, x0=x0,  max_depth = 9)

    
    t1 = time.time()    
    if adapt:
        posterior_samples = MySampler.sample_adapt(Ns)
    else:
        posterior_samples = MySampler.sample(Ns)
    t2 = time.time()
    case["sampling_time"] = t2-t1
    
    ### Not to be included in the paper ###
    case["updated_scale"] = MySampler.scale
    case["ESS"] = posterior_samples.compute_ess()


    pickle.dump(data, open(data_folder+case_name + '/data.pkl', 'wb'))
    pickle.dump(x_exact, open(data_folder+case_name + '/x_exact.pkl', 'wb'))
    pickle.dump(y_exact, open(data_folder+case_name + '/y_exact.pkl', 'wb'))
    case['x_exact_geometry'] = x_exact.geometry
    case['y_exact_geometry'] = y_exact.geometry
    case['data_geometry'] = data.geometry
    case['x_exact_is_par'] = x_exact.is_par
    case['y_exact_is_par'] = y_exact.is_par
    case['data_is_par'] = data.is_par
    
    # Save prior samples:
    pickle.dump(prior_samples, open(data_folder+case_name + '/prior_samples.pkl', 'wb'))
    
    # Save posterior samples:
    pickle.dump(posterior_samples, open(data_folder+case_name + '/samples.pkl', 'wb'))

    # Save the case parameters
    pickle.dump(case, open(data_folder+case_name + '/parameters.pkl', 'wb'))
    
    # Save prior plot
    plt.figure()
    for s in prior_samples:
        domain_geometry.plot(s, is_par=True)
    plt.savefig(data_folder+case_name + '/prior.png')

    # Plot true solution, exact data and noisy data
    plt.figure()
    legend_list = []
    if dg != 'GaussianPulse':
        x_exact.plot()
        legend_list.append('exact solution')
    y_exact.plot()
    legend_list.append('exact data')
    data.plot()
    legend_list.append('noisy data')
    plt.legend(legend_list);
    plt.savefig(data_folder+case_name + '/sol_data.png')

    # Plot ESS
    plt.figure()
    plt.plot(case["ESS"], 'o-')
    plt.savefig(data_folder+case_name + '/ESS.png')

    # Plot trace
    plt.figure()
    idx_list = [0,1,2,3,4,5,6,7,8,9,10]
    idx_list = [i for i in idx_list if i < model.domain_dim]
    posterior_samples.plot_trace(idx_list);
    plt.savefig(data_folder+case_name + '/trace.png')

    # Plot pair
    plt.figure()
    idx_list = [0,1,2,5,10]
    idx_list = [i for i in idx_list if i < model.domain_dim]
    posterior_samples.plot_pair(idx_list);
    plt.savefig(data_folder+case_name + '/pair_plot.png')

    # Plot the ci as par and save the plot
    plt.figure()
    posterior_samples.plot_ci(95, plot_par=True)
    plt.savefig(data_folder+case_name + '/plot_ci_par.png')

    # Plot ci as funvals and save the plot
    plt.figure()
    try:
        posterior_samples.plot_ci(95, exact=x_exact)
    except:
        posterior_samples.plot_ci(95)	
    plt.savefig(data_folder+case_name + '/plot_ci.png')
    
    # Plot the ci after funvals conversion
    plt.figure()
    try:
        posterior_samples.funvals.plot_ci(95, exact=x_exact)
    except:
        posterior_samples.funvals.plot_ci(95)
    plt.savefig(data_folder+case_name + '/plot_ci_funvals.png')