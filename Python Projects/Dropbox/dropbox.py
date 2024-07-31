import dropbox

# Set up credentials
dbx = dropbox.Dropbox('sl.B6HpD_zdvX757hMA5ZhnWPYHWQwl1953UVPcUKacDIVqrjZOgItaZ9TA-YJqM0V3mvamsoqjGJard8EB2gabsWhwyu1svz7DkR56KqYNWIRGqTYr1CzXgAPKN5KZAhvozFGUFPR8dfHW')

# Upload a file
file_path = input("File Path: ")
file_name = input("File Name: ")
with open(file_path, 'rb') as f:
    dbx.files_upload(f.read(), '/' + file_name)

# Get the file URL
file_url = dbx.files_get_temporary_link('/' + file_name).link
print(f'File uploaded: {file_url}')