class Character_LCD_RGB_I2C:
    RIGHT_TO_LEFT = "RTL"
    LEFT_TO_RIGHT = "LTR"

    def __init__(self, i2c, columns, rows):
        self.i2c = i2c
        self.columns = columns
        self.rows = rows
        self._color = [0, 0, 0]
        self._message = ''

    def clear(self):
        print("Clearing LCD")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        print("Setting LCD color to {}".format(value))
        self._color = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        lines = value.split('\n')
        print("Setting LCD message:")
        print("╔"+"═"*self.columns+"╗")
        for i in range(0, self.rows):
            try:
                line = lines[i]
            except IndexError:
                line = " "
            print("║{:<{width}}║".format(line, width=self.columns))

        print("╚"+"═"*self.columns+"╝")
        self._message = value
