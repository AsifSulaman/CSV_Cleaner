# CSV Cleaner

A simple Python script that cleans a CSV file. It uses only the standard library, so there is nothing to install.

## What it does

- Removes extra spaces around every cell
- Removes completely empty rows
- Removes duplicate rows
- Saves the result to a new file (your original file is not changed)

## Requirements

Python 3.8 or newer.

## Usage

```bash
python csv_cleaner.py input.csv output.csv
```

Try it with the included sample:

```bash
python csv_cleaner.py sample.csv sample_cleaned.csv
```

## Example

`sample.csv` (before):

```csv
name,email,city
  alice ,alice@mail.com, Multan
bob,bob@mail.com,Lahore
,,
alice,alice@mail.com,Multan
  
carol,carol@mail.com,Karachi
```

`sample_cleaned.csv` (after):

```csv
name,email,city
alice,alice@mail.com,Multan
bob,bob@mail.com,Lahore
carol,carol@mail.com,Karachi
```

Console output:

```
Empty rows removed:     2
Duplicate rows removed: 1
Rows saved:             4
```

## Limitations

- The whole cleaning happens in memory, so it is meant for small files.
- Duplicates are found after trimming spaces, but capital letters still count (`Alice` and `alice` are different).

MIT LISCENCED
