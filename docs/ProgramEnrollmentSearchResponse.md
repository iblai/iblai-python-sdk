# ProgramEnrollmentSearchResponse

Response serializer for ProgramEnrollmentSearchView GET endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ProgramEnrollmentPlus]**](ProgramEnrollmentPlus.md) | List of program enrollments | 
**count** | **int** | Total number of reviews | 
**next_page** | **int** | Next page number | 
**previous_page** | **int** | Previous page number | 

## Example

```python
from iblai.models.program_enrollment_search_response import ProgramEnrollmentSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramEnrollmentSearchResponse from a JSON string
program_enrollment_search_response_instance = ProgramEnrollmentSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ProgramEnrollmentSearchResponse.to_json())

# convert the object into a dict
program_enrollment_search_response_dict = program_enrollment_search_response_instance.to_dict()
# create an instance of ProgramEnrollmentSearchResponse from a dict
program_enrollment_search_response_from_dict = ProgramEnrollmentSearchResponse.from_dict(program_enrollment_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


