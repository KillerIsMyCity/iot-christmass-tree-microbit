serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    inp = _py.py_string_split(serial.readUntil(serial.delimiters(Delimiters.NewLine)), ",")
ledNum = parseInt(inp[0])
    RedClr = parseInt(inp[1])
    GreenClr = parseInt(inp[2])
    BlueClr = parseInt(inp[3])
    strip.setPixelColor(Math.trunc(ledNum), neopixel.rgb(Math.trunc(RedClr), Math.trunc(GreenClr), Math.trunc(BlueClr)))
    serial.writeLine("---------------" + "\nLedNumber:" + ("" + ledNum) + "\nRed: " + ("" + RedClr) + "\nGreen: " + ("" + GreenClr) + "\nBlue: " + ("" + BlueClr) + "\n---------------")
})
let BlueClr = 0
let GreenClr = 0
let RedClr = 0
let ledNum = 0
let strip: neopixel.Strip = null
let inp2: number[] = []
let inp : string[] = []
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate115200
)
strip = neopixel.create(DigitalPin.P1, 50, NeoPixelMode.RGB_RGB)
basic.showLeds(`
    . . . . .
    # . # . .
    # # . # .
    # . # . .
    . . . . .
    `)
strip.showColor(neopixel.colors(NeoPixelColors.Green))
basic.pause(500)
strip.showColor(neopixel.colors(NeoPixelColors.Black))
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
