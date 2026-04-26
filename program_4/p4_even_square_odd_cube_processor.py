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
        print("--- Square of Even Numbers ---")
        f = open(self.double_file, "r")
        print(f.read())
        f.close

        print("--- Cube of Odd Numbers ---")
        f = open(self.triple_file, "r")
        print(f.read())
        f.close

processor = PowerSeparator("integers.txt", "double.txt", "triple.txt")
processor.process()
processor.display_results()