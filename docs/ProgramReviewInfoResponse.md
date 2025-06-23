# ProgramReviewInfoResponse

Serializer for program review info response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_key** | **str** | The program key associated with the reviews | 
**avg_rating** | **float** | Average rating of the program | 
**count** | **int** | Total number of reviews for the program | 

## Example

```python
from iblai.models.program_review_info_response import ProgramReviewInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramReviewInfoResponse from a JSON string
program_review_info_response_instance = ProgramReviewInfoResponse.from_json(json)
# print the JSON string representation of the object
print(ProgramReviewInfoResponse.to_json())

# convert the object into a dict
program_review_info_response_dict = program_review_info_response_instance.to_dict()
# create an instance of ProgramReviewInfoResponse from a dict
program_review_info_response_from_dict = ProgramReviewInfoResponse.from_dict(program_review_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


