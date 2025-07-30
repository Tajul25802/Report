# Source Generated with ShoaibxAmer Pycdc
# File: report.pyc (Python 3.12)
# Decoded By: TAJUL ISLAM RABBI

import requests
import random
import os
import pyfiglet
import sys
import webbrowser
from datetime import datetime
E = '\x1b[1;31m'
B = '\x1b[2;36m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
r = '\x1b[31m'
group_url = 'https://www.facebook.com/tajula.isalama.bepari.2024'
profile_url = 'https://www.facebook.com/tajula.isalama.bepari.2024'
correct_password = 'RABBI'
os.system('clear')
banner1 = pyfiglet.figlet_format('Social Media report', font = 'slant')
print(S + banner1)
password = input(f'''{S}[•] Enter Password To Access Tool: {G}''')
if password != correct_password:
    print(f'''\n{E}[×] Wrong password!''')
    print(f'''{S}Collect password from our group:''')
    print(f'''{B}{group_url}\n''')
    webbrowser.open(group_url)
    sys.exit()
webbrowser.open(profile_url)
os.system('clear')
banner2 = pyfiglet.figlet_format('Social Media report', font = 'slant')
print(S + banner2)
print(r + '\n=============================\nAuthor : Shawon Islam Saim\n=============================\nTeam : Bangladesh Cyber RABBI(T . I . R Team)\n=============================\n𝐓𝐎𝐎𝐋 : Social Media All Platfrom Report Tools\n=============================\n')
user = input(f'''{B}[+] Victim Accaunt Name : {G}''')
name = input(f'''{B}[+] Victim Accaunt URL :   {G}''')
print(f'''{E}=======================================''')
head = {
    'cookie': 'ig_nrcb=1' }
r = 0
dt1 = datetime.now()
ts1 = str(datetime.timestamp(dt1)).split('.')[0]
us = 'qwertyuiopasdfghjklzxcvbnm._1234567890'
Warning: block stack is not empty!
boy = (lambda .0: for i in .0:
random.choice(us)None)(range(10)())
email = boy + '@gmail.com'
data = f'''jazoest=2931&lsd=AVq5uabXj48&Field258021274378282={user}&Field735407019826414={name}&Field506888789421014[year]=2014&Field506888789421014[month]=11&Field506888789421014[day]=11&Field294540267362199=Parent&inputEmail={email}&support_form_id=723586364339719&support_form_locale_id=en_US&support_form_hidden_fields=%7B%7D&support_form_fact_false_fields=[]&__user=0&__a=1&__req=6&__hs=19552.BP%3ADEFAULT.2.0..0.0&dpr=1&__ccg=GOOD&__rev=1007841948&__s=s4c6vz%3Anapxo9%3An9ncx2&__hsi=7255652935514227640&__dyn=7xe6E5aQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXw5ux60Vo1upE4W0OE2WxO2O1Vwooa81VohwnU1e42C220qu1Tw40wdq0Ho2ewnE3fw6iw4vwbS1Lw4Cwcq&__csr=&__spin_r=1007841948&__spin_b=trunk&__spin_t={ts1}'''
res = requests.post('https://help.instagram.com/ajax/help/contact/submit/page', data = data, headers = head).status_code
if res == 200:
    r += 1
    print(f'''{G}[√] Done Report : {B}{r} {S}| {B}{user}''')
print(f'''{E}[×] Error Code : {S}{res}''')
''.join
print(f'''{E}[×] Error Code : {S}666''')
