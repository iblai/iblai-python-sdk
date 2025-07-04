# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.course_license_group_assignment_detail import CourseLicenseGroupAssignmentDetail

class TestCourseLicenseGroupAssignmentDetail(unittest.TestCase):
    """CourseLicenseGroupAssignmentDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CourseLicenseGroupAssignmentDetail:
        """Test CourseLicenseGroupAssignmentDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CourseLicenseGroupAssignmentDetail`
        """
        model = CourseLicenseGroupAssignmentDetail()
        if include_optional:
            return CourseLicenseGroupAssignmentDetail(
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
                course_id = ''
            )
        else:
            return CourseLicenseGroupAssignmentDetail(
                id = 56,
                group_id = 56,
                group_name = '',
                active = True,
                metadata = {
                    'key' : null
                    },
                license_id = 56,
                license_name = '',
                course_id = '',
        )
        """

    def testCourseLicenseGroupAssignmentDetail(self):
        """Test CourseLicenseGroupAssignmentDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
