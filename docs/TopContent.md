# TopContent

Serializer for top content information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_identifier** | **str** | Course identifier | 
**course_name** | **str** | Name of the course. | 
**time_spent_seconds** | **int** | Time spent on this course in seconds | 

## Example

```python
from iblai.models.top_content import TopContent

# TODO update the JSON string below
json = "{}"
# create an instance of TopContent from a JSON string
top_content_instance = TopContent.from_json(json)
# print the JSON string representation of the object
print(TopContent.to_json())

# convert the object into a dict
top_content_dict = top_content_instance.to_dict()
# create an instance of TopContent from a dict
top_content_from_dict = TopContent.from_dict(top_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


