#  Vigenere

#  Created by Tiago Ferreira on 17/11/2017.
#  Copyright (c) 2017 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import sys, string

def encrypt(alphabet, plaintext, key):
    ciphertext = ""
    for keyIndex in range(len(plaintext)):
        if plaintext[keyIndex] in alphabet:
            plainIndex = alphabet.index(plaintext[keyIndex])
            plainIndex += alphabet.index(key[keyIndex])
            plainIndex %= len(alphabet)
            ciphertext += alphabet[plainIndex]
        else:
            ciphertext += plaintext[keyIndex]
    return ciphertext

def decrypt(alphabet, ciphertext, key):
    plaintext = ""
    for keyIndex in range(len(ciphertext)):
        if ciphertext[keyIndex] in alphabet:
            cipherIndex = alphabet.index(ciphertext[keyIndex])
            cipherIndex -= alphabet.index(key[keyIndex])
            cipherIndex %= len(alphabet)
            plaintext += alphabet[cipherIndex]
        else:
            plaintext += ciphertext[keyIndex]
    return plaintext

def menu():
    alphabet = list(string.ascii_uppercase)
    print("Welcome! Here are your options: ")
    print()
    print("1. Encrypt data.")
    print("2. Decrypt data.")
    print()
    choice = int(input("Your selection (1, 2): "))
    print()

    if choice == 1:
        print("Encrypting it is.")
        plaintext = input("Please enter the plaintext: ").upper()
        key = input("Please enter the key: ").upper()
        print("Ciphertext: " + encrypt(alphabet, plaintext, key))
    elif choice == 2:
        print("Decrypting it is.")
        ciphertext = input("Please enter the ciphertext: ").upper()
        key = input("Please enter the key: ").upper()
        print("Plaintext: " + decrypt(alphabet, ciphertext, key))
    else:
        sys.exit()

menu()
