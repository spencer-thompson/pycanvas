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

def extract_keys_as_parameters():
    '''This function might not work'''
    user = User()
    js_array = courses(user.token)
    file = open('keys.txt', 'w')
    for element in js_array:
        print(element['name'])
    for key in js_array[1]:
        file.writelines(f'\t\t{key},\n')

def extract_keys_as_attributes():
    '''This function might not work'''
    user = User()
    js_array = courses(user.token)
    file = open('keys.txt', 'w')
    for element in js_array:
        print(element['name'])
    for key in js_array[1]:
        file.writelines(f'\t\t\tself.{key} = {key},\n')

extract_keys_as_parameters()