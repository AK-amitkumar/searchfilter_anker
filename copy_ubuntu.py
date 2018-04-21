import sys, string, os, subprocess

os.system('copy.bat')
os.chdir("C:\Program Files (x86)\WinSCP")
os.system('pscp.exe -pw r44xB78s -r "C:\Program Files (x86)\Odoo 10.0\server\odoo\custom-addons\searchfilter_anker" root@81.169.131.143:/usr/lib/python2.7/dist-packages/odoo/addons')
os.chdir("C:\Program Files\PuTTY")
os.system('plink.exe -ssh root@81.169.131.143 -l root -pw r44xB78s service odoo status')
