# LearnerDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserInfo**](UserInfo.md) |  | 
**data** | [**LearnerData**](LearnerData.md) |  | 

## Example

```python
from iblai.models.learner_details_response import LearnerDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerDetailsResponse from a JSON string
learner_details_response_instance = LearnerDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerDetailsResponse.to_json())

# convert the object into a dict
learner_details_response_dict = learner_details_response_instance.to_dict()
# create an instance of LearnerDetailsResponse from a dict
learner_details_response_from_dict = LearnerDetailsResponse.from_dict(learner_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


