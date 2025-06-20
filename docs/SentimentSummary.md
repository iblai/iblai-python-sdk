# SentimentSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sentiment_distribution** | **Dict[str, object]** |  | 
**total_sentiments** | **int** |  | 

## Example

```python
from iblai.models.sentiment_summary import SentimentSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SentimentSummary from a JSON string
sentiment_summary_instance = SentimentSummary.from_json(json)
# print the JSON string representation of the object
print(SentimentSummary.to_json())

# convert the object into a dict
sentiment_summary_dict = sentiment_summary_instance.to_dict()
# create an instance of SentimentSummary from a dict
sentiment_summary_from_dict = SentimentSummary.from_dict(sentiment_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


