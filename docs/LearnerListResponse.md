# LearnerListResponse

Serializer for learner list API response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | [**PlatformInfo**](PlatformInfo.md) | Platform information | 
**learners** | [**List[LearnerListItem]**](LearnerListItem.md) | List of learners | 
**pagination** | [**LearnerListPagination**](LearnerListPagination.md) | Pagination metadata | 
**generated_at** | **datetime** | Response generation timestamp | 

## Example

```python
from iblai.models.learner_list_response import LearnerListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerListResponse from a JSON string
learner_list_response_instance = LearnerListResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerListResponse.to_json())

# convert the object into a dict
learner_list_response_dict = learner_list_response_instance.to_dict()
# create an instance of LearnerListResponse from a dict
learner_list_response_from_dict = LearnerListResponse.from_dict(learner_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


