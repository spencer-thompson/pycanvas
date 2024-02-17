"""
Docstring just to push
"""

import requests
import os

class User:
    def __init__(
            self, 
            token = os.getenv('MY_CANVAS_TOKEN')
            ):
        self.token = token
        self.courses = []

class Course:
    def __init__(
            self,
            id,
            name,
            account_id,
            uuid,
            start_at,
            grading_standard_id,
            is_public,
            created_at,
            course_code,
            default_view,
            root_account_id,
            enrollment_term_id,
            license,
            grade_passback_setting,
            end_at,
            public_syllabus,
            public_syllabus_to_auth,
            storage_quota_mb,
            is_public_to_auth_users,
            homeroom_course,
            course_color,
            friendly_name,
            apply_assignment_group_weights,
            calendar,
            time_zone,
            blueprint,
            template,
            enrollments,
            hide_final_grades,
            workflow_state,
            restrict_enrollments_to_course_dates,
        ):
        self.id = id,
		self.name = name,
		self.account_id = account_id,
		self.uuid = uuid,
		self.start_at = start_at,
		self.grading_standard_id = grading_standard_id,
		self.is_public = is_public,
		self.created_at = created_at,
		self.course_code = course_code,
		self.default_view = default_view,
		self.root_account_id = root_account_id,
		self.enrollment_term_id = enrollment_term_id,
		self.license = license,
		self.grade_passback_setting = grade_passback_setting,
		self.end_at = end_at,
		self.public_syllabus = public_syllabus,
		self.public_syllabus_to_auth = public_syllabus_to_auth,
		self.storage_quota_mb = storage_quota_mb,
		self.is_public_to_auth_users = is_public_to_auth_users,
		self.homeroom_course = homeroom_course,
		self.course_color = course_color,
		self.friendly_name = friendly_name,
		self.apply_assignment_group_weights = apply_assignment_group_weights,
		self.calendar = calendar,
		self.time_zone = time_zone,
		self.blueprint = blueprint,
		self.template = template,
		self.enrollments = enrollments,
		self.hide_final_grades = hide_final_grades,
		self.workflow_state = workflow_state,
		self.restrict_enrollments_to_course_dates = restrict_enrollments_to_course_dates

def courses(token, enrollment_state = 'active'):
    url = 'https://uvu.instructure.com/api/v1/courses'
    r = requests.get(url+'?enrollment_state='+enrollment_state, headers = {'Authorization': 'Bearer ' + str( token )})

    return r.json()

def main():
     user = User()
     courses = courses(user.token)
     for course in courses:
          print(course['name'])

if __name__ == "__main__":
    main()