from pymongo import MongoClient
import requests
import re

companies = [
    "2U INC",
    "30DC INC",
    "3D PIONEER SYSTEMS INC",
    "8X8 INC",
    "A10 NETWORKS INC",
    "ACI WORLDWIDE INC",
    "ACTUA CORP",
    "ADEXA INC",
    "ADOBE INC",
    "ADVANCED VOICE RECOGNITION",
    "ADVANT-E CORP",
    "ADVANTEGO CORP",
    "AGILYSYS INC",
    "ALARM.COM HOLDINGS INC",
    "ALLDIGITAL HOLDINGS INC",
    "ALTAIR ENGINEERING INC",
    "ALTERYX INC",
    "AMERICAN SECURITY RES CORP",
    "AMERICAN SOFTWARE  -CL A",
    "ANAPLAN INC",
    "ANSYS INC",
    "APPFOLIO INC",
    "APPIAN CORP",
    "APPLIED VISUAL SCIENCES INC",
    "APT SYSTEMS INC",
    "ASANA INC",
    "ASPEN TECHNOLOGY INC",
    "ASURE SOFTWARE INC",
    "AUDIOEYE INC",
    "AUTODESK INC",
    "AUTOMATIC DATA PROCESSING",
    "AVALARA INC",
    "AVAYA HLDGS CORP",
    "AWARE INC",
    "BARRACUDA NETWORKS INC",
    "BENEFITFOCUS INC",
    "BENTLEY SYSTEMS INC",
    "BIGCOMMERCE HOLDIN INC",
    "BILL.COM HOLDINGS INC",
    "BIO-KEY INTERNATIONAL INC",
    "BLACK BOX CORP",
    "BLACKBAUD INC",
    "BLACKBOXSTOCKS INC",
    "BLACKLINE INC",
    "BLAQCLOUDS INC",
    "BOTTOMLINE TECHNOLOGIES INC",
    "BOX INC",
    "BOXLIGHT CORP",
    "BRAVATEK SOLUTIONS INC",
    "BRIDGELINE DIGITAL INC",
    "BRIDGEWAY NATIONAL CORP",
    "B-SCADA INC",
    "BSQUARE CORP",
    "BUSYBOX.COM INC",
    "CADENCE DESIGN SYSTEMS INC",
    "CDK GLOBAL INC",
    "CERENCE INC",
    "CERIDIAN CORP",
    "CERIDIAN HCM HOLDING",
    "CHANGSHENG INTERNATIONAL GRO",
    "CHANNELADVISOR CORP",
    "CHINA YANYUN YHU NTL ED GRP",
    "CICERO INC",
    "CIMETRIX INC",
    "CIPHERLOC CORP",
    "CITRIX SYSTEMS INC",
    "CLEANSPARK INC",
    "CLICKSTREAM CORP",
    "CLONE ALGO TECHNOLOGIES INC",
    "CLOUDERA INC",
    "CLOUDFLARE INC",
    "CLOUDWARD INC",
    "CODE REBEL CORP",
    "COM GUARD.COM INC",
    "COMMVAULT SYSTEMS INC",
    "CORNERSTONE ONDEMAND INC",
    "COUPA SOFTWARE INC",
    "CROWDSTRIKE HOLDINGS INC",
    "CYBERFORT SOFTWARE INC",
    "CYREN LTD",
    "DATADOG INC",
    "DATTO HOLDING CORP",
    "DEALERADVANCE INC",
    "DIGILITI MONEY GROUP INC",
    "DIGIMARC CORP",
    "DIGITAL TURBINE INC",
    "DOCUSIGN INC",
    "DOMO INC",
    "DROPBOX INC",
    "DUCK CREEK TECHNOL INC",
    "DYNATRACE INC",
    "E2OPEN INC",
    "EBIX INC",
    "ECOARK HOLDINGS INC",
    "EGAIN CORP",
    "ELASTIC NETWORKS INC",
    "ELASTIC NV",
    "ELCOM INTERNATIONAL INC",
    "ENTERPRISE INFORMATICS INC",
    "ENVESTNET INC",
    "EVERBRIDGE INC",
    "EVOLVING SYSTEMS INC",
    "EZENIA INC",
    "FAIR ISAAC CORP",
    "FALCONSTOR SOFTWARE INC",
    "FANTASY ACES DAILY FANTASY",
    "FASTLY INC",
    "FIREEYE INC",
    "FIVE9 INC",
    "FLEXSHARES IBOXX 3-YR TAR FD",
    "FLEXSHARES IBOXX 5-YR TAR FD",
    "FORTINET INC",
    "FRIENDFINDER NETWORKS INC",
    "GIVEMEPOWER CORP",
    "GRANDPARENTS.COM INC",
    "GREEN POLKADOT BOX INC",
    "GSE SYSTEMS INC",
    "GTY TECHNOLOGY HOLDINGS",
    "GUIDEWIRE SOFTWARE INC",
    "HOPTO INC",
    "HRSOFT INC",
    "HUBSPOT INC",
    "IBSG INTERNATIONAL INC",
    "IDEANOMICS INC",
    "IMAGEWARE SYSTEMS INC",
    "INFORMATION RESOURCES INC",
    "INTEGRATED BUSINESS SYS &SVC",
    "INTELLIGENT SYSTEM CORP",
    "INTELLINETICS INC",
    "INTERMAP TECHNOLOGIES CORP",
    "INTERNATIONAL LEADERS CAP CO",
    "INTRUSION INC",
    "INTUIT INC",
    "INUVO INC",
    "IRONCLAD ENCRYPTION CORP",
    "ISHARES IBOXX HIGH YLD CP BD",
    "ISHARES IBOXX INVST GR CP BD",
    "ISIGN SOLUTIONS INC",
    "ISOCIALY INC",
    "ISSUER DIRECT CORP",
    "IVEDA SOLUTIONS INC",
    "J2 GLOBAL INC",
    "JACK IN THE BOX INC",
    "JAMF HOLDING CORP",
    "JDA SOFTWARE GROUP INC",
    "JFROG LTD",
    "KIWIBOX COM INC",
    "KRONOS INC",
    "LAWSON SOFTWARE INC",
    "LEVELBLOX INC",
    "LIQUI-BOX CORP",
    "LIQUID HOLDINGS GROUP INC",
    "LIVE MICROSYSTEMS INC",
    "LIVEPERSON INC",
    "MAIL BOXES ETC",
    "MANHATTAN ASSOCIATES INC",
    "MARIN SOFTWARE INC",
    "MAX SOUND CORP",
    "MEDALLIA INC",
    "MEDALLIANCE INC",
    "MEDIATECHNICS CORP",
    "MGT CAPITAL INVESTMENTS INC",
    "MICROSOFT CORP",
    "MICROSTRATEGY INC",
    "MITEK SYSTEMS INC",
    "MIX TELEMATICS LTD",
    "MOBILEIRON INC",
    "MODEL N INC",
    "MONGODB INC",
    "MONSTER ARTS",
    "NCINO INC",
    "NEOMEDIA TECHNOLOGIES INC",
    "NETSOL TECHNOLOGIES INC",
    "NEW RELIC INC",
    "NORTONLIFELOCK INC",
    "NOTIFY TECHNOLOGY CORP",
    "NUANCE COMMUNICATIONS INC",
    "NUTANIX INC",
    "OBLONG INC",
    "OKTA INC",
    "OMTOOL LTD",
    "ONESPAN INC",
    "ORACLE CORP",
    "PAGERDUTY INC",
    "PAID INC",
    "PALANTIR TECHNOLOG INC",
    "PALO ALTO NETWORKS INC",
    "PARETEUM CORP",
    "PARK CITY GROUP INC",
    "PAYBOX CORP",
    "PAYCHEX INC",
    "PAYCOM SOFTWARE INC",
    "PAYLOCITY HOLDING CORP",
    "PEGASYSTEMS INC",
    "PHUNWARE INC",
    "PING IDENTITY HOLDING CORP",
    "PLURALSIGHT INC",
    "PRIMAL SOLUTIONS INC",
    "PROGRESS SOFTWARE CORP",
    "PROOFPOINT INC",
    "PROS HOLDINGS INC",
    "PTC INC",
    "PULSE EVOLUTION CORP",
    "Q2 HOLDINGS INC",
    "QAD INC",
    "QUALYS INC",
    "QUANTGATE SYSTEMS INC",
    "QUMU CORP",
    "RAADR INC",
    "RAND WORLDWIDE INC",
    "RAPID7 INC",
    "REALNETWORKS INC",
    "REALPAGE INC",
    "RIGHTSCORP INC",
    "RINGCENTRAL INC",
    "RIOT BLOCKCHAIN INC",
    "ROCKETFUEL BLOCKCHAIN INC",
    "RORINE INTL HOLDING CORP",
    "ROSETTA STONE INC",
    "SAILPOINT TECHNO HLDG",
    "SALESFORCE.COM INC",
    "SCIENT INC",
    "SEACHANGE INTERNATIONAL INC",
    "SECUREWORKS CORP",
    "SERVICENOW INC",
    "SHARPSPRING INC",
    "SHOTSPOTTER INC",
    "SIMTROL INC",
    "SITO MOBILE LTD",
    "SKYBOX INTL INC",
    "SLACK TECHNOLOGIES INC",
    "SMARTMETRIC INC",
    "SMARTSHEET INC",
    "SMITH MICRO SOFTWARE INC",
    "SNOWFLAKE INC",
    "SOFTECH INC",
    "SOLARWINDS CORP",
    "SONIC FOUNDRY INC",
    "SPLUNK INC",
    "SPROUT SOCIAL INC",
    "SPS COMMERCE INC",
    "SS&C TECHNOLOGIES HLDGS INC",
    "SSI INVESTMENTS II LTD",
    "SUMO LOGIC INC",
    "SVMK INC",
    "SYNACOR INC",
    "SYNCHRONOSS TECHNOLOGIES",
    "SYNOPSYS INC",
    "TAUTACHROME INC",
    "TELENAV INC",
    "TENABLE HOLDINGS INC",
    "TERADATA CORP",
    "THEGLOBE.COM INC",
    "TIBCO SOFTWARE INC",
    "TINTRI INC",
    "TMM INC",
    "TRADE DESK INC",
    "TWILIO INC",
    "TYLER TECHNOLOGIES INC",
    "ULTIMATE SOFTWARE GROUP INC",
    "UNITRONIX CORP",
    "UNITY SOFTWARE INC",
    "UPLAND SOFTWARE INC",
    "VANCORD CAPITAL INC",
    "VARONIS SYSTEMS INC",
    "VDO-PH INTERNATIONAL INC",
    "VEEVA SYSTEMS INC",
    "VERB TECHNOLOGY CO INC",
    "VERINT SYSTEMS INC",
    "VERITONE INC",
    "VERTEX INC",
    "VERTICAL COMPUTER SYS INC",
    "VIRNETX HOLDING CORP",
    "VIVA ENTERTAINMENT GROUP INC",
    "VMWARE INC -CL A",
    "VOYAGER DIGITAL LTD",
    "VUBOTICS INC",
    "WOD RETAIL SOLUTIONS",
    "WORKDAY INC",
    "WORKIVA INC",
    "XCELMOBILITY INC",
    "XPERI HOLDING CORP",
    "YAPPN CORP",
    "YEXT INC",
    "ZENDESK INC",
    "ZIX CORP",
    "ZOOM TELEPHONICS INC",
    "ZOOM VIDEO COMUNICATIONS INC",
    "ZOOMAWAY TRAVEL INC",
    "ZOOMINFO TECHNOLOGIES",
    "ZSCALER INC",
    "ZUORA INC",
]

def getTicker (company_name):
    url = "https://query1.finance.yahoo.com/v1/finance/search?q={}".format(company_name)

    payload={}
    headers = {
        'authority': 'query1.finance.yahoo.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://finance.yahoo.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://finance.yahoo.com/quote/TDCH?p=TDCH&.tsrc=fin-srch',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'B=b8bhl5pg65nca&b=3&s=ma; A1=d=AQABBIrdYmACEMNyMh4Ej8HrF-db1C41LrQFEgEBBgGhOGIaY1lQb2UB_eMBAAcIit1iYC41LrQ&S=AQAAAjcrG_EiOtBU3MtXTfPeDeE; A3=d=AQABBIrdYmACEMNyMh4Ej8HrF-db1C41LrQFEgEBBgGhOGIaY1lQb2UB_eMBAAcIit1iYC41LrQ&S=AQAAAjcrG_EiOtBU3MtXTfPeDeE; A1S=d=AQABBIrdYmACEMNyMh4Ej8HrF-db1C41LrQFEgEBBgGhOGIaY1lQb2UB_eMBAAcIit1iYC41LrQ&S=AQAAAjcrG_EiOtBU3MtXTfPeDeE&j=WORLD; GUC=AQEBBgFiOKFjGkIfLgR6; cmp=t=1647795591&j=0; PRF=t%3DTDCH'
    }


    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    company_code = ""

    if data['quotes']:
        company_code = data['quotes'][0]['symbol']
    return company_code

def getCIKs(ticker):
    URL = 'http://www.sec.gov/cgi-bin/browse-edgar?CIK={}&Find=Search&owner=exclude&action=getcompany'
    headers = {'Host': 'www.sec.gov', 'Connection': 'close',
         'Accept': 'application/json, text/javascript, */*; q=0.01', 'X-Requested-With': 'XMLHttpRequest',
         'User-Agent': 'test@test.com',
         }
    # headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
    CIK_RE = re.compile(r'.*CIK=(\d{10}).*')    
    f = requests.get(URL.format(ticker.lower()), headers, stream = True)
    print(f.text)
    results = CIK_RE.findall(f.text)
    if len(results):
        results[0] = int(re.sub('\.[0]*', '.', results[0]))
        return str(results[0])

if __name__ == "__main__":
    # Create a new connection object and initialize with the required database
    client = MongoClient('mongodb://admin:PASSWORD@20.102.85.148:27017/')
    db = client.da_new

    ciks = {}
    f = open('ticker.txt')
    for line in f.readlines():
        out = line.split("\t")
        ciks[out[0].strip()] = re.sub(r"[\n\t\s]*", "", out[1])

    for each in companies:
        ticker = getTicker(each)
        print(ticker)
        if not ticker:
            continue

        if not db.companies.find_one({ "symbol": ticker }):
            if ticker.lower() in ciks:
                cik = ciks[ticker.lower()]
                print(cik)
                db.companies.insert_one({ "name": each, "cik": cik, "symbol": ticker, "filingStart": "6236e98723bdfe662ea3be12" })