import openpyxl
import os

from openpyxl.workbook.workbook import Workbook

workbook = openpyxl.load_workbook("c:/temp python/answers.xlsx")
sheet = workbook.worksheets[0]

correct= 0
answer_list=["A","B","C","D","A","B","C","D","A","B"]

for row in range(10): # row= 2, col=2
    if sheet.cell(row+2, 2).value == answer_list[row]:
        correct = correct + 1

sheet["A15"] = "Correct: " + str(correct)
workbook.save("c:/temp python/answers.xlsx")

print("Correct answers: " + str(correct))