# ReportedRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**roles** | [**List[Role]**](Role.md) |  | 
**data** | **object** |  | [readonly] 

## Example

```python
from iblai.models.reported_role import ReportedRole

# TODO update the JSON string below
json = "{}"
# create an instance of ReportedRole from a JSON string
reported_role_instance = ReportedRole.from_json(json)
# print the JSON string representation of the object
print(ReportedRole.to_json())

# convert the object into a dict
reported_role_dict = reported_role_instance.to_dict()
# create an instance of ReportedRole from a dict
reported_role_from_dict = ReportedRole.from_dict(reported_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


