# FileUploadURLResponse

Response serializer for presigned upload URL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_url** | **str** | Presigned S3 upload URL | 
**file_key** | **str** | S3 object key for the uploaded file | 
**file_id** | **str** | Unique identifier for the ChatFile record | 
**expires_in** | **int** | URL expiration time in seconds | 
**upload_method** | **str** | HTTP method to use for upload (PUT or POST) | [optional] [default to 'PUT']

## Example

```python
from iblai.models.file_upload_url_response import FileUploadURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadURLResponse from a JSON string
file_upload_url_response_instance = FileUploadURLResponse.from_json(json)
# print the JSON string representation of the object
print(FileUploadURLResponse.to_json())

# convert the object into a dict
file_upload_url_response_dict = file_upload_url_response_instance.to_dict()
# create an instance of FileUploadURLResponse from a dict
file_upload_url_response_from_dict = FileUploadURLResponse.from_dict(file_upload_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


