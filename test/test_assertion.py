# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 2.4.1-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.assertion import Assertion

class TestAssertion(unittest.TestCase):
    """Assertion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Assertion:
        """Test Assertion
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Assertion`
        """
        model = Assertion()
        if include_optional:
            return Assertion(
                entity_id = '',
                issued_on = '',
                credential_details = {
                    'key' : ''
                    },
                recipient = {
                    'key' : ''
                    },
                metadata = None,
                course = {
                    'key' : ''
                    },
                program = {
                    'key' : ''
                    },
                narrative = '',
                revoked = True,
                revocation_reason = '',
                acceptance = 'Unaccepted',
                expires = ''
            )
        else:
            return Assertion(
                entity_id = '',
                issued_on = '',
                credential_details = {
                    'key' : ''
                    },
                recipient = {
                    'key' : ''
                    },
                course = {
                    'key' : ''
                    },
                program = {
                    'key' : ''
                    },
                revocation_reason = '',
                expires = '',
        )
        """

    def testAssertion(self):
        """Test Assertion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
