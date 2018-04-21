import sys, string, os, subprocess


os.system('xcopy D:\Projekte\openacademy "C:\Program Files (x86)\Odoo 10.0\server\odoo\custom-addons\openacademy" /D /E /Y /I')
os.startfile("C:\\Program Files (x86)\\Odoo 10.0\\service\\stop.bat")
os.chdir("C:\Program Files (x86)\Odoo 10.0\server")
os.system('odoo-bin.exe -d anker -u todo_app,todo_user,mrp,mrp_bom_planner')