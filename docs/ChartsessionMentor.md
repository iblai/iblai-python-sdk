# ChartsessionMentor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**mentor_tenant** | **str** |  | 
**description** | **str** |  | 
**profile_image** | **str** |  | 
**created_by** | **str** |  | 
**unique_id** | **str** |  | 
**proactive_prompt** | **str** |  | 

## Example

```python
from iblai.models.chartsession_mentor import ChartsessionMentor

# TODO update the JSON string below
json = "{}"
# create an instance of ChartsessionMentor from a JSON string
chartsession_mentor_instance = ChartsessionMentor.from_json(json)
# print the JSON string representation of the object
print(ChartsessionMentor.to_json())

# convert the object into a dict
chartsession_mentor_dict = chartsession_mentor_instance.to_dict()
# create an instance of ChartsessionMentor from a dict
chartsession_mentor_from_dict = ChartsessionMentor.from_dict(chartsession_mentor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


