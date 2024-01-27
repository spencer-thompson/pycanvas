"""
Docstring just to push
"""

import requests
import os

def courses(enrollment_state = 'active'):
    token = os.getenv('MY_CANVAS_TOKEN')
    url = 'https://uvu.instructure.com/api/v1/courses'

    r = requests.get(url+'?enrollment_state='+enrollment_state, headers = {'Authorization': 'Bearer ' + str( token )})

    return r.json()

def main():
    # print(courses())
    for course in courses():
        print(course['name'])

if __name__ == "__main__":
    main()
