# AddMentorToDisclaimer

Serializer for adding a mentor to a disclaimer.  This serializer validates the mentor_id input and provides proper schema documentation for the add_mentor action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentor_id** | **str** | The unique_id of the mentor to add to the disclaimer. | 

## Example

```python
from iblai.models.add_mentor_to_disclaimer import AddMentorToDisclaimer

# TODO update the JSON string below
json = "{}"
# create an instance of AddMentorToDisclaimer from a JSON string
add_mentor_to_disclaimer_instance = AddMentorToDisclaimer.from_json(json)
# print the JSON string representation of the object
print(AddMentorToDisclaimer.to_json())

# convert the object into a dict
add_mentor_to_disclaimer_dict = add_mentor_to_disclaimer_instance.to_dict()
# create an instance of AddMentorToDisclaimer from a dict
add_mentor_to_disclaimer_from_dict = AddMentorToDisclaimer.from_dict(add_mentor_to_disclaimer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


