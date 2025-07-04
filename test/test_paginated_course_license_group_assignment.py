# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.paginated_course_license_group_assignment import PaginatedCourseLicenseGroupAssignment

class TestPaginatedCourseLicenseGroupAssignment(unittest.TestCase):
    """PaginatedCourseLicenseGroupAssignment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedCourseLicenseGroupAssignment:
        """Test PaginatedCourseLicenseGroupAssignment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedCourseLicenseGroupAssignment`
        """
        model = PaginatedCourseLicenseGroupAssignment()
        if include_optional:
            return PaginatedCourseLicenseGroupAssignment(
                count = 56,
                next_page = '',
                previous_page = '',
                results = [
                    iblai.models.course_license_group_assignment_detail.CourseLicenseGroupAssignmentDetail(
                        id = 56, 
                        group_id = 56, 
                        group_name = '', 
                        active = True, 
                        fulfilled = True, 
                        redirect_to = '', 
                        metadata = {
                            'key' : null
                            }, 
                        license_id = 56, 
                        license_name = '', 
                        course_id = '', )
                    ]
            )
        else:
            return PaginatedCourseLicenseGroupAssignment(
                count = 56,
                next_page = '',
                previous_page = '',
                results = [
                    iblai.models.course_license_group_assignment_detail.CourseLicenseGroupAssignmentDetail(
                        id = 56, 
                        group_id = 56, 
                        group_name = '', 
                        active = True, 
                        fulfilled = True, 
                        redirect_to = '', 
                        metadata = {
                            'key' : null
                            }, 
                        license_id = 56, 
                        license_name = '', 
                        course_id = '', )
                    ],
        )
        """

    def testPaginatedCourseLicenseGroupAssignment(self):
        """Test PaginatedCourseLicenseGroupAssignment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
