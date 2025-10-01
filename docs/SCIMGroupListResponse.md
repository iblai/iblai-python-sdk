# SCIMGroupListResponse

SCIM group list response serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** | SCIM schema identifiers | 
**total_results** | **int** | Total number of results | 
**resources** | **List[Dict[str, object]]** | List of group resources | 
**start_index** | **int** | Starting index | [optional] 
**items_per_page** | **int** | Items per page | [optional] 

## Example

```python
from iblai.models.scim_group_list_response import SCIMGroupListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMGroupListResponse from a JSON string
scim_group_list_response_instance = SCIMGroupListResponse.from_json(json)
# print the JSON string representation of the object
print(SCIMGroupListResponse.to_json())

# convert the object into a dict
scim_group_list_response_dict = scim_group_list_response_instance.to_dict()
# create an instance of SCIMGroupListResponse from a dict
scim_group_list_response_from_dict = SCIMGroupListResponse.from_dict(scim_group_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


