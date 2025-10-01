# MentorDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mentor_id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**platform_key** | **str** |  | [optional] 
**categories** | **List[str]** |  | [optional] 
**subjects** | **List[str]** |  | [optional] 
**interactions** | [**MentorInteractions**](MentorInteractions.md) |  | 

## Example

```python
from iblai.models.mentor_detail import MentorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of MentorDetail from a JSON string
mentor_detail_instance = MentorDetail.from_json(json)
# print the JSON string representation of the object
print(MentorDetail.to_json())

# convert the object into a dict
mentor_detail_dict = mentor_detail_instance.to_dict()
# create an instance of MentorDetail from a dict
mentor_detail_from_dict = MentorDetail.from_dict(mentor_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


