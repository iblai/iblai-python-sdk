# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.6.0-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.program import Program

class TestProgram(unittest.TestCase):
    """Program unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Program:
        """Test Program
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Program`
        """
        model = Program()
        if include_optional:
            return Program(
                id = 56,
                institution = iblai.models.institution.Institution(
                    id = 56, 
                    name = '', 
                    institution_type = 'university', 
                    location = '', 
                    website = '', 
                    accreditation = '', 
                    established_year = 56, 
                    data = null, 
                    metadata = null, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                institution_id = 56,
                name = '',
                program_type = 'bachelors',
                duration = 56,
                description = '',
                data = None,
                metadata = None,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Program(
                id = 56,
                institution = iblai.models.institution.Institution(
                    id = 56, 
                    name = '', 
                    institution_type = 'university', 
                    location = '', 
                    website = '', 
                    accreditation = '', 
                    established_year = 56, 
                    data = null, 
                    metadata = null, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                institution_id = 56,
                name = '',
                program_type = 'bachelors',
                duration = 56,
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testProgram(self):
        """Test Program"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
