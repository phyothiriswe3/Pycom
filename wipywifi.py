from network import WLAN
wlan = WLAN(mode=WLAN.STA)nets = wlan.scan()
for net in nets:
    if net.ssid == 'Now Makerspace':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'nowmakerspace2020'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break
