# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

# Create your views here.

import xlrd
import os
from CatyHIS.settings import RES_DIR
from FormGen.models import Person


def home(request):
    return render(request, 'index.html')


def examination_form(request):
    persons = Person.objects.all().order_by('order')
    return render(request, 'form.html', {'persons': persons})


def update(request):
    file_path = os.path.join(RES_DIR, '40001-40900.xlsx')
    import_person_info(file_path)
    return redirect('home')


def import_person_info(file):
    work_book = xlrd.open_workbook(file)
    sheet = work_book.sheet_by_index(0)
    for row_index in range(1, sheet.nrows):
        person = Person()
        person.order = int(sheet.cell(row_index, 1).value)
        person.team = sheet.cell(row_index, 2).value
        person.team_no = get_team_no(person.team)
        person.name = sheet.cell(row_index, 3).value
        person.sex = int(sheet.cell(row_index, 4).value)
        person.age = int(sheet.cell(row_index, 5).value)
        person.community = sheet.cell(row_index, 6).value
        person.contact = format_contact(sheet.cell(row_index, 7).value)
        person.save()


def get_team_no(team_name):
    return int(team_name[0:1])


def format_contact(contact):
    if type(contact) is float:
        contact = str(contact)
        if '.0' in contact:
            return contact.replace('.0', '')
    return contact
