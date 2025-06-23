# StarMentor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_starred** | **bool** |  | [optional] 
**updated_at** | **str** |  | [readonly] 
**mentor** | **str** |  | [readonly] 
**student** | **str** |  | [readonly] 
**recently_accessed_at** | **str** |  | [readonly] 

## Example

```python
from iblai.models.star_mentor import StarMentor

# TODO update the JSON string below
json = "{}"
# create an instance of StarMentor from a JSON string
star_mentor_instance = StarMentor.from_json(json)
# print the JSON string representation of the object
print(StarMentor.to_json())

# convert the object into a dict
star_mentor_dict = star_mentor_instance.to_dict()
# create an instance of StarMentor from a dict
star_mentor_from_dict = StarMentor.from_dict(star_mentor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


