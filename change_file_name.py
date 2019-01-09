import os
from nt import chdir

class Change_name():
    def __init__(self):
        self.path = input('请输入需要修改的文件路径：')
        self.new_name = input('请输入替换的名称：')
        self.old_name = input('请输入需要替换的名称：')

    def change_dir(self):
        file_name=os.listdir(self.path)
        print(file_name)
        for files in file_name:
            file=os.path.splitext(files)
            print(file)
            if self.old_name in file[0]:
                new_name=file[0].replace(self.old_name,self.new_name)+file[1]
                chdir(self.path)#在使用rename之前需要进入文件所在的目录
                os.rename(files,new_name)

    def run(self):
        self.change_dir()

if __name__ == '__main__':
    change_name=Change_name()
    change_name.run()