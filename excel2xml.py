# python2.7.2
# author : eric zhang
# email  : ericnomail@gmail.com
# date       version   PIC    comments
# 20120518    0.0.1    eric
# 20120529    0.0.2    eric   generate strings.xml from xls file.
# 20120605    0.1.1    eric   get app name from command line arguments.
# 20120706    0.1.2    eric   remove no-used variable, add error print info.
# 20120817    0.1.3    eric   "\'" instead of "'" for strings.xml in values-fr(franch language).
# 20130608    0.2.0    eric   use xlrd instead of pyExcelerator.
# 20130614    0.3.0    eric   support 2 parameters, device name and App name.
# 20140804    0.4.1    eric   support 3 parameters, copy strings.xml to the project path.

import string
import xlrd
from BeautifulSoup import BeautifulSoup
import urllib
import codecs
import sys
import os.path

# init excel file from strings.xml Android projects used.
def android_str_2_excel():
    w = Workbook()
    ws = w.add_sheet("Android")
    parser = BeautifulSoup(urllib.urlopen('file:D:\\Android_Prj\\res\\values\\strings.xml').read())
    i = 0
    for strid in parser.findAll('string'):
        ws.write(i, 0, strid['name'])
        ws.write(i, 1, strid.text)
        i += 1
    w.save('android_str.xls')

# used only once, add the second content of strings.xml to excel file.
def reset_ch_str():
    ws = []
    w = Workbook()
    sheets = parse_xls('tvman_dvb_android_str.xls')
    ws.append(w.add_sheet(sheets[0][0]))
    for i in range(len(sheets[0][1]) / 2):
        for j in range(2):
            ws[0].write(i, j, sheets[0][1][(i, j)])
    parser = BeautifulSoup(urllib.urlopen('file:D:\\Android_Prj\\res\\values-zh-rCN\\strings.xml').read())
    i = 0
    for strid in parser.findAll('string'):
        ws[0].write(i, 2, strid.text)
        i += 1
    w.save('android_str.xls')

# template to generate a line of strings.xml
def line_template(str_id, lan_str):
    template = '''
    <string name="''' + str_id + '''">''' + lan_str + '''</string>
    '''
    return template

# template to genrate strings.xml, include xml file header and app_name from command line arguments.
def file_template(string, dev_name, app_name):
    template = '''<?xml version="1.0" encoding="utf-8"?>
    <resources>
    <string name="app_name">''' + app_name + '''</string>
    ''' + string.replace("TVman", dev_name) + '''
</resources>
    '''
    return template

# parse excel file.
def gen_string_xml(prj_path, dev_name, app_name):
    country_code = {
        'English' : '',
        'Italian' : '-it',
        'French' : '-fr',
        'Swedish' : '-sv',
        'German' : '-de',
        'Hungarian' : '-hu',
        'Slovak' : '-sk-rSK',
        'Czech' : '-cs-rCZ',
        'Greek' : '-el',
        'Spanish' : '-es',
        'Portuguese' : '-pt-rBR',
        'TranditionalChinese' : '-zh-rTW',
        'SimplifiedChinese' : '-zh-rCN',
        'Polish' : '-pl',
        'Bulgarian' : '-bg',}
    try:
        sheets = xlrd.open_workbook("translation_table.xls").sheet_by_index(0)
        #sheets = parse_xls('translation_table.xls')
    except IOError:
        print "Can't find the file translation_table.xls."
        return
    
    prj_res_path = os.path.abspath(prj_path) + r'\res\values'
    for i in range(3, sheets.ncols):
        string = ''
        for j in range(1, sheets.nrows):
            if sheets.cell_value(rowx = j, colx = 0).strip() != "":
                string += line_template(sheets.cell_value(rowx = j, colx = 0).strip(), sheets.cell_value(rowx = j, colx = i).replace("'", "\\'"))
        lan_str = sheets.cell_value(rowx = 0, colx = i).strip()
        if os.path.exists(prj_res_path + country_code[lan_str]):
            str_file = codecs.open(prj_res_path + country_code[lan_str] + '\strings.xml', 'w', "utf-8")
            str_file.write(file_template(string, dev_name, app_name))
            str_file.close()
        else:
            print "No this folder: " + prj_res_path + country_code[lan_str] 

# get command line arguments
param_dev_name = ""
param_app_name = ""
param_prj_path = ""
if len(sys.argv) > 3:
    param_prj_path = sys.argv[1]
    param_dev_name = sys.argv[2]
    param_app_name = sys.argv[3]
    for i in range(4, len(sys.argv)):
        param_app_name += " " + sys.argv[i]
    gen_string_xml(param_prj_path, param_dev_name, param_app_name)
else:
    print "Please input parameters: excel2xml prj_path device_name app_name."
