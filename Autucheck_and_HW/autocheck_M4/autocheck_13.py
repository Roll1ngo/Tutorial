from pathlib import Path


def parse_folder(path):
    files = []
    folders = []

    for i in path.iterdir():
                
        if i.is_dir():
            folders.append(i.name)
        elif i.is_file():
            files.append(i.name)
     
    return files,folders


p = Path("C:\Test_Path\Bandicam")
print(parse_folder(p))





