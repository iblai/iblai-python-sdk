# MediaResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**title** | **str** | Title of the media resource | 
**description** | **str** | Description of the media resource | [optional] 
**media_type** | [**MediaTypeEnum**](MediaTypeEnum.md) | Type of media  * &#x60;video&#x60; - Video * &#x60;image&#x60; - Image * &#x60;document&#x60; - Document * &#x60;audio&#x60; - Audio * &#x60;other&#x60; - Other | 
**item_type** | [**ItemTypeEnum**](ItemTypeEnum.md) | Type of item this media is associated with  * &#x60;course&#x60; - Course * &#x60;unit&#x60; - Unit * &#x60;resource&#x60; - Resource * &#x60;course_unit&#x60; - Course and Unit * &#x60;course_resource&#x60; - Course and Resource * &#x60;unit_resource&#x60; - Unit and Resource * &#x60;all&#x60; - Course, Unit, and Resource | [readonly] 
**course_id** | **str** | ID of the associated course | [optional] 
**unit_id** | **str** | ID of the associated unit | [optional] 
**item_id** | **str** | ID of the associated item (resource) | [optional] 
**platform** | **int** | The platform this media resource belongs to | [readonly] 
**file_url** | **str** | External URL for the media resource | [optional] 
**file** | **str** | Uploaded media file | [optional] 
**created_by** | **int** | User who created this media resource | [readonly] 
**created_at** | **datetime** | When this record was created | [readonly] 
**updated_at** | **datetime** | When this record was last updated | [readonly] 

## Example

```python
from iblai.models.media_resource import MediaResource

# TODO update the JSON string below
json = "{}"
# create an instance of MediaResource from a JSON string
media_resource_instance = MediaResource.from_json(json)
# print the JSON string representation of the object
print(MediaResource.to_json())

# convert the object into a dict
media_resource_dict = media_resource_instance.to_dict()
# create an instance of MediaResource from a dict
media_resource_from_dict = MediaResource.from_dict(media_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


