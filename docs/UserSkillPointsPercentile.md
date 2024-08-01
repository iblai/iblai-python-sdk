# UserSkillPointsPercentile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**total_points** | **float** |  | 
**percentile** | **float** | Percentile of points for user. If an &#x60;org&#x60; was provided, this is the percentile of the user relative to users within the org. | 

## Example

```python
from iblai.models.user_skill_points_percentile import UserSkillPointsPercentile

# TODO update the JSON string below
json = "{}"
# create an instance of UserSkillPointsPercentile from a JSON string
user_skill_points_percentile_instance = UserSkillPointsPercentile.from_json(json)
# print the JSON string representation of the object
print(UserSkillPointsPercentile.to_json())

# convert the object into a dict
user_skill_points_percentile_dict = user_skill_points_percentile_instance.to_dict()
# create an instance of UserSkillPointsPercentile from a dict
user_skill_points_percentile_from_dict = UserSkillPointsPercentile.from_dict(user_skill_points_percentile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


