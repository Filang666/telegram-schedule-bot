import re
from os import listdir, rename
from posixpath import pardir

import pypdf
from typing_extensions import List


def rename_files():
    for file in listdir():
        if file.endswith(".pdf"):
            text = pypdf.PdfReader(file).pages[0].extract_text()
            if text.find("ПОНЕДЕЛЬНИК") != -1:
                rename(file, "Понедельник.pdf")
            if text.find("ВТОРНИК") != -1:
                rename(file, "Вторник.pdf")
            if text.find("СРЕДА") != -1:
                rename(file, "Среда.pdf")
            if text.find("ЧЕТВЕРГ") != -1:
                rename(file, "Четверг.pdf")
            if text.find("ПЯТНИЦА") != -1:
                rename(file, "Пятница.pdf")
            if text.find("СУББОТА") != -1:
                rename(file, "Суббота.pdf")


def parse_schedule_text(class_number, day=None):
    text = pypdf.PdfReader(f"{day}.pdf").pages[0].extract_text()
    print(text.find("РОВ"))
    # return "Расписание еще не готово"


parse_schedule_text("10Б", "Понедельник")
