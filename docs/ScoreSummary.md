# ScoreSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**count** | **int** |  | 
**zero_count** | **int** |  | 
**one_count** | **int** |  | 
**average** | **float** |  | 

## Example

```python
from iblai.models.score_summary import ScoreSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreSummary from a JSON string
score_summary_instance = ScoreSummary.from_json(json)
# print the JSON string representation of the object
print(ScoreSummary.to_json())

# convert the object into a dict
score_summary_dict = score_summary_instance.to_dict()
# create an instance of ScoreSummary from a dict
score_summary_from_dict = ScoreSummary.from_dict(score_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


