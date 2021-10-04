# import urllib library
from urllib.request import urlopen
import json
from pypresence import Presence
from pathlib import Path

import time
import yaml
import io
import os

get_nickname = "none"
nickname_isExist = False

def start():  

    rpc = Presence("890789468150329414")
    rpc.connect()
    lasttrigger = time.time()
    print(type(lasttrigger))
    successmessage = "none"

    print("Rich Presence Discord for Pumpkincraft server")
    print("> Version: 0.1 Alpha-1")
    print("> Author: Low_Scarlet")
    print("> Project Name: Rich Presence Discord For Pumpkincraft")
    print("")
    print("© 2021 pumpkinProject. All rights reserved.")
    print("")
    get_nickname = str(input("Nickname: "))
    print("")
    print("Berhasil input nickname :D")

    while True: 
        url = "http://sg-1.leyzstore.net:8200/"
        
        response = urlopen(url)
        data = str(response.read())
        data = data.split("///")
        data = data[1].split("|||")
        database = list()
        count = "none"

        for i, listed_data in enumerate(data):
            if count == "none":
                count = 0
            else:
                count += 1

            nickname_n_data = listed_data.split(":+++")
            nickname = nickname_n_data[0]
            subdata = nickname_n_data[1].split(">>>")
            lastlogin = subdata[0]
            status = subdata[1]
            database.append({nickname: [{"lastlogin":lastlogin}, {"status":status}]})
            
            if nickname == get_nickname:
                index = count
                nickname_isExist = True
                break
            else:
                nickname_isExist = False

        if nickname_isExist == True:
            if database[index][get_nickname][0]["lastlogin"] != "not-found":
                timespan = float(database[index][get_nickname][0]["lastlogin"])
            else:  
                timespan = lasttrigger
            
            if database[index][get_nickname][1]["status"] == "Logging out.." or "Not registered yet!":
                smallimage_id = "yellow_circle"
            elif database[index][get_nickname][1]["status"] == "Offline":
                smallimage_id = "red_circle"
            else:
                smallimage_id = "green_circle"

            rpc.update(
                details="Nickname: " + get_nickname,
                state=" - " + database[index][get_nickname][1]["status"],
                large_image="large",
                small_image=smallimage_id,
                start=timespan,
                large_text="@pumpkinProject: Pumpkincraft",
                buttons=[
                        {"label": "IP: mc.pumpkinproject-id.com", "url": "http://mc.pumpkinproject-id.com"},
                        {"label": "Discord Server", "url": "https://discord.gg/UYhQCqUj6F"}
                    ])
            if successmessage == "none":
                successmessage = True
                print("Berhasil mendapatkan data untuk nickname", get_nickname)
            time.sleep(5)

        else:
            print("Nickname tidak ditemukan!, pastikan kamu sudah join ke dalam server setidaknya 1x sebelum server restart!")
            break
    str(input("System di close karena error? lakukan report kepada owner untuk bantuan!, ketik apa aja untuk close!: "))
start()

str(input("System di close karena error? lakukan report kepada owner untuk bantuan!, ketik apa aja untuk close!: "))