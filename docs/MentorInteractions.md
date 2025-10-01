# MentorInteractions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_messages** | **int** |  | 
**latest_interaction** | **datetime** |  | [optional] 
**rating** | **float** |  | [optional] 

## Example

```python
from iblai.models.mentor_interactions import MentorInteractions

# TODO update the JSON string below
json = "{}"
# create an instance of MentorInteractions from a JSON string
mentor_interactions_instance = MentorInteractions.from_json(json)
# print the JSON string representation of the object
print(MentorInteractions.to_json())

# convert the object into a dict
mentor_interactions_dict = mentor_interactions_instance.to_dict()
# create an instance of MentorInteractions from a dict
mentor_interactions_from_dict = MentorInteractions.from_dict(mentor_interactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


