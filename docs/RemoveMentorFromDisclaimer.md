# RemoveMentorFromDisclaimer

Serializer for removing a mentor from a disclaimer.  This serializer validates the mentor_id input and provides proper schema documentation for the remove_mentor action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentor_id** | **str** | The unique_id of the mentor to remove from the disclaimer. | 

## Example

```python
from iblai.models.remove_mentor_from_disclaimer import RemoveMentorFromDisclaimer

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveMentorFromDisclaimer from a JSON string
remove_mentor_from_disclaimer_instance = RemoveMentorFromDisclaimer.from_json(json)
# print the JSON string representation of the object
print(RemoveMentorFromDisclaimer.to_json())

# convert the object into a dict
remove_mentor_from_disclaimer_dict = remove_mentor_from_disclaimer_instance.to_dict()
# create an instance of RemoveMentorFromDisclaimer from a dict
remove_mentor_from_disclaimer_from_dict = RemoveMentorFromDisclaimer.from_dict(remove_mentor_from_disclaimer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


