#Function Challenge

#  Created by Tiago Ferreira on 08/02/2016.
#  Copyright (c) 2016 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

def Average():
    NumberOfNumbers = int(input("How many numbers do you want to calculate? "))
    NumArray = []
    for x in range(NumberOfNumbers):
        Number = float(input("Number: "))
        NumArray.append(Number)
    Total = 0
    for i in range(NumberOfNumbers):
        Total = Total + NumArray[(i-1)]
    Total = Total / NumberOfNumbers
    print("Your average is: "+ str(Total))

Average()
