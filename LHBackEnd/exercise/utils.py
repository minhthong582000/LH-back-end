from django.http import Http404

from .models import Courses


# we will be having query_related work here in utils, or some other utils methods,
# we can replace this file to services too for better understanding
def get_all_un_hide_courses():
    return Courses.objects.filter()


def get_course_object(slug):
    try:
        return Courses.objects.get(slug=slug)
    except Courses.DoesNotExist:
        raise Http404


def update_course(course, request_data):
    course.title = request_data.get('title', course.title)
    course.number = request_data.get('number', course.number)
    course.description = request_data.get('description', course.description)
    course.start_date = request_data.get('start_date', course.start_date)
    course.end_date = request_data.get('end_date', course.end_date)
    course.save()
    return course