# coding: utf-8

"""
    ibl-data-manager

    API for iblai

    The version of the OpenAPI document: 3.54.3-ai-plus
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from iblai.models.paginated_assertions_response import PaginatedAssertionsResponse

class TestPaginatedAssertionsResponse(unittest.TestCase):
    """PaginatedAssertionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedAssertionsResponse:
        """Test PaginatedAssertionsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedAssertionsResponse`
        """
        model = PaginatedAssertionsResponse()
        if include_optional:
            return PaginatedAssertionsResponse(
                next = '',
                previous = '',
                count = 56,
                num_pages = 56,
                page_number = 56,
                max_page_size = 56,
                data = [
                    iblai.models.assertion.Assertion(
                        entity_id = '', 
                        issued_on = '', 
                        credential_details = {
                            'key' : ''
                            }, 
                        recipient = {
                            'key' : ''
                            }, 
                        metadata = null, 
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
                        expires = '', )
                    ]
            )
        else:
            return PaginatedAssertionsResponse(
                next = '',
                previous = '',
                count = 56,
                num_pages = 56,
                page_number = 56,
                max_page_size = 56,
                data = [
                    iblai.models.assertion.Assertion(
                        entity_id = '', 
                        issued_on = '', 
                        credential_details = {
                            'key' : ''
                            }, 
                        recipient = {
                            'key' : ''
                            }, 
                        metadata = null, 
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
                        expires = '', )
                    ],
        )
        """

    def testPaginatedAssertionsResponse(self):
        """Test PaginatedAssertionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
