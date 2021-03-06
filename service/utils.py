import requests
from data_collection_service.settings import API_URL


def req (url):
    """ запрос к серверу API"""
    session = requests.Session()
    r = session.get(url)
    if r.status_code == 400:
        return None
    return r

def get_data_from_api(name):
    '''Формирование данных для API'''
    res_dict = {}

    url = f'{API_URL}{name}/repos'
    r = req(url).json()
    if r and type(r) == list:
        repo_lst =[]
        for repo in r:
            url_rm = f'https://raw.githubusercontent.com/{name}/{repo["name"]}/{repo["default_branch"]}/README.md'
            readme = req(url_rm).text
            d= {"repo": repo.get("name", None),
                "read_me": readme,
                "created": repo.get("created_at",)
                }
            repo_lst.append(d)
        res_dict = {"name": name,
                        "repository":repo_lst }
        return res_dict
    return dict()