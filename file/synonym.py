import random

from Django_test.file.file import *


class synonymf():
    def __init__(self):
        self.file = file_path(file_name="同义词导入.xls")

    def synonymf_xls(self):
        print("请输入WhoDrug同义词数量")
        WHoDrug_int = int(input())
        print("请输入Meddra同义词数量")
        Meddra_int = int(input())

        delect_file()
        self.WHoDrug_xls(number=WHoDrug_int)
        self.Meddra_xls(number=Meddra_int)

    def WHoDrug_xls(self, number):
        Verbatim = open_xls(5)
        WHoDrug_Verbatim = open_xls(6)
        if os.path.exists(self.file):
                wookbooks = load_workbook(self.file)
        else:
            wookbooks = openpyxl.Workbook()
            wookbooks.save("同义词导入.xls", )
        sheel = wookbooks.create_sheet("MedDRA同义词")
        wookbooks.remove(wookbooks["Sheet"])
        list = ["标准值：药品名", "同义词名称"]
        sheel.append(list)
        i = 0
        while i < number:
            i = i + 1
            sheel_list = [WHoDrug_Verbatim[random.randint(0, 300)], Verbatim[random.randint(0, 300)]]
            sheel.append(sheel_list)
        wookbooks.save(file_path())
        wookbooks.close()

    def Meddra_xls(self, number):
        Verbatim = open_xls(4)
        LLT_Verbatim = open_xls(3)
        if os.path.exists(self.file):
            wookbooks = load_workbook(self.file)
        else:
            wookbooks = openpyxl.Workbook()
            wookbooks.save("同义词导入.xls", )
        sheel = wookbooks.create_sheet("MedDRA同义词")
        wookbooks.remove(wookbooks["Sheet"])
        list = ["标准值:LLT", "同义词名称"]
        sheel.append(list)
        i = 0
        while i < number:
            i = i + 1
            sheel_list = [LLT_Verbatim[random.randint(0, 300)], Verbatim[random.randint(0, 300)]]
            sheel.append(sheel_list)
        wookbooks.save(file_path())
        wookbooks.close()


if __name__ == '__main__':
    i = synonymf()
    i.synonymf_xls()
