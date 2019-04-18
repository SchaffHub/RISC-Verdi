// 
// Permission is hereby granted, free of charge, to any person
// obtaining a copy of this software and associated documentation
// files (the "Software"), to deal in the Software without restriction,
// including without limitation the rights to use, copy, modify, merge,
// publish, distribute, sublicense, and/or sell copies of the Software,
// and to permit persons to whom the Software is furnished to do so,
// subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be
// included in all copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
// NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
// HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
// WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
// DEALINGS IN THE SOFTWARE.
//

typedef unsigned char bool;
const bool true  = 1;
const bool false = 0;

typedef unsigned long uint32_t;

// A write to the address (top of SRAM) will end the simulation.
volatile uint32_t *const outputPort    = (uint32_t *)(0x3FFFF8);
volatile uint32_t *const endSimulation = (uint32_t *)(0x3FFFFC);

char license[] = 
    "Permission is hereby granted, free of charge, to any person "
    "obtaining a copy of this software and associated documentation "
    "files (the \"Software\"), to deal in the Software without restriction, "
    "including without limitation the rights to use, copy, modify, merge, "
    "publish, distribute, sublicense, and/or sell copies of the Software, "
    "and to permit persons to whom the Software is furnished to do so, "
    "subject to the following conditions: "
    "The above copyright notice and this permission notice shall be "
    "included in all copies or substantial portions of the Software.  "
    "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, "
    "EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF "
    "MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND "
    "NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT "
    "HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, "
    "WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, "
    "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER "
    "DEALINGS IN THE SOFTWARE.";

bool isCharInWord(char ch) {
    return (bool)(((ch >= 'a') & (ch <= 'z')) | ((ch >= 'A') & (ch <= 'Z')));
}

int countWords(char *text) {
    int numWords = 0;
    bool inWord = false;

    for (; *text; text++) {
        if (inWord && !isCharInWord(*text)) {
            numWords++;
            inWord = false;
        } else if (!inWord && isCharInWord(*text)) {
            inWord = true;
        }
    }
    if (inWord) {
        numWords++;
    }
    return numWords;
}

void printWord(char *text) {
    for (; *text & (*text != ' '); text++) {
        *outputPort = (uint32_t)(*text);
    }
}

void printString(char *text) {
    for (; *text; text++) {
        *outputPort = (uint32_t)(*text);
    }
}

void printInt(int num) {

    // Determine the number of digits.
    int digits  = 1;
    int divisor = 1;
    for (int tmpNum = num; tmpNum >= 10; digits++) {
        tmpNum /= 10;
        divisor *= 10;
    }

    // Now stream out by most significant digit.
    for (int tmpNum = num; digits > 0; digits--) {
        char ch = (char)(tmpNum / divisor) + '0';
        *outputPort = (uint32_t)(ch);
        tmpNum %= divisor;
        divisor /= 10;
    }
}

int printFibonacci(int count) {
    int f[2] = { 1, 1 };
    for (int i = 0; i < count; i++) {
        if (i < 2) {
            printInt(f[i]);
        } else {
            int newF = f[1] + f[0];
            printInt(newF);
            f[0] = f[1];
            f[1] = newF;
        }
        if (i != (count-1)) {
            printString(",");
        }
    }
}

void main() {
    int numWords = countWords(license);
    printString("Number of words in license: ");
    printInt(numWords);
    printString("; First 10 Fibonacci numbers are: ");
    printFibonacci(10);
    printString("; Test complete.");
    *endSimulation = 0;
}
