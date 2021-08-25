import requests



def serach():
    text = input("Enter the IP address")
    url = "http://{0}/Logs/HealthMonitor.log".format(text)
    word = "HealthMonitorSvc::ShowFaultScreen()"
    page = requests.get(url).text

    while True:
        if word in page:
            break
    print("Game has been crashed please check the EGM of IP address-{0}".format(text))

if __name__=="__main__":
    serach()



