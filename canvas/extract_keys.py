''''''

import requests
import os

class User:
    def __init__(
            self, 
            token = os.getenv('MY_CANVAS_TOKEN')
            ):
        self.token = token
        self.courses = []


def courses(token, enrollment_state = 'active'):
    url = 'https://uvu.instructure.com/api/v1/courses'
    r = requests.get(url+'?enrollment_state='+enrollment_state, headers = {'Authorization': 'Bearer ' + str( token )})

    return r.json()

def main():
    '''Exports the keys from the json object as a list of attribute assignments'''
    user = User()
    json_object = courses(user.token)
    file = open('keys.txt', 'w')
    for element in json_object:
        print(element['name'])
    for key in json_object[1]:
        file.writelines(f'self.{key} = dictionary[\'{key}\']\n')

if __name__ == "__main__":
    main()