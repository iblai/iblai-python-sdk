# PaginatedRbacPolicyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[RbacPolicy]**](RbacPolicy.md) |  | 

## Example

```python
from iblai.models.paginated_rbac_policy_list import PaginatedRbacPolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRbacPolicyList from a JSON string
paginated_rbac_policy_list_instance = PaginatedRbacPolicyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRbacPolicyList.to_json())

# convert the object into a dict
paginated_rbac_policy_list_dict = paginated_rbac_policy_list_instance.to_dict()
# create an instance of PaginatedRbacPolicyList from a dict
paginated_rbac_policy_list_from_dict = PaginatedRbacPolicyList.from_dict(paginated_rbac_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


