# CourseLicenseDetail

Response serializer for course license details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the license | 
**created** | **datetime** | When the license was created | 
**started** | **datetime** | When the license becomes active | 
**expired** | **datetime** | When the license expires | 
**name** | **str** | The display name of the license | 
**count** | **int** | The number of seats purchased | 
**active** | **bool** | Whether the license is active | 
**metadata** | **Dict[str, object]** | Additional license metadata | 
**source** | **str** | The source identifier for the license | 
**external_id** | **str** | External identifier for the license | 
**platform_key** | **str** | The platform key associated with the license | 
**course_id** | **str** | The course ID associated with the license | 
**usage_count** | **int** | The number of seats purchased | [optional] [default to 0]

## Example

```python
from iblai.models.course_license_detail import CourseLicenseDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CourseLicenseDetail from a JSON string
course_license_detail_instance = CourseLicenseDetail.from_json(json)
# print the JSON string representation of the object
print(CourseLicenseDetail.to_json())

# convert the object into a dict
course_license_detail_dict = course_license_detail_instance.to_dict()
# create an instance of CourseLicenseDetail from a dict
course_license_detail_from_dict = CourseLicenseDetail.from_dict(course_license_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


