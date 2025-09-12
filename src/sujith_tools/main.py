from pathlib import Path
from formatingAlgorithm import file_cleaner

def main() -> None:
    main_dir = Path(__file__).resolve().parent.parent.parent


    print (f"Source Directory: {main_dir}")
    
    # Input/output paths relative to repo root
    read_path = main_dir / "data" / "unit_testing" / "poorly_formatted_markdown_testing.txt"
    write_path = main_dir / "data" / "unit_testing" / "cleanedFile_testing.txt"

    file_cleaner(read_path, write_path)


if __name__ == "__main__":
    main()
    print("*Not imported*")
