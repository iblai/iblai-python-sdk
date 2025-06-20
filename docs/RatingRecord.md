# RatingRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | 
**total_ratings** | **int** |  | 

## Example

```python
from iblai.models.rating_record import RatingRecord

# TODO update the JSON string below
json = "{}"
# create an instance of RatingRecord from a JSON string
rating_record_instance = RatingRecord.from_json(json)
# print the JSON string representation of the object
print(RatingRecord.to_json())

# convert the object into a dict
rating_record_dict = rating_record_instance.to_dict()
# create an instance of RatingRecord from a dict
rating_record_from_dict = RatingRecord.from_dict(rating_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


