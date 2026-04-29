import os

class PowerSeparator:
    def __init__(self, source_file, double_file, triple_file):
        base = os.path.dirname(os.path.abspath(__file__))
        self.source_file = os.path.join(base, source_file)
        self.double_file = os.path.join(base, double_file)
        self.triple_file = os.path.join(base, triple_file)

    def process(self):
        src = open(self.source_file, "r")
        square = open(self.double_file, "w")
        cube = open(self.triple_file, "w")

        for line in src:
            num = int(line.strip())
            if num % 2 == 0:
                square.write(str(num ** 2) + "\n")
            else:
                cube.write(str(num ** 3) + "\n")
        
        src.close
        square.close
        cube.close
    
    def display_results(self):
        f = open(self.double_file, "r")
        even_results = sorted([int(line.strip()) for line in f])
        f.close()

        f = open(self.source_file, "r")
        all_nums = [int(line.strip()) for line in f]
        f.close()
        even_nums = sorted([n for n in all_nums if n % 2 == 0])
        odd_nums = sorted([n for n in all_nums if n % 2 != 0])

        f = open(self.triple_file, "r")
        odd_results = sorted([int(line.strip()) for line in f])
        f.close()

        print("--- Square of Even Numbers ---")
        print("Numbers used: ", ", ".join(str(n) for n in even_nums))
        print("Results:      ", ", ".join(str(n) for n in even_results))

        print()

        print("--- Cube of Odd Numbers ---")
        print("Numbers used: ", ", ".join(str(n) for n in odd_nums))
        print("Results:      ", ", ".join(str(n) for n in odd_results))

processor = PowerSeparator("integers.txt", "double.txt", "triple.txt")
processor.process()
processor.display_results()