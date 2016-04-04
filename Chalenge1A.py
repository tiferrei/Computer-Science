#Chalenge 1A

#  Created by Tiago Ferreira on 12/11/2015.
#  Copyright (c) 2015 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.


animals = []

num = 1 + int(input("How many animals do you want to add? "))

for n in range(1,num):
    animalToAdd = input("which animal do you want to add? ")
    animals.append(animalToAdd)


Reversed = input("Do you want your list reversed? (YES, NO): ")

if Reversed == "YES":

    animals.reverse()
    print(animals)
else:

    print(animals)

numberOnArray = int(input("Choose a number from 1 to " + str(num) + ". "))

print(animals[numberOnArray])
