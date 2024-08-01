# MentorData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentor** | **str** |  | 
**total_cost** | **float** |  | 
**total_latency** | **float** |  | 
**mentor_traces** | [**List[MentorTrace]**](MentorTrace.md) |  | 

## Example

```python
from iblai.models.mentor_data import MentorData

# TODO update the JSON string below
json = "{}"
# create an instance of MentorData from a JSON string
mentor_data_instance = MentorData.from_json(json)
# print the JSON string representation of the object
print(MentorData.to_json())

# convert the object into a dict
mentor_data_dict = mentor_data_instance.to_dict()
# create an instance of MentorData from a dict
mentor_data_from_dict = MentorData.from_dict(mentor_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


