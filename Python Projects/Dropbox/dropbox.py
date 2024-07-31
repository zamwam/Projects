import dropbox

# Set up credentials
dbx = dropbox.Dropbox('api_key')

# Upload a file
file_path = input("File Path: ")
file_name = input("File Name: ")
with open(file_path, 'rb') as f:
    dbx.files_upload(f.read(), '/' + file_name)

# Get the file URL
file_url = dbx.files_get_temporary_link('/' + file_name).link
print(f'File uploaded: {file_url}')