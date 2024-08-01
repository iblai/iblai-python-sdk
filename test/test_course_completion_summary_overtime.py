# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.3.38-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.course_completion_summary_overtime import CourseCompletionSummaryOvertime

class TestCourseCompletionSummaryOvertime(unittest.TestCase):
    """CourseCompletionSummaryOvertime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CourseCompletionSummaryOvertime:
        """Test CourseCompletionSummaryOvertime
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CourseCompletionSummaryOvertime`
        """
        model = CourseCompletionSummaryOvertime()
        if include_optional:
            return CourseCompletionSummaryOvertime(
                data = iblai.models.course_completion_summary_data_overtime.CourseCompletionSummaryDataOvertime(
                    overtime = {
                        'key' : null
                        }, 
                    total_user_count = 56, 
                    completed_count = 56, 
                    completed_percent = 1.337, ),
                meta = iblai.models.overtime_meta.OvertimeMeta(
                    total = 56, 
                    change_range = 56, 
                    change_last_seven_days = 56, 
                    change_last_thirty_days = 56, 
                    change_last_seven_days_percent = 1.337, 
                    change_last_thirty_days_percent = 1.337, 
                    change_range_percent = 1.337, )
            )
        else:
            return CourseCompletionSummaryOvertime(
                data = iblai.models.course_completion_summary_data_overtime.CourseCompletionSummaryDataOvertime(
                    overtime = {
                        'key' : null
                        }, 
                    total_user_count = 56, 
                    completed_count = 56, 
                    completed_percent = 1.337, ),
                meta = iblai.models.overtime_meta.OvertimeMeta(
                    total = 56, 
                    change_range = 56, 
                    change_last_seven_days = 56, 
                    change_last_thirty_days = 56, 
                    change_last_seven_days_percent = 1.337, 
                    change_last_thirty_days_percent = 1.337, 
                    change_range_percent = 1.337, ),
        )
        """

    def testCourseCompletionSummaryOvertime(self):
        """Test CourseCompletionSummaryOvertime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
