import os

if __name__ == '__main__':
    os.chdir("c:/temp/MyTestWeb")
    print(os.getcwd())
    # print(os.listdir())
    # for elem in os.walk(os.getcwd()):  # os.scandir():
    #     cur, dirs, files = elem
    #     print(cur, dirs, files)
        # if elem.is_file():
        #     print('file', elem.stat())
        # else:
        #     print(elem.stat())
    if os.path.exists("input.txt"):
        print('yes')
    else:
        with open("input.txt", 'w') as file:
            file.write('hello')
        print('created')