#Random Number Input

#  Created by Tiago Ferreira on 05/11/2015.
#  Copyright (c) 2015 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.




import random
import sys
import time

NumberOne = random.randint(1,5000)
NumberTwo = random.randint(1,5000)
Again = True

while Again == True:

    Operation = input("Which operation do you want to use? (+, -, :, x)")

    if Operation == "+":
        total = (NumberOne + NumberTwo)
        print("Your random number is: " + str(total))
    elif Operation == "-":
        total = (NumberOne - NumberTwo)
        print("Your random number is: " + str(total))
    elif Operation == ":":
        total = (NumberOne / NumberTwo)
        print("Your random number is: " + str(total))
    elif Operation == "x":
        total = (NumberOne * NumberTwo)
        print("Your random number is: " + str(total))

    AgainYN = input("Do you want to do another operation? (YES, NO)")
    if AgainYN == "YES":
        time.sleep(1)
    else:
        break
        sys.exit()
