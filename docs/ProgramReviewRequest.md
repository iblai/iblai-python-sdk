# ProgramReviewRequest

Request serializer for ProgramReviewUpdateView POST endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_key** | **str** | The program key to review (format: program-v1:org+program_id) | 
**username** | **str** | The username of the reviewer | 
**user_id** | **int** | The user ID of the reviewer (alternative to username) | [optional] 
**rating** | **float** | The rating value (typically 1-5) | [optional] 
**title** | **str** | The review title | [optional] 
**content** | **str** | The review content/text | [optional] 
**visible** | **bool** | Whether the review is visible | [optional] [default to True]
**metadata** | **object** | Additional review metadata | [optional] 

## Example

```python
from iblai.models.program_review_request import ProgramReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramReviewRequest from a JSON string
program_review_request_instance = ProgramReviewRequest.from_json(json)
# print the JSON string representation of the object
print(ProgramReviewRequest.to_json())

# convert the object into a dict
program_review_request_dict = program_review_request_instance.to_dict()
# create an instance of ProgramReviewRequest from a dict
program_review_request_from_dict = ProgramReviewRequest.from_dict(program_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


