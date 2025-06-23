# BlockSkillPointInfoRequest

Request serializer for BlockSkillPointInfoView POST endpoint. Validates request body for updating block skill point information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | **str** | ID of the block to update skill point information for | 
**point_data** | **Dict[str, int]** | Dictionary mapping skill names to point values. Example: {&#39;skill_name&#39;: 5} | 
**overwrite** | **bool** | If True, removes all skills not in point_data. If False, only updates specified skills. | [optional] [default to True]

## Example

```python
from iblai.models.block_skill_point_info_request import BlockSkillPointInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlockSkillPointInfoRequest from a JSON string
block_skill_point_info_request_instance = BlockSkillPointInfoRequest.from_json(json)
# print the JSON string representation of the object
print(BlockSkillPointInfoRequest.to_json())

# convert the object into a dict
block_skill_point_info_request_dict = block_skill_point_info_request_instance.to_dict()
# create an instance of BlockSkillPointInfoRequest from a dict
block_skill_point_info_request_from_dict = BlockSkillPointInfoRequest.from_dict(block_skill_point_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


