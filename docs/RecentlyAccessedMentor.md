# RecentlyAccessedMentor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [readonly] 
**name** | **str** |  | [readonly] 
**description** | **str** |  | [readonly] 
**recently_accessed_at** | **str** |  | [readonly] 
**platform_key** | **str** |  | [readonly] 
**last_accessed_by** | **str** |  | [readonly] 

## Example

```python
from iblai.models.recently_accessed_mentor import RecentlyAccessedMentor

# TODO update the JSON string below
json = "{}"
# create an instance of RecentlyAccessedMentor from a JSON string
recently_accessed_mentor_instance = RecentlyAccessedMentor.from_json(json)
# print the JSON string representation of the object
print(RecentlyAccessedMentor.to_json())

# convert the object into a dict
recently_accessed_mentor_dict = recently_accessed_mentor_instance.to_dict()
# create an instance of RecentlyAccessedMentor from a dict
recently_accessed_mentor_from_dict = RecentlyAccessedMentor.from_dict(recently_accessed_mentor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


