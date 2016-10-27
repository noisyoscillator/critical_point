# -*- coding: utf-8 -*-
# used to handle interactive

class Dialog:

    def __init__(self):
        pass

    def cont_or_not(self):
        print('Are you done with your questions? \n ',
              'If the question only asks for T_c, p_c, a or b, you can terminate the program now.\n',
              '[1] terminate\n', '[0] continue\n')
        #switch = int(input('press a button now: '))
        switch = 0
        if switch == 1:
            quit()
        else:
            print('continue\n')
