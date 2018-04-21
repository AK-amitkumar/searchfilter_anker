import sys, string, os, subprocess

os.startfile("C:\\Program Files (x86)\\Odoo 10.0\\service\\stop.bat")
os.system('copy.bat')
os.chdir("C:\Program Files (x86)\WinSCP")
os.system('pscp.exe -pw r44xB78s -r "C:\Program Files (x86)\Odoo 10.0\server\odoo\custom-addons\searchfilter_anker" root@81.169.131.143:/usr/lib/python2.7/dist-packages/odoo/addons')
os.chdir("C:\Program Files (x86)\Odoo 10.0\server")
os.system('odoo-bin.exe -d anker -u searchfilter_anker')
os.startfile("C:\\Program Files (x86)\\Odoo 10.0\\service\\start.bat")