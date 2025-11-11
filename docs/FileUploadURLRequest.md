# FileUploadURLRequest

Request serializer for generating presigned upload URL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Chat session ID | 
**file_name** | **str** | Original filename | 
**content_type** | **str** | MIME type of the file | 
**file_size** | **int** | File size in bytes | 

## Example

```python
from iblai.models.file_upload_url_request import FileUploadURLRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadURLRequest from a JSON string
file_upload_url_request_instance = FileUploadURLRequest.from_json(json)
# print the JSON string representation of the object
print(FileUploadURLRequest.to_json())

# convert the object into a dict
file_upload_url_request_dict = file_upload_url_request_instance.to_dict()
# create an instance of FileUploadURLRequest from a dict
file_upload_url_request_from_dict = FileUploadURLRequest.from_dict(file_upload_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


