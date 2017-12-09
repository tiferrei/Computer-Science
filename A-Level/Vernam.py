#  Vernam

#  Created by Tiago Ferreira on 30/11/2017.
#  Copyright (c) 2017 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import base64

def generateB64OTP(length):
    print("Generating truly random OTP for your plaintext...")
    b64OTP = open("/dev/urandom","rb").read(length + 8)
    b64OTP = base64.b64encode(b64OTP).decode()
    b64OTP = b64OTP[0:length]
    print("Your OTP is: " + b64OTP)
    return b64OTP

def encodeToB64(string):
    return base64.b64encode(str.encode(string)).decode()

def decodeFromB64(string):
    return base64.b64decode(str.encode(string)).decode()

def encrypt(plaintext):
    OTP = generateB64OTP(len(plaintext))
    ciphertext = ""
    for charIndex in range(len(plaintext)):
        ciphertext += chr(ord(OTP[charIndex]) ^ ord(plaintext[charIndex]))
    ciphertext = encodeToB64(ciphertext)
    return ciphertext

def decrypt(OTP, ciphertext):
    plaintext = ""
    ciphertext = decodeFromB64(ciphertext)
    for charIndex in range(len(ciphertext)):
        plaintext += chr(ord(OTP[charIndex]) ^ ord(ciphertext[charIndex]))
    return plaintext

def menu():
    print("welcome. Please select an option.")
    print("1. Encrypt data.")
    print("2. Decrypt data.")
    choice = input("Selection: ")
    if choice == "1":
        print("Encrypted file saved to: " + encrypt(input("Please enter the file path to encrypt: ")))
    else:
        print("Decrypted file saved to: " + decrypt(input("Please enter the OTP: "), input("Please enter the cipher file path to decrypt: ")))

menu()
