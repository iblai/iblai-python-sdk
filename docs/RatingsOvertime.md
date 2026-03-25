# RatingsOvertime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | 
**points** | [**List[RatingAverageRecord]**](RatingAverageRecord.md) |  | 

## Example

```python
from iblai.models.ratings_overtime import RatingsOvertime

# TODO update the JSON string below
json = "{}"
# create an instance of RatingsOvertime from a JSON string
ratings_overtime_instance = RatingsOvertime.from_json(json)
# print the JSON string representation of the object
print(RatingsOvertime.to_json())

# convert the object into a dict
ratings_overtime_dict = ratings_overtime_instance.to_dict()
# create an instance of RatingsOvertime from a dict
ratings_overtime_from_dict = RatingsOvertime.from_dict(ratings_overtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


