def inverse(a, n):
    t = 0
    newT = 1
    r = n
    newR = a

    while newR != 0:
        q = r // newR
        t, newT = newT, t - q * newT
        r, newR = newR, r - q * newR

    if r > 1:
        print("a is not invertible")
        return -1
    if t < 0:
        t = t + n

    return t

def gcd(a, b):
    m = a
    n = b
    if a < b:
        m, n = b, a
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n

class KnapsackCypto:
    def __init__(self):
        self.a = [2, 5, 18, 26, 82, 135, 280]
        self.q = 1209
        self.r = 1003
        self.r1 = inverse(self.r, self.q)

    def GeneratePublicKey(self):
        b = []
        for i in range(len(self.a)):
            b.append(self.a[i] * self.r % self.q)
        return b

    def Decript(self, value):
        str = ''
        newSum = value * self.r1 % self.q
        for i in range(len(self.a) - 1, -1, -1):
            if newSum >= self.a[i]:
                newSum -= self.a[i]
                str = '1' + str
            else:
                str = '0' + str
        return chr(int(str, 2))

class Encrypt:
    def __init__(self):
        self.b = []

    def SetPublicKey(self, keys):
        self.b = keys

    def Encrypt(self, char):
        dec = ord(char)
        bin_str = bin(dec)[2:]
        while len(bin_str) < 7:
            bin_str = '0' + bin_str
        result = 0
        for i in range(len(self.b)):
            if bin_str[i] == '1':
                result += self.b[i]
        return result

decryption = KnapsackCypto()
encryption = Encrypt()
encryption.SetPublicKey(decryption.GeneratePublicKey())

class Test:
    def __init__(self):
        self.decryption = KnapsackCypto()
        self.encryption = Encrypt()
        self.encryption.SetPublicKey(decryption.GeneratePublicKey())
        self.input = ''

    def SetPlainTest(self, input):
        self.input = input

    def EncryptTest(self):
        result = []
        for a in self.input:
            result.append(self.encryption.Encrypt(a))
        return result

    def DecryptCipher(self, cipher):
        result = ''
        for v in cipher:
            result += self.decryption.Decript(v)
        return result

test = Test()
test.SetPlainTest("For the love of Christ constraineth us; because we thus judge, that one died for all, therefore all died; and he died for all, that they that live should no longer live unto themselves, but unto him who for their sakes died and rose again.")
code = test.EncryptTest()
print(code)
print(test.DecryptCipher(code))

