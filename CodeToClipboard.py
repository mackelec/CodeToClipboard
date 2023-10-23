import os
import pyperclip

def copy_folder_content_to_clipboard(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("The specified folder does not exist!")
        return

    # Walk through the folder and collect file contents
    combined_content = []
    eligible_files = []

    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            # Check for .ino, .h, .cpp files
            if filename.endswith(('.ino', '.h', '.cpp')):
                eligible_files.append((dirpath, filename))

    # Display files and ask for exclusions
    print("\nEligible files found:")
    for idx, (dirpath, filename) in enumerate(eligible_files, 1):
        print(f"{idx}. {filename} from {dirpath}")

    exclusion_indices = input("\nEnter the numbers (comma-separated) of the files you wish to exclude, or press enter to include all: ").strip()
    exclusion_set = set(int(idx) for idx in exclusion_indices.split(",") if idx)

    for idx, (dirpath, filename) in enumerate(eligible_files, 1):
        if idx not in exclusion_set:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            header_line = "=" * 50
            header = f"\n\n{header_line}\n=== {filename} from {dirpath} ===\n{header_line}\n\n"
            combined_content.append(header + content)

    # Copy combined content to clipboard
    pyperclip.copy(''.join(combined_content))
    print("\nContent copied to clipboard!")

if __name__ == '__main__':
    default_folder_path = os.path.dirname(os.path.realpath(__file__))
    print(f"Default Arduino source code folder: {default_folder_path}")
    custom_folder_path = input("Enter a different folder path or press Enter to use the default: ").strip()
    
    # If the user doesn't provide a custom path, use the default path
    if not custom_folder_path:
        custom_folder_path = default_folder_path

    copy_folder_content_to_clipboard(custom_folder_path)
