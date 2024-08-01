# LearnerInformationAPI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerInformationAPIData**](LearnerInformationAPIData.md) |  | 

## Example

```python
from iblai.models.learner_information_api import LearnerInformationAPI

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerInformationAPI from a JSON string
learner_information_api_instance = LearnerInformationAPI.from_json(json)
# print the JSON string representation of the object
print(LearnerInformationAPI.to_json())

# convert the object into a dict
learner_information_api_dict = learner_information_api_instance.to_dict()
# create an instance of LearnerInformationAPI from a dict
learner_information_api_from_dict = LearnerInformationAPI.from_dict(learner_information_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


