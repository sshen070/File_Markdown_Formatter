import sys
from pathlib import Path
from markdown_formatter_sshen070.file_formatting_algorithm import markdown_cleaner
from markdown_formatter_sshen070.string_formatting_algorithm import str_markdown_cleaner


# Task 1: Accepts a string and returns a formatted string
def main_string(arg_string: str) -> None:
    print("\n")
    print("Original String:")
    print(arg_string)

    print("\n")
    print("Formatted String:")
    print(str_markdown_cleaner(arg_string))


# Task 2: Accepts input and output file names, reads from input file, writes to output file
def main_files(arg_file1: str, arg_file2: str) -> None:

    input_file = Path(arg_file1)
    output_file = Path(arg_file2)

    main_dir = Path(__file__).resolve().parent.parent.parent
    print(f"Source Directory: {main_dir}")

    # Files located in tests/ folder
    input_path = main_dir / "tests" / input_file
    output_path = main_dir / "tests" / output_file

    # Run cleaner
    markdown_cleaner(input_path, output_path)


if __name__ == "__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <output_file>")
        print("Or: python main.py <input_string>")
        sys.exit(1)

    # Task 1: String to String
    if (len(sys.argv) == 2):
        main_string(sys.argv[1])

    # Task 2: File to File
    elif (len(sys.argv) == 3):
        main_files(sys.argv[1], sys.argv[2])
