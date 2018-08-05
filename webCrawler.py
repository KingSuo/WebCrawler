# -*- coding: utf-8 -*-
import os
import json
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
        print(soup)
        _, filename = os.path.split(url.split("://")[1])
        # with open(os.path.join(self.save_path, "%s.txt" % filename), "w") as fd:
        #     fd.writelines(soup)


def clean(string):
    result = string.split("td")
    return result


if __name__ == "__main__":
    # web_crawler = WebCrawler()
    # url = "https://github.com/kubernetes-client/python/tree/master/kubernetes"
    # web_crawler.get_urls(url)

    soup = BeautifulSoup(open("/home/kingsuo/workspace/git/WebCrawler/File/kubernetes.txt"))
    # print(soup.prettify())
    print(soup.find_all("tr")[16:])
    d = {}
    for i in soup.find_all("tr")[16:]:
        api_class = i.em.string
        print("api_class: ", api_class)
        method = i.strong.string
        print("method: ", method)
        url = "https://github.com%s" % i.a["href"].lstrip()
        print("url: ", url)
        http_request = i.find_all("td")[-2].strong.string + str(i.find_all("td")[-2]).split("</strong>")[1].split("<")[0]
        print("HTTP request: ",  http_request)

        d[url] = (method, api_class, http_request)

    with open("/home/kingsuo/workspace/git/WebCrawler/File/kubernetes.json", "w") as fd:
        json.dump(d, fd)
        fd.write('\n')