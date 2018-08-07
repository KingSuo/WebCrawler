# -*- coding: utf-8 -*-
import os
import json
from multiprocessing import pool as ProcessPoll
from multiprocessing.dummy import Pool as ThreadPool

import requests
from bs4 import BeautifulSoup


class WebCrawler(object):
    def __init__(self):
        base_path, _ = os.path.split(__file__)
        save_path = os.path.join(base_path, "File")
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        self.save_path = save_path

    def get_urls(self, url):
        result = requests.get(url)
        soup = BeautifulSoup(result.content, "html.parser")
        _, filename = os.path.split(url.split("://")[1])
        print(soup.find_all("tr")[16:])
        d = {}
        for i in soup.find_all("tr")[16:]:
            api_class = i.em.string
            print("api_class: ", api_class)
            method = i.strong.string
            print("method: ", method)
            url = "https://github.com%s" % i.a["href"].lstrip()
            print("url: ", url)
            http_request = i.find_all("td")[-2].strong.string + \
                           str(i.find_all("td")[-2]).split("</strong>")[1].split("<")[
                               0]
            print("HTTP request: ", http_request)

            d[url] = (method, api_class, http_request)

        with open(os.path.join(self.save_path, filename + ".json"), "w") as fd:
            json.dump(d, fd)
            fd.write('\n')

    def get_param(self):
        pass

    def save_html(self, api_vision, method, html_data):
        save_path = os.path.join("F:\workspace\git\WebCrawler\File", api_vision)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        with open("%s/%s.html" % (save_path, method), "w", encoding="utf-8") as fd:
            fd.writelines(str(html_data))


if __name__ == "__main__":

    path = "F:\workspace\git\WebCrawler\File\AppsV1Api\create_namespaced_deployment.html"
    soup = BeautifulSoup(open(path, encoding="utf-8"), "html.parser")
    tables = soup.find_all("table")
    print(len(tables))
    for i in tables:
        print(i)
