# GroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GroupListData]**](GroupListData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from iblai.models.group_list import GroupList

# TODO update the JSON string below
json = "{}"
# create an instance of GroupList from a JSON string
group_list_instance = GroupList.from_json(json)
# print the JSON string representation of the object
print(GroupList.to_json())

# convert the object into a dict
group_list_dict = group_list_instance.to_dict()
# create an instance of GroupList from a dict
group_list_from_dict = GroupList.from_dict(group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


