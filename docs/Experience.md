# Experience


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**user** | **int** | edX user ID | [readonly] 
**user_info** | [**UserInfo**](UserInfo.md) |  | [readonly] 
**company** | [**Company**](Company.md) |  | [readonly] 
**company_id** | **int** |  | 
**title** | **str** |  | 
**employment_type** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**start_date** | **date** |  | 
**end_date** | **date** |  | [optional] 
**is_current** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**data** | **object** | Metadata | [optional] 
**metadata** | **object** | Metadata | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.experience import Experience

# TODO update the JSON string below
json = "{}"
# create an instance of Experience from a JSON string
experience_instance = Experience.from_json(json)
# print the JSON string representation of the object
print(Experience.to_json())

# convert the object into a dict
experience_dict = experience_instance.to_dict()
# create an instance of Experience from a dict
experience_from_dict = Experience.from_dict(experience_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


