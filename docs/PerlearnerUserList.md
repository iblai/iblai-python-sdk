# PerlearnerUserList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PerlearnerUserListData]**](PerlearnerUserListData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from iblai.models.perlearner_user_list import PerlearnerUserList

# TODO update the JSON string below
json = "{}"
# create an instance of PerlearnerUserList from a JSON string
perlearner_user_list_instance = PerlearnerUserList.from_json(json)
# print the JSON string representation of the object
print(PerlearnerUserList.to_json())

# convert the object into a dict
perlearner_user_list_dict = perlearner_user_list_instance.to_dict()
# create an instance of PerlearnerUserList from a dict
perlearner_user_list_from_dict = PerlearnerUserList.from_dict(perlearner_user_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


