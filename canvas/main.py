"""
Comments:
    The Assignment Class is incomplete. Or rather, we need to define more Assignment classes, as Canvas recognizes different 
    classes of assignments with different numbers of attributes. So when the info from r.json is used to 
    instantiate an Assignment, it doesn't work.
"""

import requests
import os


class User:
    """Corresponds to the Canvas Class in the branch dev."""

    def __init__(
        self,
        token=os.getenv("MY_CANVAS_TOKEN"),
        url="https://uvu.instructure.com/api/v1",
    ):
        self.token = token
        self.url = url
        self.courses = []
        self.assignments = []

    def get_courses(
        self, enrollment_type: str = "student", enrollment_state: str = "active"
    ):
        """Get all the courses for the user."""
        r = requests.get(
            self.url
            + "/courses"
            + f"?enrollment_type={enrollment_type}&enrollment_state={enrollment_state}",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        num = 0
        input(r.json())
        for course in r.json():
            num += 1
            self.courses.append(Course(course, num))
        return r.json()  # in case you still want to work with the dictionary

    def get_assignments(
        self, enrollment_type: str = "student", enrollment_state: str = "active", bucket: str = 'upcoming'
    ):
        """Get all the courses for the user. It doesn't work"""
        r = requests.get(
            self.url
            + "/courses"
            + f"/{self.courses[0].id}"
            + "//assignments"
            + f"?enrollment_type={enrollment_type}&enrollment_state={enrollment_state}&bucket={bucket}",
            headers={"Authorization": f"Bearer {self.token}"},
        )
        for assignment in r.json():
            print(assignment)
            input()
            self.assignments.append(Assignment(assignment))
        return r.json()  # in case you still want to work with the dictionary


class Course:
    """New class for storing attributes related to the courses."""

    def __init__(self, dictionary, num):
        self.num = num
        self.id = dictionary["id"]
        self.name = dictionary["name"]
        self.account_id = dictionary["account_id"]
        self.uuid = dictionary["uuid"]
        self.start_at = dictionary["start_at"]
        self.grading_standard_id = dictionary["grading_standard_id"]
        self.is_public = dictionary["is_public"]
        self.created_at = dictionary["created_at"]
        self.course_code = dictionary["course_code"]
        self.default_view = dictionary["default_view"]
        self.root_account_id = dictionary["root_account_id"]
        self.enrollment_term_id = dictionary["enrollment_term_id"]
        self.license = dictionary["license"]
        self.grade_passback_setting = dictionary["grade_passback_setting"]
        self.end_at = dictionary["end_at"]
        self.public_syllabus = dictionary["public_syllabus"]
        self.public_syllabus_to_auth = dictionary["public_syllabus_to_auth"]
        self.storage_quota_mb = dictionary["storage_quota_mb"]
        self.is_public_to_auth_users = dictionary["is_public_to_auth_users"]
        self.homeroom_course = dictionary["homeroom_course"]
        self.course_color = dictionary["course_color"]
        self.friendly_name = dictionary["friendly_name"]
        self.apply_assignment_group_weights = dictionary[
            "apply_assignment_group_weights"
        ]
        self.calendar = dictionary["calendar"]
        self.time_zone = dictionary["time_zone"]
        self.blueprint = dictionary["blueprint"]
        self.template = dictionary["template"]
        self.enrollments = dictionary["enrollments"]
        self.hide_final_grades = dictionary["hide_final_grades"]
        self.workflow_state = dictionary["workflow_state"]
        self.restrict_enrollments_to_course_dates = dictionary[
            "restrict_enrollments_to_course_dates"
        ]

    def __repr__(self):
        return f"Course({self.name}, {self.id})"

    def __str__(self):
        return f"{self.num: <5}. {self.name}"


class Assignment:
    def __init__(self, dictionary):
        self.id = dictionary["id"]
        self.due_at = dictionary["due_at"]
        self.unlock_at = dictionary["unlock_at"]
        self.lock_at = dictionary["lock_at"]
        self.points_possible = dictionary["points_possible"]
        self.grading_type = dictionary["grading_type"]
        self.assignment_group_id = dictionary["assignment_group_id"]
        self.grading_standard_id = dictionary["grading_standard_id"]
        self.created_at = dictionary["created_at"]
        self.updated_at = dictionary["updated_at"]
        self.peer_reviews = dictionary["peer_reviews"]
        self.automatic_peer_reviews = dictionary["automatic_peer_reviews"]
        self.position = dictionary["position"]
        self.grade_group_students_individually = dictionary[
            "grade_group_students_individually"
        ]
        self.anonymous_peer_reviews = dictionary["anonymous_peer_reviews"]
        self.group_category_id = dictionary["group_category_id"]
        self.post_to_sis = dictionary["post_to_sis"]
        self.moderated_grading = dictionary["moderated_grading"]
        self.omit_from_final_grade = dictionary["omit_from_final_grade"]
        self.intra_group_peer_reviews = dictionary["intra_group_peer_reviews"]
        self.anonymous_instructor_annotations = dictionary[
            "anonymous_instructor_annotations"
        ]
        self.anonymous_grading = dictionary["anonymous_grading"]
        self.graders_anonymous_to_graders = dictionary["graders_anonymous_to_graders"]
        self.grader_count = dictionary["grader_count"]
        self.grader_comments_visible_to_graders = dictionary[
            "grader_comments_visible_to_graders"
        ]
        self.final_grader_id = dictionary["final_grader_id"]
        self.grader_names_visible_to_final_grader = dictionary[
            "grader_names_visible_to_final_grader"
        ]
        self.allowed_attempts = dictionary["allowed_attempts"]
        self.annotatable_attachment_id = dictionary["annotatable_attachment_id"]
        self.hide_in_gradebook = dictionary["hide_in_gradebook"]
        self.lock_info = dictionary["lock_info"]
        self.secure_params = dictionary["secure_params"]
        self.lti_context_id = dictionary["lti_context_id"]
        self.course_id = dictionary["course_id"]
        self.name = dictionary["name"]
        self.submission_types = dictionary["submission_types"]
        self.has_submitted_submissions = dictionary["has_submitted_submissions"]
        self.due_date_required = dictionary["due_date_required"]
        self.max_name_length = dictionary["max_name_length"]
        self.in_closed_grading_period = dictionary["in_closed_grading_period"]
        self.graded_submissions_exist = dictionary["graded_submissions_exist"]
        self.is_quiz_assignment = dictionary["is_quiz_assignment"]
        self.can_duplicate = dictionary["can_duplicate"]
        self.original_course_id = dictionary["original_course_id"]
        self.original_assignment_id = dictionary["original_assignment_id"]
        self.original_lti_resource_link_id = dictionary["original_lti_resource_link_id"]
        self.original_assignment_name = dictionary["original_assignment_name"]
        self.original_quiz_id = dictionary["original_quiz_id"]
        self.workflow_state = dictionary["workflow_state"]
        self.important_dates = dictionary["important_dates"]
        self.description = dictionary["description"]
        self.muted = dictionary["muted"]
        self.html_url = dictionary["html_url"]
        self.quiz_id = dictionary["quiz_id"]
        self.anonymous_submissions = dictionary["anonymous_submissions"]
        self.published = dictionary["published"]
        self.only_visible_to_overrides = dictionary["only_visible_to_overrides"]
        self.locked_for_user = dictionary["locked_for_user"]
        self.lock_explanation = dictionary["lock_explanation"]
        self.submissions_download_url = dictionary["submissions_download_url"]
        self.post_manually = dictionary["post_manually"]
        self.anonymize_students = dictionary["anonymize_students"]
        self.require_lockdown_browser = dictionary["require_lockdown_browser"]
        self.restrict_quantitative_data = dictionary["restrict_quantitative_data"]


def main():
    user = User()
    user.get_courses()
    for course in user.courses:
        print(course)
    user.get_assignments()
    for assignment in user.assignments:
        print(assignment)


if __name__ == "__main__":
    main()
