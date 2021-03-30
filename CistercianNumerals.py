
#######################
# Class for implementing and drawing aravis numerals.
#######################

from math import ceil, floor

class CistercianNumeralGenerator:
    """
        Class for generating Cistercian numerals from Arabic numerals. Can only be used to generate numbers 1-9999.

        width:      x-axis
        height:     y-axis
        flipped:    set to true if origin is at bottom left
        horizontal: set to true for numerals generated horizontally
        padx:       x-axis padding
        pady:       y-axis padding
    """

    def __init__(self, width, height, flipped=False, horizontal=False, padx=0, \
                 pady=0):
        """
            width:      x-axis
            height:     y-axis
            flipped:    set to true if origin is at bottom left
            horizontal: set to true for numerals generated horizontally
            padx:       x-axis padding
            pady:       y-axis padding
        """
        self.width = width
        self.height = height
        self.flipped = flipped
        self.horizontal = horizontal
        self.padx = padx
        self.pady = pady

        self.generate_points()


    # TODO: make a diagram for how these are spread out
    def generate_points(self):
        """Should not be called directly, determines points used for number generation."""
        if self.horizontal:
            if self.flipped:
                ones_hundreds = self.height - self.pady
                tens_thousands = self.pady
            else:
                ones_hundreds = self.pady
                tens_thousands = self.height - self.pady

            centerline = ceil((ones_hundreds + tens_thousands)/2)

            a_line = self.padx
            d_line = self.width - self.padx
            b_line = floor(a_line + ((d_line - a_line) * .35))
            c_line = ceil(a_line + ((d_line - a_line) * .65))

            self.stem_a = (a_line, centerline)
            self.stem_b = (b_line, centerline)
            self.stem_c = (c_line, centerline)
            self.stem_d = (d_line, centerline)

            self.ones_a = (a_line, ones_hundreds)
            self.ones_b = (b_line, ones_hundreds)
            self.hundreds_c = (c_line, ones_hundreds)
            self.hundreds_d = (d_line, ones_hundreds)

            self.tens_a = (a_line, tens_thousands)
            self.tens_b = (b_line, tens_thousands)
            self.thousands_c = (c_line, tens_thousands)
            self.thousands_d = (d_line, tens_thousands)
        else:
            ones_hundreds = self.width - self.padx
            tens_thousands = self.padx
            centerline = ceil((ones_hundreds + tens_thousands)/2)

            if self.flipped:
                a_line = self.height - self.pady
                d_line = self.pady
            else:
                a_line = self.pady
                d_line = self.height - self.pady

            b_line = floor(a_line + ((d_line - a_line) * .35))
            c_line = ceil(a_line + ((d_line - a_line) * .65))

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
        """Returns set of points used to draw stem of numeral."""
        return (self.stem_a, self.stem_d)


    def draw_ones(self, num):
        """Returns set of points used to draw ones digit of numeral."""
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
        """Returns set of points used to draw tens digit of numeral."""
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
        """Returns set of points used to draw hundreds digit of numeral."""
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
        """Returns set of points used to draw thousands digit of numeral."""

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
        """
        Returns list of tuples of points to draw lines of form: [((x1,y1),(x2,y2)), ((x1,y1),(x2,y2)), ...]
        """
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

        return finalized_lines
