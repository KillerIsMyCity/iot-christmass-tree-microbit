def on_data_received():
    global inp, ledNum, RedClr, GreenClr, BlueClr
    inp = serial.read_until(serial.delimiters(Delimiters.NEW_LINE)).split(",")
    ledNum = int(inp[0])
    RedClr = int(inp[1])
    GreenClr = int(inp[2])
    BlueClr = int(inp[3])
    strip.set_pixel_color(int(ledNum),
        neopixel.rgb(int(RedClr),
            int(GreenClr),
            int(BlueClr)))
    serial.write_line("---------------" + "\nLedNumber:" + ("" + str(ledNum)) + "\nRed: " + ("" + str(RedClr)) + "\nGreen: " + ("" + str(GreenClr)) + "\nBlue: " + ("" + str(BlueClr)) + "\n---------------")
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

BlueClr = 0
GreenClr = 0
RedClr = 0
ledNum = 0
strip: neopixel.Strip = None
inp: List[str] = []
inp2: List[number] = []
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)
strip = neopixel.create(DigitalPin.P1, 50, NeoPixelMode.RGB_RGB)
basic.show_leds("""
    . . . . .
        # . # . .
        # # . # .
        # . # . .
        . . . . .
""")
strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
basic.pause(500)
strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")