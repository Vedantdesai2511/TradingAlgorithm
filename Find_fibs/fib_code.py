class UpperFibFindABCD:
    def __init__(self):
        self.local_minimum_a = 0
        self.local_maximum_b = 0

    def find_a(self, z):
        """
        This side takes tick data as an in put and finds the fractal low in the data given
        input: array of five flots
        output: Value of fractal low
        """
        i = 2
        flag_a = 0
        if len(z) >= 5:  # if the length of input array is less grater than 5 use only last four terms of the array
            # for the analysis
            z = z[-5:]
        elif len(z) < 5:  # if the length  pf the input array is less than five do no proced as to find the fractal
            # low minimum number of points needed is 5
            return self.local_minimum_a, flag_a

        # ===== main logic =====
        # find fractal low (below given code)

        if ((z[i]) - (z[i-1]) < 0) and ((z[i]) - (z[i-2]) < 0):
            if ((z[i+1]) - (z[i]) > 0) and ((z[i+2]) - (z[i]) > 0):
                self.local_minimum_a = z[i]
                flag_a = 1
                return self.local_minimum_a, flag_a

        return self.local_minimum_a, flag_a

    def find_b(self, z, local_minimum_upfib_a):
        """
        Find fractal low after finding fractal high in previous function to mark down 'B' in fibonacci ABCD swing
        """
        i = 2  # initialize a variable to 2 for the calculation of fractal high (calculation can be seen in the mail
        # log part of the code
        level2 = 0  # To make level 2 in the fibonacci ABCD swing
        upper_level = 0  # to find upper level in the fibonacci ABCD swing
        flag_a = 1  # flag for code to know where it is at the moment
        if len(z) > 5:  # if the input z array is bigger than 5 then consider only last five elementa of the array
            z = z[-5:]
        else:
            pass

        # ===== main logic =====

        if ((z[i]) - (z[i-1]) > 0) and ((z[i]) - (z[i-2]) > 0):
            if ((z[i+1]) - (z[i]) < 0) and ((z[i+2]) - (z[i]) < 0):
                self.local_maximum_b = z[i]
                print(self.local_maximum_b)
                flag_a = 2

                diff = self.local_maximum_b - local_minimum_upfib_a
                level2 = self.local_maximum_b - (0.5 * diff)  # TODO: Have to change 0.786 to 0.618 and give option
                # TODO: to user to do this change according to risk calculation
                # TODO: eventually make algorithm to calculae risk and adjust the value by it self
                upper_level = local_minimum_upfib_a + (1.618 * diff)

                return self.local_maximum_b, level2, upper_level, flag_a
        return self.local_maximum_b, level2, upper_level, flag_a
