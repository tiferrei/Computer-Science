#Double Entry Check

#  Created by Tiago Ferreira on 22/11/2015.
#  Copyright (c) 2015 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import sys
import time

passwordMatches = False

while passwordMatches == False:
    password = input("New password: ")
    CheckPassword = input("Re-enter new password: ")

    if password == CheckPassword:
        print("Password changed.")
        time.sleep(0.5)
        passwordMatches = True
        sys.exit()
    else:
        print("Passwords don't match, please try again.")
        time.sleep(0.5)
