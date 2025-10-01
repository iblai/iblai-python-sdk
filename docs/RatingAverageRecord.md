# RatingAverageRecord

Serializer for rating average overtime data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**value** | **float** | Average rating value for this time period | 

## Example

```python
from iblai.models.rating_average_record import RatingAverageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of RatingAverageRecord from a JSON string
rating_average_record_instance = RatingAverageRecord.from_json(json)
# print the JSON string representation of the object
print(RatingAverageRecord.to_json())

# convert the object into a dict
rating_average_record_dict = rating_average_record_instance.to_dict()
# create an instance of RatingAverageRecord from a dict
rating_average_record_from_dict = RatingAverageRecord.from_dict(rating_average_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


