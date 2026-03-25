# CreateXblock

Validate input for creating an xblock under a parent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_xblock_id** | **str** | The xblock locator of the parent block. | 
**xblock_type** | [**XblockTypeEnum**](XblockTypeEnum.md) | The type of block to create (section, subsection, unit, html, problem, video).  * &#x60;section&#x60; - section * &#x60;subsection&#x60; - subsection * &#x60;unit&#x60; - unit * &#x60;html&#x60; - html * &#x60;problem&#x60; - problem * &#x60;video&#x60; - video | 
**display_name** | **str** | Display name for the new block. | 
**position** | **str** | Position within the parent (&#39;first&#39;, &#39;last&#39;, or a 1-based index). | [optional] [default to 'last']
**content** | **str** | HTML content body. Only used for html/problem component types. | [optional] [default to '']
**markdown** | **str** | Markdown source. Only used for problem (multiplechoice) components. | [optional] [default to '']

## Example

```python
from iblai.models.create_xblock import CreateXblock

# TODO update the JSON string below
json = "{}"
# create an instance of CreateXblock from a JSON string
create_xblock_instance = CreateXblock.from_json(json)
# print the JSON string representation of the object
print(CreateXblock.to_json())

# convert the object into a dict
create_xblock_dict = create_xblock_instance.to_dict()
# create an instance of CreateXblock from a dict
create_xblock_from_dict = CreateXblock.from_dict(create_xblock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


