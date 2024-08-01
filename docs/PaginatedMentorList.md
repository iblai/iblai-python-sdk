# PaginatedMentorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Mentor]**](Mentor.md) |  | [optional] 

## Example

```python
from iblai.models.paginated_mentor_list import PaginatedMentorList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMentorList from a JSON string
paginated_mentor_list_instance = PaginatedMentorList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMentorList.to_json())

# convert the object into a dict
paginated_mentor_list_dict = paginated_mentor_list_instance.to_dict()
# create an instance of PaginatedMentorList from a dict
paginated_mentor_list_from_dict = PaginatedMentorList.from_dict(paginated_mentor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


