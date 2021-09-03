import requests
from data_collection_service.settings import API_URL


def req (url):
    """ запрос к серверу API"""
    session = requests.Session()
    r = session.get(url)
    return r

def get_data_from_api(name):
    '''Формирование данных для API'''
    res_dict = {}

    url = f'{API_URL}{name}/repos'
    r = req(url).json()
    if r:
        repo_lst =[]
        for repo in r:
            url_rm = f'https://raw.githubusercontent.com/{name}/{repo["name"]}/{repo["default_branch"]}/README.md'
            readme = req(url_rm).text
            d= {"repo": repo["name"],
                "read_me": readme ,
                "created": repo["created_at"]
                }
            repo_lst.append(d)
        res_dict = {"name": name,
                        "repository":repo_lst }
        return res_dict
    return None