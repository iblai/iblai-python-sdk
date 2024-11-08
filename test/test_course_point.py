# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.course_point import CoursePoint

class TestCoursePoint(unittest.TestCase):
    """CoursePoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoursePoint:
        """Test CoursePoint
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoursePoint`
        """
        model = CoursePoint()
        if include_optional:
            return CoursePoint(
                course_id = '',
                points = 56
            )
        else:
            return CoursePoint(
                course_id = '',
                points = 56,
        )
        """

    def testCoursePoint(self):
        """Test CoursePoint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
