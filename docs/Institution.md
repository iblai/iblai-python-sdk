# Institution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**institution_type** | [**InstitutionTypeEnum**](InstitutionTypeEnum.md) |  | [optional] 
**location** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**accreditation** | **str** |  | [optional] 
**established_year** | **int** |  | [optional] 
**data** | **object** | Metadata | [optional] 
**metadata** | **object** | Metadata | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from iblai.models.institution import Institution

# TODO update the JSON string below
json = "{}"
# create an instance of Institution from a JSON string
institution_instance = Institution.from_json(json)
# print the JSON string representation of the object
print(Institution.to_json())

# convert the object into a dict
institution_dict = institution_instance.to_dict()
# create an instance of Institution from a dict
institution_from_dict = Institution.from_dict(institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


