#Lookup Table Check

#  Created by Tiago Ferreira on 22/11/2015.
#  Copyright (c) 2015 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.


import time
import sys

valid = False
favouriteOptions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


while valid == False:
    favouriteNumber = int(input("Whats your favourite number from 0 to 9? "))
    if favouriteNumber in favouriteOptions:
        print("Valid... saving data.")
        time.sleep(0.5)
        valid = True
        sys.exit()
    else:
        print("Invalid, try again.")
