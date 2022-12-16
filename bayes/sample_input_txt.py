class SampleInputTXT():
    def generate_sample(self) -> bool:
        current_path = 'example_bayesnet.txt'
        file = """
        5, B, E, A, J, M
        B, +b, -b
        E, +e, -e
        A, +a, -a
        J, +j, -j
        M, +m, -m
        B |
        +b, 0.001
        -b, 0.999
        E |
        +e, 0.002
        -e, 0.998
        A | B,E
        +b, +e, +a, 0.95
        +b, +e, -a, 0.05
        +b, -e, +a, 0.94
        +b, -e, -a, 0.06
        -b, +e, +a, 0.29
        -b, +e, -a, 0.71
        -b, -e, +a, 0.001
        -b, -e, -a, 0.999
        J | A
        +a, +j, 0.9
        +a, -j, 0.1
        -a, +j, 0.05
        -a, -j, 0.95
        M | A
        +a, +m, 0.7
        +a, -m, 0.3
        -a, +m, 0.01
        -a, -m, 0.99
        Query: P( B=+b| J=+j)
        """
        print(file)
        print("-"*25)
        print(f"visit for more information: https://github.com/srajan-kiyotaka/bayes_Net_Sample")
        return True

if __name__ == '__main__':
    SampleInputTXT().generate_sample()
