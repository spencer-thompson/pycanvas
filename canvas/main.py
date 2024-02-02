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

def assignments(course_id, order_by = 'due_at'):
    token = os.getenv('MY_CANVAS_TOKEN')
    url = 'https://uvu.instructure.com/api/v1/courses'
    url += f'/{course_id}/assignments'

    r = requests.get(url+'?order_by='+order_by, headers = {'Authorization': 'Bearer ' + str( token )})

    return r.json()

def main():
    # print(courses())
    for course in courses():
        print(f"{course['name']} -- COURSE ID:  {course['id']}")
    course_id = input("Input an ID to see assignments: ")
    for assignment in assignments(course_id):
        print(f"{assignment['name']} -- DUE DATE:  {assignment['due_at']}")


if __name__ == "__main__":
    main()
