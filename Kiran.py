import os
import shutil
import openpyxl

for file in os.listdir("c:/temp python/"):
    ext = file[file.find("."):]
    if ext == '.xlsx':
        workbook = openpyxl.load_workbook("c:/temp python/"+file)
        sheet = workbook.worksheets[0]

        correct= 0
        answer_list=["A","B","C","D","A","B","C","D","A","B"]

        for row in range(10): # row= 2, col=2
            if (sheet.cell(row+2, 2).value) == answer_list[row]:
                correct = correct + 1

        sheet["A15"] = "Correct: " + str(correct)
        workbook.save("c:/temp python/"+file)

        print("Correct answers: " + str(correct ))
        
        shutil.move("c:/temp python/" + file, "c:/temp python/dest/" + file)
        print("move " + file)
    else:
        print(file + "not moved")