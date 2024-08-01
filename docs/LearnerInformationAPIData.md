# LearnerInformationAPIData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | learner username | 
**name** | **str** | learner Name | 
**email** | **str** | learner email | 
**date_joined** | **str** | Registration Timestamp e.g 2022-05-05T00:00:00+00:00 | 
**last_activity** | **str** | Last Activity Timestamp e.g 2022-05-05T00:00:00+00:00 | 
**total_assessments** | **int** | Total assessments attempted | [optional] 
**total_time_spent** | **int** | Total time spent in seconds | [optional] 
**total_videos** | **int** | Total videos watched | [optional] 
**course_completions** | **int** | Total courses completed | [optional] 
**time_spent_overtime** | **Dict[str, object]** |  | [optional] 
**continent** | **str** | last location - continent | [optional] 
**continent_code** | **str** | last location - continent code | [optional] 
**country** | **str** | last location - country | [optional] 
**country_code** | **str** | last location - country code | [optional] 
**region** | **str** | last location - region | [optional] 
**region_code** | **str** | last location - region code | [optional] 
**location** | **str** | last location | [optional] 
**city** | **str** | last location - city | [optional] 
**browser** | **str** | last known browser | [optional] 
**operating_system** | **str** | last known operating system | [optional] 
**resolution** | **str** | last known browser resolution | [optional] 

## Example

```python
from iblai.models.learner_information_api_data import LearnerInformationAPIData

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerInformationAPIData from a JSON string
learner_information_api_data_instance = LearnerInformationAPIData.from_json(json)
# print the JSON string representation of the object
print(LearnerInformationAPIData.to_json())

# convert the object into a dict
learner_information_api_data_dict = learner_information_api_data_instance.to_dict()
# create an instance of LearnerInformationAPIData from a dict
learner_information_api_data_from_dict = LearnerInformationAPIData.from_dict(learner_information_api_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


