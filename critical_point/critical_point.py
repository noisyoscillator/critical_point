# -*- coding: utf-8 -*-

# solve path problem
import sys
import os
# get source file directory so that the program can be executable from anywhere
dir_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
sys.path.append(dir_root)
# Begin importing packages
from get_ab import GetAB

# aliases
init = GetAB()

# constants
R = 8.314

# get input value for T_c and p_c
T_c, p_c = init.user_input()
# calculate a and b
a, b, V_M = init.get_ab_from_tp(T_c, p_c, R)
print('a =', a, 'b =', b, 'V_M =', V_M)
