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

        # find fractal low (below given code)

        if ((z[i]) - (z[i-1]) < 0) and ((z[i]) - (z[i-2]) < 0):
            if ((z[i+1]) - (z[i]) > 0) and ((z[i+2]) - (z[i]) > 0):
                self.local_minimum_a = z[i]
                flag_a = 1
                return self.local_minimum_a, flag_a

        return self.local_minimum_a, flag_a

    def find_b(self, z):
        i = 2
        level2 = 0
        upper_level = 0
        flag_a = 1
        # print("Yo")
        if len(z) > 5:
            z = z[-5:]
        else:
            # print("Hmmm")
            pass

            if ((z[i]) - (z[i-1]) > 0) and ((z[i]) - (z[i-2]) > 0):
                if ((z[i+1]) - (z[i]) < 0) and ((z[i+2]) - (z[i]) < 0):
                    # print("Found up fib b")
                    self.local_maximum_b = z[i]
                    print(self.local_maximum_b)
                    flag_a = 2

                    return self.local_maximum_b, level2, upper_level, flag_a
        return self.local_maximum_b, level2, upper_level, flag_a
