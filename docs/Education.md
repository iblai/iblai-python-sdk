# Education


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**user** | **int** | edX user ID | [readonly] 
**user_info** | [**UserInfo**](UserInfo.md) |  | [readonly] 
**institution** | [**Institution**](Institution.md) |  | [readonly] 
**institution_id** | **int** |  | 
**degree** | **str** |  | [optional] 
**field_of_study** | **str** |  | [optional] 
**start_date** | **date** |  | 
**end_date** | **date** |  | [optional] 
**grade** | **decimal.Decimal** |  | [optional] 
**activities** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**data** | **object** | Metadata | [optional] 
**metadata** | **object** | Metadata | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [readonly] 
**is_current** | **bool** |  | [optional] 

## Example

```python
from iblai.models.education import Education

# TODO update the JSON string below
json = "{}"
# create an instance of Education from a JSON string
education_instance = Education.from_json(json)
# print the JSON string representation of the object
print(Education.to_json())

# convert the object into a dict
education_dict = education_instance.to_dict()
# create an instance of Education from a dict
education_from_dict = Education.from_dict(education_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


