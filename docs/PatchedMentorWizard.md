# PatchedMentorWizard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from iblai.models.patched_mentor_wizard import PatchedMentorWizard

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMentorWizard from a JSON string
patched_mentor_wizard_instance = PatchedMentorWizard.from_json(json)
# print the JSON string representation of the object
print(PatchedMentorWizard.to_json())

# convert the object into a dict
patched_mentor_wizard_dict = patched_mentor_wizard_instance.to_dict()
# create an instance of PatchedMentorWizard from a dict
patched_mentor_wizard_from_dict = PatchedMentorWizard.from_dict(patched_mentor_wizard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


