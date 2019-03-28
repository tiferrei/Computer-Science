#  ShuntingYard

#  Created by Tiago Ferreira on 14/02/2019.
#  Copyright (c) 2019 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import string

def tokenize(inputString):
    tokens = []
    for char in inputString:
        if char != " ":
            tokens.append(char)
    return tokens

def shuntingYard(inputTokens):
    operatorStack = []
    outputQueue = []
    for token in inputTokens:
        if token in list(string.ascii_lowercase):
            outputQueue.append(token)
        elif token in ["-", "+", "*", "/"]:
            while len(operatorStack) != 0 and ((token in ["-", "+"] and operatorStack[-1] in ["*", "/"])
                                            or (token in ["-", "+", "*", "/"] and operatorStack[-1] == ")")):
                outputQueue.append(operatorStack.pop())
            operatorStack.append(token)
        elif token == "(":
            operatorStack.append(token)
        elif token == ")":
            while len(operatorStack) != 0 and operatorStack[-1] != "(":
                outputQueue.append(operatorStack.pop())
            if len(operatorStack) != 0 and operatorStack[-1] == "(":
                operatorStack.pop()
    for operator in reversed(operatorStack):
        outputQueue.append(operator)
    return outputQueue

if __name__ == '__main__':
    inputTokens = tokenize(input("Please enter infix expression: "))
    outputTokens = shuntingYard(inputTokens)
    RPNString = ' '.join(outputTokens)
    print("RPN equivalent expression: " + RPNString)
