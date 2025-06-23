# UserCountRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | 
**user_count** | **int** |  | 

## Example

```python
from iblai.models.user_count_record import UserCountRecord

# TODO update the JSON string below
json = "{}"
# create an instance of UserCountRecord from a JSON string
user_count_record_instance = UserCountRecord.from_json(json)
# print the JSON string representation of the object
print(UserCountRecord.to_json())

# convert the object into a dict
user_count_record_dict = user_count_record_instance.to_dict()
# create an instance of UserCountRecord from a dict
user_count_record_from_dict = UserCountRecord.from_dict(user_count_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


