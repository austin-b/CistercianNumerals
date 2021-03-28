
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

        self.generate_points()

    def generate_points(self):
        pass

    def draw_stem(self):
        return [(51, 26), (51, 126)]

    def draw_ones(self, num):
        pass

    def draw_tens(self, num):
        pass

    def draw_hundreds(self, num):
        pass

    def draw_thousands(self, num):
        pass

    def draw_number(self, num):
        if not isinstance(num, int) or num < 0 or num > 9999:
            raise ValueError("Num must be an integer between 0 and 9999.")

        tens, ones = divmod(num, 10)
        hundreds, tens = divmod(tens, 10)
        thousands, hundreds = divmod(hundreds, 10)

        lines = []
        lines.append(self.draw_stem())

        return lines
