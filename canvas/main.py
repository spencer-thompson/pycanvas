"""
Docstring just to push
"""

import requests
import os

class User:
    '''Corresponds to the Canvas Class in the branch dev.'''
    def __init__(
        self, 
        token = os.getenv('MY_CANVAS_TOKEN'),
        url = "https://uvu.instructure.com/api/v1"
    ):
        self.token = token
        self.url = url
        self.courses = []

class Course:
    '''New class for storing attributes related to the courses.'''
    def __init__(self, dictionary):
        self.id = dictionary['id']
        self.name = dictionary['name']
        self.account_id = dictionary['account_id']
        self.uuid = dictionary['uuid']
        self.start_at = dictionary['start_at']
        self.grading_standard_id = dictionary['grading_standard_id']
        self.is_public = dictionary['is_public']
        self.created_at = dictionary['created_at']
        self.course_code = dictionary['course_code']
        self.default_view = dictionary['default_view']
        self.root_account_id = dictionary['root_account_id']
        self.enrollment_term_id = dictionary['enrollment_term_id']
        self.license = dictionary['license']
        self.grade_passback_setting = dictionary['grade_passback_setting']
        self.end_at = dictionary['end_at']
        self.public_syllabus = dictionary['public_syllabus']
        self.public_syllabus_to_auth = dictionary['public_syllabus_to_auth']
        self.storage_quota_mb = dictionary['storage_quota_mb']
        self.is_public_to_auth_users = dictionary['is_public_to_auth_users']
        self.homeroom_course = dictionary['homeroom_course']
        self.course_color = dictionary['course_color']
        self.friendly_name = dictionary['friendly_name']
        self.apply_assignment_group_weights = dictionary['apply_assignment_group_weights']
        self.calendar = dictionary['calendar']
        self.time_zone = dictionary['time_zone']
        self.blueprint = dictionary['blueprint']
        self.template = dictionary['template']
        self.enrollments = dictionary['enrollments']
        self.hide_final_grades = dictionary['hide_final_grades']
        self.workflow_state = dictionary['workflow_state']
        self.restrict_enrollments_to_course_dates = dictionary['restrict_enrollments_to_course_dates']

def courses(token, enrollment_state = 'active'):
    '''Returns a json object with several dictionaries, each corresponding with the user's courses in Canvas.'''
    url = 'https://uvu.instructure.com/api/v1/courses'
    r = requests.get(url+'?enrollment_state='+enrollment_state, headers = {'Authorization': 'Bearer ' + str( token )})

    return r.json()

def main():
     user = User()
     courses_list = courses(user.token)
     for course in courses_list:
          user.courses.append(Course(course))
     for course in user.courses:
         print(course.name)

if __name__ == "__main__":
    main()