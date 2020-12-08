import requests
import json
class school:
    def __init__(self, school : str) -> None:
        url = f'https://schoolmenukr.ml/code/api?q={school}'
        response = requests.get(url)
        school_infos = json.loads(response.text)
        self.school = school_infos
    def meal(self):
        for i in self.school['school_infos']:
            code = i['code']
            name = i['name']
        global school
        if '초등' in name:
            school = "elementary"
        if '중학교' in name:
            school = "middle"
        if '고등' in name:
            school = "high"
        mealurl = f'https://schoolmenukr.ml/api/{school}/{code}'
        response = requests.get(mealurl)
        school_menu = json.loads(response.text)
        return school_menu
    
        

# License 5d-jh
# https://github.com/5d-jh
