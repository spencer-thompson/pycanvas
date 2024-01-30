"""
This is the module contains the Canvas class.

This is the wrapper around the Canvas API.
"""
import requests
import os

class Canvas:

    def __init__(
        self,
        token: str | None,
        url: str = "https://uvu.instructure.com/api/v1",
    ):
        """
        Initialize the Canvas object with the given personal access token.
        """
        # try:
        #     self.token = os.environ["MY_CANVAS_TOKEN"]
        #
        #     if self.token is None:
        #         raise KeyError
        #
        # except KeyError:
        #     print("Please set the environment variable MY_CANVAS_TOKEN to your personal access token.")
        #     exit(1)

        self.token = token
        self.url = url

    def courses(
        self,
        enrollment_type: str = "student",
        enrollment_state: str = "active",
    ):
        """
        Get all the courses for the user.
        """
        r = requests.get(
            self.url + "/courses" + f"?enrollment_type={enrollment_type}&enrollment_state={enrollment_state}",
            headers={"Authorization": f"Bearer {self.token}"}
        )

        return r.json()

if __name__ == "__main__":
    client = Canvas(os.getenv("MY_CANVAS_TOKEN"))

    for course in client.courses():
        # print(course["name"])
        for k, v in course.items():
            print(k, v)
