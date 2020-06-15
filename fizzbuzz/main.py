def run_fizzbuzz(multiples):
    for i in range(1, 101):
        output = ''
        for multiple in multiples:
            if i % multiple == 0:
                output += str(multiples[multiple])
        if output == '':
            output += str(i)
        print(output)


def main():
    multiples = {
    3 : 'fizz',
    5 : 'buzz'
    }
    run_fizzbuzz(multiples)


if __name__ == '__main__':
    main()