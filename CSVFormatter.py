#CSV Formatter

#  Created by Tiago Ferreira on 25/04/2016.
#  Copyright (c) 2015 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import csv

states = []
statesPop = 0

with open ("USStates.txt") as csvfile:
    statesCsv = csv.reader(csvfile, delimiter = ",")
    for row in statesCsv:
        states.append(row)
        
listLength = len(states)

print("--------------------------------------")
for i in range(listLength):
    print("|{0:15}|{1:4}|{2:15}|".format(states[i][0], states[i][1].center(4), states[i][3]))
print("--------------------------------------")

for x in range(listLength):
    statesPop = statesPop + int(states[x][4])

print("Total population: " + str(statesPop))
