# TenantMentorTraces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | **str** |  | 
**tenant_total_cost** | **float** |  | 
**mentor_data** | [**List[MentorData]**](MentorData.md) |  | 

## Example

```python
from iblai.models.tenant_mentor_traces import TenantMentorTraces

# TODO update the JSON string below
json = "{}"
# create an instance of TenantMentorTraces from a JSON string
tenant_mentor_traces_instance = TenantMentorTraces.from_json(json)
# print the JSON string representation of the object
print(TenantMentorTraces.to_json())

# convert the object into a dict
tenant_mentor_traces_dict = tenant_mentor_traces_instance.to_dict()
# create an instance of TenantMentorTraces from a dict
tenant_mentor_traces_from_dict = TenantMentorTraces.from_dict(tenant_mentor_traces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


