# MentorFork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_mentor_name** | **str** |  | 
**destination_platform_key** | **str** |  | 
**clone_documents** | **bool** |  | [optional] [default to False]

## Example

```python
from iblai.models.mentor_fork import MentorFork

# TODO update the JSON string below
json = "{}"
# create an instance of MentorFork from a JSON string
mentor_fork_instance = MentorFork.from_json(json)
# print the JSON string representation of the object
print(MentorFork.to_json())

# convert the object into a dict
mentor_fork_dict = mentor_fork_instance.to_dict()
# create an instance of MentorFork from a dict
mentor_fork_from_dict = MentorFork.from_dict(mentor_fork_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


