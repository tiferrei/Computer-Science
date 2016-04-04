#Consistency Check

#  Created by Tiago Ferreira on 18/11/2015.
#  Copyright (c) 2015 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.


DataIsCorrect = False
while DataIsCorrect == False:
    Gender = input("What's your gender? (M / F): ")
    Title = input("What's your title? (MR / MRS / MISS): ")

    if Gender == "M" and Title == "MR":
        print("Your data is valid, thank you for completing this survey.")
        DataIsCorrect = True
    elif Gender == "M" and Title == "MRS":
        print("Your data is invalid, please revise it.")
    elif Gender == "M" and Title == "MISS":
        print("Your data is invalid, please revise it.")
    elif Gender == "F" and Title == "MR":
        print("Your data is invalid, please revise it.")
    elif Gender == "F" and Title == "MRS":
        print("Your data is valid, thank you for completing this survey.")
        DataIsCorrect = True
    elif Gender == "F" and Title == "MISS":
        print("Your data is valid, thank you for completing this survey.")
        DataIsCorrect = True
