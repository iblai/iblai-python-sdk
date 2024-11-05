# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.time_spent_per_course import TimeSpentPerCourse

class TestTimeSpentPerCourse(unittest.TestCase):
    """TimeSpentPerCourse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeSpentPerCourse:
        """Test TimeSpentPerCourse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeSpentPerCourse`
        """
        model = TimeSpentPerCourse()
        if include_optional:
            return TimeSpentPerCourse(
                data = [
                    iblai.models.time_spent_per_course_data.TimeSpentPerCourseData(
                        name = '', 
                        course_id = '', 
                        time_spent = 56, 
                        course_start = '', 
                        course_end = '', 
                        average_time = 1.337, )
                    ],
                pagination = iblai.models.pagination.Pagination(
                    total_items = 56, 
                    current_page = 56, 
                    per_page = 56, 
                    total_pages = 56, )
            )
        else:
            return TimeSpentPerCourse(
                pagination = iblai.models.pagination.Pagination(
                    total_items = 56, 
                    current_page = 56, 
                    per_page = 56, 
                    total_pages = 56, ),
        )
        """

    def testTimeSpentPerCourse(self):
        """Test TimeSpentPerCourse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
