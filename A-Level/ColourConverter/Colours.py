#  Colour Converter

#  Created by Tiago Ferreira on 25/01/2018.
#  Copyright (c) 2018 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

def getRGB():
    red = int(input("Please enter the Red RGB value: "))
    green = int(input("Please enter the Green RGB value: "))
    blue = int(input("Please enter the Blue RGB value: "))
    return [red, green, blue]

def readDB():
    colours = []
    with open("Colours.txt", 'r') as db:
        for line in db:
            colours.append(line.rstrip('\n').split(","))
    return colours

def RGBToBin(RGB):
    red = '{0:08b}'.format(RGB[0])
    green = '{0:08b}'.format(RGB[1])
    blue = '{0:08b}'.format(RGB[2])
    return red + green + blue

def RGBToHex(RGB):
    red = "%0.2X" % RGB[0]
    green = "%0.2X" % RGB[1]
    blue = "%0.2X" % RGB[2]
    return "#" + red + green + blue

def IntToHex(integer):
    return hex(integer).lstrip("0x")

def getColourName(hexCode):
    colours = readDB()
    colourCodes = []
    for colour in colours:
        colourCodes.append(int(colour[1].lstrip("#"), 16))
        if colour[1] == hexCode:
            return [colour[0]]
    intCode = int(hexCode.lstrip("#"), 16)
    closestColour = min(colourCodes, key=lambda x:abs(x - intCode))
    closestColourIndex = colourCodes.index(closestColour)
    if closestColour > intCode:
        return [colours[closestColourIndex][0], colours[closestColourIndex + 1][0]]
    else:
        return [colours[closestColourIndex - 1][0], colours[closestColourIndex][0]]

def main():
    RGB = getRGB()
    print("RGB:")
    print("    RED: " + str(RGB[0]))
    print("    GREEN: " + str(RGB[1]))
    print("    BLUE: " + str(RGB[2]))
    print("HEX: " + RGBToHex(RGB))
    print("BINARY: " + RGBToBin(RGB))
    names = getColourName(RGBToHex(RGB))
    if len(names) == 1:
        print("COLOUR NAME: " + names[0])
    else:
        print("COLOUR NAME: Something between " + names[0] + " and " + names[1])

main()
