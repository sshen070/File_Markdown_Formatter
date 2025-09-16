from pathlib import Path
from formatingAlgorithm import file_cleaner


def main() -> None:
    main_dir = Path(__file__).resolve().parent.parent.parent


    print (f"Source Directory: {main_dir}")
    
    # # Input/output paths for unit_testing
    read_path = main_dir / "tests" / "unit_testing" / "poorly_formatted_markdown_testing.txt"
    write_path = main_dir / "tests" / "unit_testing" / "cleanedFile_testing.txt"

    # Input/output paths for full file
    full_read_path = main_dir / "tests" / "poorly_formatted_full.txt"
    full_write_path = main_dir / "tests" / "cleaned_full.txt"


    file_cleaner(read_path, write_path)
    file_cleaner(full_read_path, full_write_path)


if __name__ == "__main__":
    main()
