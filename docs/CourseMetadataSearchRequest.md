# CourseMetadataSearchRequest

Serializer for course metadata search request body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data__contains** | **object** | Filter by metadata fields (JSON object) | [optional] 
**slug** | **str** | Filter by course slug | [optional] 
**course_id** | **str** | Filter by course ID | [optional] 

## Example

```python
from iblai.models.course_metadata_search_request import CourseMetadataSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CourseMetadataSearchRequest from a JSON string
course_metadata_search_request_instance = CourseMetadataSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CourseMetadataSearchRequest.to_json())

# convert the object into a dict
course_metadata_search_request_dict = course_metadata_search_request_instance.to_dict()
# create an instance of CourseMetadataSearchRequest from a dict
course_metadata_search_request_from_dict = CourseMetadataSearchRequest.from_dict(course_metadata_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


