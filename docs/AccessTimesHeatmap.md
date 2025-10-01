# AccessTimesHeatmap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | **int** |  | 
**hour** | **int** |  | 
**value** | **int** |  | 

## Example

```python
from iblai.models.access_times_heatmap import AccessTimesHeatmap

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTimesHeatmap from a JSON string
access_times_heatmap_instance = AccessTimesHeatmap.from_json(json)
# print the JSON string representation of the object
print(AccessTimesHeatmap.to_json())

# convert the object into a dict
access_times_heatmap_dict = access_times_heatmap_instance.to_dict()
# create an instance of AccessTimesHeatmap from a dict
access_times_heatmap_from_dict = AccessTimesHeatmap.from_dict(access_times_heatmap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


