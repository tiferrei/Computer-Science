#Password Manager

#  Created by Tiago Ferreira on 26/02/2016.
#  Copyright (c) 2016 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import sys

username = input("Add username: ")
password = input("Add password: ")

with open("Username.txt", mode="a", encoding="utf-8") as writeUsernameFile: ##initialize file in append mode
    writeUsernameFile.write(username + "\n")

with open("Password.txt", mode="a", encoding="utf-8") as writePasswordFile: ##initialize file in append mode
    writePasswordFile.write(password + "\n")

username = input("Username: ")
password = input("Password: ")

with open("Username.txt", mode="r", encoding="utf-8") as readUsernameFile: ##initialize file in append mode
    for line in readUsernameFile:
        line = line.rstrip("\n")
        if line == username:
            with open("Password.txt", mode="r", encoding="utf-8") as readPasswordFile: ##initialize file in append mode
                line = line.rstrip("\n")
                if line == password:
                    print("User logged in")
                    sys.exit()
    print("Login incorrect")
