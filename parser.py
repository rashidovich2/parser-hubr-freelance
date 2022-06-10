import requests
from bs4 import BeautifulSoup as bs
import configparser
import bot 
import time

config = configparser.ConfigParser()
config.read("config.ini")
URL = config["Telegram"]['url']

pages = [1]
vac = []

async def parser_main_menu():
    while True:
        for p in pages:
            rest = requests.get(f"{URL}&page={p}")
            soup = bs(rest.text, "lxml")
            card_tasks = soup.find_all("li", class_="content-list__item")

            for task in card_tasks:
                link = task.find("div", class_="task__title").find("a").get("href")
                if link[7:] not in vac: 
                    name_task = task.find("div", class_="task__title").text
                    try:
                        price = task.find("span", class_="count").text
                    except Exception as err:
                        price = "договорная"
                    tags = task.find_all("a", class_="tags__item_link")
                    tag = []
                    for t in tags:
                        tag.append(t.text)
                    description = pars_vac(link)
                    time_pub = task.find("span", class_="params__published-at icon_task_publish_at").text 
                    vac.append(link[7:])
                    await bot.send_vacancies(f"{name_task}\n{price}\n\n{description}\nTags: {tag}\n\nTime: {time_pub}\n\nLink: https://freelance.habr.com{link}")
        if len(vac) >= 50:
            del vac[0:5]
        time.sleep(20)
        


def pars_vac(link):
    url = 'https://freelance.habr.com'+link
    rest_task = requests.get(url)
    soup = bs(rest_task.text, "lxml")
    task_description = soup.find("div", class_="task__description").text
    return task_description
