import sys
def compare_files(file1, file2):
    with open(file1, 'rb') as f1:
        content1 = f1.read()
    with open(file2, 'rb') as f2:
        content2 = f2.read()

    if content1 == content2:
        print("ok")
    else:
        print("nok")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Debes especificar el nombre del archivo a comparar")
        sys.exit()
    file = sys.argv[1]
    file1 = sys.argv[2]
    compare_files(file, file1)
    


