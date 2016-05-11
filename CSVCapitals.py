#CSV Capitals

#  Created by Tiago Ferreira on 11/05/2016.
#  Copyright (c) 2016 Tiago Ferreira and Alex Butler

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import csv
capitalQuestions = []
points = 0
with open ("Capitals.txt") as csvfile:
    capitalsCsv = csv.reader(csvfile, delimiter = ",")
    for row in capitalsCsv:
        capitalQuestions.append(row)
numberOfQuestions = len(capitalQuestions)
for x in range(numberOfQuestions):
    print(capitalQuestions[x][1])
    print()
    print("A -> " + capitalQuestions[x][3])
    print("B -> " + capitalQuestions[x][4])
    print("C -> " + capitalQuestions[x][5])
    print("D -> " + capitalQuestions[x][6])
    userChoice = input("Answer (A, B, C, D): ")
    userChoice = userChoice.upper()
    if userChoice == capitalQuestions[x][2]:
        print("Correct!")
        points = points + 1
    else:
        print("Wrong!")
print("You scored " + str(points) + " points!")
