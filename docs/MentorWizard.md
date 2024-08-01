# MentorWizard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from iblai.models.mentor_wizard import MentorWizard

# TODO update the JSON string below
json = "{}"
# create an instance of MentorWizard from a JSON string
mentor_wizard_instance = MentorWizard.from_json(json)
# print the JSON string representation of the object
print(MentorWizard.to_json())

# convert the object into a dict
mentor_wizard_dict = mentor_wizard_instance.to_dict()
# create an instance of MentorWizard from a dict
mentor_wizard_from_dict = MentorWizard.from_dict(mentor_wizard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


