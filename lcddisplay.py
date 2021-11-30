# Class simplifying working with adafurit LCD display
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd


class LCD:
    # since there's only one LCD display, it can be a global parameter
    lcd_columns = 16
    lcd_rows = 2
    lcd = character_lcd.Character_LCD_RGB_I2C(
        busio.I2C(board.SCL, board.SDA),
        lcd_columns, lcd_rows)

    def __init__(self):
        """Clear the previous message and switch on the display"""
        self.clear()
        self.on()

    def display_message(self, message, clear=True):
        # TODO: check that message fits in the dimentions
        # and try to display it, using scrolling if needed
        if (clear):
            self.clear()
        self.lcd.message = message

    def on(self):
        """Turning LCD backlight on

        Any previously set text will re-appear"""
        self.lcd.color = [100, 100, 100]

    def off(self):
        """Turning LCD backlight off

        This method does not clear the text
        """
        self.lcd.color = [0, 0, 0]

    def clear(self):
        self.lcd.clear()
