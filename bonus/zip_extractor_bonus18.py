import zipfile

def extract_file(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_file("C:/Users/manis/PycharmProjects/todo-app/bonus/compressed.zip",
                 "C:/Users/manis/PycharmProjects/todo-app/files")