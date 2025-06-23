# OnboardingStatusUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**onboarding_completed** | **bool** |  | 
**app** | **str** | The app url or name or id | 

## Example

```python
from iblai.models.onboarding_status_update import OnboardingStatusUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingStatusUpdate from a JSON string
onboarding_status_update_instance = OnboardingStatusUpdate.from_json(json)
# print the JSON string representation of the object
print(OnboardingStatusUpdate.to_json())

# convert the object into a dict
onboarding_status_update_dict = onboarding_status_update_instance.to_dict()
# create an instance of OnboardingStatusUpdate from a dict
onboarding_status_update_from_dict = OnboardingStatusUpdate.from_dict(onboarding_status_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


