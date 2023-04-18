import os
from datetime import datetime
import shutil

# root = "C:\\Users\\jmeyrelles\\"
# folderTo = f"teste\\"
# folderTo = f"{root}OneDrive - MDL Realty Incorporadora SA\\Documentos\\teste"
folderTo = "C:\\FINNET\\O0055FINNET\\ENTRADA\\ITAU\\EXTRATO\\"
arr_folders = [
    "C:\\FINNET\\O0055FINNET\\ENTRADA\\ITAU\\EXTRATO\\",
    "C:\\FINNET\\O0055FINNET\\ENTRADA\\ITAU\\COBRANCA\\",
    "C:\\FINNET\\O0055FINNET\\ENTRADA\\ITAU\\PAGAMENTO\\",
    "C:\\FINNET\\O0055FINNET\\ENTRADA\\BRADESCO\\EXTRATO\\",
    "C:\\FINNET\\O0055FINNET\\ENTRADA\\BRADESCO\\COBRANCA\\",
    "C:\\FINNET\\O0055FINNET\\ENTRADA\\BRADESCO\\PAGAMENTO\\",
]


# https://www.hashtagtreinamentos.com/executar-codigo-automaticamente-python


def create_new_dir(time, folder):
    for name in os.listdir(folder):
        infilename = os.path.join(folder, name)
        oldbase = os.path.splitext(name)
        if not os.path.isdir(infilename):
            continue

        if (oldbase[0] == time):
            return f"{folder}{time}\\"

    os.makedirs(f"{folder}{time}\\")
    return f"{folder}{time}\\"


def move_file(old_dir, new_dir):
    try:
        # try to remove file
        os.rename(old_dir, new_dir)
    except FileExistsError:
        # if there's any error, the local file is removed
        os.remove(new_dir)
        # then, the new file is moved
        os.rename(old_dir, new_dir)


def rename(folder):
    # if there's no directory finalize
    if not folder:
        return print("There is no any directory here!!")
    # read directory content as an elements list
    for filename in os.listdir(folder):
        # building the file address
        infilename = os.path.join(folder, filename)
        # taking the timestamp of file
        time = os.path.getmtime(infilename)
        dt_c = datetime.fromtimestamp(time).strftime("%Y%m%d")
        # verify if the element is file. If it is not, jump
        if not os.path.isfile(infilename):
            continue
        if (".zip" in filename):
            # verify if there is a folder and if there is not, create one
            new_dir = create_new_dir(dt_c, folder)
            dir = new_dir + filename
            # replacement
            move_file(infilename, dir)
        # if there is a file with no extension
        if (".txt" not in filename and ".zip" not in filename):
            # newname = infilename + ".txt"
            # verify if there is a folder and if there is not, create one
            new_dir = create_new_dir(dt_c, folder)
            dir = new_dir + filename + ".txt"
            # replacement
            move_file(infilename, dir)
        elif (".txt" in filename):
            # verify if there is a folder and if there is not, create one
            new_dir = create_new_dir(dt_c, folder)
            # complete the file address
            dir = new_dir + filename
            # replacement
            move_file(infilename, dir)
        else:
            continue
    return


def delete_dir(folder):
    for name in os.listdir(folder):
        # taking the time of today
        today = datetime.now()
        # difference between today and the file timestamp
        difference = today - datetime.strptime(name, '%Y%m%d')
        # if diff in days' more than twenty disconsidering 20th day, remove it.
        if (difference.days > 40):
            rfile = os.path.join(folder, name)
            shutil.rmtree(rfile)
        else:
            continue


def organizing_folder(default):
    # asking for the file address
    # folder = input("Cole aqui o endereço da pasta (ctrl+shift+v):")
    # if folder == '':
    #     folder = folderTo
    for path in default:
        try:
            # folder = default
            print("Modificando e movendo arquivos...")
            # function to rename files
            rename(path)

            print("Deletando arquivos com idade maior que 40 dias")
            # function to delete directory with more than 40 days of creation
            delete_dir(path)
            print("Finalizado")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


# calling the main function
if __name__ == "__main__":
    organizing_folder(arr_folders)
