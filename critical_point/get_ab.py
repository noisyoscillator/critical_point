# subroutine to get the value of a and b in van der Waals equation of non-ideal gas


class GetAB:

    def __init__(self):
        pass

    def user_input(self):
        print("Note: all values should be in SI units, e.g. Pa for pressure, kelvin for temperature")
        t = float(input("please type the value of critical temperature, T_c: "))
        p = float(input("please type the value of critical pressure, p_c: "))
        return t, p

    def get_ab_from_tp(self, t, p, r):
        b = r*t/(8*p)
        a = 27*r*t*b/8
        v = 3*b
        return a, b, v

