# AIUserProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | 
**detail** | **str** |  | 

## Example

```python
from iblai.models.ai_user_profile_request import AIUserProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AIUserProfileRequest from a JSON string
ai_user_profile_request_instance = AIUserProfileRequest.from_json(json)
# print the JSON string representation of the object
print(AIUserProfileRequest.to_json())

# convert the object into a dict
ai_user_profile_request_dict = ai_user_profile_request_instance.to_dict()
# create an instance of AIUserProfileRequest from a dict
ai_user_profile_request_from_dict = AIUserProfileRequest.from_dict(ai_user_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


