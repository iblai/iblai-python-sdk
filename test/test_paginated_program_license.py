# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.paginated_program_license import PaginatedProgramLicense

class TestPaginatedProgramLicense(unittest.TestCase):
    """PaginatedProgramLicense unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedProgramLicense:
        """Test PaginatedProgramLicense
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedProgramLicense`
        """
        model = PaginatedProgramLicense()
        if include_optional:
            return PaginatedProgramLicense(
                count = 56,
                next_page = '',
                previous_page = '',
                results = [
                    iblai.models.program_license_detail.ProgramLicenseDetail(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expired = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        count = 56, 
                        active = True, 
                        metadata = {
                            'key' : null
                            }, 
                        source = '', 
                        external_id = '', 
                        platform_key = '', 
                        program_id = '', 
                        program_key = '', 
                        program_name = '', 
                        usage_count = 56, 
                        assignments = {
                            'key' : 56
                            }, )
                    ]
            )
        else:
            return PaginatedProgramLicense(
                count = 56,
                next_page = '',
                previous_page = '',
                results = [
                    iblai.models.program_license_detail.ProgramLicenseDetail(
                        id = 56, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        started = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expired = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        count = 56, 
                        active = True, 
                        metadata = {
                            'key' : null
                            }, 
                        source = '', 
                        external_id = '', 
                        platform_key = '', 
                        program_id = '', 
                        program_key = '', 
                        program_name = '', 
                        usage_count = 56, 
                        assignments = {
                            'key' : 56
                            }, )
                    ],
        )
        """

    def testPaginatedProgramLicense(self):
        """Test PaginatedProgramLicense"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
