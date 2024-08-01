# Score


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**timestamp** | **datetime** |  | 
**name** | **str** |  | 
**value** | **float** |  | 
**comment** | **str** |  | 
**trace_id** | **str** |  | 
**observation_id** | **str** |  | 
**trace** | **object** |  | [optional] 

## Example

```python
from iblai.models.score import Score

# TODO update the JSON string below
json = "{}"
# create an instance of Score from a JSON string
score_instance = Score.from_json(json)
# print the JSON string representation of the object
print(Score.to_json())

# convert the object into a dict
score_dict = score_instance.to_dict()
# create an instance of Score from a dict
score_from_dict = Score.from_dict(score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


