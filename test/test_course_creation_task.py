# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.course_creation_task import CourseCreationTask

class TestCourseCreationTask(unittest.TestCase):
    """CourseCreationTask unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CourseCreationTask:
        """Test CourseCreationTask
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CourseCreationTask`
        """
        model = CourseCreationTask()
        if include_optional:
            return CourseCreationTask(
                id = 56,
                user_id = '',
                student = 56,
                name = '',
                description = '',
                target_audience = '',
                platform = 56,
                platform_key = '',
                status = 'Pending',
                publish_course = True,
                course_data = None,
                provider = '',
                model = '',
                desired_number_of_sections = 56,
                logs = '',
                files = [
                    iblai.models.course_creation_task_file.CourseCreationTaskFile(
                        id = 56, 
                        course_creation_task = 56, 
                        file = '', 
                        date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return CourseCreationTask(
                id = 56,
                user_id = '',
                student = 56,
                name = '',
                description = '',
                target_audience = '',
                platform = 56,
                platform_key = '',
                status = 'Pending',
                course_data = None,
                logs = '',
                files = [
                    iblai.models.course_creation_task_file.CourseCreationTaskFile(
                        id = 56, 
                        course_creation_task = 56, 
                        file = '', 
                        date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testCourseCreationTask(self):
        """Test CourseCreationTask"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
