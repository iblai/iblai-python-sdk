# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.36-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.engagement_per_course import EngagementPerCourse

class TestEngagementPerCourse(unittest.TestCase):
    """EngagementPerCourse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EngagementPerCourse:
        """Test EngagementPerCourse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EngagementPerCourse`
        """
        model = EngagementPerCourse()
        if include_optional:
            return EngagementPerCourse(
                data = [
                    iblai.models.engagement_per_course_data.EngagementPerCourseData(
                        course_id = '', 
                        course_start = '', 
                        course_end = '', 
                        average_days = 56, 
                        average_time_spent = 1.337, 
                        name = '', )
                    ],
                pagination = iblai.models.pagination.Pagination(
                    total_items = 56, 
                    current_page = 56, 
                    per_page = 56, 
                    total_pages = 56, )
            )
        else:
            return EngagementPerCourse(
                pagination = iblai.models.pagination.Pagination(
                    total_items = 56, 
                    current_page = 56, 
                    per_page = 56, 
                    total_pages = 56, ),
        )
        """

    def testEngagementPerCourse(self):
        """Test EngagementPerCourse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()