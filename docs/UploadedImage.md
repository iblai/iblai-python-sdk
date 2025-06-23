# UploadedImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | [optional] 
**image** | **str** |  | [readonly] 

## Example

```python
from iblai.models.uploaded_image import UploadedImage

# TODO update the JSON string below
json = "{}"
# create an instance of UploadedImage from a JSON string
uploaded_image_instance = UploadedImage.from_json(json)
# print the JSON string representation of the object
print(UploadedImage.to_json())

# convert the object into a dict
uploaded_image_dict = uploaded_image_instance.to_dict()
# create an instance of UploadedImage from a dict
uploaded_image_from_dict = UploadedImage.from_dict(uploaded_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


