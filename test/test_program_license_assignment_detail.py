# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.program_license_assignment_detail import ProgramLicenseAssignmentDetail

class TestProgramLicenseAssignmentDetail(unittest.TestCase):
    """ProgramLicenseAssignmentDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProgramLicenseAssignmentDetail:
        """Test ProgramLicenseAssignmentDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProgramLicenseAssignmentDetail`
        """
        model = ProgramLicenseAssignmentDetail()
        if include_optional:
            return ProgramLicenseAssignmentDetail(
                id = 56,
                user_id = 56,
                username = '',
                name = '',
                email = '',
                active = True,
                fulfilled = True,
                direct = True,
                redirect_to = '',
                metadata = {
                    'key' : null
                    },
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                license_id = 56,
                license_name = '',
                program_key = ''
            )
        else:
            return ProgramLicenseAssignmentDetail(
                id = 56,
                user_id = 56,
                username = '',
                name = '',
                email = '',
                active = True,
                fulfilled = True,
                metadata = {
                    'key' : null
                    },
                license_id = 56,
                license_name = '',
                program_key = '',
        )
        """

    def testProgramLicenseAssignmentDetail(self):
        """Test ProgramLicenseAssignmentDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
