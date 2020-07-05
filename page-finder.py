import sys
import requests
import os
import platform
from colorama import Fore

u = platform.platform()
if 'Windows' in u:
    os.system('cls')
else:
    os.system('clear')

def main(url,combo):
    print("{}[*] {} Reading Wordlist ".format(Fore.GREEN, Fore.RED))
    if "http://" or "https://" in url:
        pass
    else:
        url = "http://" + url
    if not url.endswith("/"):
        url = url + "/"
    with open(combo, 'r') as f:
        data = f.read().splitlines()
        edited = []

        for i in data:
            if "\n" in i:
                i.split("\n")

            if "/" in i:
                pass
            else:
                i = i + "/"
            edited.append(i)

        urls = []

        for log in edited:
            url2 = url + log

            urls.append(url2)
        h = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
        }


        for j in urls :
            a = requests.post(j, headers=h, allow_redirects =False)
            if a.status_code == 200 or 201 :
                print("{}[+] {} Founded {}".format(Fore.GREEN, Fore.YELLOW, j))

                with open("Founded.txt","a+") as file:
                    file.write("URL = {} FOUNDED PAGES = {}".format(url,j))

            else:
                pass




def default(url):
    print("{} Reading .. . .".format(Fore.YELLOW))
    if "http://" or "https://" in url:
        pass
    else:
        url = "http://" + url
    if not url.endswith("/"):
        url = url + "/"

    Dorks = """
        index.php
        index.html
        login.php
        login.html
        login
        admin.php
        admin
        home.html
        home.php
        news.html
        news.php
        info.php
        information.php
        info.html
        information.html
        login.asp
        login.jsp
        admin.aspx
        admin.asp
        admin.jsp
        login/login.php
        login/register.php
        admin/login.php
        w.html
        admin/
        administrator/
        admin1/
        admin2/
        admin3/
        admin4/
        admin5/
        evmsadmin/
        usuarios/
        usuario/
        moderator/
        webadmin/
        adminarea/
        bb-admin/
        adminLogin/
        admin_area/
        panel-administracion/
        instadmin/
        memberadmin/
        administratorlogin/
        adm/
        admin/account.php
        admin/index.php
        admin/login.php
        admin/admin.php
        admin_area/admin.php
        admin_area/login.php
        siteadmin/login.php
        siteadmin/index.php
        siteadmin/login.html
        admin/account.html
        admin/index.html
        admin/login.html
        admin/admin.html
        admin_area/index.php
        bb-admin/index.php
        bb-admin/login.php
        bb-admin/admin.php
        admin/home.php
        admin_area/login.html
        admin_area/index.html
        admin/controlpanel.php
        admin.php
        admincp/index.asp
        admincp/login.asp
        admincp/index.html
        adminpanel.html
        webadmin.html
        webadmin/index.html
        webadmin/admin.html
        webadmin/login.html
        admin/admin_login.html
        admin_login.html
        panel-administracion/login.html
        admin/cp.php
        cp.php
        administrator/index.php
        administrator/login.php
        nsw/admin/login.php
        webadmin/login.php
        admin/admin_login.php
        admin_login.php
        administrator/account.php
        administrator.php
        admin_area/admin.html
        pages/admin/admin-login.php
        admin/admin-login.php
        admin-login.php
        bb-admin/index.html
        bb-admin/login.html
        acceso.php
        bb-admin/admin.html
        admin/home.html
        login.php
        modelsearch/login.php
        moderator.php
        moderator/login.php
        moderator/admin.php
        account.php
        pages/admin/admin-login.html
        admin/admin-login.html
        admin-login.html
        controlpanel.php
        admincontrol.php
        admin/adminLogin.html
        adminLogin.html
        home.html
        rcjakar/admin/login.php
        adminarea/index.html
        adminarea/admin.html
        webadmin.php
       webadmin/index.php
        webadmin/admin.php
        admin/controlpanel.html
        admin.html
        admin/cp.html
        cp.html
        adminpanel.php
        moderator.html
        administrator/index.html
        administrator/login.html
        user.html
        administrator/account.html
        administrator.html
        login.html
        modelsearch/login.html
        moderator/login.html
        adminarea/login.html
        panel-administracion/index.html
        panel-administracion/admin.html
        modelsearch/index.html
        modelsearch/admin.html
        admincontrol/login.html
        adm/index.html
        adm.html
        moderator/admin.html
        user.php
        account.html
        controlpanel.html
        admincontrol.html
        panel-administracion/login.php
        wp-login.php
        adminLogin.php
        admin/adminLogin.php
        home.php
        adminarea/index.php
        adminarea/admin.php
        adminarea/login.php
        panel-administracion/index.php
        panel-administracion/admin.php
        modelsearch/index.php
       modelsearch/admin.php
        admincontrol/login.php
        adm/admloginuser.php
        admloginuser.php
        admin2.php
        admin2/login.php
        admin2/index.php
        usuarios/login.php
        adm/index.php
        adm.php
        affiliate.php
        adm_auth.php
        memberadmin.php
        administratorlogin.php
        account.asp
        admin/account.asp
        admin/index.asp
        admin/login.asp
        admin/admin.asp
        admin_area/admin.asp
        admin_area/login.asp
        admin_area/index.asp
        bb-admin/index.asp
        bb-admin/login.asp
        bb-admin/admin.asp
        admin/home.asp
        admin/controlpanel.asp
        admin.asp
        pages/admin/admin-login.asp
        admin/admin-login.asp
        admin-login.asp
        home.asp
        adminarea/admin.asp
        adminarea/login.asp
        panel-administracion/index.asp
        panel-administracion/admin.asp
        modelsearch/index.asp
        modelsearch/admin.asp
        administrator/index.asp
        admincontrol/login.asp
        adm/admloginuser.asp
        admloginuser.asp
        admin2.asp
        admin2/login.asp
        admin2/index.asp
        adm/index.asp
        adm.asp
        affiliate.asp
        adm_auth.asp
        memberadmin.asp
        administratorlogin.asp
        siteadmin/login.asp
        siteadmin/index.asp
        admin1.php
        admin1.html
        admin2.html
        yonetim.php
        yonetim.html
        yonetici.php
        yonetici.html
        ccms/
        ccms/login.php
        ccms/index.php
        maintenance/
        webmaster/
        configuration/
        configure/
        websvn/
        controlpanel/
        admin1.asp
        yonetim.asp
        yonetici.asp
        fileadmin/
        fileadmin.php
        fileadmin.asp
        fileadmin.html
        administration/
        administration.php
        administration.html
        sysadmin.php
        sysadmin.html
        phpmyadmin/
        myadmin/
        sysadmin.asp
        Server/
        wp-admin/
        wplogin/
        administr8.php
        administr8.html
        administr8/
        administr8.asp
        administratie/
        admins/
        admins.php
        admins.asp
        admins.html
        administrivia/   
        navSiteAdmin/
        server_admin_small/
        logo_sysadmin/
        server/
        database_administration/
        power_user/
        system_administration/
        ss_vms_admin_sm/
        ADMIN/
        paneldecontrol/
        login/
        cms/
        panel.php
        administracion.php
        administrator
        admon/
        ADMON/
        administrador/
        ADMIN/login.php
        panelc/
        w.php
        """
    data = Dorks.split()
    urls = []
    for i in data:
        url2 = url+i
        urls.append(url2)

    for j in urls:
        h = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
        }
        a = requests.post(j, headers=h, allow_redirects =False)
        if a.status_code == 200 or 203 or 201 :
            print("{}[+] {} Founded {}".format(Fore.GREEN, Fore.YELLOW, j))
            with open('Founded.txt','a+') as file:
                file.write("URL {} AND FOUNDED PAGES ARE {}".format(url,j))
        else:
            pass



def usage():
    print("""
        PAGE FINDER WROTE BY IPZX
        USAGE:
            To use default option --- > python3 page-finder.py [url] [-D]
            To use custom dorks you can use --- > python3 page-finder.py [url] [location of dork you want to use]
        HOPE YOU ENJOY :)
        """
    )

try:
    if __name__ == "__main__":
        if len(sys.argv) == 3:
            if sys.argv[2] == "-D":
                url = sys.argv[1]
                default(url)
            else:
                url = sys.argv[1]
                combo = sys.argv[2]
                main(url,combo)
                
        else:
            usage()
except:
    print("""
        please try again
        Example :
            python3 page-finder.py http://target.com dork.txt
    """)