# Company


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**user** | **int** | edX user ID | [readonly] 
**user_info** | [**UserInfo**](UserInfo.md) |  | [readonly] 
**name** | **str** |  | 
**industry** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**data** | **object** | Metadata | [optional] 
**metadata** | **object** | Metadata | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.company import Company

# TODO update the JSON string below
json = "{}"
# create an instance of Company from a JSON string
company_instance = Company.from_json(json)
# print the JSON string representation of the object
print(Company.to_json())

# convert the object into a dict
company_dict = company_instance.to_dict()
# create an instance of Company from a dict
company_from_dict = Company.from_dict(company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


