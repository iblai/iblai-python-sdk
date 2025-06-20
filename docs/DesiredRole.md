# DesiredRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**roles** | [**List[Role]**](Role.md) |  | 
**data** | **object** |  | [readonly] 

## Example

```python
from iblai.models.desired_role import DesiredRole

# TODO update the JSON string below
json = "{}"
# create an instance of DesiredRole from a JSON string
desired_role_instance = DesiredRole.from_json(json)
# print the JSON string representation of the object
print(DesiredRole.to_json())

# convert the object into a dict
desired_role_dict = desired_role_instance.to_dict()
# create an instance of DesiredRole from a dict
desired_role_from_dict = DesiredRole.from_dict(desired_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


