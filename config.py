class Student:

    def __init__(self, code, name, g1, g2):
        self.code = code
        self.name = name
        self.g1 = g1
        self.g2 = g2
        self.g = self.calc_grade()

        # Approve condition
        if self.g >= 6:
            self.apprv = "yes"
        else:
            self.apprv = "no"

    # Calculate final grade
    def calc_grade(self):
        avg = round((self.g1 + 2 * self.g2) / 3, 2)
        return avg

# Get a positive a positive integer
def get_positive_int(m):
    while True:
        value = input(m)
        try:
            value = int(value)
            if value > 0:
                break
            else:
                print("Must provide a positive integer.")
                continue
        except:
            print("Must provide a positive integer.")
            continue
    return value

# Get student grade
def get_grade(m):
    while True:
        value = input(m)
        try:
            value = float(value)
            if value >= 0 and value <= 10:
                break
            else:
                print("Must provide a valid grade.")
                continue
        except:
            print("Must provide a valid grade.")
            continue
    return value
