# MentorSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 
**cost** | **float** |  | 

## Example

```python
from iblai.models.mentor_session import MentorSession

# TODO update the JSON string below
json = "{}"
# create an instance of MentorSession from a JSON string
mentor_session_instance = MentorSession.from_json(json)
# print the JSON string representation of the object
print(MentorSession.to_json())

# convert the object into a dict
mentor_session_dict = mentor_session_instance.to_dict()
# create an instance of MentorSession from a dict
mentor_session_from_dict = MentorSession.from_dict(mentor_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


