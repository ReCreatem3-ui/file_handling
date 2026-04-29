import os
import time
import sys

class Spacer:
    def __init__(self):
        pass

    def one_space(self):
        print()

    def light_space(self):
        for i in range(2):
            print()

    def medium_space(self):
        for i in range(3):
            print()

    def heavy_space(self):
        for i in range(5):
            print()

    def clear_screen(self):
        for i in range(35):
            print()

    def custom_space(self, lines=1):
        for i in range(lines):
            print()

    def line_separator(self):
        print("-" * 50)

    def equals_separator(self):
        print("=" * 50)

class Elements:
    def loading_bar(self, label="", total=26, duration=2):
        for i in range(total + 1):
            bar = '▄' * i + ' ' * (total - i)
            percent = int((i / total) * 100)
            sys.stdout.write(f'\r{label}{bar} {percent}%')
            sys.stdout.flush()
            time.sleep(duration / total)
        print()
    
    def slowtype(self, text, duration):
        delay = duration / len(text) if len(text) > 0 else 0
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

class FileWriter:
    def __init__(self, output_file):
        base = os.path.dirname(os.path.abspath(__file__))
        self.output_file = os.path.join(base, output_file)
        self.element = Elements()
        self.space = Spacer()

    def write_lines(self):
        f = open(self.output_file, "w")
        more = "y"

        while more.lower() == "y":
            self.space.clear_screen()
            line = input("Enter a line: ")
            f.write(line + "\n")
            self.space.one_space()
            more = input("Add more lines? (y/n): ")

        f.close()
        self.space.clear_screen()
        print("Saved to", self.output_file)
    
    def append_lines(self):
        f = open(self.output_file, "a")
        more = "y"

        while more.lower() == "y":
            self.space.clear_screen()
            line = input("Enter a line: ")
            f.write(line + "\n")
            self.space.one_space()
            more = input("Add more lines? (y/n): ")

        f.close()
        self.space.clear_screen()
        print("Appended to", self.output_file)

    def display_contents(self):
        self.space.clear_screen()
        f = open(self.output_file, "r")
        content = f.read()
        f.close()

        self.space.clear_screen()
        print(f"--- {self.output_file} ---")
        self.space.one_space()

        for line in content.splitlines():
            self.element.slowtype(" " * 60 + line.center(60), duration=max(0.5, len(line) / 10))

class SelectMenu:
    def __init__(self):
        self.space = Spacer()
        self.element = Elements()

        while True:
            self.space.clear_screen()
            print("Select mode:")
            print("  [1] Create new file")
            print("  [2] Open existing file")
            print("  [3] Exit")
            mode = input("Enter choice: ")

            if mode == "1":
                self.space.clear_screen()
                filename = input("Enter new filename (e.g. mylife.txt): ")
                writer = FileWriter(filename)
                writer.write_lines()
                writer.display_contents()
                break

            elif mode == "2":
                self.space.clear_screen()
                filename = input("Enter existing filename (e.g. mylife.txt): ")
                writer = FileWriter(filename)

                if not os.path.exists(writer.output_file):
                    self.space.clear_screen()
                    self.element.slowtype(f"File '{filename}' not found. Try again.")
                    time.sleep(2)
                    continue
                
                self.space.clear_screen()
                print("\nFile found. What do you want to do?")
                print("  [1] Read only")
                print("  [2] Append new lines")
                action = input("Enter choice: ")

                if action == "1":
                    writer.display_contents()
                elif action == "2":
                    writer.display_contents()
                    writer.append_lines()
                    writer.display_contents()
                break

            elif mode == "3":
                self.space.clear_screen()
                self.element.loading_bar("Exiting ")
                break
            else:
                self.space.clear_screen()
                print("Invalid choice. Enter 1, 2, or 3 only.")
                time.sleep(1.5)

selection = SelectMenu()
filename = input("Enter output filename: ")
writer = FileWriter(filename)
writer.write_lines()
writer.display_contents()

