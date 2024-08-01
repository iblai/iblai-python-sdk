# PointsPercentile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**points** | **float** |  | 
**percentile** | **float** | Percentile of points for user. If an &#x60;org&#x60; was provided, this is the percentile of the user relative to users within the org. | 

## Example

```python
from iblai.models.points_percentile import PointsPercentile

# TODO update the JSON string below
json = "{}"
# create an instance of PointsPercentile from a JSON string
points_percentile_instance = PointsPercentile.from_json(json)
# print the JSON string representation of the object
print(PointsPercentile.to_json())

# convert the object into a dict
points_percentile_dict = points_percentile_instance.to_dict()
# create an instance of PointsPercentile from a dict
points_percentile_from_dict = PointsPercentile.from_dict(points_percentile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


