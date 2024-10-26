from .courses import courses


def total_duration():

    return sum(course.duration for course in courses)
