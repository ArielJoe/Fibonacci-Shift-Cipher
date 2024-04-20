def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def fibShiftCipher(msg):
    encoded = ''
    cnt = 1
    for char in msg:
        unicode = ord(char)
        shift = fib(cnt)

        unicodeShift = unicode + shift

        while unicodeShift > 90:
            unicodeShift -= 26

        encoded += chr(unicodeShift)

        cnt += 1

    if msg.islower():
        return encoded.lower()
    return encoded.upper()

def main():
    msg = input('Message : ')
    print(f'Encoded : {fibShiftCipher(msg)}')

if __name__ == '__main__':
    main()