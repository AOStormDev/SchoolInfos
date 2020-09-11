import requests
import json
def SchoolInfos(school=str):
    url = f'https://schoolmenukr.ml/code/api?q={school}'
    response = requests.get(url)
    school_infos = json.loads(response.text)
    return school_infos

# License 5d-jh
# https://github.com/5d-jh
