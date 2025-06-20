# CourseMetadataUpdateRequest

Serializer for course metadata update request body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | The course ID to update metadata for | 
**metadata** | **object** | The metadata to update | 
**update** | **bool** | Whether to update (True) or overwrite (False) existing metadata | [optional] [default to True]

## Example

```python
from iblai.models.course_metadata_update_request import CourseMetadataUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CourseMetadataUpdateRequest from a JSON string
course_metadata_update_request_instance = CourseMetadataUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CourseMetadataUpdateRequest.to_json())

# convert the object into a dict
course_metadata_update_request_dict = course_metadata_update_request_instance.to_dict()
# create an instance of CourseMetadataUpdateRequest from a dict
course_metadata_update_request_from_dict = CourseMetadataUpdateRequest.from_dict(course_metadata_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


