import requests
import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
import pprint
import tweepy
import re
import time

from selenium.webdriver import Keys

pp = pprint.PrettyPrinter(indent=4)

server_id = ['963457354966376448', '982497246023122974']
discords = ['961662560086671391', '976845236523397142']


headers = {'authorization': 'MjMwMzY3MTY1NjQ2MjQxNzkz.Gdvje0.crxOLXlu-T1DEI5jjy1DFS-egsGXFhUqgT_-nQ'}
outside_list = []


while True:
    for server in server_id:
        index = server_id.index(server)
        channel_id = server
        outside_list = []
        r = requests.get('https://discord.com/api/v9/channels/' + channel_id + '/messages?limit=50', headers=headers)
        j = json.loads(r.text)
        outside_list.append(j)
        # get_last_50_messages_from_channel('982497246023122974')
        # pp.pprint(outside_list[0][6])
        battle_royal_location = []
        try:
            for x in range(0, 24):
                if outside_list[0][x]['embeds']:
                    if "description" not in outside_list[0][x]['embeds'][0]:
                        pass
                    elif ("Click the emoji below to join." in outside_list[0][x]['embeds'][0]['description']) and (outside_list[0][x]['reactions'][0]['me'] == False):
                        print("yes at: " + str(x))
                        battle_royal_location.append(x)
                    else:
                        pass
                else:
                    pass
                    print("no at: " + str(x) + " on server: " + discords[index])
        except:
            pass
            # if "Click the emoji below to join." in outside_list[0][x]['embeds'][0]['description']:
            #     print("yes")
        if(len(battle_royal_location) != 0):
            print(battle_royal_location[0])
            print(str(outside_list[0][battle_royal_location[0]]))
            options = Options()
            options.headless = False
            driver = webdriver.Firefox(options=options, executable_path='C:\\Users\\lmicu\\Documents\\selenium\\geckodriver.exe')
            driver.get('https://discord.com/login')
            time.sleep(5)
            discord_channel = driver.find_element_by_xpath("//input[@name='email']")
            discord_channel.click()
            discord_channel.send_keys("bsorbun@gmail.com")
            time.sleep(1)
            discord_channel.send_keys(Keys.TAB)
            discord_channel = driver.find_element_by_xpath("//input[@name='password']")
            discord_channel.send_keys("Da1andOnlyBOGG@")
            time.sleep(1)
            discord_channel.send_keys(Keys.TAB)
            discord_channel.send_keys(Keys.TAB)
            discord_channel.send_keys(Keys.ENTER)
            time.sleep(1)
            time.sleep(1)
            time.sleep(10)
            driver.get('https://discord.com/channels/' + str(discords[index]) + "/" + str(server_id[index]))
            time.sleep(15)
            discord_channel = driver.find_element_by_xpath(
                "//div[@id='message-reactions-" + str(outside_list[0][battle_royal_location[0]]['id']) + "']/div")
            # discord_channel = driver.find_element_by_id("message-reactions-" + str(outside_list[0][battle_royal_location[0]]['id']))
            discord_channel.click()
            driver.close()
            time.sleep(1)
        else:
            print("\n")
            print("nothing so now we wait :)")
            time.sleep(5)
