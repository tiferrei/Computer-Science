#  Algorithm Practise

#  Created by Tiago Ferreira on 28/09/2016.
#  Copyright (c) 2016 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

mark = []
maxMark = []

numberOfMarks = int(input("Enter number of marks: "))

for x in range(1, numberOfMarks):
    actualMark = int(input("Enter mark number " + str(mark) + ": "))
    actualMaxMark = int(input("Maximum mark for number " + str(mark) + ": "))
    mark.append(actualMark)
    maxMark.append(actualMaxMark)

for y in range(1, numberOfMarks):
    totalMark += mark[y-1]
    totalMaxMark += maxMark[y-1]

print("Total: " + str(totalMark) + " out of " + str(totalMaxMark) + ".")
