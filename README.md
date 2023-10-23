# CodeToClipboard

A versatile Python utility for quickly copying the content of multiple code files (with a focus on Arduino-related extensions like `.ino`, `.h`, and `.cpp`) from a specified folder to the clipboard. The tool enhances usability by allowing users to select which files to include and by appending each file's content with a distinct and noticeable header.

## Features

- Efficiently searches a folder for `.ino`, `.h`, and `.cpp` files.
- Displays a concise list of available files, offering users the choice to exclude any from the final output.
- Merges the content of the chosen files, bracketing each with easily identifiable headers, and then copies everything to the clipboard.
- By default, it checks the folder where the script resides, but users can optionally specify another directory.

## Usage

1. Clone this repository or simply download the main script.
2. Before you get started, make sure `pyperclip` is installed in your environment. If it's missing, just run:
   ```
   pip install pyperclip
   ```
3. Execute the script with:
   ```
   python CodeToClipboard.py
   ```
4. Adhere to the on-screen instructions.

## License

[MIT License](LICENSE) (If you decide to use the MIT License or any other, make sure to add a corresponding LICENSE file in your repository and reference it here.)

## Contributions

We always appreciate contributions! If you're thinking about a significant modification, kindly raise an issue beforehand to talk over your ideas.
