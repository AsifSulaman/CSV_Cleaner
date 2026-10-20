import csv
import sys


def clean_row(row):
    return [cell.strip() for cell in row]


def clean_csv(input_file, output_file):
    seen = set()          # rows we have already kept
    cleaned_rows = []
    empty_count = 0
    duplicate_count = 0

    with open(input_file, newline="", encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            row = clean_row(row)

            if not any(row):              
                empty_count += 1
                continue

            if tuple(row) in seen:       
                duplicate_count += 1
                continue

            seen.add(tuple(row))
            cleaned_rows.append(row)

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(cleaned_rows)

    print(f"Empty rows removed:     {empty_count}")
    print(f"Duplicate rows removed: {duplicate_count}")
    print(f"Rows saved:             {len(cleaned_rows)}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python csv_cleaner.py input.csv output.csv")
        return
    input_file, output_file = sys.argv[1], sys.argv[2]
    if input_file == output_file:
        print("Output file must be different from the input file.")
        return
    try:
        clean_csv(input_file, output_file)
    except FileNotFoundError:
        print(f"File not found: {input_file}")


if __name__ == "__main__":
    main()
