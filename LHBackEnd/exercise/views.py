from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


from . import utils
from .serializers import CourseSerializer, ScheduleSerializer


# returning course list
class CourseList(APIView):
    serializer_class = CourseSerializer
    permission_classes = (AllowAny,)

    def get(self, request):
        courses = utils.get_all_un_hide_courses()
        courses_serializer = CourseSerializer(courses, context={'request': request}, many=True)
        return Response(courses_serializer.data)

    def post(self, request):
        # if not request.user.is_superuser:
        #     return Response('Your are not authorize to perform this action', status=status.HTTP_400_BAD_REQUEST)

        courses_serializer = CourseSerializer(data=request.data, context={'request': request})
        if courses_serializer.is_valid():
            courses_serializer.save()
        else:
            return Response(courses_serializer.errors)
        return Response(courses_serializer.data)


class CourseDetails(APIView):
    serializer_class = CourseSerializer
    permission_classes = (AllowAny,)

    def get(self, request, slug):
        courses = utils.get_course_object(slug)
        courses_serializer = CourseSerializer(courses, context={'request': request})
        return Response(courses_serializer.data)

    def put(self, request, slug):
        # if not request.user.is_superuser:
        #     return Response('Your are not authorize to perform this action', status=status.HTTP_400_BAD_REQUEST)

        try:
            course = utils.get_course_object(slug)
            course = utils.update_course(course, request.data)
        except Exception as e:
            print(e)
            return Response('Course not found.', status=status.HTTP_400_BAD_REQUEST)

        return Response(CourseSerializer(course).data)

    def delete(self, request, slug):
        # if not request.user.is_superuser:
        #     return Response('Your are not authorize to perform this action', status=status.HTTP_400_BAD_REQUEST)

        course = utils.get_course_object(slug)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ScheduleList(APIView):
    serializer_class = ScheduleSerializer
    permission_classes = (AllowAny,)

    def get(self, request):
        schedule = utils.get_all_schedule()
        schedule_serializer = ScheduleSerializer(schedule, context={'request': request}, many=True)
        return Response(schedule_serializer.data)

    def post(self, request):
        schedule_serializer = ScheduleSerializer(data=request.data, context={'request': request})
        if schedule_serializer.is_valid():
            schedule_serializer.save()
        else:
            return Response(schedule_serializer.errors)
        return Response(schedule_serializer.data)

class ScheduleDetail(APIView):
    serializer_class = ScheduleSerializer
    permission_classes = (AllowAny,)

    def get(self, request, userid):
        schedule = utils.get_schedule_by_userid(userid)
        schedule_serializer = ScheduleSerializer(schedule, context={'request': request}, many=True)
        return Response(schedule_serializer.data)

    def delete(self, request, userid):
        schedule = utils.get_schedule_by_pk(userid)
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)