import sys, string, os, subprocess


#os.chdir("C:\Program Files (x86)\WinSCP")
#os.system('pscp.exe -pw r44xB78s -r "C:\Program Files (x86)\Odoo 10.0\server\odoo\custom-addons\searchfilter_anker" root@81.169.131.143:/home/')
#os.chdir("C:\Program Files\PuTTY")
#os.system('pscp.exe  -r test root@81.169.131.143:/home -pw r44xB78s')
#os.system('plink.exe -ssh root@81.169.131.143 -l root -pw r44xB78s service odoo status')
os.system('plink.exe -ssh root@81.169.131.143 -l root -pw r44xB78s service odoo stop')
os.system('plink.exe -ssh root@81.169.131.143 -l root -pw r44xB78s service odoo -d anker_test -u searchfilter_anker')