# HeygenTemplateResponseSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | [readonly] 
**preview_image_url** | **str** |  | [readonly] 
**name** | **str** |  | 
**provider** | **str** |  | 

## Example

```python
from iblai.models.heygen_template_response_single import HeygenTemplateResponseSingle

# TODO update the JSON string below
json = "{}"
# create an instance of HeygenTemplateResponseSingle from a JSON string
heygen_template_response_single_instance = HeygenTemplateResponseSingle.from_json(json)
# print the JSON string representation of the object
print(HeygenTemplateResponseSingle.to_json())

# convert the object into a dict
heygen_template_response_single_dict = heygen_template_response_single_instance.to_dict()
# create an instance of HeygenTemplateResponseSingle from a dict
heygen_template_response_single_from_dict = HeygenTemplateResponseSingle.from_dict(heygen_template_response_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


