# subroutine to get the value of a and b in van der Waals equation of non-ideal gas


class GetAB:

    def __init__(self):
        pass

    def get_ab_from_tp(self, t, p, r):
        b = r*t/(8*p)
        a = 27*r*t*b/8
        v = 3*b
        return a, b, v

