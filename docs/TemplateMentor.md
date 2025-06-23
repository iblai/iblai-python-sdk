# TemplateMentor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**slug** | **str** |  | [optional] 
**unique_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**system_prompt** | **str** |  | [optional] 
**platform_key** | **str** |  | 

## Example

```python
from iblai.models.template_mentor import TemplateMentor

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateMentor from a JSON string
template_mentor_instance = TemplateMentor.from_json(json)
# print the JSON string representation of the object
print(TemplateMentor.to_json())

# convert the object into a dict
template_mentor_dict = template_mentor_instance.to_dict()
# create an instance of TemplateMentor from a dict
template_mentor_from_dict = TemplateMentor.from_dict(template_mentor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


