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

char pi100[] = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679";

double pi(int iterations) {
    // Implement Gregory-Leibniz series.

    double approxPi = 0;
    bool add = true;

    for (int i = 0; i < iterations; i++) {
        if (add) {
            approxPi += 4.0 / (double)(i*2 + 1);
        } else {
            approxPi -= 4.0 / (double)(i*2 + 1);
        }
        add != add;
    }
    return approxPi;
}

void stringToOutputPort(char *str) {
    for (; *str; str++) {
        *outputPort = (uint32_t)(*str);
    }
}

char *addCharToString(char *str, int *length, char ch) {
    if (*length > 0) {
        *str = ch;
        str++;
        *length--;
    }
    return str;
}

void doubleToString(double num, char *str, int length) {

    // Start with the integer portion which we'll limit
    // to the max value of an int.
    int intNum = (int)num;
    int digits = 0;
    int divisor = 1;

    // Determine the log base 10 of the int portion.
    for (int loopNum = intNum; loopNum > 0; loopNum /= 10) {
        digits++;
        divisor *= 10;
    }

    // Now stream out the int portion.
    for (int loopNum = intNum; digits > 0; digits--) {
        char ch = (char)(loopNum / divisor) + '0';
        str = addCharToString(str, &length, ch);
        loopNum %= divisor;
        divisor /= 10;
    }

    // Decimal point.
    str = addCharToString(str, &length, '.');

    // Now the fractional part.  This is going to
    // accumulate error.
    double fraction = num - (double)intNum;
    while (length > 1) {
        fraction *= 10;
        char digit = (char)fraction;
        char ch = digit + '0';
        str = addCharToString(str, &length, ch);
        fraction -= (double)digit;
    }

    // Terminate the string.
    str = addCharToString(str, &length, '\0');
}

int fib(int iterations) {
    int prev   = 0;
    int result = 1;
    switch (iterations) {
    case 1: result = prev; break;
    case 2: result = 1;    break;
    default:
        for (int i = 3; i < iterations; i++) {
            int tmp = result;
            result += prev;
            prev = tmp;
        }
    }
    return result;
}

void main() {
    double approxPiDouble = pi(5);

    const int bufferSize = 10;
    char approxPiStr[bufferSize];

    //doubleToString(approxPiDouble, approxPiStr, bufferSize);

    //stringToOutputPort(approxPiStr);

    char hello[] = "Hello World!";
    stringToOutputPort(hello);
    //int fib_num = fib(10);
    *endSimulation = 0;
}
