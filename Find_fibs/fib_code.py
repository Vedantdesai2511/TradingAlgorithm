class UpperFibFindABCD:
    def __init__(self):
        self.local_minimum_a = 0

    def find_a(self, z):
        """
        This side takes tick data as an in put and finds the fractal low in the data given
        input: array of five flots
        output: Value of fractal low
        """
        i = 2
        flag_a = 0
        # print("Yo 1")
        if len(z) >= 5:
            # print("length of z is bigger or equal to 5") ######################
            z = z[-5:]
        elif len(z) < 5:
            # print("length of z is smaller than 5") ######################
            return self.local_minimum_a, flag_a

        if ((z[i]) - (z[i-1]) < 0) and ((z[i]) - (z[i-2]) < 0):
            if ((z[i+1]) - (z[i]) > 0) and ((z[i+2]) - (z[i]) > 0):
                self.local_minimum_a = z[i]
                # print("Found up fib a")
                # print(self.local_minimum_a)
                flag_a = 1
                return self.local_minimum_a, flag_a

        # print("no a found")
        return self.local_minimum_a, flag_a
