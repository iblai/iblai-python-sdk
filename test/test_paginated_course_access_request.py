# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.paginated_course_access_request import PaginatedCourseAccessRequest

class TestPaginatedCourseAccessRequest(unittest.TestCase):
    """PaginatedCourseAccessRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedCourseAccessRequest:
        """Test PaginatedCourseAccessRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedCourseAccessRequest`
        """
        model = PaginatedCourseAccessRequest()
        if include_optional:
            return PaginatedCourseAccessRequest(
                count = 56,
                next_page = '',
                previous_page = '',
                results = [
                    iblai.models.course_access_request_detail.CourseAccessRequestDetail(
                        id = 56, 
                        user_id = 56, 
                        username = '', 
                        name = '', 
                        approved = True, 
                        reviewed = True, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        metadata = {
                            'key' : null
                            }, 
                        platform_key = '', 
                        course_id = '', )
                    ]
            )
        else:
            return PaginatedCourseAccessRequest(
                count = 56,
                next_page = '',
                previous_page = '',
                results = [
                    iblai.models.course_access_request_detail.CourseAccessRequestDetail(
                        id = 56, 
                        user_id = 56, 
                        username = '', 
                        name = '', 
                        approved = True, 
                        reviewed = True, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        metadata = {
                            'key' : null
                            }, 
                        platform_key = '', 
                        course_id = '', )
                    ],
        )
        """

    def testPaginatedCourseAccessRequest(self):
        """Test PaginatedCourseAccessRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
