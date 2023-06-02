from Django_test.file.file import *
from Django_test.common.loggin import logger


class synonymf():
    def __init__(self):
        self.file = file_path(file_name="同义词导入.xlsx")
        self.i = 0

    def synonymf_xls(self):
        print("请输入WhoDrug同义词数量")
        WHoDrug_int = int(input())
        print("请输入Meddra同义词数量")
        Meddra_int = int(input())

        delect_file()
        self.WHoDrug_xls(number=WHoDrug_int)
        self.Meddra_xls(number=Meddra_int)

    def WHoDrug_xls(self, number):
        Verbatim = open_xls(4)
        WHoDrug_Verbatim = open_xls(5)
        if os.path.exists(self.file):
            wookbooks = load_workbook(self.file)
        else:
            wookbooks = openpyxl.Workbook()
            wookbooks.save("同义词导入.xlsx", )
            wookbooks.remove(wookbooks["WHODrug同义词"])
        sheel = wookbooks.create_sheet("WHODrug同义词")
        wookbooks.remove(wookbooks["Sheet1"])
        list = ["标准值：药品名", "同义词名称"]
        sheel.append(list)
        while self.i < number:
            self.i += 1
            print("循环次数｛｝".format(str(self.i)))
            logger.info("循环次数｛｝".format(str(self.i)))
            Verbatimstr = Verbatim[random.randint(0, 300)] + str(self.i)
            sheel_list = [Verbatimstr, WHoDrug_Verbatim[random.randint(0, 300)]]
            sheel.append(sheel_list)
        wookbooks.save(self.file)
        wookbooks.close()

    def Meddra_xls(self, number):
        Verbatim = open_xls(2)
        LLT_Verbatim = open_xls(3)
        if os.path.exists(self.file):
            wookbooks = load_workbook(self.file)
        else:
            wookbooks = openpyxl.Workbook()
            wookbooks.save("同义词导入.xlsx", )
            wookbooks.remove(wookbooks["MedDRA同义词"])
        sheel = wookbooks.create_sheet("MedDRA同义词")
        # wookbooks.remove(wookbooks["Sheet"])
        list = ["标准值:LLT", "同义词名称"]
        sheel.append(list)
        while self.i < number:
            self.i += 1
            print("循环次数｛｝".format(str(self.i)))
            logger.info("循环次数｛｝".format(str(self.i)))
            Verbatimstr = Verbatim[random.randint(0, 300)] + str(self.i)
            sheel_list = [Verbatimstr, LLT_Verbatim[random.randint(0, 300)]]
            sheel.append(sheel_list)
        wookbooks.save(self.file)
        wookbooks.close()


if __name__ == '__main__':
    i = synonymf()
    i.synonymf_xls()
