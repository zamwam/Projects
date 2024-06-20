import zipfile
import os
def unzip_file(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # Once extracted, remove the original zip file
    os.remove(zip_file)

# Example usage
zip_file = input(": ")  # Path to your ZIP file
user_folder = os.getenv('USERPROFILE')  # Gets the current user's profile folder on Windows
cwd = os.getcwd()
extract_to = os.path.join(cwd, 'extracted_folder')  # Folder where you want to extract the contents
unzip_file(zip_file, extract_to)