# ActivateUserFreeTrial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_trial_started** | **bool** |  | [optional] [default to True]
**app** | **str** | The app url or name or id | 
**platform** | **str** | The platform key | 

## Example

```python
from iblai.models.activate_user_free_trial import ActivateUserFreeTrial

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateUserFreeTrial from a JSON string
activate_user_free_trial_instance = ActivateUserFreeTrial.from_json(json)
# print the JSON string representation of the object
print(ActivateUserFreeTrial.to_json())

# convert the object into a dict
activate_user_free_trial_dict = activate_user_free_trial_instance.to_dict()
# create an instance of ActivateUserFreeTrial from a dict
activate_user_free_trial_from_dict = ActivateUserFreeTrial.from_dict(activate_user_free_trial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


