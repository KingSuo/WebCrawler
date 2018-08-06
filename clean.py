import os
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool

import json

import requests
from bs4 import BeautifulSoup


class Clean:
    def __init__(self):
        pass

    def clean(self):
        new_dict = {}
        with open("F:\workspace\git\WebCrawler\File\kubernetes.json") as fp:
            data = json.load(fp)
        for key in data.keys():
            api_vision = data[key][1]
            new_dict[api_vision] = {}
        for key in data.keys():
            api_vision = data[key][1]
            method = data[key][0]
            object_type = method.split("_", 1)[1]
            new_dict[api_vision][object_type] = {}
        for key in data.keys():
            method = data[key][0]
            api_vision = data[key][1]
            fun, object_type = method.split("_", 1)
            new_dict[api_vision][object_type][fun] = method

        print(new_dict["AdmissionregistrationV1alpha1Api"])
        with open("F:\workspace\git\WebCrawler\File\K8s_API.json", "w") as fp:
            json.dump(new_dict, fp, indent=4)

    def get_urls(self):
        new_list = set()
        with open("F:\workspace\git\WebCrawler\File\kubernetes.json") as fp:
            urls = json.load(fp)
        for key in urls.keys():
            new_list.add(key.split("#")[0])
        with open(r"F:\workspace\git\WebCrawler\File\urls.txt", "w") as fp:
            for url in new_list:
                fp.write(url + '\n')
        return urls

    def generate_urls(self):
        with open(r"F:\workspace\git\WebCrawler\File\urls.txt") as fp:
            return fp.read().split('\n')

    def save_html(self, html_data, filename):
        with open(r"F:\workspace\git\WebCrawler\File\HTML\%s.html" % filename, "w", encoding="utf-8") as fp:
            fp.writelines(str(html_data))
            print("Save html file OK!")

    def get_html(self, url):
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        filename = url.split("/")[-1].split(".md")[0]
        self.save_html(str(soup), filename)

    def clean_html(self, ):
        pass


if __name__ == "__main__":
    # c = Clean()
    # urls = c.generate_urls()
    # pool = ProcessPool()
    # results = pool.map(c.get_html, urls)

    soup = BeautifulSoup(open(r"F:\workspace\git\WebCrawler\File\HTML\CoreV1Api.html", encoding="utf-8"), "html.parser")
    strongs = soup.find_all("h1")[2:]
    print(len(strongs))
    for i in strongs:
        print(i.a["href"])
