import os

class SampleInputTXT():
    def generate_sample(self) -> bool:
        current_path = os.getcwd() + '/sample/example_bayesnet.txt'
        with open(current_path, 'r') as f:
            print(f.read())
        print("-"*25)
        print(f"See the txt file for more information: {current_path}")
        print("-"*25)
        print(f"visit for more information: https://github.com/srajan-kiyotaka/bayes_Net_Sample")
        return True

if __name__ == '__main__':
    SampleInputTXT().generate_sample()
