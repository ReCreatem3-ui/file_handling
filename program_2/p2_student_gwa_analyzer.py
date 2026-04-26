import os

class GWAFinder:
    def __init__(self, source_file):
        base = os.path.dirname(os.path.abspath(__file__))
        self.source_file = os.path.join(base, source_file)
        self.top_name = ""
        self.top_gwa = float("inf")

    def find_highest(self):
        f = open(self.source_file, "r")

        for line in f:
            parts = line.strip().split(",")
            name = parts[0]
            gwa = float(parts[1])
            if gwa < self.top_gwa:
                self.top_gwa = gwa
                self.top_name = name
        f.close()
 
    def display_result(self):
        print("Student with the Highest GWA:")
        print(f"  Name : {self.top_name}")
        print(f"  GWA  : {self.top_gwa}")
 
 
finder = GWAFinder("students_with_gwa.txt")
finder.find_highest()
finder.display_result()