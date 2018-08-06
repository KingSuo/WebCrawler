import json


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


if __name__ == "__main__":
    c = Clean()
    c.clean()
