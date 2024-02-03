"""
Docstring just to push
"""

import click
import requests
import os


@click.group()
def main():
    """Canvas CLI Tool"""
    pass


@main.command()
@click.option("--enrollmentstate", default="active", help="An example parameter.")
def courses(enrollmentstate):
    """This sub command runs all interfaces related to courses"""
    token = os.getenv("MY_CANVAS_TOKEN")
    url = "https://uvu.instructure.com/api/v1/courses"
    r = requests.get(
        url,
        params={"enrollment_state": enrollmentstate},
        headers={"Authorization": "Bearer " + str(token)},
    )
    for course in r.json():
        click.echo(course["name"])


if __name__ == "__main__":
    main()
