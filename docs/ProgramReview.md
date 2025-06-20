# ProgramReview

Serializer for program review data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The user identifier | 
**username** | **str** | The username of the reviewer | 
**content** | **str** | Review content/text | 
**rating** | **float** | Rating value (typically 1-5) | 
**title** | **str** | Review title | 
**visible** | **bool** | Whether the review is visible | 
**created** | **str** | Date when review was created | 
**modified** | **str** | Date when review was last modified | 
**program_key** | **str** | The program key identifier | 

## Example

```python
from iblai.models.program_review import ProgramReview

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramReview from a JSON string
program_review_instance = ProgramReview.from_json(json)
# print the JSON string representation of the object
print(ProgramReview.to_json())

# convert the object into a dict
program_review_dict = program_review_instance.to_dict()
# create an instance of ProgramReview from a dict
program_review_from_dict = ProgramReview.from_dict(program_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


