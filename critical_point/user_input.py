# handle the user input functions

class UserInput:

    def __init__(self):
        pass

    def init_input_tp(self):
        print("Note: all values should be in SI units, e.g. Pa for pressure, kelvin for temperature")
        #t = float(input("please type the value of critical temperature, T_c: "))
        #p = float(input("please type the value of critical pressure, p_c: "))
        #print("\n")
        t = 304
        p = 7.39e6
        return t, p

    def temp_for_plot(self):
        temp = input("please type the temperature you want to plot\n"
                     "if you have multiple values, split two values by one space: ")
        temp_list = list(map(int, temp.split()))
        return temp_list
