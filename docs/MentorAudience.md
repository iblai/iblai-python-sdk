# MentorAudience


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from iblai.models.mentor_audience import MentorAudience

# TODO update the JSON string below
json = "{}"
# create an instance of MentorAudience from a JSON string
mentor_audience_instance = MentorAudience.from_json(json)
# print the JSON string representation of the object
print(MentorAudience.to_json())

# convert the object into a dict
mentor_audience_dict = mentor_audience_instance.to_dict()
# create an instance of MentorAudience from a dict
mentor_audience_from_dict = MentorAudience.from_dict(mentor_audience_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


