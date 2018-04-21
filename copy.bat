echo off
xcopy D:\Projekte\searchfilter_anker\controllers "C:\Program Files (x86)\Odoo 10.0\server\odoo\custom-addons\searchfilter_anker\controllers" /D /E /Y /I
xcopy D:\Projekte\searchfilter_anker\demo "C:\Program Files (x86)\Odoo 10.0\server\odoo\custom-addons\searchfilter_anker\demo" /D /E /Y /I
xcopy D:\Projekte\searchfilter_anker\models "C:\Program Files (x86)\Odoo 10.0\server\odoo\custom-addons\searchfilter_anker\models" /D /E /Y /I
xcopy D:\Projekte\searchfilter_anker\security "C:\Program Files (x86)\Odoo 10.0\server\odoo\custom-addons\searchfilter_anker\security" /D /E /Y /I
xcopy "D:\Projekte\searchfilter_anker\views" "C:\Program Files (x86)\Odoo 10.0\server\odoo\custom-addons\searchfilter_anker\views" /D /E /Y /I
xcopy D:\Projekte\searchfilter_anker\__init__.py "C:\Program Files (x86)\Odoo 10.0\server\odoo\custom-addons\searchfilter_anker" /Y
xcopy D:\Projekte\searchfilter_anker\__manifest__.py "C:\Program Files (x86)\Odoo 10.0\server\odoo\custom-addons\searchfilter_anker" /Y
xcopy D:\Projekte\searchfilter_anker\report "C:\Program Files (x86)\Odoo 10.0\server\odoo\custom-addons\searchfilter_anker\report" /D /E /Y /I