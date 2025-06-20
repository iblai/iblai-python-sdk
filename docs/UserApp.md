# UserApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**app** | [**App**](App.md) | The app details | 
**platform** | [**Platform**](Platform.md) | The platform details | [readonly] 
**subscription** | **Dict[str, object]** | The subscription details, would contain identifier, active, created_on, last_updated | [readonly] 
**provider** | **str** |  | 
**is_admin** | **bool** |  | [readonly] 
**is_active** | **bool** |  | [readonly] 
**metadata** | **object** |  | [optional] 
**onboarding_completed** | **bool** |  | [optional] 
**free_trial_started** | **bool** |  | [optional] 
**free_trial_expired** | **bool** |  | [optional] 
**has_active_subscription** | **bool** |  | [optional] 

## Example

```python
from iblai.models.user_app import UserApp

# TODO update the JSON string below
json = "{}"
# create an instance of UserApp from a JSON string
user_app_instance = UserApp.from_json(json)
# print the JSON string representation of the object
print(UserApp.to_json())

# convert the object into a dict
user_app_dict = user_app_instance.to_dict()
# create an instance of UserApp from a dict
user_app_from_dict = UserApp.from_dict(user_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


