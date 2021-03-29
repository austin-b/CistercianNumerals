
#######################
# Class for implementing and drawing aravis numerals.
#######################

class CistercianNumeralGenerator:
    """Class for implementing and drawing arabic numerals."""

    def __init__(self, width, height, flipped=False, horizontal=False, padx=0, \
                 pady=0):
        self.width = width
        self.height = height
        self.flipped = flipped
        self.horizontal = horizontal
        self.padx = padx
        self.pady = pady

        self.generate_points()


    # TODO: make a diagram for how these are spread out
    def generate_points(self):

        centerline = 51
        ones_hundreds = 88
        tens_thousands = 13

        a_line = 26
        b_line = 56
        c_line = 96
        d_line = 126

        # grouping by columns
        self.stem_a = (centerline, a_line)
        self.stem_b = (centerline, b_line)
        self.stem_c = (centerline, c_line)
        self.stem_d = (centerline, d_line)

        self.ones_a = (ones_hundreds, a_line)
        self.ones_b = (ones_hundreds, b_line)
        self.hundreds_c = (ones_hundreds, c_line)
        self.hundreds_d = (ones_hundreds, d_line)

        self.tens_a = (tens_thousands, a_line)
        self.tens_b = (tens_thousands, b_line)
        self.thousands_c = (tens_thousands, c_line)
        self.thousands_d = (tens_thousands, d_line)


    def draw_stem(self):
        return (self.stem_a, self.stem_d)


    def draw_ones(self, num):
        if num == 1:
            return (self.stem_a, self.ones_a)
        elif num == 2:
            return (self.stem_b, self.ones_b)
        elif num == 3:
            return (self.stem_a, self.ones_b)
        elif num == 4:
            return (self.stem_b, self.ones_a)
        elif num == 5:
            return [(self.stem_a, self.ones_a), (self.stem_b, self.ones_a)]
        elif num == 6:
            return (self.ones_a, self.ones_b)
        elif num == 7:
            return [(self.stem_a, self.ones_a), (self.ones_a, self.ones_b)]
        elif num == 8:
            return [(self.stem_b, self.ones_b), (self.ones_a, self.ones_b)]
        elif num == 9:
            return [(self.stem_a, self.ones_a), (self.stem_b, self.ones_b), \
                    (self.ones_a, self.ones_b)]


    def draw_tens(self, num):
        if num == 1:
            return (self.stem_a, self.tens_a)
        elif num == 2:
            return (self.stem_b, self.tens_b)
        elif num == 3:
            return (self.stem_a, self.tens_b)
        elif num == 4:
            return (self.stem_b, self.tens_a)
        elif num == 5:
            return [(self.stem_a, self.tens_a), (self.stem_b, self.tens_a)]
        elif num == 6:
            return (self.tens_a, self.tens_b)
        elif num == 7:
            return [(self.stem_a, self.tens_a), (self.tens_a, self.tens_b)]
        elif num == 8:
            return [(self.stem_b, self.tens_b), (self.tens_a, self.tens_b)]
        elif num == 9:
            return [(self.stem_a, self.tens_a), (self.stem_b, self.tens_b), \
                    (self.tens_a, self.tens_b)]


    def draw_hundreds(self, num):
        if num == 1:
            return (self.stem_d, self.hundreds_d)
        elif num == 2:
            return (self.stem_c, self.hundreds_c)
        elif num == 3:
            return (self.stem_d, self.hundreds_c)
        elif num == 4:
            return (self.stem_c, self.hundreds_d)
        elif num == 5:
            return [(self.stem_d, self.hundreds_d), (self.stem_c, self.hundreds_d)]
        elif num == 6:
            return (self.hundreds_c, self.hundreds_d)
        elif num == 7:
            return [(self.stem_d, self.hundreds_d), (self.hundreds_c, self.hundreds_d)]
        elif num == 8:
            return [(self.stem_c, self.hundreds_c), (self.hundreds_c, self.hundreds_d)]
        elif num == 9:
            return [(self.stem_c, self.hundreds_c), (self.stem_d, self.hundreds_d), \
                    (self.hundreds_c, self.hundreds_d)]


    def draw_thousands(self, num):
        if num == 1:
            return (self.stem_d, self.thousands_d)
        elif num == 2:
            return (self.stem_c, self.thousands_c)
        elif num == 3:
            return (self.stem_d, self.thousands_c)
        elif num == 4:
            return (self.stem_c, self.thousands_d)
        elif num == 5:
            return [(self.stem_d, self.thousands_d), (self.stem_c, self.thousands_d)]
        elif num == 6:
            return (self.thousands_c, self.thousands_d)
        elif num == 7:
            return [(self.stem_d, self.thousands_d), (self.thousands_c, self.thousands_d)]
        elif num == 8:
            return [(self.stem_c, self.thousands_c), (self.thousands_c, self.thousands_d)]
        elif num == 9:
            return [(self.stem_c, self.thousands_c), (self.stem_d, self.thousands_d), \
                    (self.thousands_c, self.thousands_d)]


    def draw_number(self, num):
        if not isinstance(num, int) or num < 0 or num > 9999:
            raise ValueError("Num must be an integer between 0 and 9999.")

        tens, ones = divmod(num, 10)
        hundreds, tens = divmod(tens, 10)
        thousands, hundreds = divmod(hundreds, 10)

        lines = []
        lines.append(self.draw_stem())
        if ones > 0: lines.append(self.draw_ones(ones))
        if tens > 0: lines.append(self.draw_tens(tens))
        if hundreds > 0: lines.append(self.draw_hundreds(hundreds))
        if thousands > 0: lines.append(self.draw_thousands(thousands))

        finalized_lines = []
        for i in lines:
            if isinstance(i, list):
                for j in i:
                    finalized_lines.append(j)
            else:
                finalized_lines.append(i)


        print(finalized_lines)

        return finalized_lines
