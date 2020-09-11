class UpperFibFindABCD:
    def __init__(self):
        self.local_minimum_a = 0
        self.local_maximum_b = 0
        self.local_minimum_C = 0
        self.c_above_b_flag = 0
        self.local_maximum_d = 0

    def find_a(self, z):
        """
        This side takes tick data as an in put and finds the fractal low in the data given
        input: array of five flats
        return: float (Value of fractal low) amd int (flag)
        """
        i = 2
        flag_a = 0
        if len(z) >= 5:  # if the length of input array is less grater than 5 use only last four terms of the array
            # for the analysis
            z = z[-5:]
        elif len(z) < 5:  # if the length  of the input array is less than five do no proceed as to find the fractal
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

    def find_b(self, z, volatility, local_minimum_upfib_a):
        """
        Find fractal low after finding fractal high in previous function to mark down 'B' in fibonacci ABCD swing
        """
        i = 2  # initialize a variable to 2 for the calculation of fractal high (calculation can be seen in the main
        # log part of the code
        level2 = 0  # To make level 2 in the fibonacci ABCD swing
        upper_level = 0  # to find upper level in the fibonacci ABCD swing
        flag_a = 1  # flag for algorithm to know where it is at the moment
        if len(z) > 5:  # if the input z array is bigger than 5 then consider only last five elements of the array
            z = z[-5:]
        elif len(z) < 5:  # if the length  of the input array is less than five do no proceed as to find the fractal
            # low minimum number of points needed is 5,
            return self.local_maximum_b, level2, upper_level, flag_a

        # ===== main logic =====

        if z[-1] > (local_minimum_upfib_a + (volatility * 1.5)):  # This if statement is to avoid very small fibs
            # tobe detected by the algorithm, If algorithm detects very small fibs it becomes difficult or
            # impossible in code case to put limit and stop order to make sense (i.e. algo cannot put oco because
            # the range is too small)
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
        return self.local_maximum_b, level2, upper_level, flag_a

    def find_c(self, z, level2, local_minimum, local_maximum):
        """
        This side takes tick data as an in put and finds the fractal low in between AB boundery in up ABCD swing in
        the data given
        input: array of five flots
        return: float (Value of fractal low)
        """
        i = 2  # initialize a variable to 2 for the calculation of fractal low
        flag_a = 2  # flag for algorithm to know where it is at the moment

        if self.c_above_b_flag == 1:  # function to handle situation when value goes above B boundary without making
            # fractal low in between A-B boundary
            print("Current price was above a B")
            print("will go to 1.270")
            flag_a = 0
            return self.local_minimum_C, flag_a

        if ((z[i]) - (z[i-1]) < 0) and ((z[i]) - (z[i-2]) < 0):
            if ((z[i+1]) - (z[i]) > 0) and ((z[i+2]) - (z[i]) > 0):
                if level2 > z[i] > local_minimum:  # find fractal low only if current value is in between A-B boundary
                    self.local_minimum_C = z[i]
                    flag_a = 3

                elif z[i] < local_minimum:  # if value goes below B in A-B boundary the fib is broken - flag_a = 0
                    # print("Fib broke")
                    flag_a = 0

                # push below given two condition tomorrow and add local_maximum as an input to the function find_c
                elif level2 < z[i] < local_maximum:  # no fractal low but the price is in between A-B boundary
                    pass
                    # print("searching for a good c") ######################

                elif z[i] > local_maximum:  # price did not make fractal low and went above B the B boundary
                    print("Above B")
                    print("will go to 1.270")
                    print("buy now")
                    flag_a = 0

                return self.local_minimum_C, flag_a
            return self.local_minimum_C, flag_a
        return self.local_minimum_C, flag_a

    def find_if_c_is_above_b(self, current_price, local_maximum, flag_a):
        """
        This function tracks value at each ticker and notifies if the value went above B without making fractal low
        withing A-B boundary

        return: bool (if value is above B or not)
        """

        if flag_a == 2:
            if current_price > local_maximum:
                print("Above B")
                print("will go to 1.270")
                print(f'buy now- current price: {current_price}')
                self.c_above_b_flag = 1
                return True
            else:
                return False
        else:
            return False

    def find_d(self, current_price, level2, upper_level, local_minimum):

        """
        This function tracks value at each ticker and notifies what the value is doing after making fractal low
        within the A-B boundary
        """

        flag_a = 3  # flag for algorithm to know where it is at the moment

        if upper_level > current_price > level2:
            # print("no D found") ######################
            print(current_price)
        elif current_price > upper_level:
            self.local_maximum_d = current_price
            flag_a = 0
            return flag_a
        elif level2 > current_price > local_minimum:
            # print("Looking for deeper c") ######################
            pass
        elif local_minimum > current_price:
            # print("fib broke D") ######################
            flag_a = 0
            return flag_a
        return flag_a


class DownFibABCD:

    def __init__(self, ):
        self.local_maximum_a = 0
        self.local_minimum_b = 0
        self.local_maximum_C = 0
        self.local_minimum_d = 0
        self.c_below_b_flag = 0

    def find_a(self, z):
        """
        This side takes tick data as an in put and finds the fractal high in the data given
        input: array of five flats
        return: float (Value of fractal low) amd int (flag)
        """

        i = 2  # initialize a variable to 2 for the calculation of fractal high (calculation can be seen in the main
        # log part of the code
        flag_a = 0

        if len(z) >= 5:  # if the length of input array is less grater than 5 use only last four terms of the array
            # for the analysis
            z = z[-5:]
        elif len(z) < 5:  # if the length  of the input array is less than five do no proceed as to find the fractal
            # low minimum number of points needed is 5
            return self.local_maximum_a, flag_a

        # ===== main logic =====

        if ((z[i]) - (z[i-1]) > 0) and ((z[i]) - (z[i-2]) > 0):
            if ((z[i+1]) - (z[i]) < 0) and ((z[i+2]) - (z[i]) < 0):
                self.local_maximum_a = z[i]
                print(self.local_maximum_a)
                flag_a = 1

        return self.local_maximum_a, flag_a

    def find_b(self, z, volatality, local_maximum_downfib_a):
        flag_a = 1
        if len(z) >= 5:
            z = z[-5:]
        elif len(z) < 5:
            return self.local_minimum_b, flag_a
        # flag = 5
        level2 = 0
        lower_level = 0
        i = 2
        if z[-1] < (local_maximum_downfib_a + (volatality * 1.5)):
            if ((z[i]) - (z[i - 1]) < 0) and ((z[i]) - (z[i - 2]) < 0):
                if ((z[i + 1]) - (z[i]) > 0) and ((z[i + 2]) - (z[i]) > 0):
                    # print("Found down fib b") #####################
                    self.local_minimum_b = z[i]
                    # print(self.local_minimum_b) #############
                    flag_a = 2

                    diff = local_maximum_downfib_a - self.local_minimum_b
                    level2 = self.local_minimum_b + 0.5 * diff
                    lower_level = self.local_minimum_b - (1.270 * diff)

                    return self.local_minimum_b, level2, lower_level, flag_a
            return self.local_minimum_b, level2, lower_level, flag_a
        return self.local_minimum_b, level2, lower_level, flag_a
