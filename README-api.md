## Documentation for API Endpoints

All URIs are relative to *https://base.manager.iblai.app*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FallbackLLMApi* | [**ai_account_orgs_fallback_llm_create**](docs/FallbackLLMApi.md#ai_account_orgs_fallback_llm_create) | **POST** /api/ai-account/orgs/{org}/fallback-llm/ | Create fallback LLM configuration
*FallbackLLMApi* | [**ai_account_orgs_fallback_llm_destroy**](docs/FallbackLLMApi.md#ai_account_orgs_fallback_llm_destroy) | **DELETE** /api/ai-account/orgs/{org}/fallback-llm/{id}/ | Delete fallback LLM configuration
*FallbackLLMApi* | [**ai_account_orgs_fallback_llm_partial_update**](docs/FallbackLLMApi.md#ai_account_orgs_fallback_llm_partial_update) | **PATCH** /api/ai-account/orgs/{org}/fallback-llm/{id}/ | Partially update fallback LLM configuration
*FallbackLLMApi* | [**ai_account_orgs_fallback_llm_retrieve**](docs/FallbackLLMApi.md#ai_account_orgs_fallback_llm_retrieve) | **GET** /api/ai-account/orgs/{org}/fallback-llm/{id}/ | Get fallback LLM configuration
*FallbackLLMApi* | [**ai_account_orgs_fallback_llm_update**](docs/FallbackLLMApi.md#ai_account_orgs_fallback_llm_update) | **PUT** /api/ai-account/orgs/{org}/fallback-llm/{id}/ | Update fallback LLM configuration
*AccessCheckApi* | [**access_check_retrieve**](docs/AccessCheckApi.md#access_check_retrieve) | **GET** /access-check/{item_type}/{item_id}/ | 
*AccountApi* | [**account_partial_update**](docs/AccountApi.md#account_partial_update) | **PATCH** /account/ | Partially update auto-recharge preferences
*AccountApi* | [**account_retrieve**](docs/AccountApi.md#account_retrieve) | **GET** /account/ | Get credit account information
*AccountApi* | [**account_update**](docs/AccountApi.md#account_update) | **PUT** /account/ | Update auto-recharge preferences
*AiAccountApi* | [**ai_account_connected_services_callback_retrieve**](docs/AiAccountApi.md#ai_account_connected_services_callback_retrieve) | **GET** /api/ai-account/connected-services/callback/ | 
*AiAccountApi* | [**ai_account_connected_services_orgs_users_destroy**](docs/AiAccountApi.md#ai_account_connected_services_orgs_users_destroy) | **DELETE** /api/ai-account/connected-services/orgs/{org}/users/{user_id}/{id}/ | 
*AiAccountApi* | [**ai_account_connected_services_orgs_users_list**](docs/AiAccountApi.md#ai_account_connected_services_orgs_users_list) | **GET** /api/ai-account/connected-services/orgs/{org}/users/{user_id}/ | 
*AiAccountApi* | [**ai_account_connected_services_orgs_users_retrieve**](docs/AiAccountApi.md#ai_account_connected_services_orgs_users_retrieve) | **GET** /api/ai-account/connected-services/orgs/{org}/users/{user_id}/{id}/ | 
*AiAccountApi* | [**ai_account_connected_services_orgs_users_retrieve2**](docs/AiAccountApi.md#ai_account_connected_services_orgs_users_retrieve2) | **GET** /api/ai-account/connected-services/orgs/{org}/users/{user_id}/{provider}/{service}/ | 
*AiAccountApi* | [**ai_account_orgs_credential_create**](docs/AiAccountApi.md#ai_account_orgs_credential_create) | **POST** /api/ai-account/orgs/{org}/credential/ | 
*AiAccountApi* | [**ai_account_orgs_credential_destroy**](docs/AiAccountApi.md#ai_account_orgs_credential_destroy) | **DELETE** /api/ai-account/orgs/{org}/credential/ | 
*AiAccountApi* | [**ai_account_orgs_credential_partial_update**](docs/AiAccountApi.md#ai_account_orgs_credential_partial_update) | **PATCH** /api/ai-account/orgs/{org}/credential/ | 
*AiAccountApi* | [**ai_account_orgs_credential_retrieve**](docs/AiAccountApi.md#ai_account_orgs_credential_retrieve) | **GET** /api/ai-account/orgs/{org}/credential/ | 
*AiAccountApi* | [**ai_account_orgs_credential_schema_retrieve**](docs/AiAccountApi.md#ai_account_orgs_credential_schema_retrieve) | **GET** /api/ai-account/orgs/{org}/credential/schema/ | 
*AiAccountApi* | [**ai_account_orgs_fallback_llm_list**](docs/AiAccountApi.md#ai_account_orgs_fallback_llm_list) | **GET** /api/ai-account/orgs/{org}/fallback-llm/ | List fallback LLM configurations
*AiAccountApi* | [**ai_account_orgs_integration_credential_create**](docs/AiAccountApi.md#ai_account_orgs_integration_credential_create) | **POST** /api/ai-account/orgs/{org}/integration-credential/ | 
*AiAccountApi* | [**ai_account_orgs_integration_credential_destroy**](docs/AiAccountApi.md#ai_account_orgs_integration_credential_destroy) | **DELETE** /api/ai-account/orgs/{org}/integration-credential/ | 
*AiAccountApi* | [**ai_account_orgs_integration_credential_partial_update**](docs/AiAccountApi.md#ai_account_orgs_integration_credential_partial_update) | **PATCH** /api/ai-account/orgs/{org}/integration-credential/ | 
*AiAccountApi* | [**ai_account_orgs_integration_credential_retrieve**](docs/AiAccountApi.md#ai_account_orgs_integration_credential_retrieve) | **GET** /api/ai-account/orgs/{org}/integration-credential/ | 
*AiAccountApi* | [**ai_account_orgs_integration_credential_schema_retrieve**](docs/AiAccountApi.md#ai_account_orgs_integration_credential_schema_retrieve) | **GET** /api/ai-account/orgs/{org}/integration-credential/schema/ | 
*AiAccountApi* | [**ai_account_orgs_llm_credential_create**](docs/AiAccountApi.md#ai_account_orgs_llm_credential_create) | **POST** /api/ai-account/orgs/{org}/llm-credential/ | 
*AiAccountApi* | [**ai_account_orgs_llm_credential_destroy**](docs/AiAccountApi.md#ai_account_orgs_llm_credential_destroy) | **DELETE** /api/ai-account/orgs/{org}/llm-credential/ | 
*AiAccountApi* | [**ai_account_orgs_llm_credential_partial_update**](docs/AiAccountApi.md#ai_account_orgs_llm_credential_partial_update) | **PATCH** /api/ai-account/orgs/{org}/llm-credential/ | 
*AiAccountApi* | [**ai_account_orgs_llm_credential_retrieve**](docs/AiAccountApi.md#ai_account_orgs_llm_credential_retrieve) | **GET** /api/ai-account/orgs/{org}/llm-credential/ | 
*AiAccountApi* | [**ai_account_orgs_masked_integration_credential_list**](docs/AiAccountApi.md#ai_account_orgs_masked_integration_credential_list) | **GET** /api/ai-account/orgs/{org}/masked-integration-credential/ | 
*AiAccountApi* | [**ai_account_orgs_masked_llm_credential_retrieve**](docs/AiAccountApi.md#ai_account_orgs_masked_llm_credential_retrieve) | **GET** /api/ai-account/orgs/{org}/masked-llm-credential/ | 
*AiAccountApi* | [**ai_account_orgs_oauth_services_list**](docs/AiAccountApi.md#ai_account_orgs_oauth_services_list) | **GET** /api/ai-account/orgs/{org}/oauth-services/ | 
*AiAccountApi* | [**ai_account_orgs_oauth_services_scopes_list**](docs/AiAccountApi.md#ai_account_orgs_oauth_services_scopes_list) | **GET** /api/ai-account/orgs/{org}/oauth-services/{service_name}/scopes/ | 
*AiAccountApi* | [**ai_account_orgs_use_default_llm_key_create**](docs/AiAccountApi.md#ai_account_orgs_use_default_llm_key_create) | **POST** /api/ai-account/orgs/{org}/use-default-llm-key/ | 
*AiAccountApi* | [**ai_account_orgs_use_free_trial_create**](docs/AiAccountApi.md#ai_account_orgs_use_free_trial_create) | **POST** /api/ai-account/orgs/{org}/use-free-trial/ | 
*AiAccountApi* | [**ai_account_orgs_users_chat_privacy_config_retrieve**](docs/AiAccountApi.md#ai_account_orgs_users_chat_privacy_config_retrieve) | **GET** /api/ai-account/orgs/{org}/users/{user_id}/chat-privacy-config/ | 
*AiAccountApi* | [**ai_account_orgs_users_chat_privacy_settings_create**](docs/AiAccountApi.md#ai_account_orgs_users_chat_privacy_settings_create) | **POST** /api/ai-account/orgs/{org}/users/{user_id}/chat-privacy-settings/ | 
*AiAccountApi* | [**ai_account_orgs_users_chat_privacy_settings_retrieve**](docs/AiAccountApi.md#ai_account_orgs_users_chat_privacy_settings_retrieve) | **GET** /api/ai-account/orgs/{org}/users/{user_id}/chat-privacy-settings/ | 
*AiAccountApi* | [**ai_account_orgs_users_default_llm_key_usage_retrieve**](docs/AiAccountApi.md#ai_account_orgs_users_default_llm_key_usage_retrieve) | **GET** /api/ai-account/orgs/{org}/users/{user_id}/default-llm-key-usage | 
*AiAccountApi* | [**ai_account_orgs_users_free_trial_retrieve**](docs/AiAccountApi.md#ai_account_orgs_users_free_trial_retrieve) | **GET** /api/ai-account/orgs/{org}/users/{user_id}/free-trial | 
*AiAccountApi* | [**ai_account_orgs_users_tenant_settings_create**](docs/AiAccountApi.md#ai_account_orgs_users_tenant_settings_create) | **POST** /api/ai-account/orgs/{org}/users/{user_id}/tenant-settings/ | 
*AiAccountApi* | [**ai_account_orgs_users_tenant_settings_retrieve**](docs/AiAccountApi.md#ai_account_orgs_users_tenant_settings_retrieve) | **GET** /api/ai-account/orgs/{org}/users/{user_id}/tenant-settings/ | 
*AiAnalyticsApi* | [**ai_analytics_audience_orgs_active_users_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_audience_orgs_active_users_over_time_retrieve) | **GET** /api/ai-analytics/audience/orgs/{org}/active-users/over-time | 
*AiAnalyticsApi* | [**ai_analytics_audience_orgs_active_users_per_course_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_audience_orgs_active_users_per_course_retrieve) | **GET** /api/ai-analytics/audience/orgs/{org}/active-users/per-course | 
*AiAnalyticsApi* | [**ai_analytics_audience_orgs_active_users_users_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_audience_orgs_active_users_users_retrieve) | **GET** /api/ai-analytics/audience/orgs/{org}/active-users/users | 
*AiAnalyticsApi* | [**ai_analytics_audience_orgs_enrollments_courses_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_audience_orgs_enrollments_courses_over_time_retrieve) | **GET** /api/ai-analytics/audience/orgs/{org}/enrollments/courses/{course_id}/over-time | 
*AiAnalyticsApi* | [**ai_analytics_audience_orgs_enrollments_courses_users_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_audience_orgs_enrollments_courses_users_retrieve) | **GET** /api/ai-analytics/audience/orgs/{org}/enrollments/courses/{course_id}/users | 
*AiAnalyticsApi* | [**ai_analytics_audience_orgs_enrollments_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_audience_orgs_enrollments_over_time_retrieve) | **GET** /api/ai-analytics/audience/orgs/{org}/enrollments/over-time | 
*AiAnalyticsApi* | [**ai_analytics_audience_orgs_enrollments_per_course_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_audience_orgs_enrollments_per_course_retrieve) | **GET** /api/ai-analytics/audience/orgs/{org}/enrollments/per-course | 
*AiAnalyticsApi* | [**ai_analytics_audience_orgs_registered_users_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_audience_orgs_registered_users_over_time_retrieve) | **GET** /api/ai-analytics/audience/orgs/{org}/registered-users/over-time | 
*AiAnalyticsApi* | [**ai_analytics_audience_orgs_registered_users_per_course_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_audience_orgs_registered_users_per_course_retrieve) | **GET** /api/ai-analytics/audience/orgs/{org}/registered-users/per-course | 
*AiAnalyticsApi* | [**ai_analytics_audience_orgs_registered_users_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_audience_orgs_registered_users_retrieve) | **GET** /api/ai-analytics/audience/orgs/{org}/registered-users/ | 
*AiAnalyticsApi* | [**ai_analytics_costs_pertenant_list**](docs/AiAnalyticsApi.md#ai_analytics_costs_pertenant_list) | **GET** /api/ai-analytics/costs/pertenant/ | 
*AiAnalyticsApi* | [**ai_analytics_departments_orgs_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_departments_orgs_retrieve) | **GET** /api/ai-analytics/departments/orgs/{org}/ | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_activity_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_activity_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/activity | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_course_completion_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_course_completion_over_time_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/course_completion/over-time | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_course_completion_per_course_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_course_completion_per_course_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/course_completion/per-course | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_courses_time_average_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_courses_time_average_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/courses/{course_id}/time/average | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_courses_time_detail_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_courses_time_detail_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/courses/{course_id}/time/detail | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_courses_time_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_courses_time_over_time_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/courses/{course_id}/time/over-time | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_courses_time_users_detail_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_courses_time_users_detail_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/courses/{course_id}/time/users/{user_id}/detail | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_courses_time_users_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_courses_time_users_over_time_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/courses/{course_id}/time/users/{user_id}/over-time | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_courses_time_users_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_courses_time_users_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/courses/{course_id}/time/users | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_courses_videos_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_courses_videos_over_time_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/courses/{course_id}/videos/over-time | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_courses_videos_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_courses_videos_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/courses/{course_id}/videos/ | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_courses_videos_summary_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_courses_videos_summary_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/courses/{course_id}/videos/summary | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_courses_videos_users_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_courses_videos_users_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/courses/{course_id}/videos/users | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_time_average_perlearner_percourse_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_time_average_perlearner_percourse_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/time/average-perlearner-percourse | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_time_average_with_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_time_average_with_over_time_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/time/average-with-over-time | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_time_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_time_over_time_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/time/over-time | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_time_per_course_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_time_per_course_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/time/per-course | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_videos_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_videos_over_time_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/videos/over-time | 
*AiAnalyticsApi* | [**ai_analytics_engagement_orgs_videos_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_engagement_orgs_videos_retrieve) | **GET** /api/ai-analytics/engagement/orgs/{org}/videos/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_average_messages_per_session_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_average_messages_per_session_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/average-messages-per-session/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_chat_history_create**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_chat_history_create) | **POST** /api/ai-analytics/orgs/{org}/users/{user_id}/chat-history/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_chat_history_destroy**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_chat_history_destroy) | **DELETE** /api/ai-analytics/orgs/{org}/users/{user_id}/chat-history/{id}/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_chat_history_filter_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_chat_history_filter_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/chat-history-filter/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_chat_history_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_chat_history_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/chat-history/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_chat_history_partial_update**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_chat_history_partial_update) | **PATCH** /api/ai-analytics/orgs/{org}/users/{user_id}/chat-history/{id}/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_chat_history_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_chat_history_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/chat-history/{id}/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_chat_history_update**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_chat_history_update) | **PUT** /api/ai-analytics/orgs/{org}/users/{user_id}/chat-history/{id}/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_conversation_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_conversation_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/conversation/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_conversation_summary_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_conversation_summary_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/conversation-summary/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_costs_model_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_costs_model_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/costs/model/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_costs_permentor_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_costs_permentor_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/costs/permentor/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_costs_peruser_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_costs_peruser_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/costs/peruser/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_mentor_detail_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_mentor_detail_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/mentor-detail/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_mentor_summary_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_mentor_summary_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/mentor-summary/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_mentors_cost_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_mentors_cost_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/mentors/{mentor_unique_id}/cost/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_most_discussed_topics_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_most_discussed_topics_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/most-discussed-topics/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_observations_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_observations_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/observations/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_observations_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_observations_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/observations/{id}/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_overview_summary_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_overview_summary_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/overview-summary/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_rating_summary_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_rating_summary_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/rating-summary/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_registered_users_trend_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_registered_users_trend_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/registered-users-trend/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_sentiment_count_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_sentiment_count_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/sentiment-count/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_tenant_cost_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_tenant_cost_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/tenant-cost/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_top_students_by_chat_messages_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_top_students_by_chat_messages_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/top-students-by-chat-messages/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_topic_overview_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_topic_overview_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/topic-overview/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_topic_statistics_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_topic_statistics_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/topic-statistics/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_topics_summary_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_topics_summary_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/topics/summary/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_total_users_by_mentor_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_total_users_by_mentor_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/total-users-by-mentor/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_traces_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_traces_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/traces/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_traces_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_traces_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/traces/{id}/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_transcripts_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_transcripts_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/transcripts/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_usage_summary_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_usage_summary_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/usage-summary/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_user_cohorts_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_user_cohorts_over_time_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/user-cohorts-over-time/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_user_cost_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_user_cost_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/user-cost/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_user_feedback_list**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_user_feedback_list) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/user-feedback/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_user_metrics_pie_chart_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_user_metrics_pie_chart_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/user-metrics-pie-chart/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_user_metrics_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_user_metrics_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/user-metrics/ | 
*AiAnalyticsApi* | [**ai_analytics_orgs_users_user_sentiment_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_orgs_users_user_sentiment_retrieve) | **GET** /api/ai-analytics/orgs/{org}/users/{user_id}/user-sentiment/ | 
*AiAnalyticsApi* | [**ai_analytics_overview_orgs_active_users_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_overview_orgs_active_users_retrieve) | **GET** /api/ai-analytics/overview/orgs/{org}/active-users | 
*AiAnalyticsApi* | [**ai_analytics_overview_orgs_average_grade_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_overview_orgs_average_grade_retrieve) | **GET** /api/ai-analytics/overview/orgs/{org}/average-grade | 
*AiAnalyticsApi* | [**ai_analytics_overview_orgs_courses_completions_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_overview_orgs_courses_completions_retrieve) | **GET** /api/ai-analytics/overview/orgs/{org}/courses/completions | 
*AiAnalyticsApi* | [**ai_analytics_overview_orgs_learners_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_overview_orgs_learners_retrieve) | **GET** /api/ai-analytics/overview/orgs/{org}/learners | 
*AiAnalyticsApi* | [**ai_analytics_overview_orgs_most_active_courses_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_overview_orgs_most_active_courses_retrieve) | **GET** /api/ai-analytics/overview/orgs/{org}/most-active-courses | 
*AiAnalyticsApi* | [**ai_analytics_overview_orgs_registered_users_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_overview_orgs_registered_users_retrieve) | **GET** /api/ai-analytics/overview/orgs/{org}/registered-users | 
*AiAnalyticsApi* | [**ai_analytics_performance_orgs_courses_grading_average_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_performance_orgs_courses_grading_average_retrieve) | **GET** /api/ai-analytics/performance/orgs/{org}/courses/{course_id}/grading/average | 
*AiAnalyticsApi* | [**ai_analytics_performance_orgs_courses_grading_average_with_cutoff_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_performance_orgs_courses_grading_average_with_cutoff_retrieve) | **GET** /api/ai-analytics/performance/orgs/{org}/courses/{course_id}/grading/average-with-cutoff | 
*AiAnalyticsApi* | [**ai_analytics_performance_orgs_courses_grading_detail_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_performance_orgs_courses_grading_detail_retrieve) | **GET** /api/ai-analytics/performance/orgs/{org}/courses/{course_id}/grading/detail | 
*AiAnalyticsApi* | [**ai_analytics_performance_orgs_courses_grading_per_learner_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_performance_orgs_courses_grading_per_learner_retrieve) | **GET** /api/ai-analytics/performance/orgs/{org}/courses/{course_id}/grading/per-learner | 
*AiAnalyticsApi* | [**ai_analytics_performance_orgs_courses_grading_summary_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_performance_orgs_courses_grading_summary_retrieve) | **GET** /api/ai-analytics/performance/orgs/{org}/courses/{course_id}/grading/summary | 
*AiAnalyticsApi* | [**ai_analytics_performance_orgs_grading_average_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_performance_orgs_grading_average_retrieve) | **GET** /api/ai-analytics/performance/orgs/{org}/grading/average | 
*AiAnalyticsApi* | [**ai_analytics_performance_orgs_grading_per_course_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_performance_orgs_grading_per_course_retrieve) | **GET** /api/ai-analytics/performance/orgs/{org}/grading/per-course | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_learners_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_learners_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/learners | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_activity_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_activity_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/activity/ | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_courses_grading_cutoffs_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_courses_grading_cutoffs_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/grading/cutoffs | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_courses_grading_detail_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_courses_grading_detail_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/grading/detail | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_courses_grading_summary_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_courses_grading_summary_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/grading/summary | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_courses_overview_engagement_index_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_courses_overview_engagement_index_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/overview/engagement-index | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_courses_overview_grade_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_courses_overview_grade_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/overview/grade | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_courses_overview_performance_index_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_courses_overview_performance_index_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/overview/performance-index | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_courses_overview_time_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_courses_overview_time_over_time_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/overview/time/over-time | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_courses_videos_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_courses_videos_over_time_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/videos/over-time | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_courses_videos_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_courses_videos_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/videos | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_grades_per_course_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_grades_per_course_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/grades/per-course | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_info_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_info_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/info | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_last_access_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_last_access_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/last-access | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_overview_engagement_index_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_overview_engagement_index_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/overview/engagement-index | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_overview_grades_average_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_overview_grades_average_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/overview/grades/average | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_overview_performance_index_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_overview_performance_index_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/overview/performance-index | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_overview_time_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_overview_time_over_time_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/overview/time/over-time | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_videos_over_time_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_videos_over_time_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/videos/over-time | 
*AiAnalyticsApi* | [**ai_analytics_perlearner_orgs_users_videos_per_course_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_perlearner_orgs_users_videos_per_course_retrieve) | **GET** /api/ai-analytics/perlearner/orgs/{org}/users/{user_id}/videos/per-course | 
*AiAnalyticsApi* | [**ai_analytics_user_groups_orgs_retrieve**](docs/AiAnalyticsApi.md#ai_analytics_user_groups_orgs_retrieve) | **GET** /api/ai-analytics/user-groups/orgs/{org}/ | 
*AiAnalyticsApi* | [**analytics_conversations_retrieve**](docs/AiAnalyticsApi.md#analytics_conversations_retrieve) | **GET** /api/analytics/conversations/ | 
*AiAnalyticsApi* | [**analytics_financial_details_retrieve**](docs/AiAnalyticsApi.md#analytics_financial_details_retrieve) | **GET** /api/analytics/financial/details/ | 
*AiAnalyticsApi* | [**analytics_financial_invoice_retrieve**](docs/AiAnalyticsApi.md#analytics_financial_invoice_retrieve) | **GET** /api/analytics/financial/invoice/ | 
*AiAnalyticsApi* | [**analytics_financial_retrieve**](docs/AiAnalyticsApi.md#analytics_financial_retrieve) | **GET** /api/analytics/financial/ | 
*AiAnalyticsApi* | [**analytics_learner_details_retrieve**](docs/AiAnalyticsApi.md#analytics_learner_details_retrieve) | **GET** /api/analytics/learner/details | 
*AiAnalyticsApi* | [**analytics_learners_list_retrieve**](docs/AiAnalyticsApi.md#analytics_learners_list_retrieve) | **GET** /api/analytics/learners/list/ | 
*AiAnalyticsApi* | [**analytics_learners_retrieve**](docs/AiAnalyticsApi.md#analytics_learners_retrieve) | **GET** /api/analytics/learners/ | 
*AiAnalyticsApi* | [**analytics_messages_details_retrieve**](docs/AiAnalyticsApi.md#analytics_messages_details_retrieve) | **GET** /api/analytics/messages/details/ | 
*AiAnalyticsApi* | [**analytics_messages_retrieve**](docs/AiAnalyticsApi.md#analytics_messages_retrieve) | **GET** /api/analytics/messages/ | 
*AiAnalyticsApi* | [**analytics_orgs_time_update_create**](docs/AiAnalyticsApi.md#analytics_orgs_time_update_create) | **POST** /api/analytics/orgs/{org}/time/update/ | 
*AiAnalyticsApi* | [**analytics_ratings_retrieve**](docs/AiAnalyticsApi.md#analytics_ratings_retrieve) | **GET** /api/analytics/ratings/ | 
*AiAnalyticsApi* | [**analytics_sessions_retrieve**](docs/AiAnalyticsApi.md#analytics_sessions_retrieve) | **GET** /api/analytics/sessions/ | 
*AiAnalyticsApi* | [**analytics_time_retrieve**](docs/AiAnalyticsApi.md#analytics_time_retrieve) | **GET** /api/analytics/time/ | 
*AiAnalyticsApi* | [**analytics_time_spent_user_retrieve**](docs/AiAnalyticsApi.md#analytics_time_spent_user_retrieve) | **GET** /api/analytics/time-spent/user/ | Get total time spent for current user
*AiAnalyticsApi* | [**analytics_topics_details_retrieve**](docs/AiAnalyticsApi.md#analytics_topics_details_retrieve) | **GET** /api/analytics/topics/details/ | 
*AiAnalyticsApi* | [**analytics_topics_retrieve**](docs/AiAnalyticsApi.md#analytics_topics_retrieve) | **GET** /api/analytics/topics/ | 
*AiAnalyticsApi* | [**analytics_users_details_retrieve**](docs/AiAnalyticsApi.md#analytics_users_details_retrieve) | **GET** /api/analytics/users/details/ | 
*AiAnalyticsApi* | [**analytics_users_retrieve**](docs/AiAnalyticsApi.md#analytics_users_retrieve) | **GET** /api/analytics/users/ | 
*AiAnalyticsApi* | [**audience_orgs_active_users_over_time_retrieve**](docs/AiAnalyticsApi.md#audience_orgs_active_users_over_time_retrieve) | **GET** /api/audience/orgs/{org}/active-users/over-time | 
*AiAnalyticsApi* | [**audience_orgs_active_users_per_course_retrieve**](docs/AiAnalyticsApi.md#audience_orgs_active_users_per_course_retrieve) | **GET** /api/audience/orgs/{org}/active-users/per-course | 
*AiAnalyticsApi* | [**audience_orgs_active_users_users_retrieve**](docs/AiAnalyticsApi.md#audience_orgs_active_users_users_retrieve) | **GET** /api/audience/orgs/{org}/active-users/users | 
*AiAnalyticsApi* | [**audience_orgs_enrollments_courses_over_time_retrieve**](docs/AiAnalyticsApi.md#audience_orgs_enrollments_courses_over_time_retrieve) | **GET** /api/audience/orgs/{org}/enrollments/courses/{course_id}/over-time | 
*AiAnalyticsApi* | [**audience_orgs_enrollments_courses_users_retrieve**](docs/AiAnalyticsApi.md#audience_orgs_enrollments_courses_users_retrieve) | **GET** /api/audience/orgs/{org}/enrollments/courses/{course_id}/users | 
*AiAnalyticsApi* | [**audience_orgs_enrollments_over_time_retrieve**](docs/AiAnalyticsApi.md#audience_orgs_enrollments_over_time_retrieve) | **GET** /api/audience/orgs/{org}/enrollments/over-time | 
*AiAnalyticsApi* | [**audience_orgs_enrollments_per_course_retrieve**](docs/AiAnalyticsApi.md#audience_orgs_enrollments_per_course_retrieve) | **GET** /api/audience/orgs/{org}/enrollments/per-course | 
*AiAnalyticsApi* | [**audience_orgs_registered_users_over_time_retrieve**](docs/AiAnalyticsApi.md#audience_orgs_registered_users_over_time_retrieve) | **GET** /api/audience/orgs/{org}/registered-users/over-time | 
*AiAnalyticsApi* | [**audience_orgs_registered_users_per_course_retrieve**](docs/AiAnalyticsApi.md#audience_orgs_registered_users_per_course_retrieve) | **GET** /api/audience/orgs/{org}/registered-users/per-course | 
*AiAnalyticsApi* | [**audience_orgs_registered_users_retrieve**](docs/AiAnalyticsApi.md#audience_orgs_registered_users_retrieve) | **GET** /api/audience/orgs/{org}/registered-users/ | 
*AiAnalyticsApi* | [**engagement_orgs_activity_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_activity_retrieve) | **GET** /api/engagement/orgs/{org}/activity | 
*AiAnalyticsApi* | [**engagement_orgs_course_completion_over_time_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_course_completion_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/course_completion/over-time | 
*AiAnalyticsApi* | [**engagement_orgs_course_completion_per_course_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_course_completion_per_course_retrieve) | **GET** /api/engagement/orgs/{org}/course_completion/per-course | 
*AiAnalyticsApi* | [**engagement_orgs_courses_time_average_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_courses_time_average_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/time/average | 
*AiAnalyticsApi* | [**engagement_orgs_courses_time_detail_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_courses_time_detail_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/time/detail | 
*AiAnalyticsApi* | [**engagement_orgs_courses_time_over_time_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_courses_time_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/time/over-time | 
*AiAnalyticsApi* | [**engagement_orgs_courses_time_users_detail_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_courses_time_users_detail_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/time/users/{user_id}/detail | 
*AiAnalyticsApi* | [**engagement_orgs_courses_time_users_over_time_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_courses_time_users_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/time/users/{user_id}/over-time | 
*AiAnalyticsApi* | [**engagement_orgs_courses_time_users_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_courses_time_users_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/time/users | 
*AiAnalyticsApi* | [**engagement_orgs_courses_videos_over_time_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_courses_videos_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/videos/over-time | 
*AiAnalyticsApi* | [**engagement_orgs_courses_videos_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_courses_videos_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/videos/ | 
*AiAnalyticsApi* | [**engagement_orgs_courses_videos_summary_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_courses_videos_summary_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/videos/summary | 
*AiAnalyticsApi* | [**engagement_orgs_courses_videos_users_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_courses_videos_users_retrieve) | **GET** /api/engagement/orgs/{org}/courses/{course_id}/videos/users | 
*AiAnalyticsApi* | [**engagement_orgs_time_average_perlearner_percourse_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_time_average_perlearner_percourse_retrieve) | **GET** /api/engagement/orgs/{org}/time/average-perlearner-percourse | 
*AiAnalyticsApi* | [**engagement_orgs_time_average_with_over_time_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_time_average_with_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/time/average-with-over-time | 
*AiAnalyticsApi* | [**engagement_orgs_time_over_time_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_time_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/time/over-time | 
*AiAnalyticsApi* | [**engagement_orgs_time_per_course_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_time_per_course_retrieve) | **GET** /api/engagement/orgs/{org}/time/per-course | 
*AiAnalyticsApi* | [**engagement_orgs_videos_over_time_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_videos_over_time_retrieve) | **GET** /api/engagement/orgs/{org}/videos/over-time | 
*AiAnalyticsApi* | [**engagement_orgs_videos_retrieve**](docs/AiAnalyticsApi.md#engagement_orgs_videos_retrieve) | **GET** /api/engagement/orgs/{org}/videos/ | 
*AiAnalyticsApi* | [**get_content_analytics**](docs/AiAnalyticsApi.md#get_content_analytics) | **GET** /api/analytics/content/ | Get Content Analytics
*AiAnalyticsApi* | [**get_content_details**](docs/AiAnalyticsApi.md#get_content_details) | **GET** /api/analytics/content/details/{content_id}/ | Get Content Details
*AiAnalyticsApi* | [**overview_orgs_active_users_retrieve**](docs/AiAnalyticsApi.md#overview_orgs_active_users_retrieve) | **GET** /api/overview/orgs/{org}/active-users | 
*AiAnalyticsApi* | [**overview_orgs_average_grade_retrieve**](docs/AiAnalyticsApi.md#overview_orgs_average_grade_retrieve) | **GET** /api/overview/orgs/{org}/average-grade | 
*AiAnalyticsApi* | [**overview_orgs_courses_completions_retrieve**](docs/AiAnalyticsApi.md#overview_orgs_courses_completions_retrieve) | **GET** /api/overview/orgs/{org}/courses/completions | 
*AiAnalyticsApi* | [**overview_orgs_learners_retrieve**](docs/AiAnalyticsApi.md#overview_orgs_learners_retrieve) | **GET** /api/overview/orgs/{org}/learners | 
*AiAnalyticsApi* | [**overview_orgs_most_active_courses_retrieve**](docs/AiAnalyticsApi.md#overview_orgs_most_active_courses_retrieve) | **GET** /api/overview/orgs/{org}/most-active-courses | 
*AiAnalyticsApi* | [**overview_orgs_registered_users_retrieve**](docs/AiAnalyticsApi.md#overview_orgs_registered_users_retrieve) | **GET** /api/overview/orgs/{org}/registered-users | 
*AiAnalyticsApi* | [**performance_orgs_courses_grading_average_retrieve**](docs/AiAnalyticsApi.md#performance_orgs_courses_grading_average_retrieve) | **GET** /api/performance/orgs/{org}/courses/{course_id}/grading/average | 
*AiAnalyticsApi* | [**performance_orgs_courses_grading_average_with_cutoff_retrieve**](docs/AiAnalyticsApi.md#performance_orgs_courses_grading_average_with_cutoff_retrieve) | **GET** /api/performance/orgs/{org}/courses/{course_id}/grading/average-with-cutoff | 
*AiAnalyticsApi* | [**performance_orgs_courses_grading_detail_retrieve**](docs/AiAnalyticsApi.md#performance_orgs_courses_grading_detail_retrieve) | **GET** /api/performance/orgs/{org}/courses/{course_id}/grading/detail | 
*AiAnalyticsApi* | [**performance_orgs_courses_grading_per_learner_retrieve**](docs/AiAnalyticsApi.md#performance_orgs_courses_grading_per_learner_retrieve) | **GET** /api/performance/orgs/{org}/courses/{course_id}/grading/per-learner | 
*AiAnalyticsApi* | [**performance_orgs_courses_grading_summary_retrieve**](docs/AiAnalyticsApi.md#performance_orgs_courses_grading_summary_retrieve) | **GET** /api/performance/orgs/{org}/courses/{course_id}/grading/summary | 
*AiAnalyticsApi* | [**performance_orgs_grading_average_retrieve**](docs/AiAnalyticsApi.md#performance_orgs_grading_average_retrieve) | **GET** /api/performance/orgs/{org}/grading/average | 
*AiAnalyticsApi* | [**performance_orgs_grading_per_course_retrieve**](docs/AiAnalyticsApi.md#performance_orgs_grading_per_course_retrieve) | **GET** /api/performance/orgs/{org}/grading/per-course | 
*AiAnalyticsApi* | [**perlearner_orgs_learners_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_learners_retrieve) | **GET** /api/perlearner/orgs/{org}/learners | 
*AiAnalyticsApi* | [**perlearner_orgs_users_activity_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_activity_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/activity/ | 
*AiAnalyticsApi* | [**perlearner_orgs_users_courses_grading_cutoffs_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_courses_grading_cutoffs_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/grading/cutoffs | 
*AiAnalyticsApi* | [**perlearner_orgs_users_courses_grading_detail_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_courses_grading_detail_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/grading/detail | 
*AiAnalyticsApi* | [**perlearner_orgs_users_courses_grading_summary_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_courses_grading_summary_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/grading/summary | 
*AiAnalyticsApi* | [**perlearner_orgs_users_courses_overview_engagement_index_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_courses_overview_engagement_index_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/overview/engagement-index | 
*AiAnalyticsApi* | [**perlearner_orgs_users_courses_overview_grade_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_courses_overview_grade_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/overview/grade | 
*AiAnalyticsApi* | [**perlearner_orgs_users_courses_overview_performance_index_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_courses_overview_performance_index_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/overview/performance-index | 
*AiAnalyticsApi* | [**perlearner_orgs_users_courses_overview_time_over_time_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_courses_overview_time_over_time_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/overview/time/over-time | 
*AiAnalyticsApi* | [**perlearner_orgs_users_courses_videos_over_time_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_courses_videos_over_time_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/videos/over-time | 
*AiAnalyticsApi* | [**perlearner_orgs_users_courses_videos_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_courses_videos_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/courses/{course_id}/videos | 
*AiAnalyticsApi* | [**perlearner_orgs_users_grades_per_course_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_grades_per_course_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/grades/per-course | 
*AiAnalyticsApi* | [**perlearner_orgs_users_info_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_info_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/info | 
*AiAnalyticsApi* | [**perlearner_orgs_users_last_access_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_last_access_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/last-access | 
*AiAnalyticsApi* | [**perlearner_orgs_users_overview_engagement_index_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_overview_engagement_index_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/overview/engagement-index | 
*AiAnalyticsApi* | [**perlearner_orgs_users_overview_grades_average_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_overview_grades_average_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/overview/grades/average | 
*AiAnalyticsApi* | [**perlearner_orgs_users_overview_performance_index_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_overview_performance_index_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/overview/performance-index | 
*AiAnalyticsApi* | [**perlearner_orgs_users_overview_time_over_time_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_overview_time_over_time_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/overview/time/over-time | 
*AiAnalyticsApi* | [**perlearner_orgs_users_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_retrieve) | **GET** /api/perlearner/orgs/{org}/users | 
*AiAnalyticsApi* | [**perlearner_orgs_users_videos_over_time_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_videos_over_time_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/videos/over-time | 
*AiAnalyticsApi* | [**perlearner_orgs_users_videos_per_course_retrieve**](docs/AiAnalyticsApi.md#perlearner_orgs_users_videos_per_course_retrieve) | **GET** /api/perlearner/orgs/{org}/users/{user_id}/videos/per-course | 
*AiAnalyticsApi* | [**platform_orgs_courses_count_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_count_retrieve) | **GET** /api/platform/orgs/{org}/courses/count | 
*AiAnalyticsApi* | [**platform_orgs_courses_grades_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_grades_retrieve) | **GET** /api/platform/orgs/{org}/courses/grades | 
*AiAnalyticsApi* | [**platform_orgs_courses_progress_average_days_to_complete_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_progress_average_days_to_complete_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/average-days-to-complete | 
*AiAnalyticsApi* | [**platform_orgs_courses_progress_average_time_to_complete_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_progress_average_time_to_complete_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/average-time-to-complete | 
*AiAnalyticsApi* | [**platform_orgs_courses_progress_completed_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_progress_completed_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/completed | 
*AiAnalyticsApi* | [**platform_orgs_courses_progress_completion_rate_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_progress_completion_rate_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/completion-rate | 
*AiAnalyticsApi* | [**platform_orgs_courses_progress_in_progress_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_progress_in_progress_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/in-progress | 
*AiAnalyticsApi* | [**platform_orgs_courses_progress_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_progress_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/ | 
*AiAnalyticsApi* | [**platform_orgs_courses_progress_started_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_progress_started_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/progress/started | 
*AiAnalyticsApi* | [**platform_orgs_courses_users_grades_passed_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_users_grades_passed_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/grades/passed | 
*AiAnalyticsApi* | [**platform_orgs_courses_users_progress_days_to_complete_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_users_progress_days_to_complete_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/progress/days-to-complete | 
*AiAnalyticsApi* | [**platform_orgs_courses_users_progress_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_users_progress_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/progress | 
*AiAnalyticsApi* | [**platform_orgs_courses_users_time_count_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_users_time_count_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/time/count | 
*AiAnalyticsApi* | [**platform_orgs_courses_users_videos_count_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_users_videos_count_retrieve) | **GET** /api/platform/orgs/{org}/courses/{course_id}/users/{user_id}/videos/count | 
*AiAnalyticsApi* | [**platform_orgs_courses_videos_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_courses_videos_retrieve) | **GET** /api/platform/orgs/{org}/courses/videos | 
*AiAnalyticsApi* | [**platform_orgs_courses_videos_retrieve2**](docs/AiAnalyticsApi.md#platform_orgs_courses_videos_retrieve2) | **GET** /api/platform/orgs/{org}/courses/{course_id}/videos/ | 
*AiAnalyticsApi* | [**platform_orgs_progress_completed_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_progress_completed_retrieve) | **GET** /api/platform/orgs/{org}/progress/completed | 
*AiAnalyticsApi* | [**platform_orgs_progress_completion_rate_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_progress_completion_rate_retrieve) | **GET** /api/platform/orgs/{org}/progress/completion-rate | 
*AiAnalyticsApi* | [**platform_orgs_progress_in_progress_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_progress_in_progress_retrieve) | **GET** /api/platform/orgs/{org}/progress/in-progress | 
*AiAnalyticsApi* | [**platform_orgs_progress_started_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_progress_started_retrieve) | **GET** /api/platform/orgs/{org}/progress/started | 
*AiAnalyticsApi* | [**platform_orgs_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_retrieve) | **GET** /api/platform/orgs/{org}/ | 
*AiAnalyticsApi* | [**platform_orgs_time_count_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_time_count_retrieve) | **GET** /api/platform/orgs/{org}/time/count | 
*AiAnalyticsApi* | [**platform_orgs_users_active_count_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_users_active_count_retrieve) | **GET** /api/platform/orgs/{org}/users/active/count | 
*AiAnalyticsApi* | [**platform_orgs_users_count_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_users_count_retrieve) | **GET** /api/platform/orgs/{org}/users/count | 
*AiAnalyticsApi* | [**platform_orgs_users_courses_completed_count_retrieve**](docs/AiAnalyticsApi.md#platform_orgs_users_courses_completed_count_retrieve) | **GET** /api/platform/orgs/{org}/users/courses-completed/count | 
*AiBotApi* | [**ai_bot_v1_bots_bot_commands_create**](docs/AiBotApi.md#ai_bot_v1_bots_bot_commands_create) | **POST** /api/ai-bot/v1/bots/{org}/bot-commands/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_commands_destroy**](docs/AiBotApi.md#ai_bot_v1_bots_bot_commands_destroy) | **DELETE** /api/ai-bot/v1/bots/{org}/bot-commands/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_commands_list**](docs/AiBotApi.md#ai_bot_v1_bots_bot_commands_list) | **GET** /api/ai-bot/v1/bots/{org}/bot-commands/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_commands_partial_update**](docs/AiBotApi.md#ai_bot_v1_bots_bot_commands_partial_update) | **PATCH** /api/ai-bot/v1/bots/{org}/bot-commands/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_commands_retrieve**](docs/AiBotApi.md#ai_bot_v1_bots_bot_commands_retrieve) | **GET** /api/ai-bot/v1/bots/{org}/bot-commands/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_commands_update**](docs/AiBotApi.md#ai_bot_v1_bots_bot_commands_update) | **PUT** /api/ai-bot/v1/bots/{org}/bot-commands/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_config_discord_partial_update**](docs/AiBotApi.md#ai_bot_v1_bots_bot_config_discord_partial_update) | **PATCH** /api/ai-bot/v1/bots/{org}/bot/{id}/config/discord/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_config_discord_retrieve**](docs/AiBotApi.md#ai_bot_v1_bots_bot_config_discord_retrieve) | **GET** /api/ai-bot/v1/bots/{org}/bot/{id}/config/discord/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_config_slack_retrieve**](docs/AiBotApi.md#ai_bot_v1_bots_bot_config_slack_retrieve) | **GET** /api/ai-bot/v1/bots/{org}/bot/{id}/config/slack/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_config_slack_update_create**](docs/AiBotApi.md#ai_bot_v1_bots_bot_config_slack_update_create) | **POST** /api/ai-bot/v1/bots/{org}/bot/{id}/config/slack/update/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_config_slack_update_partial_update**](docs/AiBotApi.md#ai_bot_v1_bots_bot_config_slack_update_partial_update) | **PATCH** /api/ai-bot/v1/bots/{org}/bot/{id}/config/slack/update/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_config_slack_update_update**](docs/AiBotApi.md#ai_bot_v1_bots_bot_config_slack_update_update) | **PUT** /api/ai-bot/v1/bots/{org}/bot/{id}/config/slack/update/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_config_teams_retrieve**](docs/AiBotApi.md#ai_bot_v1_bots_bot_config_teams_retrieve) | **GET** /api/ai-bot/v1/bots/{org}/bot/{id}/config/teams/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_config_teams_update_create**](docs/AiBotApi.md#ai_bot_v1_bots_bot_config_teams_update_create) | **POST** /api/ai-bot/v1/bots/{org}/bot/{id}/config/teams/update/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_config_teams_update_partial_update**](docs/AiBotApi.md#ai_bot_v1_bots_bot_config_teams_update_partial_update) | **PATCH** /api/ai-bot/v1/bots/{org}/bot/{id}/config/teams/update/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_config_teams_update_update**](docs/AiBotApi.md#ai_bot_v1_bots_bot_config_teams_update_update) | **PUT** /api/ai-bot/v1/bots/{org}/bot/{id}/config/teams/update/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_config_webex_partial_update**](docs/AiBotApi.md#ai_bot_v1_bots_bot_config_webex_partial_update) | **PATCH** /api/ai-bot/v1/bots/{org}/bot/{id}/config/webex/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_config_webex_retrieve**](docs/AiBotApi.md#ai_bot_v1_bots_bot_config_webex_retrieve) | **GET** /api/ai-bot/v1/bots/{org}/bot/{id}/config/webex/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_config_whatsapp_retrieve**](docs/AiBotApi.md#ai_bot_v1_bots_bot_config_whatsapp_retrieve) | **GET** /api/ai-bot/v1/bots/{org}/bot/{id}/config/whatsapp/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_create**](docs/AiBotApi.md#ai_bot_v1_bots_bot_create) | **POST** /api/ai-bot/v1/bots/{org}/bot/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_destroy**](docs/AiBotApi.md#ai_bot_v1_bots_bot_destroy) | **DELETE** /api/ai-bot/v1/bots/{org}/bot/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_list**](docs/AiBotApi.md#ai_bot_v1_bots_bot_list) | **GET** /api/ai-bot/v1/bots/{org}/bot/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_partial_update**](docs/AiBotApi.md#ai_bot_v1_bots_bot_partial_update) | **PATCH** /api/ai-bot/v1/bots/{org}/bot/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_retrieve**](docs/AiBotApi.md#ai_bot_v1_bots_bot_retrieve) | **GET** /api/ai-bot/v1/bots/{org}/bot/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_update**](docs/AiBotApi.md#ai_bot_v1_bots_bot_update) | **PUT** /api/ai-bot/v1/bots/{org}/bot/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_whatsapp_config_partial_update**](docs/AiBotApi.md#ai_bot_v1_bots_bot_whatsapp_config_partial_update) | **PATCH** /api/ai-bot/v1/bots/{org}/bot/{id}/whatsapp-config/ | 
*AiBotApi* | [**ai_bot_v1_bots_bot_whatsapp_config_update**](docs/AiBotApi.md#ai_bot_v1_bots_bot_whatsapp_config_update) | **PUT** /api/ai-bot/v1/bots/{org}/bot/{id}/whatsapp-config/ | 
*AiBotApi* | [**ai_bot_v1_bots_discord_user_config_create**](docs/AiBotApi.md#ai_bot_v1_bots_discord_user_config_create) | **POST** /api/ai-bot/v1/bots/{org}/discord-user-config/ | 
*AiBotApi* | [**ai_bot_v1_bots_discord_user_config_destroy**](docs/AiBotApi.md#ai_bot_v1_bots_discord_user_config_destroy) | **DELETE** /api/ai-bot/v1/bots/{org}/discord-user-config/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_discord_user_config_list**](docs/AiBotApi.md#ai_bot_v1_bots_discord_user_config_list) | **GET** /api/ai-bot/v1/bots/{org}/discord-user-config/ | 
*AiBotApi* | [**ai_bot_v1_bots_discord_user_config_partial_update**](docs/AiBotApi.md#ai_bot_v1_bots_discord_user_config_partial_update) | **PATCH** /api/ai-bot/v1/bots/{org}/discord-user-config/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_discord_user_config_retrieve**](docs/AiBotApi.md#ai_bot_v1_bots_discord_user_config_retrieve) | **GET** /api/ai-bot/v1/bots/{org}/discord-user-config/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_discord_user_config_update**](docs/AiBotApi.md#ai_bot_v1_bots_discord_user_config_update) | **PUT** /api/ai-bot/v1/bots/{org}/discord-user-config/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_slack_user_config_create**](docs/AiBotApi.md#ai_bot_v1_bots_slack_user_config_create) | **POST** /api/ai-bot/v1/bots/{org}/slack-user-config/ | 
*AiBotApi* | [**ai_bot_v1_bots_slack_user_config_destroy**](docs/AiBotApi.md#ai_bot_v1_bots_slack_user_config_destroy) | **DELETE** /api/ai-bot/v1/bots/{org}/slack-user-config/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_slack_user_config_list**](docs/AiBotApi.md#ai_bot_v1_bots_slack_user_config_list) | **GET** /api/ai-bot/v1/bots/{org}/slack-user-config/ | 
*AiBotApi* | [**ai_bot_v1_bots_slack_user_config_partial_update**](docs/AiBotApi.md#ai_bot_v1_bots_slack_user_config_partial_update) | **PATCH** /api/ai-bot/v1/bots/{org}/slack-user-config/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_slack_user_config_retrieve**](docs/AiBotApi.md#ai_bot_v1_bots_slack_user_config_retrieve) | **GET** /api/ai-bot/v1/bots/{org}/slack-user-config/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_slack_user_config_update**](docs/AiBotApi.md#ai_bot_v1_bots_slack_user_config_update) | **PUT** /api/ai-bot/v1/bots/{org}/slack-user-config/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_webhooks_discord_create**](docs/AiBotApi.md#ai_bot_v1_bots_webhooks_discord_create) | **POST** /api/ai-bot/v1/bots/webhooks/{org}/discord/{name}/ | 
*AiBotApi* | [**ai_bot_v1_bots_webhooks_slack_create**](docs/AiBotApi.md#ai_bot_v1_bots_webhooks_slack_create) | **POST** /api/ai-bot/v1/bots/webhooks/{org}/slack/{name}/ | 
*AiBotApi* | [**ai_bot_v1_bots_webhooks_teams_create**](docs/AiBotApi.md#ai_bot_v1_bots_webhooks_teams_create) | **POST** /api/ai-bot/v1/bots/webhooks/{org}/teams/{name}/ | 
*AiBotApi* | [**ai_bot_v1_bots_webhooks_teams_retrieve**](docs/AiBotApi.md#ai_bot_v1_bots_webhooks_teams_retrieve) | **GET** /api/ai-bot/v1/bots/webhooks/{org}/teams/{name}/ | 
*AiBotApi* | [**ai_bot_v1_bots_webhooks_webex_create**](docs/AiBotApi.md#ai_bot_v1_bots_webhooks_webex_create) | **POST** /api/ai-bot/v1/bots/webhooks/{org}/webex/{name}/ | 
*AiBotApi* | [**ai_bot_v1_bots_webhooks_whatsapp_create**](docs/AiBotApi.md#ai_bot_v1_bots_webhooks_whatsapp_create) | **POST** /api/ai-bot/v1/bots/webhooks/{org}/whatsapp/{name}/ | 
*AiBotApi* | [**ai_bot_v1_bots_webhooks_whatsapp_retrieve**](docs/AiBotApi.md#ai_bot_v1_bots_webhooks_whatsapp_retrieve) | **GET** /api/ai-bot/v1/bots/webhooks/{org}/whatsapp/{name}/ | 
*AiBotApi* | [**ai_bot_v1_bots_whatsapp_user_config_create**](docs/AiBotApi.md#ai_bot_v1_bots_whatsapp_user_config_create) | **POST** /api/ai-bot/v1/bots/{org}/whatsapp-user-config/ | 
*AiBotApi* | [**ai_bot_v1_bots_whatsapp_user_config_destroy**](docs/AiBotApi.md#ai_bot_v1_bots_whatsapp_user_config_destroy) | **DELETE** /api/ai-bot/v1/bots/{org}/whatsapp-user-config/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_whatsapp_user_config_list**](docs/AiBotApi.md#ai_bot_v1_bots_whatsapp_user_config_list) | **GET** /api/ai-bot/v1/bots/{org}/whatsapp-user-config/ | 
*AiBotApi* | [**ai_bot_v1_bots_whatsapp_user_config_partial_update**](docs/AiBotApi.md#ai_bot_v1_bots_whatsapp_user_config_partial_update) | **PATCH** /api/ai-bot/v1/bots/{org}/whatsapp-user-config/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_whatsapp_user_config_retrieve**](docs/AiBotApi.md#ai_bot_v1_bots_whatsapp_user_config_retrieve) | **GET** /api/ai-bot/v1/bots/{org}/whatsapp-user-config/{id}/ | 
*AiBotApi* | [**ai_bot_v1_bots_whatsapp_user_config_update**](docs/AiBotApi.md#ai_bot_v1_bots_whatsapp_user_config_update) | **PUT** /api/ai-bot/v1/bots/{org}/whatsapp-user-config/{id}/ | 
*AiFinetuningApi* | [**ai_finetuning_v1_org_user_datasets_create**](docs/AiFinetuningApi.md#ai_finetuning_v1_org_user_datasets_create) | **POST** /api/ai-finetuning/v1/org/{org}/user/{username}/datasets/ | 
*AiFinetuningApi* | [**ai_finetuning_v1_org_user_datasets_destroy**](docs/AiFinetuningApi.md#ai_finetuning_v1_org_user_datasets_destroy) | **DELETE** /api/ai-finetuning/v1/org/{org}/user/{username}/datasets/{id}/ | 
*AiFinetuningApi* | [**ai_finetuning_v1_org_user_datasets_list**](docs/AiFinetuningApi.md#ai_finetuning_v1_org_user_datasets_list) | **GET** /api/ai-finetuning/v1/org/{org}/user/{username}/datasets/ | 
*AiFinetuningApi* | [**ai_finetuning_v1_org_user_datasets_partial_update**](docs/AiFinetuningApi.md#ai_finetuning_v1_org_user_datasets_partial_update) | **PATCH** /api/ai-finetuning/v1/org/{org}/user/{username}/datasets/{id}/ | 
*AiFinetuningApi* | [**ai_finetuning_v1_org_user_datasets_retrieve**](docs/AiFinetuningApi.md#ai_finetuning_v1_org_user_datasets_retrieve) | **GET** /api/ai-finetuning/v1/org/{org}/user/{username}/datasets/{id}/ | 
*AiFinetuningApi* | [**ai_finetuning_v1_org_user_datasets_update**](docs/AiFinetuningApi.md#ai_finetuning_v1_org_user_datasets_update) | **PUT** /api/ai-finetuning/v1/org/{org}/user/{username}/datasets/{id}/ | 
*AiFinetuningApi* | [**ai_finetuning_v1_org_user_trainings_create**](docs/AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_create) | **POST** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/ | 
*AiFinetuningApi* | [**ai_finetuning_v1_org_user_trainings_destroy**](docs/AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_destroy) | **DELETE** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/{id}/ | 
*AiFinetuningApi* | [**ai_finetuning_v1_org_user_trainings_finetuned_models_retrieve**](docs/AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_finetuned_models_retrieve) | **GET** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/finetuned-models/ | 
*AiFinetuningApi* | [**ai_finetuning_v1_org_user_trainings_list**](docs/AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_list) | **GET** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/ | 
*AiFinetuningApi* | [**ai_finetuning_v1_org_user_trainings_partial_update**](docs/AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_partial_update) | **PATCH** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/{id}/ | 
*AiFinetuningApi* | [**ai_finetuning_v1_org_user_trainings_retrieve**](docs/AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_retrieve) | **GET** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/{id}/ | 
*AiFinetuningApi* | [**ai_finetuning_v1_org_user_trainings_update**](docs/AiFinetuningApi.md#ai_finetuning_v1_org_user_trainings_update) | **PUT** /api/ai-finetuning/v1/org/{org}/user/{username}/trainings/{id}/ | 
*AiIndexApi* | [**ai_index_orgs_users_documents_destroy**](docs/AiIndexApi.md#ai_index_orgs_users_documents_destroy) | **DELETE** /api/ai-index/orgs/{org}/users/{user_id}/documents/{document_id}/ | 
*AiIndexApi* | [**ai_index_orgs_users_documents_document_from_pool_create**](docs/AiIndexApi.md#ai_index_orgs_users_documents_document_from_pool_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/document-from-pool/ | 
*AiIndexApi* | [**ai_index_orgs_users_documents_pathways_list**](docs/AiIndexApi.md#ai_index_orgs_users_documents_pathways_list) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/documents/pathways/{pathway}/ | 
*AiIndexApi* | [**ai_index_orgs_users_documents_retrieve**](docs/AiIndexApi.md#ai_index_orgs_users_documents_retrieve) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/documents/{document_id}/ | 
*AiIndexApi* | [**ai_index_orgs_users_documents_search_create**](docs/AiIndexApi.md#ai_index_orgs_users_documents_search_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/search/ | 
*AiIndexApi* | [**ai_index_orgs_users_documents_settings_create**](docs/AiIndexApi.md#ai_index_orgs_users_documents_settings_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/{document_id}/settings/ | 
*AiIndexApi* | [**ai_index_orgs_users_documents_settings_retrieve**](docs/AiIndexApi.md#ai_index_orgs_users_documents_settings_retrieve) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/documents/{document_id}/settings/ | 
*AiIndexApi* | [**ai_index_orgs_users_documents_sources_create**](docs/AiIndexApi.md#ai_index_orgs_users_documents_sources_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/sources/ | 
*AiIndexApi* | [**ai_index_orgs_users_documents_tasks_retrieve**](docs/AiIndexApi.md#ai_index_orgs_users_documents_tasks_retrieve) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/documents/tasks/{task_id}/ | 
*AiIndexApi* | [**ai_index_orgs_users_documents_train_create**](docs/AiIndexApi.md#ai_index_orgs_users_documents_train_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/train/ | 
*AiIndexApi* | [**ai_index_orgs_users_documents_train_retriever_create**](docs/AiIndexApi.md#ai_index_orgs_users_documents_train_retriever_create) | **POST** /api/ai-index/orgs/{org}/users/{user_id}/documents/train/retriever/ | 
*AiIndexApi* | [**ai_index_orgs_users_documents_update**](docs/AiIndexApi.md#ai_index_orgs_users_documents_update) | **PUT** /api/ai-index/orgs/{org}/users/{user_id}/documents/{document_id}/ | 
*AiIndexApi* | [**ai_index_orgs_users_resource_data_scrapped_list**](docs/AiIndexApi.md#ai_index_orgs_users_resource_data_scrapped_list) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/resource/data/scrapped/ | 
*AiIndexApi* | [**ai_index_orgs_users_resource_data_scrapped_retrieve**](docs/AiIndexApi.md#ai_index_orgs_users_resource_data_scrapped_retrieve) | **GET** /api/ai-index/orgs/{org}/users/{user_id}/resource/{resource_id}/data/scrapped/ | 
*AiIndexApi* | [**ai_index_webhook_scan_create**](docs/AiIndexApi.md#ai_index_webhook_scan_create) | **POST** /api/ai-index/webhook/scan/ | 
*AiMarketingApi* | [**ai_marketing_orgs_users_heygen_videos_create**](docs/AiMarketingApi.md#ai_marketing_orgs_users_heygen_videos_create) | **POST** /api/ai-marketing/orgs/{org}/users/{user_id}/heygen-videos/ | 
*AiMarketingApi* | [**ai_marketing_orgs_users_heygen_videos_list**](docs/AiMarketingApi.md#ai_marketing_orgs_users_heygen_videos_list) | **GET** /api/ai-marketing/orgs/{org}/users/{user_id}/heygen-videos/ | 
*AiMarketingApi* | [**ai_marketing_orgs_users_heygen_videos_retrieve**](docs/AiMarketingApi.md#ai_marketing_orgs_users_heygen_videos_retrieve) | **GET** /api/ai-marketing/orgs/{org}/users/{user_id}/heygen-videos/{name}/ | 
*AiMediaApi* | [**ai_media_orgs_users_heygen_templates_create**](docs/AiMediaApi.md#ai_media_orgs_users_heygen_templates_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/heygen/templates/ | 
*AiMediaApi* | [**ai_media_orgs_users_heygen_templates_destroy**](docs/AiMediaApi.md#ai_media_orgs_users_heygen_templates_destroy) | **DELETE** /api/ai-media/orgs/{org}/users/{user_id}/heygen/templates/{template_name}/ | 
*AiMediaApi* | [**ai_media_orgs_users_heygen_templates_list**](docs/AiMediaApi.md#ai_media_orgs_users_heygen_templates_list) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/heygen/templates/ | 
*AiMediaApi* | [**ai_media_orgs_users_heygen_video_captions_create**](docs/AiMediaApi.md#ai_media_orgs_users_heygen_video_captions_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/heygen/video-captions/{heygen_marketing_video_id}/ | 
*AiMediaApi* | [**ai_media_orgs_users_heygen_video_captions_retrieve**](docs/AiMediaApi.md#ai_media_orgs_users_heygen_video_captions_retrieve) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/heygen/video-captions/{heygen_marketing_video_id}/ | 
*AiMediaApi* | [**ai_media_orgs_users_heygen_video_download_retrieve**](docs/AiMediaApi.md#ai_media_orgs_users_heygen_video_download_retrieve) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/heygen/video-download/{heygen_marketing_video_id}/ | 
*AiMediaApi* | [**ai_media_orgs_users_heygen_videos_create**](docs/AiMediaApi.md#ai_media_orgs_users_heygen_videos_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/heygen/videos/ | 
*AiMediaApi* | [**ai_media_orgs_users_heygen_videos_destroy**](docs/AiMediaApi.md#ai_media_orgs_users_heygen_videos_destroy) | **DELETE** /api/ai-media/orgs/{org}/users/{user_id}/heygen/videos/{heygen_marketing_video_id}/ | 
*AiMediaApi* | [**ai_media_orgs_users_heygen_videos_list**](docs/AiMediaApi.md#ai_media_orgs_users_heygen_videos_list) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/heygen/videos/ | 
*AiMediaApi* | [**ai_media_orgs_users_heygen_videos_retrieve**](docs/AiMediaApi.md#ai_media_orgs_users_heygen_videos_retrieve) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/heygen/videos/{heygen_marketing_video_id}/ | 
*AiMediaApi* | [**ai_media_orgs_users_veo_video_download_retrieve**](docs/AiMediaApi.md#ai_media_orgs_users_veo_video_download_retrieve) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/veo/video-download/{veo_video_id}/ | 
*AiMediaApi* | [**ai_media_orgs_users_veo_videos_create**](docs/AiMediaApi.md#ai_media_orgs_users_veo_videos_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/veo/videos/ | 
*AiMediaApi* | [**ai_media_orgs_users_veo_videos_destroy**](docs/AiMediaApi.md#ai_media_orgs_users_veo_videos_destroy) | **DELETE** /api/ai-media/orgs/{org}/users/{user_id}/veo/videos/{veo_video_id}/ | 
*AiMediaApi* | [**ai_media_orgs_users_veo_videos_list**](docs/AiMediaApi.md#ai_media_orgs_users_veo_videos_list) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/veo/videos/ | 
*AiMediaApi* | [**ai_media_orgs_users_veo_videos_retrieve**](docs/AiMediaApi.md#ai_media_orgs_users_veo_videos_retrieve) | **GET** /api/ai-media/orgs/{org}/users/{user_id}/veo/videos/{veo_video_id}/ | 
*AiMediaApi* | [**ai_media_orgs_users_video_script_generation_audio_create**](docs/AiMediaApi.md#ai_media_orgs_users_video_script_generation_audio_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/video-script-generation/audio/ | 
*AiMediaApi* | [**ai_media_orgs_users_video_script_generation_document_create**](docs/AiMediaApi.md#ai_media_orgs_users_video_script_generation_document_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/video-script-generation/document/ | 
*AiMediaApi* | [**ai_media_orgs_users_video_script_generation_text_create**](docs/AiMediaApi.md#ai_media_orgs_users_video_script_generation_text_create) | **POST** /api/ai-media/orgs/{org}/users/{user_id}/video-script-generation/text/ | 
*AiMentorApi* | [**ai_mentor_langfuse_health_retrieve**](docs/AiMentorApi.md#ai_mentor_langfuse_health_retrieve) | **GET** /api/ai-mentor/langfuse/health/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_configs_create**](docs/AiMentorApi.md#ai_mentor_orgs_agent_configs_create) | **POST** /api/ai-mentor/orgs/{org}/agent-configs/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_configs_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_agent_configs_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/agent-configs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_configs_list**](docs/AiMentorApi.md#ai_mentor_orgs_agent_configs_list) | **GET** /api/ai-mentor/orgs/{org}/agent-configs/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_configs_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_agent_configs_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/agent-configs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_configs_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_agent_configs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/agent-configs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_configs_update**](docs/AiMentorApi.md#ai_mentor_orgs_agent_configs_update) | **PUT** /api/ai-mentor/orgs/{org}/agent-configs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_skill_resources_create**](docs/AiMentorApi.md#ai_mentor_orgs_agent_skill_resources_create) | **POST** /api/ai-mentor/orgs/{org}/agent-skill-resources/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_skill_resources_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_agent_skill_resources_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/agent-skill-resources/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_skill_resources_list**](docs/AiMentorApi.md#ai_mentor_orgs_agent_skill_resources_list) | **GET** /api/ai-mentor/orgs/{org}/agent-skill-resources/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_skill_resources_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_agent_skill_resources_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/agent-skill-resources/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_skill_resources_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_agent_skill_resources_retrieve) | **GET** /api/ai-mentor/orgs/{org}/agent-skill-resources/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_skill_resources_update**](docs/AiMentorApi.md#ai_mentor_orgs_agent_skill_resources_update) | **PUT** /api/ai-mentor/orgs/{org}/agent-skill-resources/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_skills_create**](docs/AiMentorApi.md#ai_mentor_orgs_agent_skills_create) | **POST** /api/ai-mentor/orgs/{org}/agent-skills/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_skills_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_agent_skills_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/agent-skills/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_skills_list**](docs/AiMentorApi.md#ai_mentor_orgs_agent_skills_list) | **GET** /api/ai-mentor/orgs/{org}/agent-skills/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_skills_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_agent_skills_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/agent-skills/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_skills_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_agent_skills_retrieve) | **GET** /api/ai-mentor/orgs/{org}/agent-skills/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_agent_skills_update**](docs/AiMentorApi.md#ai_mentor_orgs_agent_skills_update) | **PUT** /api/ai-mentor/orgs/{org}/agent-skills/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_all_triggers_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_all_triggers_retrieve) | **GET** /api/ai-mentor/orgs/{org}/all-triggers/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_instances_create**](docs/AiMentorApi.md#ai_mentor_orgs_claw_instances_create) | **POST** /api/ai-mentor/orgs/{org}/claw/instances/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_instances_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_claw_instances_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/claw/instances/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_instances_health_check_create**](docs/AiMentorApi.md#ai_mentor_orgs_claw_instances_health_check_create) | **POST** /api/ai-mentor/orgs/{org}/claw/instances/{id}/health-check/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_instances_list**](docs/AiMentorApi.md#ai_mentor_orgs_claw_instances_list) | **GET** /api/ai-mentor/orgs/{org}/claw/instances/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_instances_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_claw_instances_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/claw/instances/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_instances_push_providers_create**](docs/AiMentorApi.md#ai_mentor_orgs_claw_instances_push_providers_create) | **POST** /api/ai-mentor/orgs/{org}/claw/instances/{id}/push-providers/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_instances_refresh_version_create**](docs/AiMentorApi.md#ai_mentor_orgs_claw_instances_refresh_version_create) | **POST** /api/ai-mentor/orgs/{org}/claw/instances/{id}/refresh-version/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_instances_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_claw_instances_retrieve) | **GET** /api/ai-mentor/orgs/{org}/claw/instances/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_instances_security_audit_create**](docs/AiMentorApi.md#ai_mentor_orgs_claw_instances_security_audit_create) | **POST** /api/ai-mentor/orgs/{org}/claw/instances/{id}/security-audit/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_instances_test_connectivity_create**](docs/AiMentorApi.md#ai_mentor_orgs_claw_instances_test_connectivity_create) | **POST** /api/ai-mentor/orgs/{org}/claw/instances/{id}/test-connectivity/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_instances_update**](docs/AiMentorApi.md#ai_mentor_orgs_claw_instances_update) | **PUT** /api/ai-mentor/orgs/{org}/claw/instances/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_mentor_configs_create**](docs/AiMentorApi.md#ai_mentor_orgs_claw_mentor_configs_create) | **POST** /api/ai-mentor/orgs/{org}/claw/mentor-configs/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_mentor_configs_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_claw_mentor_configs_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/claw/mentor-configs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_mentor_configs_list**](docs/AiMentorApi.md#ai_mentor_orgs_claw_mentor_configs_list) | **GET** /api/ai-mentor/orgs/{org}/claw/mentor-configs/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_mentor_configs_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_claw_mentor_configs_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/claw/mentor-configs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_mentor_configs_push_config_create**](docs/AiMentorApi.md#ai_mentor_orgs_claw_mentor_configs_push_config_create) | **POST** /api/ai-mentor/orgs/{org}/claw/mentor-configs/{id}/push-config/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_mentor_configs_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_claw_mentor_configs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/claw/mentor-configs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_mentor_configs_update**](docs/AiMentorApi.md#ai_mentor_orgs_claw_mentor_configs_update) | **PUT** /api/ai-mentor/orgs/{org}/claw/mentor-configs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_model_providers_create**](docs/AiMentorApi.md#ai_mentor_orgs_claw_model_providers_create) | **POST** /api/ai-mentor/orgs/{org}/claw/model-providers/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_model_providers_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_claw_model_providers_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/claw/model-providers/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_model_providers_list**](docs/AiMentorApi.md#ai_mentor_orgs_claw_model_providers_list) | **GET** /api/ai-mentor/orgs/{org}/claw/model-providers/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_model_providers_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_claw_model_providers_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/claw/model-providers/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_model_providers_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_claw_model_providers_retrieve) | **GET** /api/ai-mentor/orgs/{org}/claw/model-providers/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_claw_model_providers_update**](docs/AiMentorApi.md#ai_mentor_orgs_claw_model_providers_update) | **PUT** /api/ai-mentor/orgs/{org}/claw/model-providers/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentor_skill_assignments_create**](docs/AiMentorApi.md#ai_mentor_orgs_mentor_skill_assignments_create) | **POST** /api/ai-mentor/orgs/{org}/mentor-skill-assignments/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentor_skill_assignments_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_mentor_skill_assignments_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/mentor-skill-assignments/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentor_skill_assignments_list**](docs/AiMentorApi.md#ai_mentor_orgs_mentor_skill_assignments_list) | **GET** /api/ai-mentor/orgs/{org}/mentor-skill-assignments/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentor_skill_assignments_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_mentor_skill_assignments_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/mentor-skill-assignments/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentor_skill_assignments_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_mentor_skill_assignments_retrieve) | **GET** /api/ai-mentor/orgs/{org}/mentor-skill-assignments/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentor_skill_assignments_update**](docs/AiMentorApi.md#ai_mentor_orgs_mentor_skill_assignments_update) | **PUT** /api/ai-mentor/orgs/{org}/mentor-skill-assignments/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentors_by_email_create**](docs/AiMentorApi.md#ai_mentor_orgs_mentors_by_email_create) | **POST** /api/ai-mentor/orgs/{org}/mentors/by-email/ | Get accessible mentors by email
*AiMentorApi* | [**ai_mentor_orgs_mentors_email_inbox_list**](docs/AiMentorApi.md#ai_mentor_orgs_mentors_email_inbox_list) | **GET** /api/ai-mentor/orgs/{org}/mentors/{mentor}/email-inbox/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentors_email_inbox_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_mentors_email_inbox_retrieve) | **GET** /api/ai-mentor/orgs/{org}/mentors/{mentor}/email-inbox/{email_prompt_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentors_email_inbox_summary_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_mentors_email_inbox_summary_retrieve) | **GET** /api/ai-mentor/orgs/{org}/mentors/{mentor}/email-inbox-summary/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentors_link_course_create**](docs/AiMentorApi.md#ai_mentor_orgs_mentors_link_course_create) | **POST** /api/ai-mentor/orgs/{org}/mentors/{mentor}/link-course/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentors_link_course_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_mentors_link_course_retrieve) | **GET** /api/ai-mentor/orgs/{org}/mentors/{mentor}/link-course/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentors_lti_grant_mentor_access_create**](docs/AiMentorApi.md#ai_mentor_orgs_mentors_lti_grant_mentor_access_create) | **POST** /api/ai-mentor/orgs/{org}/mentors/{mentor_unique_id}/lti/grant-mentor-access/ | Grant LTI Mentor Access
*AiMentorApi* | [**ai_mentor_orgs_mentors_memory_categories_create**](docs/AiMentorApi.md#ai_mentor_orgs_mentors_memory_categories_create) | **POST** /api/ai-mentor/orgs/{org}/mentors/{mentor_id}/memory-categories/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentors_memory_categories_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_mentors_memory_categories_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/mentors/{mentor_id}/memory-categories/{category_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentors_memory_categories_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_mentors_memory_categories_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/mentors/{mentor_id}/memory-categories/{category_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_mentors_memory_categories_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_mentors_memory_categories_retrieve) | **GET** /api/ai-mentor/orgs/{org}/mentors/{mentor_id}/memory-categories/ | 
*AiMentorApi* | [**ai_mentor_orgs_metadata_create**](docs/AiMentorApi.md#ai_mentor_orgs_metadata_create) | **POST** /api/ai-mentor/orgs/{org}/metadata/ | 
*AiMentorApi* | [**ai_mentor_orgs_offline_mentors_config_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_offline_mentors_config_retrieve) | **GET** /api/ai-mentor/orgs/{org}/offline/mentors/{mentor_unique_id}/config/ | 
*AiMentorApi* | [**ai_mentor_orgs_offline_mentors_datasets_list**](docs/AiMentorApi.md#ai_mentor_orgs_offline_mentors_datasets_list) | **GET** /api/ai-mentor/orgs/{org}/offline/mentors/{mentor_unique_id}/datasets/ | 
*AiMentorApi* | [**ai_mentor_orgs_projects_create**](docs/AiMentorApi.md#ai_mentor_orgs_projects_create) | **POST** /api/ai-mentor/orgs/{org}/projects/ | Create a new project
*AiMentorApi* | [**ai_mentor_orgs_projects_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_projects_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/projects/{id}/ | Delete a project
*AiMentorApi* | [**ai_mentor_orgs_projects_list**](docs/AiMentorApi.md#ai_mentor_orgs_projects_list) | **GET** /api/ai-mentor/orgs/{org}/projects/ | List projects
*AiMentorApi* | [**ai_mentor_orgs_projects_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_projects_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/projects/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_projects_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_projects_retrieve) | **GET** /api/ai-mentor/orgs/{org}/projects/{id}/ | Retrieve a project
*AiMentorApi* | [**ai_mentor_orgs_projects_update**](docs/AiMentorApi.md#ai_mentor_orgs_projects_update) | **PUT** /api/ai-mentor/orgs/{org}/projects/{id}/ | Update a project
*AiMentorApi* | [**ai_mentor_orgs_quiz_customizer_create**](docs/AiMentorApi.md#ai_mentor_orgs_quiz_customizer_create) | **POST** /api/ai-mentor/orgs/{org}/quiz-customizer/ | 
*AiMentorApi* | [**ai_mentor_orgs_quiz_customizer_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_quiz_customizer_retrieve) | **GET** /api/ai-mentor/orgs/{org}/quiz-customizer/ | 
*AiMentorApi* | [**ai_mentor_orgs_sessions_create**](docs/AiMentorApi.md#ai_mentor_orgs_sessions_create) | **POST** /api/ai-mentor/orgs/{org}/sessions/ | 
*AiMentorApi* | [**ai_mentor_orgs_trigger_create**](docs/AiMentorApi.md#ai_mentor_orgs_trigger_create) | **POST** /api/ai-mentor/orgs/{org}/trigger/ | 
*AiMentorApi* | [**ai_mentor_orgs_trigger_deletion_create**](docs/AiMentorApi.md#ai_mentor_orgs_trigger_deletion_create) | **POST** /api/ai-mentor/orgs/{org}/trigger/{slug}/deletion/ | 
*AiMentorApi* | [**ai_mentor_orgs_trigger_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_trigger_retrieve) | **GET** /api/ai-mentor/orgs/{org}/trigger/{slug}/ | 
*AiMentorApi* | [**ai_mentor_orgs_trigger_templates_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_trigger_templates_retrieve) | **GET** /api/ai-mentor/orgs/{org}/trigger-templates/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_ai_generated_images_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_ai_generated_images_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-generated-images/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_ai_generated_images_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_ai_generated_images_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-generated-images/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_ai_generated_images_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_ai_generated_images_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-generated-images/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_ai_user_profile_memory_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_ai_user_profile_memory_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-user-profile-memory/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_ai_user_profile_memory_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_ai_user_profile_memory_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-user-profile-memory/{tag}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_ai_user_profile_memory_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_ai_user_profile_memory_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-user-profile-memory/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_artifacts_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_artifacts_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/artifacts/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_artifacts_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_artifacts_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/artifacts/{id}/ | Delete an artifact
*AiMentorApi* | [**ai_mentor_orgs_users_artifacts_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_artifacts_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/artifacts/ | List artifacts
*AiMentorApi* | [**ai_mentor_orgs_users_artifacts_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_artifacts_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/artifacts/{id}/ | Partially update an artifact
*AiMentorApi* | [**ai_mentor_orgs_users_artifacts_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_artifacts_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/artifacts/{id}/ | Retrieve an artifact
*AiMentorApi* | [**ai_mentor_orgs_users_artifacts_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_artifacts_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/artifacts/{id}/ | Update an artifact
*AiMentorApi* | [**ai_mentor_orgs_users_artifacts_versions_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_artifacts_versions_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/artifacts/{id}/versions/ | List artifact versions
*AiMentorApi* | [**ai_mentor_orgs_users_artifacts_versions_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_artifacts_versions_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/artifacts/{id}/versions/{version_id}/ | Get specific artifact version
*AiMentorApi* | [**ai_mentor_orgs_users_artifacts_versions_set_current_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_artifacts_versions_set_current_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/artifacts/{id}/versions/set-current/ | Set artifact version as current
*AiMentorApi* | [**ai_mentor_orgs_users_assumed_knowledge_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_assumed_knowledge_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/assumed-knowledge/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_assumed_knowledge_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_assumed_knowledge_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/assumed-knowledge/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_audio_to_text_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_audio_to_text_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/audio-to-text/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_available_template_mentors_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_available_template_mentors_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/available-template-mentors/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_call_configurations_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_call_configurations_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/call-configurations/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_call_configurations_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_call_configurations_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/call-configurations/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_call_configurations_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_call_configurations_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/call-configurations/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_call_configurations_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_call_configurations_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/call-configurations/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_call_configurations_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_call_configurations_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/call-configurations/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_category_groups_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_category_groups_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/category-groups/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_category_groups_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_category_groups_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/category-groups/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_category_groups_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_category_groups_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/category-groups/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_category_groups_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_category_groups_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/category-groups/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_category_groups_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_category_groups_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/category-groups/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_category_groups_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_category_groups_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/category-groups/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_chat_files_upload_url_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_chat_files_upload_url_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/chat/files/upload-url/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_clean_vector_results_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_clean_vector_results_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/clean-vector-results/{session_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_clean_vector_results_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_clean_vector_results_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/clean-vector-results/{session_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_clear_chathistory_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_clear_chathistory_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/clear-chathistory | Delete User Chat History
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_create_xblock_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_create_xblock_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/create-xblock/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_delete_xblock_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_delete_xblock_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/delete-xblock/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_draft_content_for_all_units_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_draft_content_for_all_units_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/draft-content-for-all-units/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_draft_content_for_unit_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_draft_content_for_unit_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/draft-content-for-unit/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_full_structure_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_full_structure_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/full-structure/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_outline_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_outline_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/outline/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_reorder_children_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_reorder_children_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/reorder-children/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_student_progress_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_student_progress_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/student-progress/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_sync_to_edx_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_sync_to_edx_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/sync-to-edx/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_sync_to_edx_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_sync_to_edx_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/sync-to-edx/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_course_update_xblock_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_update_xblock_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/update-xblock/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_files_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_files_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/files/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_files_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_files_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/files/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_files_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_files_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/files/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_files_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_files_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/files/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_files_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_files_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/files/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_files_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_files_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/files/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_task_files_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_task_files_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-task-files/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_task_files_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_task_files_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-task-files/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_task_files_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_task_files_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-task-files/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_task_files_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_task_files_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-task-files/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_task_files_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_task_files_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-task-files/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_task_files_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_task_files_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-task-files/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/{id}/cancel/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve2**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve2) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/{id}/cancel/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_create2**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create2) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_create_course_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create_course_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/{id}/create-course/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_create_course_create2**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create_course_create2) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/{id}/create-course/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/{id}/create-course-outline/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create2**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create2) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/{id}/create-course-outline/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/{id}/create-course-outline/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve2**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve2) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/{id}/create-course-outline/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_destroy2**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_destroy2) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_list2**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_list2) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_retrieve2**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_retrieve2) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_start_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_start_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/{id}/start/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_course_creation_tasks_start_retrieve2**](docs/AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_start_retrieve2) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/{id}/start/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_create_mentor_wizard_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_create_mentor_wizard_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/create-mentor-wizard/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_custom_instruction_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_custom_instruction_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/custom-instruction/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_custom_instruction_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_custom_instruction_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/custom-instruction/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_custom_instruction_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_custom_instruction_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/custom-instruction/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/{name}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_disclaimer_agreements_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_disclaimer_agreements_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/disclaimer-agreements/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_disclaimer_agreements_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_disclaimer_agreements_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/disclaimer-agreements/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_disclaimer_agreements_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_disclaimer_agreements_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/disclaimer-agreements/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_disclaimer_agreements_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_disclaimer_agreements_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/disclaimer-agreements/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_disclaimers_add_mentor_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_disclaimers_add_mentor_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/disclaimers/{id}/add-mentor/ | Add mentor to disclaimer
*AiMentorApi* | [**ai_mentor_orgs_users_disclaimers_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_disclaimers_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/disclaimers/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_disclaimers_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_disclaimers_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/disclaimers/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_disclaimers_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_disclaimers_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/disclaimers/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_disclaimers_remove_mentor_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_disclaimers_remove_mentor_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/disclaimers/{id}/remove-mentor/ | Remove mentor from disclaimer
*AiMentorApi* | [**ai_mentor_orgs_users_disclaimers_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_disclaimers_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/disclaimers/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_disclaimers_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_disclaimers_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/disclaimers/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_downloads_tasks_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_downloads_tasks_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/downloads/tasks/{task_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_edx_memory_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_edx_memory_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/edx-memory/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_edx_memory_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_edx_memory_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/edx-memory/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_edx_memory_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_edx_memory_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/edx-memory/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_elevenlabs_voice_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_elevenlabs_voice_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/elevenlabs-voice/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_elevenlabs_voice_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_elevenlabs_voice_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/elevenlabs-voice/{voice_name}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_elevenlabs_voice_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_elevenlabs_voice_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/elevenlabs-voice/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_export_chathistory_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_export_chathistory_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/export-chathistory/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_extracted_memories_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_extracted_memories_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/extracted-memories/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_filtered_memories_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_filtered_memories_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/filtered-memories/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_free_usage_count_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_free_usage_count_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/free-usage-count | 
*AiMentorApi* | [**ai_mentor_orgs_users_global_memories_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_global_memories_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/global-memories/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_global_memories_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_global_memories_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/global-memories/{memory_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_global_memories_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_global_memories_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/global-memories/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_google_agents_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_google_agents_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/google-agents/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_google_agents_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_google_agents_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/google-agents/{unique_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_google_agents_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_google_agents_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/google-agents/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_google_agents_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_google_agents_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/google-agents/{unique_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_google_agents_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_google_agents_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/google-agents/{unique_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mcp_server_connections_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mcp_server_connections_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-server-connections/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mcp_server_connections_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_mcp_server_connections_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-server-connections/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mcp_server_connections_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_mcp_server_connections_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-server-connections/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mcp_server_connections_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_mcp_server_connections_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-server-connections/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mcp_server_connections_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mcp_server_connections_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-server-connections/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mcp_server_connections_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_mcp_server_connections_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-server-connections/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mcp_servers_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mcp_servers_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-servers/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mcp_servers_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_mcp_servers_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-servers/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mcp_servers_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_mcp_servers_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-servers/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mcp_servers_oauth_find_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mcp_servers_oauth_find_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-servers/oauth-find/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mcp_servers_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_mcp_servers_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-servers/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mcp_servers_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mcp_servers_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-servers/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mcp_servers_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_mcp_servers_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-servers/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_memories_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_memories_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/memories/ | Create memory
*AiMentorApi* | [**ai_mentor_orgs_users_memories_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_memories_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/memories/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_memory_categories_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_memory_categories_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/memory-categories/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_memory_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_memory_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/memory/{memory_unique_id_or_name}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_memory_entries_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_memory_entries_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/memory-entries/{entry_unique_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_memory_entries_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_memory_entries_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/memory-entries/{entry_unique_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_memory_entries_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_memory_entries_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/memory-entries/{entry_unique_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_memory_filter_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_memory_filter_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/memory-filter/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_memory_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_memory_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/memory/{memory_unique_id_or_name}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_memsearch_config_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_memsearch_config_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/memsearch-config/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_memsearch_config_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_memsearch_config_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/memsearch-config/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_memsearch_settings_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_memsearch_settings_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/memsearch-settings/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_memsearch_settings_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_memsearch_settings_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/memsearch-settings/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_audience_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_audience_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/audience/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_audience_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_audience_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/audience/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_audience_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_audience_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/audience/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_categories_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_categories_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/categories/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_categories_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_categories_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/categories/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_categories_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_categories_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/categories/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_feedback_create_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_feedback_create_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-feedback/create/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_feedback_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_feedback_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-feedback/{feedback_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_feedback_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_feedback_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-feedback/{feedback_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_llms_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_llms_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-llms/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_memories_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_memories_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-memories/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_seed_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_seed_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/seed/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_tools_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_tools_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-tools/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_types_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_types_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-types/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentor_with_settings_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentor_with_settings_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-with-settings/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_auto_memory_prompt_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_auto_memory_prompt_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/auto-memory-prompt/ | Set or reset auto memory prompt
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_auto_memory_prompt_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_auto_memory_prompt_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/auto-memory-prompt/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_available_tools_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_available_tools_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/available-tools/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_create_call_credentials_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_create_call_credentials_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/create-call-credentials/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_current_memory_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_current_memory_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/current-memory/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_current_memory_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_current_memory_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/current-memory/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_custom_voice_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_custom_voice_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/custom-voice/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_custom_voice_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_custom_voice_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/custom-voice/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_custom_voice_tts_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_custom_voice_tts_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/custom-voice-tts/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_edit_scenarios_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_edit_scenarios_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/edit-scenarios/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_fork_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_fork_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/fork/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_historical_memory_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_historical_memory_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/historical-memory/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_memory_progress_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_memory_progress_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/memory-progress/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_memory_settings_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_memory_settings_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/memory-settings/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_memory_settings_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_memory_settings_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/memory-settings/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_mentor_eval_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_mentor_eval_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/mentor-eval/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_mentor_eval_execution_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_mentor_eval_execution_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/mentor-eval-execution/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_mentor_eval_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_mentor_eval_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/mentor-eval/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_mentor_memories_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_mentor_memories_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor_id}/mentor-memories/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_mentor_memories_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_mentor_memories_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor_id}/mentor-memories/{memory_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_mentor_memories_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_mentor_memories_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor_id}/mentor-memories/{memory_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_mentor_memories_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_mentor_memories_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor_id}/mentor-memories/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_mentor_user_settings_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_mentor_user_settings_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/mentor-user-settings/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_mentor_user_settings_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_mentor_user_settings_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/mentor-user-settings/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_public_settings_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_public_settings_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/public-settings/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_public_sharable_link_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_public_sharable_link_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/public-sharable-link/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_reports_mentor_eval_report_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_reports_mentor_eval_report_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/reports/{report_id}/mentor-eval-report/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_scenarios_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_scenarios_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/scenarios/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_settings_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_settings_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/settings/ | Retrieve Mentor Settings
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_settings_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_settings_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/settings/ | Update Mentor Settings
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_sharable_link_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_sharable_link_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/sharable-link | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_sharable_link_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_sharable_link_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/sharable-link | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_sharable_link_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_sharable_link_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/sharable-link | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_sharable_link_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_sharable_link_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/sharable-link | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_spaced_repetition_question_stats_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_spaced_repetition_question_stats_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/spaced-repetition-question-stats/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/spaced-repetition-recommended-paths/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/spaced-repetition-recommended-paths/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_star_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_star_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/star/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_star_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_star_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/star/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_summaries_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_summaries_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/summaries/{summary_type}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_mentors_unstar_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_mentors_unstar_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/unstar/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_metadata_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_metadata_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/metadata | 
*AiMentorApi* | [**ai_mentor_orgs_users_moderation_logs_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_moderation_logs_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/moderation-logs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_moderation_logs_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_moderation_logs_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/moderation-logs/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_moderation_logs_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_moderation_logs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/moderation-logs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/{name}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_periodic_agent_logs_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_periodic_agent_logs_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agent-logs/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_periodic_agent_logs_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_periodic_agent_logs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agent-logs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_periodic_agents_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_periodic_agents_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_periodic_agents_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_periodic_agents_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_periodic_agents_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_periodic_agents_statistics_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_statistics_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/statistics/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_periodic_agents_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_pin_message_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_pin_message_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/pin-message/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_pin_message_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_pin_message_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/pin-message/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_pin_message_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_pin_message_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/pin-message/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_planned_jobs_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_planned_jobs_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/planned-jobs/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_planned_jobs_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_planned_jobs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/planned-jobs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_playwright_scripts_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_playwright_scripts_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_playwright_scripts_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_playwright_scripts_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_playwright_scripts_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_playwright_scripts_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_predictive_analytics_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_predictive_analytics_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/predictive-analytics/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_projects_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_projects_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/projects/ | Create a new project
*AiMentorApi* | [**ai_mentor_orgs_users_projects_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_projects_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/projects/{id}/ | Delete a project
*AiMentorApi* | [**ai_mentor_orgs_users_projects_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_projects_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/projects/ | List projects
*AiMentorApi* | [**ai_mentor_orgs_users_projects_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_projects_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/projects/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_projects_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_projects_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/projects/{id}/ | Retrieve a project
*AiMentorApi* | [**ai_mentor_orgs_users_projects_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_projects_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/projects/{id}/ | Update a project
*AiMentorApi* | [**ai_mentor_orgs_users_recent_messages_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_recent_messages_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/recent-messages/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_recently_accessed_mentors_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_recently_accessed_mentors_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/recently-accessed-mentors/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_resources_web_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_resources_web_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/resources/web/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/{name}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_safety_logs_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_safety_logs_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/safety-logs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_safety_logs_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_safety_logs_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/safety-logs/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_safety_logs_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_safety_logs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/safety-logs/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_session_detail_mentors_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_session_detail_mentors_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/session-detail/mentors/{mentor}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_sessionid_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessionid_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessionid/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_browser_screenshot_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_browser_screenshot_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/browser-screenshot/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_download_session_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_download_session_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/download-session | 
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_memories_set_attached_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_memories_set_attached_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/memories/{memory_unique_id}/set-attached/ | Create session memory attachment
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_memories_set_attached_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_memories_set_attached_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/memories/{memory_unique_id}/set-attached/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_memory_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_memory_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/memory/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/ | Retrieve Chat Messages
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_shared_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_shared_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/shared/ | Retrieve Shared Messages
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_shared_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_shared_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/shared/ | Share Session
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_shell_logs_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_shell_logs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/shell-logs/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_suggestion_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_suggestion_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/suggestion | 
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_tasks_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_tasks_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/tasks/{task_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_sessions_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_sessions_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_settings_tenant_llm_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_settings_tenant_llm_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/settings/tenant-llm/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_settings_tenant_llm_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_settings_tenant_llm_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/settings/tenant-llm/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_starred_mentors_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_starred_mentors_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/starred-mentors/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_stop_generation_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_stop_generation_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/stop-generation/ | Stop an active chat generation
*AiMentorApi* | [**ai_mentor_orgs_users_subjects_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_subjects_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/subjects/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_support_ticket_messages_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_support_ticket_messages_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/support-ticket-messages/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_support_ticket_messages_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_support_ticket_messages_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/support-ticket-messages/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_support_ticket_messages_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_support_ticket_messages_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/support-ticket-messages/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_support_ticket_messages_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_support_ticket_messages_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/support-ticket-messages/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_support_ticket_messages_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_support_ticket_messages_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/support-ticket-messages/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_support_ticket_messages_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_support_ticket_messages_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/support-ticket-messages/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_support_tickets_close_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_support_tickets_close_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/support-tickets/{id}/close/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_support_tickets_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_users_support_tickets_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/support-tickets/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_support_tickets_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_support_tickets_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/support-tickets/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_support_tickets_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_support_tickets_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/support-tickets/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_support_tickets_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_support_tickets_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/support-tickets/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_support_tickets_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_support_tickets_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/support-tickets/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_tasks_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_tasks_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/tasks/{task_id} | 
*AiMentorApi* | [**ai_mentor_orgs_users_tasks_sessions_create**](docs/AiMentorApi.md#ai_mentor_orgs_users_tasks_sessions_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/tasks/sessions/{session_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_tool_categories_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_tool_categories_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/tool-categories/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_update**](docs/AiMentorApi.md#ai_mentor_orgs_users_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/{name}/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_voices_list**](docs/AiMentorApi.md#ai_mentor_orgs_users_voices_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/voices/ | 
*AiMentorApi* | [**ai_mentor_orgs_users_voices_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_users_voices_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/voices/{id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_webhooks_azure_trigger_create**](docs/AiMentorApi.md#ai_mentor_orgs_webhooks_azure_trigger_create) | **POST** /api/ai-mentor/orgs/{org}/webhooks/azure/trigger/{slug}/ | 
*AiMentorApi* | [**ai_mentor_orgs_webhooks_github_pullrequest_create**](docs/AiMentorApi.md#ai_mentor_orgs_webhooks_github_pullrequest_create) | **POST** /api/ai-mentor/orgs/{org}/webhooks/github/pullrequest/ | 
*AiMentorApi* | [**ai_mentor_orgs_workflows_activate_create**](docs/AiMentorApi.md#ai_mentor_orgs_workflows_activate_create) | **POST** /api/ai-mentor/orgs/{org}/workflows/{unique_id}/activate/ | Activate a workflow
*AiMentorApi* | [**ai_mentor_orgs_workflows_chat_create**](docs/AiMentorApi.md#ai_mentor_orgs_workflows_chat_create) | **POST** /api/ai-mentor/orgs/{org}/workflows/{unique_id}/chat/ | Chat with workflow
*AiMentorApi* | [**ai_mentor_orgs_workflows_create**](docs/AiMentorApi.md#ai_mentor_orgs_workflows_create) | **POST** /api/ai-mentor/orgs/{org}/workflows/ | Create a new workflow
*AiMentorApi* | [**ai_mentor_orgs_workflows_deactivate_create**](docs/AiMentorApi.md#ai_mentor_orgs_workflows_deactivate_create) | **POST** /api/ai-mentor/orgs/{org}/workflows/{unique_id}/deactivate/ | Deactivate a workflow
*AiMentorApi* | [**ai_mentor_orgs_workflows_destroy**](docs/AiMentorApi.md#ai_mentor_orgs_workflows_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/workflows/{unique_id}/ | Delete a workflow
*AiMentorApi* | [**ai_mentor_orgs_workflows_list**](docs/AiMentorApi.md#ai_mentor_orgs_workflows_list) | **GET** /api/ai-mentor/orgs/{org}/workflows/ | List workflows
*AiMentorApi* | [**ai_mentor_orgs_workflows_node_types_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_workflows_node_types_retrieve) | **GET** /api/ai-mentor/orgs/{org}/workflows/node-types/ | Get available node types
*AiMentorApi* | [**ai_mentor_orgs_workflows_partial_update**](docs/AiMentorApi.md#ai_mentor_orgs_workflows_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/workflows/{unique_id}/ | 
*AiMentorApi* | [**ai_mentor_orgs_workflows_publish_create**](docs/AiMentorApi.md#ai_mentor_orgs_workflows_publish_create) | **POST** /api/ai-mentor/orgs/{org}/workflows/{unique_id}/publish/ | Publish a workflow
*AiMentorApi* | [**ai_mentor_orgs_workflows_retrieve**](docs/AiMentorApi.md#ai_mentor_orgs_workflows_retrieve) | **GET** /api/ai-mentor/orgs/{org}/workflows/{unique_id}/ | Retrieve a workflow
*AiMentorApi* | [**ai_mentor_orgs_workflows_unpublish_create**](docs/AiMentorApi.md#ai_mentor_orgs_workflows_unpublish_create) | **POST** /api/ai-mentor/orgs/{org}/workflows/{unique_id}/unpublish/ | Unpublish a workflow
*AiMentorApi* | [**ai_mentor_orgs_workflows_update**](docs/AiMentorApi.md#ai_mentor_orgs_workflows_update) | **PUT** /api/ai-mentor/orgs/{org}/workflows/{unique_id}/ | Update a workflow
*AiMentorApi* | [**ai_mentor_orgs_workflows_validate_create**](docs/AiMentorApi.md#ai_mentor_orgs_workflows_validate_create) | **POST** /api/ai-mentor/orgs/{org}/workflows/{unique_id}/validate/ | Validate workflow for execution
*AiMentorApi* | [**ai_mentor_webhooks_azure_emailchat_create**](docs/AiMentorApi.md#ai_mentor_webhooks_azure_emailchat_create) | **POST** /api/ai-mentor/webhooks/azure/emailchat/ | 
*AiMentorApi* | [**ai_mentor_webhooks_n8n_progress_create**](docs/AiMentorApi.md#ai_mentor_webhooks_n8n_progress_create) | **POST** /api/ai-mentor/webhooks/n8n-progress/ | 
*AiPromptApi* | [**ai_prompt_orgs_metadata_create**](docs/AiPromptApi.md#ai_prompt_orgs_metadata_create) | **POST** /api/ai-prompt/orgs/{org}/metadata/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_all_chats_memory_create**](docs/AiPromptApi.md#ai_prompt_orgs_users_all_chats_memory_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/all-chats-memory/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_all_chats_memory_destroy**](docs/AiPromptApi.md#ai_prompt_orgs_users_all_chats_memory_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/all-chats-memory/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_all_chats_memory_destroy2**](docs/AiPromptApi.md#ai_prompt_orgs_users_all_chats_memory_destroy2) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/all-chats-memory/{memory_id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_all_chats_memory_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_all_chats_memory_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/all-chats-memory/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_all_chats_memory_update**](docs/AiPromptApi.md#ai_prompt_orgs_users_all_chats_memory_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/all-chats-memory/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_all_chats_memory_update2**](docs/AiPromptApi.md#ai_prompt_orgs_users_all_chats_memory_update2) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/all-chats-memory/{memory_id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_chat_memory_status_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_chat_memory_status_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/chat-memory-status/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_chat_memory_status_update**](docs/AiPromptApi.md#ai_prompt_orgs_users_chat_memory_status_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/chat-memory-status/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_languages_create**](docs/AiPromptApi.md#ai_prompt_orgs_users_languages_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/languages/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_languages_destroy**](docs/AiPromptApi.md#ai_prompt_orgs_users_languages_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/languages/{language_id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_languages_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_languages_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/languages/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_languages_update**](docs/AiPromptApi.md#ai_prompt_orgs_users_languages_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/languages/{language_id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_memory_context_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_memory_context_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/memory-context/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_memory_context_update**](docs/AiPromptApi.md#ai_prompt_orgs_users_memory_context_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/memory-context/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_memory_create**](docs/AiPromptApi.md#ai_prompt_orgs_users_memory_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/memory/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_memory_destroy**](docs/AiPromptApi.md#ai_prompt_orgs_users_memory_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/memory/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_memory_destroy2**](docs/AiPromptApi.md#ai_prompt_orgs_users_memory_destroy2) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/memory/{memory_id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_memory_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_memory_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/memory/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_memory_status_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_memory_status_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/memory-status/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_memory_status_update**](docs/AiPromptApi.md#ai_prompt_orgs_users_memory_status_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/memory-status/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_memory_update**](docs/AiPromptApi.md#ai_prompt_orgs_users_memory_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/memory/{memory_id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_metadata_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_metadata_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/metadata | 
*AiPromptApi* | [**ai_prompt_orgs_users_prompt_create**](docs/AiPromptApi.md#ai_prompt_orgs_users_prompt_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/prompt/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_prompt_destroy**](docs/AiPromptApi.md#ai_prompt_orgs_users_prompt_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/prompt/{id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_prompt_list**](docs/AiPromptApi.md#ai_prompt_orgs_users_prompt_list) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/prompt/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_prompt_partial_update**](docs/AiPromptApi.md#ai_prompt_orgs_users_prompt_partial_update) | **PATCH** /api/ai-prompt/orgs/{org}/users/{user_id}/prompt/{id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_prompt_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_prompt_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/prompt/{id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_prompt_update**](docs/AiPromptApi.md#ai_prompt_orgs_users_prompt_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/prompt/{id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_prompts_category_create**](docs/AiPromptApi.md#ai_prompt_orgs_users_prompts_category_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/prompts/category/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_prompts_category_destroy**](docs/AiPromptApi.md#ai_prompt_orgs_users_prompts_category_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/prompts/category/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_prompts_category_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_prompts_category_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/prompts/category/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_prompts_public_list**](docs/AiPromptApi.md#ai_prompt_orgs_users_prompts_public_list) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/prompts/public/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_prompts_public_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_prompts_public_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/prompts/public/{id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_sessions_guided_prompts_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_sessions_guided_prompts_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/sessions/{session_id}/guided-prompts/ | Retrieve guided prompts for a chat session
*AiPromptApi* | [**ai_prompt_orgs_users_styles_create**](docs/AiPromptApi.md#ai_prompt_orgs_users_styles_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/styles/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_styles_destroy**](docs/AiPromptApi.md#ai_prompt_orgs_users_styles_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/styles/{style_id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_styles_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_styles_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/styles/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_styles_update**](docs/AiPromptApi.md#ai_prompt_orgs_users_styles_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/styles/{style_id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_tags_create**](docs/AiPromptApi.md#ai_prompt_orgs_users_tags_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/tags/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_tags_destroy**](docs/AiPromptApi.md#ai_prompt_orgs_users_tags_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/tags/{tag_id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_tags_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_tags_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/tags/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_tags_update**](docs/AiPromptApi.md#ai_prompt_orgs_users_tags_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/tags/{tag_id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_tones_create**](docs/AiPromptApi.md#ai_prompt_orgs_users_tones_create) | **POST** /api/ai-prompt/orgs/{org}/users/{user_id}/tones/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_tones_destroy**](docs/AiPromptApi.md#ai_prompt_orgs_users_tones_destroy) | **DELETE** /api/ai-prompt/orgs/{org}/users/{user_id}/tones/{tone_id}/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_tones_retrieve**](docs/AiPromptApi.md#ai_prompt_orgs_users_tones_retrieve) | **GET** /api/ai-prompt/orgs/{org}/users/{user_id}/tones/ | 
*AiPromptApi* | [**ai_prompt_orgs_users_tones_update**](docs/AiPromptApi.md#ai_prompt_orgs_users_tones_update) | **PUT** /api/ai-prompt/orgs/{org}/users/{user_id}/tones/{tone_id}/ | 
*AiSearchApi* | [**ai_search_orgs_users_my_mentors_retrieve**](docs/AiSearchApi.md#ai_search_orgs_users_my_mentors_retrieve) | **GET** /api/ai-search/orgs/{org}/users/{username}/my-mentors/ | 
*AiSearchApi* | [**create_platform_prompt**](docs/AiSearchApi.md#create_platform_prompt) | **POST** /api/ai-search/prompts/ | Create a new recommendation prompt
*AiSearchApi* | [**create_platform_prompt2**](docs/AiSearchApi.md#create_platform_prompt2) | **POST** /api/ai-search/recommendation/prompts/ | Create a new recommendation prompt
*AiSearchApi* | [**delete_platform_prompt**](docs/AiSearchApi.md#delete_platform_prompt) | **DELETE** /api/ai-search/prompts/ | Delete a recommendation prompt
*AiSearchApi* | [**delete_platform_prompt2**](docs/AiSearchApi.md#delete_platform_prompt2) | **DELETE** /api/ai-search/recommendation/prompts/ | Delete a recommendation prompt
*AiSearchApi* | [**list_platform_prompts**](docs/AiSearchApi.md#list_platform_prompts) | **GET** /api/ai-search/prompts/ | List recommendation prompts for a platform
*AiSearchApi* | [**list_platform_prompts2**](docs/AiSearchApi.md#list_platform_prompts2) | **GET** /api/ai-search/recommendation/prompts/ | List recommendation prompts for a platform
*AiSearchApi* | [**update_platform_prompt**](docs/AiSearchApi.md#update_platform_prompt) | **PUT** /api/ai-search/prompts/ | Update an existing recommendation prompt
*AiSearchApi* | [**update_platform_prompt2**](docs/AiSearchApi.md#update_platform_prompt2) | **PUT** /api/ai-search/recommendation/prompts/ | Update an existing recommendation prompt
*AiSearchApi* | [**v2_course_recommendations**](docs/AiSearchApi.md#v2_course_recommendations) | **GET** /api/ai-search/recommendations/ | Generate AI-driven course recommendations
*AiSearchApi* | [**v2_global_mentor_search**](docs/AiSearchApi.md#v2_global_mentor_search) | **GET** /api/ai-search/mentors/ | Search and filter AI mentors across the platform
*AiSearchApi* | [**v2_personalized_mentors**](docs/AiSearchApi.md#v2_personalized_mentors) | **GET** /api/ai-search/personalized-mentors/ | Get mentors created by a specific user
*AnalyticsApi* | [**analytics_financial_details_retrieve**](docs/AnalyticsApi.md#analytics_financial_details_retrieve) | **GET** /api/analytics/financial/details/ | 
*AnalyticsApi* | [**analytics_financial_invoice_retrieve**](docs/AnalyticsApi.md#analytics_financial_invoice_retrieve) | **GET** /api/analytics/financial/invoice/ | 
*AnalyticsApi* | [**analytics_financial_retrieve**](docs/AnalyticsApi.md#analytics_financial_retrieve) | **GET** /api/analytics/financial/ | 
*AnalyticsApi* | [**analytics_learners_list_retrieve**](docs/AnalyticsApi.md#analytics_learners_list_retrieve) | **GET** /api/analytics/learners/list/ | 
*AnalyticsApi* | [**analytics_learners_retrieve**](docs/AnalyticsApi.md#analytics_learners_retrieve) | **GET** /api/analytics/learners/ | 
*AnalyticsApi* | [**analytics_messages_details_retrieve**](docs/AnalyticsApi.md#analytics_messages_details_retrieve) | **GET** /api/analytics/messages/details/ | 
*AnalyticsApi* | [**analytics_messages_retrieve**](docs/AnalyticsApi.md#analytics_messages_retrieve) | **GET** /api/analytics/messages/ | 
*AnalyticsApi* | [**analytics_ratings_retrieve**](docs/AnalyticsApi.md#analytics_ratings_retrieve) | **GET** /api/analytics/ratings/ | 
*AnalyticsApi* | [**analytics_sessions_retrieve**](docs/AnalyticsApi.md#analytics_sessions_retrieve) | **GET** /api/analytics/sessions/ | 
*AnalyticsApi* | [**analytics_time_retrieve**](docs/AnalyticsApi.md#analytics_time_retrieve) | **GET** /api/analytics/time/ | 
*AnalyticsApi* | [**analytics_topics_details_retrieve**](docs/AnalyticsApi.md#analytics_topics_details_retrieve) | **GET** /api/analytics/topics/details/ | 
*AnalyticsApi* | [**analytics_topics_retrieve**](docs/AnalyticsApi.md#analytics_topics_retrieve) | **GET** /api/analytics/topics/ | 
*AnalyticsApi* | [**analytics_users_details_retrieve**](docs/AnalyticsApi.md#analytics_users_details_retrieve) | **GET** /api/analytics/users/details/ | 
*AnalyticsApi* | [**analytics_users_retrieve**](docs/AnalyticsApi.md#analytics_users_retrieve) | **GET** /api/analytics/users/ | 
*AnalyticsApi* | [**get_content_analytics**](docs/AnalyticsApi.md#get_content_analytics) | **GET** /api/analytics/content/ | Get Content Analytics
*AnalyticsApi* | [**get_content_details**](docs/AnalyticsApi.md#get_content_details) | **GET** /api/analytics/content/details/{content_id}/ | Get Content Details
*AutoRechargeApi* | [**auto_recharge_trigger_create**](docs/AutoRechargeApi.md#auto_recharge_trigger_create) | **POST** /auto-recharge/trigger/ | Trigger auto-recharge or manual top-up
*BillingApi* | [**billing_access_check_retrieve**](docs/BillingApi.md#billing_access_check_retrieve) | **GET** /api/billing/access-check/{item_type}/{item_id}/ | 
*BillingApi* | [**billing_account_partial_update**](docs/BillingApi.md#billing_account_partial_update) | **PATCH** /api/billing/account/ | Partially update auto-recharge preferences
*BillingApi* | [**billing_account_retrieve**](docs/BillingApi.md#billing_account_retrieve) | **GET** /api/billing/account/ | Get credit account information
*BillingApi* | [**billing_account_update**](docs/BillingApi.md#billing_account_update) | **PUT** /api/billing/account/ | Update auto-recharge preferences
*BillingApi* | [**billing_auto_recharge_trigger_create**](docs/BillingApi.md#billing_auto_recharge_trigger_create) | **POST** /api/billing/auto-recharge/trigger/ | Trigger auto-recharge or manual top-up
*BillingApi* | [**billing_platforms_items_access_check_retrieve**](docs/BillingApi.md#billing_platforms_items_access_check_retrieve) | **GET** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/access-check/ | 
*BillingApi* | [**billing_platforms_items_checkout_callback_retrieve**](docs/BillingApi.md#billing_platforms_items_checkout_callback_retrieve) | **GET** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/checkout-callback/ | Handle checkout callback
*BillingApi* | [**billing_platforms_items_checkout_callback_retrieve2**](docs/BillingApi.md#billing_platforms_items_checkout_callback_retrieve2) | **GET** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/checkout-callback/{checkout_session_id}/ | Handle checkout callback
*BillingApi* | [**billing_platforms_items_checkout_create**](docs/BillingApi.md#billing_platforms_items_checkout_create) | **POST** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/checkout/ | Create checkout session
*BillingApi* | [**billing_platforms_items_checkout_guest_create**](docs/BillingApi.md#billing_platforms_items_checkout_guest_create) | **POST** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/checkout-guest/ | Create guest checkout session
*BillingApi* | [**billing_platforms_items_paywall_create**](docs/BillingApi.md#billing_platforms_items_paywall_create) | **POST** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/paywall/ | Create or update paywall configuration
*BillingApi* | [**billing_platforms_items_paywall_destroy**](docs/BillingApi.md#billing_platforms_items_paywall_destroy) | **DELETE** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/paywall/ | Disable paywall configuration
*BillingApi* | [**billing_platforms_items_paywall_prices_create**](docs/BillingApi.md#billing_platforms_items_paywall_prices_create) | **POST** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/ | Create a price
*BillingApi* | [**billing_platforms_items_paywall_prices_destroy**](docs/BillingApi.md#billing_platforms_items_paywall_prices_destroy) | **DELETE** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/{price_id}/ | Delete a price
*BillingApi* | [**billing_platforms_items_paywall_prices_list**](docs/BillingApi.md#billing_platforms_items_paywall_prices_list) | **GET** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/ | List prices
*BillingApi* | [**billing_platforms_items_paywall_prices_retrieve**](docs/BillingApi.md#billing_platforms_items_paywall_prices_retrieve) | **GET** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/{price_id}/ | Get price details
*BillingApi* | [**billing_platforms_items_paywall_prices_update**](docs/BillingApi.md#billing_platforms_items_paywall_prices_update) | **PUT** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/{price_id}/ | Update a price
*BillingApi* | [**billing_platforms_items_paywall_retrieve**](docs/BillingApi.md#billing_platforms_items_paywall_retrieve) | **GET** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/paywall/ | Get paywall configuration
*BillingApi* | [**billing_platforms_items_paywall_update**](docs/BillingApi.md#billing_platforms_items_paywall_update) | **PUT** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/paywall/ | Update paywall configuration
*BillingApi* | [**billing_platforms_items_pricing_retrieve**](docs/BillingApi.md#billing_platforms_items_pricing_retrieve) | **GET** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/pricing/ | Get public pricing
*BillingApi* | [**billing_platforms_items_subscribers_list**](docs/BillingApi.md#billing_platforms_items_subscribers_list) | **GET** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/subscribers/ | List item subscribers
*BillingApi* | [**billing_platforms_items_subscription_cancel_create**](docs/BillingApi.md#billing_platforms_items_subscription_cancel_create) | **POST** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/subscription/cancel/ | Cancel subscription
*BillingApi* | [**billing_platforms_items_subscription_retrieve**](docs/BillingApi.md#billing_platforms_items_subscription_retrieve) | **GET** /api/billing/platforms/{platform_key}/items/{item_type}/{item_id}/subscription/ | Get user subscription
*BillingApi* | [**billing_platforms_my_subscriptions_list**](docs/BillingApi.md#billing_platforms_my_subscriptions_list) | **GET** /api/billing/platforms/{platform_key}/my-subscriptions/ | List user subscriptions
*BillingApi* | [**billing_platforms_paywalls_list**](docs/BillingApi.md#billing_platforms_paywalls_list) | **GET** /api/billing/platforms/{platform_key}/paywalls/ | List all platform paywall configurations
*BillingApi* | [**billing_platforms_revenue_retrieve**](docs/BillingApi.md#billing_platforms_revenue_retrieve) | **GET** /api/billing/platforms/{platform_key}/revenue/ | Platform sales summary
*BillingApi* | [**billing_platforms_subscribers_list**](docs/BillingApi.md#billing_platforms_subscribers_list) | **GET** /api/billing/platforms/{platform_key}/subscribers/ | List all platform subscribers
*BillingApi* | [**billing_transactions_retrieve**](docs/BillingApi.md#billing_transactions_retrieve) | **GET** /api/billing/transactions/ | List transaction history
*CareerApi* | [**career_location_orgs_users_create**](docs/CareerApi.md#career_location_orgs_users_create) | **POST** /api/career/location/orgs/{org}/users/{username}/ | 
*CareerApi* | [**career_location_orgs_users_retrieve**](docs/CareerApi.md#career_location_orgs_users_retrieve) | **GET** /api/career/location/orgs/{org}/users/{username}/ | 
*CareerApi* | [**career_location_orgs_users_update**](docs/CareerApi.md#career_location_orgs_users_update) | **PUT** /api/career/location/orgs/{org}/users/{username}/ | 
*CareerApi* | [**career_locations_orgs_retrieve**](docs/CareerApi.md#career_locations_orgs_retrieve) | **GET** /api/career/locations/orgs/{org}/ | 
*CareerApi* | [**career_orgs_companies_users_create**](docs/CareerApi.md#career_orgs_companies_users_create) | **POST** /api/career/orgs/{org}/companies/users/{username}/ | 
*CareerApi* | [**career_orgs_companies_users_destroy**](docs/CareerApi.md#career_orgs_companies_users_destroy) | **DELETE** /api/career/orgs/{org}/companies/users/{username}/ | 
*CareerApi* | [**career_orgs_companies_users_retrieve**](docs/CareerApi.md#career_orgs_companies_users_retrieve) | **GET** /api/career/orgs/{org}/companies/users/{username}/ | 
*CareerApi* | [**career_orgs_companies_users_update**](docs/CareerApi.md#career_orgs_companies_users_update) | **PUT** /api/career/orgs/{org}/companies/users/{username}/ | 
*CareerApi* | [**career_orgs_education_users_create**](docs/CareerApi.md#career_orgs_education_users_create) | **POST** /api/career/orgs/{org}/education/users/{username}/ | 
*CareerApi* | [**career_orgs_education_users_destroy**](docs/CareerApi.md#career_orgs_education_users_destroy) | **DELETE** /api/career/orgs/{org}/education/users/{username}/ | 
*CareerApi* | [**career_orgs_education_users_retrieve**](docs/CareerApi.md#career_orgs_education_users_retrieve) | **GET** /api/career/orgs/{org}/education/users/{username}/ | 
*CareerApi* | [**career_orgs_education_users_update**](docs/CareerApi.md#career_orgs_education_users_update) | **PUT** /api/career/orgs/{org}/education/users/{username}/ | 
*CareerApi* | [**career_orgs_experience_users_create**](docs/CareerApi.md#career_orgs_experience_users_create) | **POST** /api/career/orgs/{org}/experience/users/{username}/ | 
*CareerApi* | [**career_orgs_experience_users_destroy**](docs/CareerApi.md#career_orgs_experience_users_destroy) | **DELETE** /api/career/orgs/{org}/experience/users/{username}/ | 
*CareerApi* | [**career_orgs_experience_users_retrieve**](docs/CareerApi.md#career_orgs_experience_users_retrieve) | **GET** /api/career/orgs/{org}/experience/users/{username}/ | 
*CareerApi* | [**career_orgs_experience_users_update**](docs/CareerApi.md#career_orgs_experience_users_update) | **PUT** /api/career/orgs/{org}/experience/users/{username}/ | 
*CareerApi* | [**career_orgs_institutions_users_create**](docs/CareerApi.md#career_orgs_institutions_users_create) | **POST** /api/career/orgs/{org}/institutions/users/{username}/ | 
*CareerApi* | [**career_orgs_institutions_users_destroy**](docs/CareerApi.md#career_orgs_institutions_users_destroy) | **DELETE** /api/career/orgs/{org}/institutions/users/{username}/ | 
*CareerApi* | [**career_orgs_institutions_users_retrieve**](docs/CareerApi.md#career_orgs_institutions_users_retrieve) | **GET** /api/career/orgs/{org}/institutions/users/{username}/ | 
*CareerApi* | [**career_orgs_institutions_users_update**](docs/CareerApi.md#career_orgs_institutions_users_update) | **PUT** /api/career/orgs/{org}/institutions/users/{username}/ | 
*CareerApi* | [**career_orgs_programs_users_create**](docs/CareerApi.md#career_orgs_programs_users_create) | **POST** /api/career/orgs/{org}/programs/users/{username}/ | 
*CareerApi* | [**career_orgs_programs_users_destroy**](docs/CareerApi.md#career_orgs_programs_users_destroy) | **DELETE** /api/career/orgs/{org}/programs/users/{username}/ | 
*CareerApi* | [**career_orgs_programs_users_retrieve**](docs/CareerApi.md#career_orgs_programs_users_retrieve) | **GET** /api/career/orgs/{org}/programs/users/{username}/ | 
*CareerApi* | [**career_orgs_programs_users_update**](docs/CareerApi.md#career_orgs_programs_users_update) | **PUT** /api/career/orgs/{org}/programs/users/{username}/ | 
*CareerApi* | [**career_resume_orgs_users_create**](docs/CareerApi.md#career_resume_orgs_users_create) | **POST** /api/career/resume/orgs/{org}/users/{username}/ | 
*CareerApi* | [**career_resume_orgs_users_retrieve**](docs/CareerApi.md#career_resume_orgs_users_retrieve) | **GET** /api/career/resume/orgs/{org}/users/{username}/ | 
*CareerApi* | [**career_resume_orgs_users_update**](docs/CareerApi.md#career_resume_orgs_users_update) | **PUT** /api/career/resume/orgs/{org}/users/{username}/ | 
*CatalogApi* | [**catalog_access_requests_course_manage_create**](docs/CatalogApi.md#catalog_access_requests_course_manage_create) | **POST** /api/catalog/access_requests/course/manage/ | 
*CatalogApi* | [**catalog_access_requests_course_manage_retrieve**](docs/CatalogApi.md#catalog_access_requests_course_manage_retrieve) | **GET** /api/catalog/access_requests/course/manage/ | 
*CatalogApi* | [**catalog_access_requests_course_request_create**](docs/CatalogApi.md#catalog_access_requests_course_request_create) | **POST** /api/catalog/access_requests/course/request/ | 
*CatalogApi* | [**catalog_access_requests_course_request_retrieve**](docs/CatalogApi.md#catalog_access_requests_course_request_retrieve) | **GET** /api/catalog/access_requests/course/request/ | 
*CatalogApi* | [**catalog_conditionals_course_eligibility_retrieve**](docs/CatalogApi.md#catalog_conditionals_course_eligibility_retrieve) | **GET** /api/catalog/conditionals/course/eligibility/ | 
*CatalogApi* | [**catalog_conditionals_course_prerequisites_manage_bulk_create**](docs/CatalogApi.md#catalog_conditionals_course_prerequisites_manage_bulk_create) | **POST** /api/catalog/conditionals/course/prerequisites/manage/bulk/ | 
*CatalogApi* | [**catalog_conditionals_course_prerequisites_manage_retrieve**](docs/CatalogApi.md#catalog_conditionals_course_prerequisites_manage_retrieve) | **GET** /api/catalog/conditionals/course/prerequisites/manage/ | 
*CatalogApi* | [**catalog_courses_create**](docs/CatalogApi.md#catalog_courses_create) | **POST** /api/catalog/courses/ | 
*CatalogApi* | [**catalog_courses_destroy**](docs/CatalogApi.md#catalog_courses_destroy) | **DELETE** /api/catalog/courses/ | 
*CatalogApi* | [**catalog_courses_list**](docs/CatalogApi.md#catalog_courses_list) | **GET** /api/catalog/courses/ | 
*CatalogApi* | [**catalog_eligibility_courses_check_retrieve**](docs/CatalogApi.md#catalog_eligibility_courses_check_retrieve) | **GET** /api/catalog/eligibility/courses/check/ | 
*CatalogApi* | [**catalog_eligibility_courses_list**](docs/CatalogApi.md#catalog_eligibility_courses_list) | **GET** /api/catalog/eligibility/courses/ | 
*CatalogApi* | [**catalog_enrollment_courses_search_retrieve**](docs/CatalogApi.md#catalog_enrollment_courses_search_retrieve) | **GET** /api/catalog/enrollment/courses/search/ | 
*CatalogApi* | [**catalog_enrollment_pathways_create**](docs/CatalogApi.md#catalog_enrollment_pathways_create) | **POST** /api/catalog/enrollment/pathways/ | 
*CatalogApi* | [**catalog_enrollment_pathways_destroy**](docs/CatalogApi.md#catalog_enrollment_pathways_destroy) | **DELETE** /api/catalog/enrollment/pathways/ | 
*CatalogApi* | [**catalog_enrollment_pathways_retrieve**](docs/CatalogApi.md#catalog_enrollment_pathways_retrieve) | **GET** /api/catalog/enrollment/pathways/ | 
*CatalogApi* | [**catalog_enrollment_pathways_search_retrieve**](docs/CatalogApi.md#catalog_enrollment_pathways_search_retrieve) | **GET** /api/catalog/enrollment/pathways/search/ | 
*CatalogApi* | [**catalog_enrollment_pathways_self_create**](docs/CatalogApi.md#catalog_enrollment_pathways_self_create) | **POST** /api/catalog/enrollment/pathways/self/ | 
*CatalogApi* | [**catalog_enrollment_pathways_self_destroy**](docs/CatalogApi.md#catalog_enrollment_pathways_self_destroy) | **DELETE** /api/catalog/enrollment/pathways/self/ | 
*CatalogApi* | [**catalog_enrollment_programs_create**](docs/CatalogApi.md#catalog_enrollment_programs_create) | **POST** /api/catalog/enrollment/programs/ | 
*CatalogApi* | [**catalog_enrollment_programs_destroy**](docs/CatalogApi.md#catalog_enrollment_programs_destroy) | **DELETE** /api/catalog/enrollment/programs/ | 
*CatalogApi* | [**catalog_enrollment_programs_retrieve**](docs/CatalogApi.md#catalog_enrollment_programs_retrieve) | **GET** /api/catalog/enrollment/programs/ | 
*CatalogApi* | [**catalog_enrollment_programs_search_retrieve**](docs/CatalogApi.md#catalog_enrollment_programs_search_retrieve) | **GET** /api/catalog/enrollment/programs/search/ | 
*CatalogApi* | [**catalog_enrollment_programs_self_create**](docs/CatalogApi.md#catalog_enrollment_programs_self_create) | **POST** /api/catalog/enrollment/programs/self/ | 
*CatalogApi* | [**catalog_enrollment_programs_self_destroy**](docs/CatalogApi.md#catalog_enrollment_programs_self_destroy) | **DELETE** /api/catalog/enrollment/programs/self/ | 
*CatalogApi* | [**catalog_increment_create**](docs/CatalogApi.md#catalog_increment_create) | **POST** /api/catalog/increment/ | 
*CatalogApi* | [**catalog_increment_retrieve**](docs/CatalogApi.md#catalog_increment_retrieve) | **GET** /api/catalog/increment/ | 
*CatalogApi* | [**catalog_invitations_course_blank_create**](docs/CatalogApi.md#catalog_invitations_course_blank_create) | **POST** /api/catalog/invitations/course/blank/ | 
*CatalogApi* | [**catalog_invitations_course_bulk_create**](docs/CatalogApi.md#catalog_invitations_course_bulk_create) | **POST** /api/catalog/invitations/course/bulk/ | 
*CatalogApi* | [**catalog_invitations_course_create**](docs/CatalogApi.md#catalog_invitations_course_create) | **POST** /api/catalog/invitations/course/ | 
*CatalogApi* | [**catalog_invitations_course_destroy**](docs/CatalogApi.md#catalog_invitations_course_destroy) | **DELETE** /api/catalog/invitations/course/ | 
*CatalogApi* | [**catalog_invitations_course_redeem_create**](docs/CatalogApi.md#catalog_invitations_course_redeem_create) | **POST** /api/catalog/invitations/course/redeem/ | 
*CatalogApi* | [**catalog_invitations_course_retrieve**](docs/CatalogApi.md#catalog_invitations_course_retrieve) | **GET** /api/catalog/invitations/course/ | 
*CatalogApi* | [**catalog_invitations_platform_blank_create**](docs/CatalogApi.md#catalog_invitations_platform_blank_create) | **POST** /api/catalog/invitations/platform/blank/ | 
*CatalogApi* | [**catalog_invitations_platform_bulk_create**](docs/CatalogApi.md#catalog_invitations_platform_bulk_create) | **POST** /api/catalog/invitations/platform/bulk/ | 
*CatalogApi* | [**catalog_invitations_platform_check_retrieve**](docs/CatalogApi.md#catalog_invitations_platform_check_retrieve) | **GET** /api/catalog/invitations/platform/check/ | 
*CatalogApi* | [**catalog_invitations_platform_create**](docs/CatalogApi.md#catalog_invitations_platform_create) | **POST** /api/catalog/invitations/platform/ | 
*CatalogApi* | [**catalog_invitations_platform_destroy**](docs/CatalogApi.md#catalog_invitations_platform_destroy) | **DELETE** /api/catalog/invitations/platform/ | 
*CatalogApi* | [**catalog_invitations_platform_redeem_create**](docs/CatalogApi.md#catalog_invitations_platform_redeem_create) | **POST** /api/catalog/invitations/platform/redeem/ | 
*CatalogApi* | [**catalog_invitations_platform_retrieve**](docs/CatalogApi.md#catalog_invitations_platform_retrieve) | **GET** /api/catalog/invitations/platform/ | 
*CatalogApi* | [**catalog_invitations_program_blank_create**](docs/CatalogApi.md#catalog_invitations_program_blank_create) | **POST** /api/catalog/invitations/program/blank/ | 
*CatalogApi* | [**catalog_invitations_program_bulk_create**](docs/CatalogApi.md#catalog_invitations_program_bulk_create) | **POST** /api/catalog/invitations/program/bulk/ | 
*CatalogApi* | [**catalog_invitations_program_create**](docs/CatalogApi.md#catalog_invitations_program_create) | **POST** /api/catalog/invitations/program/ | 
*CatalogApi* | [**catalog_invitations_program_destroy**](docs/CatalogApi.md#catalog_invitations_program_destroy) | **DELETE** /api/catalog/invitations/program/ | 
*CatalogApi* | [**catalog_invitations_program_redeem_create**](docs/CatalogApi.md#catalog_invitations_program_redeem_create) | **POST** /api/catalog/invitations/program/redeem/ | 
*CatalogApi* | [**catalog_invitations_program_retrieve**](docs/CatalogApi.md#catalog_invitations_program_retrieve) | **GET** /api/catalog/invitations/program/ | 
*CatalogApi* | [**catalog_licenses_course_assignment_create**](docs/CatalogApi.md#catalog_licenses_course_assignment_create) | **POST** /api/catalog/licenses/course/assignment/ | 
*CatalogApi* | [**catalog_licenses_course_assignment_destroy**](docs/CatalogApi.md#catalog_licenses_course_assignment_destroy) | **DELETE** /api/catalog/licenses/course/assignment/ | 
*CatalogApi* | [**catalog_licenses_course_assignment_group_create**](docs/CatalogApi.md#catalog_licenses_course_assignment_group_create) | **POST** /api/catalog/licenses/course/assignment/group/ | 
*CatalogApi* | [**catalog_licenses_course_assignment_group_destroy**](docs/CatalogApi.md#catalog_licenses_course_assignment_group_destroy) | **DELETE** /api/catalog/licenses/course/assignment/group/ | 
*CatalogApi* | [**catalog_licenses_course_assignment_group_retrieve**](docs/CatalogApi.md#catalog_licenses_course_assignment_group_retrieve) | **GET** /api/catalog/licenses/course/assignment/group/ | 
*CatalogApi* | [**catalog_licenses_course_assignment_retrieve**](docs/CatalogApi.md#catalog_licenses_course_assignment_retrieve) | **GET** /api/catalog/licenses/course/assignment/ | 
*CatalogApi* | [**catalog_licenses_course_create_create**](docs/CatalogApi.md#catalog_licenses_course_create_create) | **POST** /api/catalog/licenses/course/create/ | 
*CatalogApi* | [**catalog_licenses_course_retrieve**](docs/CatalogApi.md#catalog_licenses_course_retrieve) | **GET** /api/catalog/licenses/course/ | 
*CatalogApi* | [**catalog_licenses_course_update_create**](docs/CatalogApi.md#catalog_licenses_course_update_create) | **POST** /api/catalog/licenses/course/update/ | 
*CatalogApi* | [**catalog_licenses_platform_create_create**](docs/CatalogApi.md#catalog_licenses_platform_create_create) | **POST** /api/catalog/licenses/platform/create/ | 
*CatalogApi* | [**catalog_licenses_platform_retrieve**](docs/CatalogApi.md#catalog_licenses_platform_retrieve) | **GET** /api/catalog/licenses/platform/ | 
*CatalogApi* | [**catalog_licenses_platform_update_create**](docs/CatalogApi.md#catalog_licenses_platform_update_create) | **POST** /api/catalog/licenses/platform/update/ | 
*CatalogApi* | [**catalog_licenses_program_assignment_create**](docs/CatalogApi.md#catalog_licenses_program_assignment_create) | **POST** /api/catalog/licenses/program/assignment/ | 
*CatalogApi* | [**catalog_licenses_program_assignment_destroy**](docs/CatalogApi.md#catalog_licenses_program_assignment_destroy) | **DELETE** /api/catalog/licenses/program/assignment/ | 
*CatalogApi* | [**catalog_licenses_program_assignment_group_create**](docs/CatalogApi.md#catalog_licenses_program_assignment_group_create) | **POST** /api/catalog/licenses/program/assignment/group/ | 
*CatalogApi* | [**catalog_licenses_program_assignment_group_destroy**](docs/CatalogApi.md#catalog_licenses_program_assignment_group_destroy) | **DELETE** /api/catalog/licenses/program/assignment/group/ | 
*CatalogApi* | [**catalog_licenses_program_assignment_group_retrieve**](docs/CatalogApi.md#catalog_licenses_program_assignment_group_retrieve) | **GET** /api/catalog/licenses/program/assignment/group/ | 
*CatalogApi* | [**catalog_licenses_program_assignment_retrieve**](docs/CatalogApi.md#catalog_licenses_program_assignment_retrieve) | **GET** /api/catalog/licenses/program/assignment/ | 
*CatalogApi* | [**catalog_licenses_program_create_create**](docs/CatalogApi.md#catalog_licenses_program_create_create) | **POST** /api/catalog/licenses/program/create/ | 
*CatalogApi* | [**catalog_licenses_program_retrieve**](docs/CatalogApi.md#catalog_licenses_program_retrieve) | **GET** /api/catalog/licenses/program/ | 
*CatalogApi* | [**catalog_licenses_program_update_create**](docs/CatalogApi.md#catalog_licenses_program_update_create) | **POST** /api/catalog/licenses/program/update/ | 
*CatalogApi* | [**catalog_licenses_user_assignment_check_retrieve**](docs/CatalogApi.md#catalog_licenses_user_assignment_check_retrieve) | **GET** /api/catalog/licenses/user/assignment/check/ | 
*CatalogApi* | [**catalog_licenses_user_assignment_create**](docs/CatalogApi.md#catalog_licenses_user_assignment_create) | **POST** /api/catalog/licenses/user/assignment/ | 
*CatalogApi* | [**catalog_licenses_user_assignment_destroy**](docs/CatalogApi.md#catalog_licenses_user_assignment_destroy) | **DELETE** /api/catalog/licenses/user/assignment/ | 
*CatalogApi* | [**catalog_licenses_user_assignment_group_create**](docs/CatalogApi.md#catalog_licenses_user_assignment_group_create) | **POST** /api/catalog/licenses/user/assignment/group/ | 
*CatalogApi* | [**catalog_licenses_user_assignment_group_destroy**](docs/CatalogApi.md#catalog_licenses_user_assignment_group_destroy) | **DELETE** /api/catalog/licenses/user/assignment/group/ | 
*CatalogApi* | [**catalog_licenses_user_assignment_group_retrieve**](docs/CatalogApi.md#catalog_licenses_user_assignment_group_retrieve) | **GET** /api/catalog/licenses/user/assignment/group/ | 
*CatalogApi* | [**catalog_licenses_user_assignment_retrieve**](docs/CatalogApi.md#catalog_licenses_user_assignment_retrieve) | **GET** /api/catalog/licenses/user/assignment/ | 
*CatalogApi* | [**catalog_licenses_user_create_create**](docs/CatalogApi.md#catalog_licenses_user_create_create) | **POST** /api/catalog/licenses/user/create/ | 
*CatalogApi* | [**catalog_licenses_user_retrieve**](docs/CatalogApi.md#catalog_licenses_user_retrieve) | **GET** /api/catalog/licenses/user/ | 
*CatalogApi* | [**catalog_licenses_user_update_create**](docs/CatalogApi.md#catalog_licenses_user_update_create) | **POST** /api/catalog/licenses/user/update/ | 
*CatalogApi* | [**catalog_metadata_choices_retrieve**](docs/CatalogApi.md#catalog_metadata_choices_retrieve) | **GET** /api/catalog/metadata/choices/ | 
*CatalogApi* | [**catalog_metadata_course_create**](docs/CatalogApi.md#catalog_metadata_course_create) | **POST** /api/catalog/metadata/course/ | 
*CatalogApi* | [**catalog_metadata_course_create2**](docs/CatalogApi.md#catalog_metadata_course_create2) | **POST** /api/catalog/metadata/course/{field}/ | 
*CatalogApi* | [**catalog_metadata_course_public_retrieve**](docs/CatalogApi.md#catalog_metadata_course_public_retrieve) | **GET** /api/catalog/metadata/course-public/ | 
*CatalogApi* | [**catalog_metadata_course_public_retrieve2**](docs/CatalogApi.md#catalog_metadata_course_public_retrieve2) | **GET** /api/catalog/metadata/course-public/{field}/ | 
*CatalogApi* | [**catalog_metadata_course_retrieve**](docs/CatalogApi.md#catalog_metadata_course_retrieve) | **GET** /api/catalog/metadata/course/ | 
*CatalogApi* | [**catalog_metadata_course_retrieve2**](docs/CatalogApi.md#catalog_metadata_course_retrieve2) | **GET** /api/catalog/metadata/course/{field}/ | 
*CatalogApi* | [**catalog_metadata_course_search_create**](docs/CatalogApi.md#catalog_metadata_course_search_create) | **POST** /api/catalog/metadata/course-search/ | 
*CatalogApi* | [**catalog_metadata_program_create**](docs/CatalogApi.md#catalog_metadata_program_create) | **POST** /api/catalog/metadata/program/ | 
*CatalogApi* | [**catalog_metadata_program_create2**](docs/CatalogApi.md#catalog_metadata_program_create2) | **POST** /api/catalog/metadata/program/{field}/ | 
*CatalogApi* | [**catalog_metadata_program_public_retrieve**](docs/CatalogApi.md#catalog_metadata_program_public_retrieve) | **GET** /api/catalog/metadata/program-public/ | 
*CatalogApi* | [**catalog_metadata_program_public_retrieve2**](docs/CatalogApi.md#catalog_metadata_program_public_retrieve2) | **GET** /api/catalog/metadata/program-public/{field}/ | 
*CatalogApi* | [**catalog_metadata_program_retrieve**](docs/CatalogApi.md#catalog_metadata_program_retrieve) | **GET** /api/catalog/metadata/program/ | 
*CatalogApi* | [**catalog_metadata_program_retrieve2**](docs/CatalogApi.md#catalog_metadata_program_retrieve2) | **GET** /api/catalog/metadata/program/{field}/ | 
*CatalogApi* | [**catalog_milestones_completions_course_catalog_retrieve**](docs/CatalogApi.md#catalog_milestones_completions_course_catalog_retrieve) | **GET** /api/catalog/milestones/completions/course/catalog/ | 
*CatalogApi* | [**catalog_milestones_completions_course_manage_create**](docs/CatalogApi.md#catalog_milestones_completions_course_manage_create) | **POST** /api/catalog/milestones/completions/course/manage/ | 
*CatalogApi* | [**catalog_milestones_completions_course_manage_retrieve**](docs/CatalogApi.md#catalog_milestones_completions_course_manage_retrieve) | **GET** /api/catalog/milestones/completions/course/manage/ | 
*CatalogApi* | [**catalog_milestones_completions_pathway_query_retrieve**](docs/CatalogApi.md#catalog_milestones_completions_pathway_query_retrieve) | **GET** /api/catalog/milestones/completions/pathway/query/ | 
*CatalogApi* | [**catalog_milestones_completions_program_query_retrieve**](docs/CatalogApi.md#catalog_milestones_completions_program_query_retrieve) | **GET** /api/catalog/milestones/completions/program/query/ | 
*CatalogApi* | [**catalog_milestones_completions_resource_manage_create**](docs/CatalogApi.md#catalog_milestones_completions_resource_manage_create) | **POST** /api/catalog/milestones/completions/resource/manage/ | 
*CatalogApi* | [**catalog_milestones_completions_resource_manage_retrieve**](docs/CatalogApi.md#catalog_milestones_completions_resource_manage_retrieve) | **GET** /api/catalog/milestones/completions/resource/manage/ | 
*CatalogApi* | [**catalog_milestones_skill_points_block_create**](docs/CatalogApi.md#catalog_milestones_skill_points_block_create) | **POST** /api/catalog/milestones/skill_points/block/ | 
*CatalogApi* | [**catalog_milestones_skill_points_block_retrieve**](docs/CatalogApi.md#catalog_milestones_skill_points_block_retrieve) | **GET** /api/catalog/milestones/skill_points/block/ | 
*CatalogApi* | [**catalog_milestones_skill_points_course_create**](docs/CatalogApi.md#catalog_milestones_skill_points_course_create) | **POST** /api/catalog/milestones/skill_points/course/ | 
*CatalogApi* | [**catalog_milestones_skill_points_course_retrieve**](docs/CatalogApi.md#catalog_milestones_skill_points_course_retrieve) | **GET** /api/catalog/milestones/skill_points/course/ | 
*CatalogApi* | [**catalog_milestones_skill_points_platform_bulk_create**](docs/CatalogApi.md#catalog_milestones_skill_points_platform_bulk_create) | **POST** /api/catalog/milestones/skill_points/platform/bulk/ | 
*CatalogApi* | [**catalog_milestones_skill_points_platform_create**](docs/CatalogApi.md#catalog_milestones_skill_points_platform_create) | **POST** /api/catalog/milestones/skill_points/platform/ | 
*CatalogApi* | [**catalog_milestones_skill_points_platform_destroy**](docs/CatalogApi.md#catalog_milestones_skill_points_platform_destroy) | **DELETE** /api/catalog/milestones/skill_points/platform/ | 
*CatalogApi* | [**catalog_milestones_skill_points_platform_group_create**](docs/CatalogApi.md#catalog_milestones_skill_points_platform_group_create) | **POST** /api/catalog/milestones/skill_points/platform/group/ | 
*CatalogApi* | [**catalog_milestones_skill_points_platform_retrieve**](docs/CatalogApi.md#catalog_milestones_skill_points_platform_retrieve) | **GET** /api/catalog/milestones/skill_points/platform/ | 
*CatalogApi* | [**catalog_milestones_skill_points_user_retrieve**](docs/CatalogApi.md#catalog_milestones_skill_points_user_retrieve) | **GET** /api/catalog/milestones/skill_points/user/ | 
*CatalogApi* | [**catalog_pathways_create**](docs/CatalogApi.md#catalog_pathways_create) | **POST** /api/catalog/pathways/ | 
*CatalogApi* | [**catalog_pathways_destroy**](docs/CatalogApi.md#catalog_pathways_destroy) | **DELETE** /api/catalog/pathways/ | 
*CatalogApi* | [**catalog_pathways_list**](docs/CatalogApi.md#catalog_pathways_list) | **GET** /api/catalog/pathways/ | 
*CatalogApi* | [**catalog_programs_create**](docs/CatalogApi.md#catalog_programs_create) | **POST** /api/catalog/programs/ | 
*CatalogApi* | [**catalog_programs_destroy**](docs/CatalogApi.md#catalog_programs_destroy) | **DELETE** /api/catalog/programs/ | 
*CatalogApi* | [**catalog_programs_list**](docs/CatalogApi.md#catalog_programs_list) | **GET** /api/catalog/programs/ | 
*CatalogApi* | [**catalog_recommendation_courses_retrieve**](docs/CatalogApi.md#catalog_recommendation_courses_retrieve) | **GET** /api/catalog/recommendation/courses/ | 
*CatalogApi* | [**catalog_resources_create**](docs/CatalogApi.md#catalog_resources_create) | **POST** /api/catalog/resources/ | Create or update a resource with optional image upload
*CatalogApi* | [**catalog_resources_destroy**](docs/CatalogApi.md#catalog_resources_destroy) | **DELETE** /api/catalog/resources/ | 
*CatalogApi* | [**catalog_resources_list**](docs/CatalogApi.md#catalog_resources_list) | **GET** /api/catalog/resources/ | 
*CatalogApi* | [**catalog_reviews_course_info_retrieve**](docs/CatalogApi.md#catalog_reviews_course_info_retrieve) | **GET** /api/catalog/reviews/course/info/ | 
*CatalogApi* | [**catalog_reviews_course_retrieve**](docs/CatalogApi.md#catalog_reviews_course_retrieve) | **GET** /api/catalog/reviews/course/ | 
*CatalogApi* | [**catalog_reviews_course_update_create**](docs/CatalogApi.md#catalog_reviews_course_update_create) | **POST** /api/catalog/reviews/course/update/ | 
*CatalogApi* | [**catalog_reviews_course_update_destroy**](docs/CatalogApi.md#catalog_reviews_course_update_destroy) | **DELETE** /api/catalog/reviews/course/update/ | 
*CatalogApi* | [**catalog_reviews_program_info_retrieve**](docs/CatalogApi.md#catalog_reviews_program_info_retrieve) | **GET** /api/catalog/reviews/program/info/ | 
*CatalogApi* | [**catalog_reviews_program_retrieve**](docs/CatalogApi.md#catalog_reviews_program_retrieve) | **GET** /api/catalog/reviews/program/ | 
*CatalogApi* | [**catalog_reviews_program_update_create**](docs/CatalogApi.md#catalog_reviews_program_update_create) | **POST** /api/catalog/reviews/program/update/ | 
*CatalogApi* | [**catalog_reviews_program_update_destroy**](docs/CatalogApi.md#catalog_reviews_program_update_destroy) | **DELETE** /api/catalog/reviews/program/update/ | 
*CatalogApi* | [**catalog_roles_create**](docs/CatalogApi.md#catalog_roles_create) | **POST** /api/catalog/roles/ | 
*CatalogApi* | [**catalog_roles_desired_create**](docs/CatalogApi.md#catalog_roles_desired_create) | **POST** /api/catalog/roles/desired/ | 
*CatalogApi* | [**catalog_roles_desired_retrieve**](docs/CatalogApi.md#catalog_roles_desired_retrieve) | **GET** /api/catalog/roles/desired/ | 
*CatalogApi* | [**catalog_roles_public_create**](docs/CatalogApi.md#catalog_roles_public_create) | **POST** /api/catalog/roles/public/ | 
*CatalogApi* | [**catalog_roles_reported_create**](docs/CatalogApi.md#catalog_roles_reported_create) | **POST** /api/catalog/roles/reported/ | 
*CatalogApi* | [**catalog_roles_reported_retrieve**](docs/CatalogApi.md#catalog_roles_reported_retrieve) | **GET** /api/catalog/roles/reported/ | 
*CatalogApi* | [**catalog_roles_retrieve**](docs/CatalogApi.md#catalog_roles_retrieve) | **GET** /api/catalog/roles/ | 
*CatalogApi* | [**catalog_search_programs_create**](docs/CatalogApi.md#catalog_search_programs_create) | **POST** /api/catalog/search/programs/ | 
*CatalogApi* | [**catalog_skills_create**](docs/CatalogApi.md#catalog_skills_create) | **POST** /api/catalog/skills/ | 
*CatalogApi* | [**catalog_skills_desired_create**](docs/CatalogApi.md#catalog_skills_desired_create) | **POST** /api/catalog/skills/desired/ | 
*CatalogApi* | [**catalog_skills_desired_retrieve**](docs/CatalogApi.md#catalog_skills_desired_retrieve) | **GET** /api/catalog/skills/desired/ | 
*CatalogApi* | [**catalog_skills_public_create**](docs/CatalogApi.md#catalog_skills_public_create) | **POST** /api/catalog/skills/public/ | 
*CatalogApi* | [**catalog_skills_reported_create**](docs/CatalogApi.md#catalog_skills_reported_create) | **POST** /api/catalog/skills/reported/ | 
*CatalogApi* | [**catalog_skills_reported_retrieve**](docs/CatalogApi.md#catalog_skills_reported_retrieve) | **GET** /api/catalog/skills/reported/ | 
*CatalogApi* | [**catalog_skills_retrieve**](docs/CatalogApi.md#catalog_skills_retrieve) | **GET** /api/catalog/skills/ | 
*CatalogApi* | [**catalog_suggestions_course_manage_bulk_create**](docs/CatalogApi.md#catalog_suggestions_course_manage_bulk_create) | **POST** /api/catalog/suggestions/course/manage/bulk/ | 
*CatalogApi* | [**catalog_suggestions_course_manage_create**](docs/CatalogApi.md#catalog_suggestions_course_manage_create) | **POST** /api/catalog/suggestions/course/manage/ | 
*CatalogApi* | [**catalog_suggestions_course_manage_destroy**](docs/CatalogApi.md#catalog_suggestions_course_manage_destroy) | **DELETE** /api/catalog/suggestions/course/manage/ | 
*CatalogApi* | [**catalog_suggestions_course_manage_group_create**](docs/CatalogApi.md#catalog_suggestions_course_manage_group_create) | **POST** /api/catalog/suggestions/course/manage/group/ | 
*CatalogApi* | [**catalog_suggestions_course_manage_group_destroy**](docs/CatalogApi.md#catalog_suggestions_course_manage_group_destroy) | **DELETE** /api/catalog/suggestions/course/manage/group/ | 
*CatalogApi* | [**catalog_suggestions_course_manage_group_retrieve**](docs/CatalogApi.md#catalog_suggestions_course_manage_group_retrieve) | **GET** /api/catalog/suggestions/course/manage/group/ | 
*CatalogApi* | [**catalog_suggestions_course_manage_retrieve**](docs/CatalogApi.md#catalog_suggestions_course_manage_retrieve) | **GET** /api/catalog/suggestions/course/manage/ | 
*CatalogApi* | [**catalog_suggestions_course_user_retrieve**](docs/CatalogApi.md#catalog_suggestions_course_user_retrieve) | **GET** /api/catalog/suggestions/course/user/ | 
*CatalogApi* | [**catalog_suggestions_pathway_manage_bulk_create**](docs/CatalogApi.md#catalog_suggestions_pathway_manage_bulk_create) | **POST** /api/catalog/suggestions/pathway/manage/bulk/ | 
*CatalogApi* | [**catalog_suggestions_pathway_manage_create**](docs/CatalogApi.md#catalog_suggestions_pathway_manage_create) | **POST** /api/catalog/suggestions/pathway/manage/ | 
*CatalogApi* | [**catalog_suggestions_pathway_manage_destroy**](docs/CatalogApi.md#catalog_suggestions_pathway_manage_destroy) | **DELETE** /api/catalog/suggestions/pathway/manage/ | 
*CatalogApi* | [**catalog_suggestions_pathway_manage_group_create**](docs/CatalogApi.md#catalog_suggestions_pathway_manage_group_create) | **POST** /api/catalog/suggestions/pathway/manage/group/ | 
*CatalogApi* | [**catalog_suggestions_pathway_manage_group_destroy**](docs/CatalogApi.md#catalog_suggestions_pathway_manage_group_destroy) | **DELETE** /api/catalog/suggestions/pathway/manage/group/ | 
*CatalogApi* | [**catalog_suggestions_pathway_manage_group_retrieve**](docs/CatalogApi.md#catalog_suggestions_pathway_manage_group_retrieve) | **GET** /api/catalog/suggestions/pathway/manage/group/ | 
*CatalogApi* | [**catalog_suggestions_pathway_manage_retrieve**](docs/CatalogApi.md#catalog_suggestions_pathway_manage_retrieve) | **GET** /api/catalog/suggestions/pathway/manage/ | 
*CatalogApi* | [**catalog_suggestions_pathway_user_retrieve**](docs/CatalogApi.md#catalog_suggestions_pathway_user_retrieve) | **GET** /api/catalog/suggestions/pathway/user/ | 
*CatalogApi* | [**catalog_suggestions_program_manage_bulk_create**](docs/CatalogApi.md#catalog_suggestions_program_manage_bulk_create) | **POST** /api/catalog/suggestions/program/manage/bulk/ | 
*CatalogApi* | [**catalog_suggestions_program_manage_create**](docs/CatalogApi.md#catalog_suggestions_program_manage_create) | **POST** /api/catalog/suggestions/program/manage/ | 
*CatalogApi* | [**catalog_suggestions_program_manage_destroy**](docs/CatalogApi.md#catalog_suggestions_program_manage_destroy) | **DELETE** /api/catalog/suggestions/program/manage/ | 
*CatalogApi* | [**catalog_suggestions_program_manage_group_create**](docs/CatalogApi.md#catalog_suggestions_program_manage_group_create) | **POST** /api/catalog/suggestions/program/manage/group/ | 
*CatalogApi* | [**catalog_suggestions_program_manage_group_destroy**](docs/CatalogApi.md#catalog_suggestions_program_manage_group_destroy) | **DELETE** /api/catalog/suggestions/program/manage/group/ | 
*CatalogApi* | [**catalog_suggestions_program_manage_group_retrieve**](docs/CatalogApi.md#catalog_suggestions_program_manage_group_retrieve) | **GET** /api/catalog/suggestions/program/manage/group/ | 
*CatalogApi* | [**catalog_suggestions_program_manage_retrieve**](docs/CatalogApi.md#catalog_suggestions_program_manage_retrieve) | **GET** /api/catalog/suggestions/program/manage/ | 
*CatalogApi* | [**catalog_suggestions_program_user_retrieve**](docs/CatalogApi.md#catalog_suggestions_program_user_retrieve) | **GET** /api/catalog/suggestions/program/user/ | 
*CommerceApi* | [**provider_association_stripe_callback_retrieve**](docs/CommerceApi.md#provider_association_stripe_callback_retrieve) | **GET** /api/provider-association/stripe/callback/{launch_id}/ | 
*CommerceApi* | [**providers_apple_associate_account_create**](docs/CommerceApi.md#providers_apple_associate_account_create) | **POST** /api/providers/apple/associate-account/ | 
*CommerceApi* | [**providers_apple_hook_create**](docs/CommerceApi.md#providers_apple_hook_create) | **POST** /api/providers/apple/hook/ | 
*CommerceApi* | [**providers_apple_subscription_status_create**](docs/CommerceApi.md#providers_apple_subscription_status_create) | **POST** /api/providers/apple/subscription-status/ | 
*CommerceApi* | [**providers_apple_validate_transaction_id_create**](docs/CommerceApi.md#providers_apple_validate_transaction_id_create) | **POST** /api/providers/apple/validate-transaction-id/ | 
*CommerceApi* | [**providers_aws_create_organization_create**](docs/CommerceApi.md#providers_aws_create_organization_create) | **POST** /api/providers/aws/create-organization/ | 
*CommerceApi* | [**providers_aws_domain_status_retrieve**](docs/CommerceApi.md#providers_aws_domain_status_retrieve) | **GET** /api/providers/aws/domain-status/ | 
*CommerceApi* | [**providers_aws_launch_tenant_create**](docs/CommerceApi.md#providers_aws_launch_tenant_create) | **POST** /api/providers/aws/launch-tenant/ | 
*CommerceApi* | [**providers_aws_sync_domain_records_create**](docs/CommerceApi.md#providers_aws_sync_domain_records_create) | **POST** /api/providers/aws/sync-domain-records/ | 
*CommerceApi* | [**providers_aws_sync_domain_records_retrieve**](docs/CommerceApi.md#providers_aws_sync_domain_records_retrieve) | **GET** /api/providers/aws/sync-domain-records/ | 
*CommerceApi* | [**providers_gcp_create_organization_create**](docs/CommerceApi.md#providers_gcp_create_organization_create) | **POST** /api/providers/gcp/create-organization/ | 
*CommerceApi* | [**providers_gcp_create_organization_create2**](docs/CommerceApi.md#providers_gcp_create_organization_create2) | **POST** /api/providers/gcp/create-organization/{product_id}/ | 
*CommerceApi* | [**providers_gcp_hook_create**](docs/CommerceApi.md#providers_gcp_hook_create) | **POST** /api/providers/gcp/hook/ | 
*CommerceApi* | [**providers_gcp_launch_tenant_create**](docs/CommerceApi.md#providers_gcp_launch_tenant_create) | **POST** /api/providers/gcp/launch-tenant/ | 
*CommerceApi* | [**providers_gcp_validate_signup_token_create**](docs/CommerceApi.md#providers_gcp_validate_signup_token_create) | **POST** /api/providers/gcp/validate-signup-token/ | 
*CommerceApi* | [**providers_google_pay_get_account_retrieve**](docs/CommerceApi.md#providers_google_pay_get_account_retrieve) | **GET** /api/providers/google-pay/get-account/{bundle_id} | 
*CommerceApi* | [**providers_google_pay_hook_create**](docs/CommerceApi.md#providers_google_pay_hook_create) | **POST** /api/providers/google-pay/hook/ | 
*CommerceApi* | [**providers_google_pay_validate_transaction_id_create**](docs/CommerceApi.md#providers_google_pay_validate_transaction_id_create) | **POST** /api/providers/google-pay/validate-transaction-id/ | 
*CommerceApi* | [**providers_stripe_create_organization_create**](docs/CommerceApi.md#providers_stripe_create_organization_create) | **POST** /api/providers/stripe/create-organization/ | 
*CommerceApi* | [**provision_create**](docs/CommerceApi.md#provision_create) | **POST** /api/provision/{config_name}/ | 
*CommerceApi* | [**service_launch_tenant_create**](docs/CommerceApi.md#service_launch_tenant_create) | **POST** /api/service/launch/tenant/ | 
*CommerceApi* | [**service_manage_user_create**](docs/CommerceApi.md#service_manage_user_create) | **POST** /api/service/manage/user/ | 
*CommerceApi* | [**service_manage_user_role_create**](docs/CommerceApi.md#service_manage_user_role_create) | **POST** /api/service/manage/user/role/ | 
*CommerceApi* | [**service_orgs_stripe_course_payment_callback_retrieve**](docs/CommerceApi.md#service_orgs_stripe_course_payment_callback_retrieve) | **GET** /api/service/orgs/{platform_key}/stripe/course-payment-callback/ | 
*CommerceApi* | [**service_orgs_users_stripe_checkout_session_create**](docs/CommerceApi.md#service_orgs_users_stripe_checkout_session_create) | **POST** /api/service/orgs/{org}/users/{user_id}/stripe/checkout-session/ | 
*CommerceApi* | [**service_orgs_users_stripe_customer_portal_create**](docs/CommerceApi.md#service_orgs_users_stripe_customer_portal_create) | **POST** /api/service/orgs/{org}/users/{user_id}/stripe/customer-portal/ | 
*CommerceApi* | [**service_orgs_users_stripe_products_manage_create**](docs/CommerceApi.md#service_orgs_users_stripe_products_manage_create) | **POST** /api/service/orgs/{org}/users/{user_id}/stripe/products/manage/ | 
*CommerceApi* | [**service_orgs_users_stripe_products_retrieve**](docs/CommerceApi.md#service_orgs_users_stripe_products_retrieve) | **GET** /api/service/orgs/{org}/users/{user_id}/stripe/products/ | 
*CommerceApi* | [**service_orgs_users_stripe_subscription_renewal_create**](docs/CommerceApi.md#service_orgs_users_stripe_subscription_renewal_create) | **POST** /api/service/orgs/{org}/users/{user_id}/stripe/subscription-renewal/ | 
*CommerceApi* | [**service_orgs_users_stripe_subscriptions_retrieve**](docs/CommerceApi.md#service_orgs_users_stripe_subscriptions_retrieve) | **GET** /api/service/orgs/{org}/users/{user_id}/stripe/subscriptions/ | 
*CommerceApi* | [**service_platforms_stripe_connect_dashboard_retrieve**](docs/CommerceApi.md#service_platforms_stripe_connect_dashboard_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/connect/dashboard/ | 
*CommerceApi* | [**service_platforms_stripe_connect_destroy**](docs/CommerceApi.md#service_platforms_stripe_connect_destroy) | **DELETE** /api/service/platforms/{platform_key}/stripe/connect/ | 
*CommerceApi* | [**service_platforms_stripe_connect_onboard_create**](docs/CommerceApi.md#service_platforms_stripe_connect_onboard_create) | **POST** /api/service/platforms/{platform_key}/stripe/connect/onboard/ | 
*CommerceApi* | [**service_platforms_stripe_connect_onboard_refresh_create**](docs/CommerceApi.md#service_platforms_stripe_connect_onboard_refresh_create) | **POST** /api/service/platforms/{platform_key}/stripe/connect/onboard/refresh/ | 
*CommerceApi* | [**service_platforms_stripe_connect_status_retrieve**](docs/CommerceApi.md#service_platforms_stripe_connect_status_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/connect/status/ | 
*CommerceApi* | [**service_platforms_stripe_context_retrieve**](docs/CommerceApi.md#service_platforms_stripe_context_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/context/ | 
*CommerceApi* | [**service_platforms_stripe_credit_topup_callback_retrieve**](docs/CommerceApi.md#service_platforms_stripe_credit_topup_callback_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/credit-topup-callback/{checkout_session_id}/ | 
*CommerceApi* | [**service_platforms_stripe_pricing_page_callback_retrieve**](docs/CommerceApi.md#service_platforms_stripe_pricing_page_callback_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/pricing-page-callback/ | 
*CommerceApi* | [**service_platforms_stripe_pricing_page_callback_retrieve2**](docs/CommerceApi.md#service_platforms_stripe_pricing_page_callback_retrieve2) | **GET** /api/service/platforms/{platform_key}/stripe/pricing-page-callback/{checkout_session_id}/ | 
*CommerceApi* | [**service_platforms_stripe_pricing_page_session_retrieve**](docs/CommerceApi.md#service_platforms_stripe_pricing_page_session_retrieve) | **GET** /api/service/platforms/{platform_key}/stripe/pricing-page-session/ | 
*CommerceApi* | [**service_stripe_checkout_free_trial_create**](docs/CommerceApi.md#service_stripe_checkout_free_trial_create) | **POST** /api/service/stripe/checkout/free-trial/ | 
*CommerceApi* | [**service_stripe_checkout_retrieve**](docs/CommerceApi.md#service_stripe_checkout_retrieve) | **GET** /api/service/stripe/checkout/{checkout_uuid}/ | 
*CommerceApi* | [**service_stripe_new_user_checkout_create**](docs/CommerceApi.md#service_stripe_new_user_checkout_create) | **POST** /api/service/stripe/new-user-checkout/ | 
*CommerceApi* | [**service_tenant_validation_create**](docs/CommerceApi.md#service_tenant_validation_create) | **POST** /api/service/tenant/validation/ | 
*CommerceApi* | [**service_token_retrieve**](docs/CommerceApi.md#service_token_retrieve) | **GET** /api/service/token/ | 
*CommerceApi* | [**service_user_validation_create**](docs/CommerceApi.md#service_user_validation_create) | **POST** /api/service/user/validation/ | 
*CoreApi* | [**core_consolidated_token_proxy_create**](docs/CoreApi.md#core_consolidated_token_proxy_create) | **POST** /api/core/consolidated-token/proxy/ | 
*CoreApi* | [**core_departments_create**](docs/CoreApi.md#core_departments_create) | **POST** /api/core/departments/ | 
*CoreApi* | [**core_departments_destroy**](docs/CoreApi.md#core_departments_destroy) | **DELETE** /api/core/departments/ | 
*CoreApi* | [**core_departments_members_bulk_create**](docs/CoreApi.md#core_departments_members_bulk_create) | **POST** /api/core/departments/members/bulk/ | 
*CoreApi* | [**core_departments_members_check_retrieve**](docs/CoreApi.md#core_departments_members_check_retrieve) | **GET** /api/core/departments/members/check/ | 
*CoreApi* | [**core_departments_members_create**](docs/CoreApi.md#core_departments_members_create) | **POST** /api/core/departments/members/ | 
*CoreApi* | [**core_departments_members_destroy**](docs/CoreApi.md#core_departments_members_destroy) | **DELETE** /api/core/departments/members/ | 
*CoreApi* | [**core_departments_members_retrieve**](docs/CoreApi.md#core_departments_members_retrieve) | **GET** /api/core/departments/members/ | 
*CoreApi* | [**core_departments_retrieve**](docs/CoreApi.md#core_departments_retrieve) | **GET** /api/core/departments/ | 
*CoreApi* | [**core_domains_whitelist_create**](docs/CoreApi.md#core_domains_whitelist_create) | **POST** /api/core/domains/whitelist/ | 
*CoreApi* | [**core_domains_whitelist_retrieve**](docs/CoreApi.md#core_domains_whitelist_retrieve) | **GET** /api/core/domains/whitelist/ | 
*CoreApi* | [**core_heartbeat_celery_beat_retrieve**](docs/CoreApi.md#core_heartbeat_celery_beat_retrieve) | **GET** /api/core/heartbeat/celery-beat/ | 
*CoreApi* | [**core_heartbeat_celery_retrieve**](docs/CoreApi.md#core_heartbeat_celery_retrieve) | **GET** /api/core/heartbeat/celery/ | 
*CoreApi* | [**core_launcher_create**](docs/CoreApi.md#core_launcher_create) | **POST** /api/core/launcher/ | 
*CoreApi* | [**core_launcher_retrieve**](docs/CoreApi.md#core_launcher_retrieve) | **GET** /api/core/launcher/ | 
*CoreApi* | [**core_lti1p3_provider_lti_keys_create**](docs/CoreApi.md#core_lti1p3_provider_lti_keys_create) | **POST** /api/core/lti/1p3/provider/lti-keys/ | 
*CoreApi* | [**core_lti1p3_provider_lti_keys_destroy**](docs/CoreApi.md#core_lti1p3_provider_lti_keys_destroy) | **DELETE** /api/core/lti/1p3/provider/lti-keys/{id}/ | 
*CoreApi* | [**core_lti1p3_provider_lti_keys_list**](docs/CoreApi.md#core_lti1p3_provider_lti_keys_list) | **GET** /api/core/lti/1p3/provider/lti-keys/ | 
*CoreApi* | [**core_lti1p3_provider_lti_keys_retrieve**](docs/CoreApi.md#core_lti1p3_provider_lti_keys_retrieve) | **GET** /api/core/lti/1p3/provider/lti-keys/{id}/ | 
*CoreApi* | [**core_lti1p3_provider_lti_keys_update**](docs/CoreApi.md#core_lti1p3_provider_lti_keys_update) | **PUT** /api/core/lti/1p3/provider/lti-keys/{id}/ | 
*CoreApi* | [**core_lti1p3_provider_lti_mentors_create**](docs/CoreApi.md#core_lti1p3_provider_lti_mentors_create) | **POST** /api/core/lti/1p3/provider/lti-mentors/ | 
*CoreApi* | [**core_lti1p3_provider_lti_mentors_destroy**](docs/CoreApi.md#core_lti1p3_provider_lti_mentors_destroy) | **DELETE** /api/core/lti/1p3/provider/lti-mentors/{id}/ | 
*CoreApi* | [**core_lti1p3_provider_lti_mentors_list**](docs/CoreApi.md#core_lti1p3_provider_lti_mentors_list) | **GET** /api/core/lti/1p3/provider/lti-mentors/ | 
*CoreApi* | [**core_lti1p3_provider_lti_mentors_retrieve**](docs/CoreApi.md#core_lti1p3_provider_lti_mentors_retrieve) | **GET** /api/core/lti/1p3/provider/lti-mentors/{id}/ | 
*CoreApi* | [**core_lti1p3_provider_lti_mentors_update**](docs/CoreApi.md#core_lti1p3_provider_lti_mentors_update) | **PUT** /api/core/lti/1p3/provider/lti-mentors/{id}/ | 
*CoreApi* | [**core_lti1p3_provider_lti_tools_create**](docs/CoreApi.md#core_lti1p3_provider_lti_tools_create) | **POST** /api/core/lti/1p3/provider/lti-tools/ | 
*CoreApi* | [**core_lti1p3_provider_lti_tools_destroy**](docs/CoreApi.md#core_lti1p3_provider_lti_tools_destroy) | **DELETE** /api/core/lti/1p3/provider/lti-tools/{id}/ | 
*CoreApi* | [**core_lti1p3_provider_lti_tools_list**](docs/CoreApi.md#core_lti1p3_provider_lti_tools_list) | **GET** /api/core/lti/1p3/provider/lti-tools/ | 
*CoreApi* | [**core_lti1p3_provider_lti_tools_retrieve**](docs/CoreApi.md#core_lti1p3_provider_lti_tools_retrieve) | **GET** /api/core/lti/1p3/provider/lti-tools/{id}/ | 
*CoreApi* | [**core_lti1p3_provider_lti_tools_update**](docs/CoreApi.md#core_lti1p3_provider_lti_tools_update) | **PUT** /api/core/lti/1p3/provider/lti-tools/{id}/ | 
*CoreApi* | [**core_orgs_dark_mode_logo_create_create**](docs/CoreApi.md#core_orgs_dark_mode_logo_create_create) | **POST** /api/core/orgs/{org}/dark-mode-logo/create/ | 
*CoreApi* | [**core_orgs_dark_mode_logo_retrieve**](docs/CoreApi.md#core_orgs_dark_mode_logo_retrieve) | **GET** /api/core/orgs/{org}/dark-mode-logo/ | 
*CoreApi* | [**core_orgs_favicon_create_create**](docs/CoreApi.md#core_orgs_favicon_create_create) | **POST** /api/core/orgs/{org}/favicon/create/ | 
*CoreApi* | [**core_orgs_favicon_retrieve**](docs/CoreApi.md#core_orgs_favicon_retrieve) | **GET** /api/core/orgs/{org}/favicon/ | 
*CoreApi* | [**core_orgs_logo_create_create**](docs/CoreApi.md#core_orgs_logo_create_create) | **POST** /api/core/orgs/{org}/logo/create/ | 
*CoreApi* | [**core_orgs_logo_retrieve**](docs/CoreApi.md#core_orgs_logo_retrieve) | **GET** /api/core/orgs/{org}/logo/ | 
*CoreApi* | [**core_orgs_metadata_partial_update**](docs/CoreApi.md#core_orgs_metadata_partial_update) | **PATCH** /api/core/orgs/{org}/metadata/ | 
*CoreApi* | [**core_orgs_metadata_retrieve**](docs/CoreApi.md#core_orgs_metadata_retrieve) | **GET** /api/core/orgs/{org}/metadata/ | 
*CoreApi* | [**core_orgs_metadata_update**](docs/CoreApi.md#core_orgs_metadata_update) | **PUT** /api/core/orgs/{org}/metadata/ | 
*CoreApi* | [**core_orgs_redirect_tokens_create**](docs/CoreApi.md#core_orgs_redirect_tokens_create) | **POST** /api/core/orgs/{org}/redirect-tokens/ | 
*CoreApi* | [**core_orgs_redirect_tokens_delete_destroy**](docs/CoreApi.md#core_orgs_redirect_tokens_delete_destroy) | **DELETE** /api/core/orgs/{org}/redirect-tokens/{redirect_token}/delete | 
*CoreApi* | [**core_orgs_redirect_tokens_retrieve**](docs/CoreApi.md#core_orgs_redirect_tokens_retrieve) | **GET** /api/core/orgs/{org}/redirect-tokens/{redirect_token}/ | 
*CoreApi* | [**core_orgs_thumbnail_create_create**](docs/CoreApi.md#core_orgs_thumbnail_create_create) | **POST** /api/core/orgs/{org}/thumbnail/create/ | 
*CoreApi* | [**core_orgs_thumbnail_retrieve**](docs/CoreApi.md#core_orgs_thumbnail_retrieve) | **GET** /api/core/orgs/{org}/thumbnail/ | 
*CoreApi* | [**core_platform_api_tokens_create**](docs/CoreApi.md#core_platform_api_tokens_create) | **POST** /api/core/platform/api-tokens/ | 
*CoreApi* | [**core_platform_api_tokens_destroy**](docs/CoreApi.md#core_platform_api_tokens_destroy) | **DELETE** /api/core/platform/api-tokens/{name} | 
*CoreApi* | [**core_platform_api_tokens_list**](docs/CoreApi.md#core_platform_api_tokens_list) | **GET** /api/core/platform/api-tokens/ | 
*CoreApi* | [**core_platform_config_site_create**](docs/CoreApi.md#core_platform_config_site_create) | **POST** /api/core/platform/config/site/ | 
*CoreApi* | [**core_platform_config_site_retrieve**](docs/CoreApi.md#core_platform_config_site_retrieve) | **GET** /api/core/platform/config/site/ | 
*CoreApi* | [**core_platform_configurations_available_settings_retrieve**](docs/CoreApi.md#core_platform_configurations_available_settings_retrieve) | **GET** /api/core/platform/configurations/available-settings/ | 
*CoreApi* | [**core_platform_configurations_create**](docs/CoreApi.md#core_platform_configurations_create) | **POST** /api/core/platform/configurations/ | Set Platform Configurations
*CoreApi* | [**core_platform_configurations_delete_config_destroy**](docs/CoreApi.md#core_platform_configurations_delete_config_destroy) | **DELETE** /api/core/platform/configurations/delete-config/ | 
*CoreApi* | [**core_platform_configurations_list**](docs/CoreApi.md#core_platform_configurations_list) | **GET** /api/core/platform/configurations/ | List Platform Configurations
*CoreApi* | [**core_platform_configurations_public_retrieve**](docs/CoreApi.md#core_platform_configurations_public_retrieve) | **GET** /api/core/platform/configurations/public/ | 
*CoreApi* | [**core_platform_create**](docs/CoreApi.md#core_platform_create) | **POST** /api/core/platform/ | 
*CoreApi* | [**core_platform_retrieve**](docs/CoreApi.md#core_platform_retrieve) | **GET** /api/core/platform/ | 
*CoreApi* | [**core_platform_users_policies_update**](docs/CoreApi.md#core_platform_users_policies_update) | **PUT** /api/core/platform/users/policies/ | 
*CoreApi* | [**core_platform_users_retrieve**](docs/CoreApi.md#core_platform_users_retrieve) | **GET** /api/core/platform/users/ | 
*CoreApi* | [**core_platforms_public_image_assets_create**](docs/CoreApi.md#core_platforms_public_image_assets_create) | **POST** /api/core/platforms/{platform_key}/public-image-assets/ | 
*CoreApi* | [**core_platforms_public_image_assets_destroy**](docs/CoreApi.md#core_platforms_public_image_assets_destroy) | **DELETE** /api/core/platforms/{platform_key}/public-image-assets/{asset_id}/ | 
*CoreApi* | [**core_platforms_public_image_assets_file_retrieve**](docs/CoreApi.md#core_platforms_public_image_assets_file_retrieve) | **GET** /api/core/platforms/{platform_key}/public-image-assets/{asset_id}/file/ | 
*CoreApi* | [**core_platforms_public_image_assets_list**](docs/CoreApi.md#core_platforms_public_image_assets_list) | **GET** /api/core/platforms/{platform_key}/public-image-assets/ | 
*CoreApi* | [**core_platforms_public_image_assets_partial_update**](docs/CoreApi.md#core_platforms_public_image_assets_partial_update) | **PATCH** /api/core/platforms/{platform_key}/public-image-assets/{asset_id}/ | 
*CoreApi* | [**core_platforms_public_image_assets_retrieve**](docs/CoreApi.md#core_platforms_public_image_assets_retrieve) | **GET** /api/core/platforms/{platform_key}/public-image-assets/{asset_id}/ | 
*CoreApi* | [**core_platforms_public_image_assets_update**](docs/CoreApi.md#core_platforms_public_image_assets_update) | **PUT** /api/core/platforms/{platform_key}/public-image-assets/{asset_id}/ | 
*CoreApi* | [**core_rbac_groups_create**](docs/CoreApi.md#core_rbac_groups_create) | **POST** /api/core/rbac/groups/ | Create RBAC group
*CoreApi* | [**core_rbac_groups_destroy**](docs/CoreApi.md#core_rbac_groups_destroy) | **DELETE** /api/core/rbac/groups/{id}/ | Delete RBAC group
*CoreApi* | [**core_rbac_groups_list**](docs/CoreApi.md#core_rbac_groups_list) | **GET** /api/core/rbac/groups/ | List RBAC groups
*CoreApi* | [**core_rbac_groups_partial_update**](docs/CoreApi.md#core_rbac_groups_partial_update) | **PATCH** /api/core/rbac/groups/{id}/ | Partially update RBAC group
*CoreApi* | [**core_rbac_groups_retrieve**](docs/CoreApi.md#core_rbac_groups_retrieve) | **GET** /api/core/rbac/groups/{id}/ | Retrieve RBAC group
*CoreApi* | [**core_rbac_groups_update**](docs/CoreApi.md#core_rbac_groups_update) | **PUT** /api/core/rbac/groups/{id}/ | Update RBAC group
*CoreApi* | [**core_rbac_mentor_access_create**](docs/CoreApi.md#core_rbac_mentor_access_create) | **POST** /api/core/rbac/mentor-access/ | Control which RbacGroups and/or Users have access to a mentor and with what Role
*CoreApi* | [**core_rbac_mentor_access_list**](docs/CoreApi.md#core_rbac_mentor_access_list) | **GET** /api/core/rbac/mentor-access/ | Get mentor access status
*CoreApi* | [**core_rbac_permissions_check_create**](docs/CoreApi.md#core_rbac_permissions_check_create) | **POST** /api/core/rbac/permissions/check/ | Check user permissions
*CoreApi* | [**core_rbac_policies_create**](docs/CoreApi.md#core_rbac_policies_create) | **POST** /api/core/rbac/policies/ | Create RBAC policy
*CoreApi* | [**core_rbac_policies_destroy**](docs/CoreApi.md#core_rbac_policies_destroy) | **DELETE** /api/core/rbac/policies/{id}/ | Delete RBAC policy
*CoreApi* | [**core_rbac_policies_list**](docs/CoreApi.md#core_rbac_policies_list) | **GET** /api/core/rbac/policies/ | List RBAC policies
*CoreApi* | [**core_rbac_policies_partial_update**](docs/CoreApi.md#core_rbac_policies_partial_update) | **PATCH** /api/core/rbac/policies/{id}/ | Partially update RBAC policy
*CoreApi* | [**core_rbac_policies_retrieve**](docs/CoreApi.md#core_rbac_policies_retrieve) | **GET** /api/core/rbac/policies/{id}/ | Retrieve RBAC policy
*CoreApi* | [**core_rbac_policies_update**](docs/CoreApi.md#core_rbac_policies_update) | **PUT** /api/core/rbac/policies/{id}/ | Update RBAC policy
*CoreApi* | [**core_rbac_roles_create**](docs/CoreApi.md#core_rbac_roles_create) | **POST** /api/core/rbac/roles/ | Create RBAC role
*CoreApi* | [**core_rbac_roles_destroy**](docs/CoreApi.md#core_rbac_roles_destroy) | **DELETE** /api/core/rbac/roles/{id}/ | Delete RBAC role
*CoreApi* | [**core_rbac_roles_list**](docs/CoreApi.md#core_rbac_roles_list) | **GET** /api/core/rbac/roles/ | List RBAC roles
*CoreApi* | [**core_rbac_roles_partial_update**](docs/CoreApi.md#core_rbac_roles_partial_update) | **PATCH** /api/core/rbac/roles/{id}/ | Partially update RBAC role
*CoreApi* | [**core_rbac_roles_retrieve**](docs/CoreApi.md#core_rbac_roles_retrieve) | **GET** /api/core/rbac/roles/{id}/ | Retrieve RBAC role
*CoreApi* | [**core_rbac_roles_update**](docs/CoreApi.md#core_rbac_roles_update) | **PUT** /api/core/rbac/roles/{id}/ | Update RBAC role
*CoreApi* | [**core_rbac_student_llm_access_set_create**](docs/CoreApi.md#core_rbac_student_llm_access_set_create) | **POST** /api/core/rbac/student-llm-access/set/ | Set student LLM access permissions
*CoreApi* | [**core_rbac_student_llm_access_status_retrieve**](docs/CoreApi.md#core_rbac_student_llm_access_status_retrieve) | **GET** /api/core/rbac/student-llm-access/status/ | Get student LLM access permissions
*CoreApi* | [**core_rbac_student_mentor_creation_set_create**](docs/CoreApi.md#core_rbac_student_mentor_creation_set_create) | **POST** /api/core/rbac/student-mentor-creation/set/ | Set student mentor creation permission
*CoreApi* | [**core_rbac_student_mentor_creation_status_retrieve**](docs/CoreApi.md#core_rbac_student_mentor_creation_status_retrieve) | **GET** /api/core/rbac/student-mentor-creation/status/ | Get student mentor creation permission status
*CoreApi* | [**core_rbac_teams_access_create**](docs/CoreApi.md#core_rbac_teams_access_create) | **POST** /api/core/rbac/teams/access/ | Control which RbacGroups and/or Users have access to a UserGroup (team) and with what Role
*CoreApi* | [**core_rbac_teams_access_list**](docs/CoreApi.md#core_rbac_teams_access_list) | **GET** /api/core/rbac/teams/access/ | Get usergroup access status
*CoreApi* | [**core_rbac_user_group_access_create**](docs/CoreApi.md#core_rbac_user_group_access_create) | **POST** /api/core/rbac/user-group-access/ | Manage user access to groups
*CoreApi* | [**core_rbac_user_group_access_retrieve**](docs/CoreApi.md#core_rbac_user_group_access_retrieve) | **GET** /api/core/rbac/user-group-access/ | Get user group access status
*CoreApi* | [**core_session_logout_create**](docs/CoreApi.md#core_session_logout_create) | **POST** /api/core/session/logout/ | 
*CoreApi* | [**core_signals_edx_create**](docs/CoreApi.md#core_signals_edx_create) | **POST** /api/core/signals/edx/ | 
*CoreApi* | [**core_token_proxy_create**](docs/CoreApi.md#core_token_proxy_create) | **POST** /api/core/token/proxy/ | 
*CoreApi* | [**core_token_verify_retrieve**](docs/CoreApi.md#core_token_verify_retrieve) | **GET** /api/core/token/verify/ | 
*CoreApi* | [**core_user_groups_create**](docs/CoreApi.md#core_user_groups_create) | **POST** /api/core/user-groups/ | Create UserGroup
*CoreApi* | [**core_user_groups_create2**](docs/CoreApi.md#core_user_groups_create2) | **POST** /api/core/user_groups/ | 
*CoreApi* | [**core_user_groups_destroy**](docs/CoreApi.md#core_user_groups_destroy) | **DELETE** /api/core/user-groups/{id}/ | Delete UserGroup
*CoreApi* | [**core_user_groups_destroy2**](docs/CoreApi.md#core_user_groups_destroy2) | **DELETE** /api/core/user_groups/ | 
*CoreApi* | [**core_user_groups_link_bulk_create**](docs/CoreApi.md#core_user_groups_link_bulk_create) | **POST** /api/core/user_groups/link/bulk/ | 
*CoreApi* | [**core_user_groups_link_create**](docs/CoreApi.md#core_user_groups_link_create) | **POST** /api/core/user_groups/link/ | 
*CoreApi* | [**core_user_groups_link_destroy**](docs/CoreApi.md#core_user_groups_link_destroy) | **DELETE** /api/core/user_groups/link/ | 
*CoreApi* | [**core_user_groups_link_retrieve**](docs/CoreApi.md#core_user_groups_link_retrieve) | **GET** /api/core/user_groups/link/ | 
*CoreApi* | [**core_user_groups_list**](docs/CoreApi.md#core_user_groups_list) | **GET** /api/core/user-groups/ | List UserGroups
*CoreApi* | [**core_user_groups_partial_update**](docs/CoreApi.md#core_user_groups_partial_update) | **PATCH** /api/core/user-groups/{id}/ | Partially update UserGroup
*CoreApi* | [**core_user_groups_retrieve**](docs/CoreApi.md#core_user_groups_retrieve) | **GET** /api/core/user-groups/{id}/ | Retrieve UserGroup
*CoreApi* | [**core_user_groups_retrieve2**](docs/CoreApi.md#core_user_groups_retrieve2) | **GET** /api/core/user_groups/ | 
*CoreApi* | [**core_user_groups_update**](docs/CoreApi.md#core_user_groups_update) | **PUT** /api/core/user-groups/{id}/ | Update UserGroup
*CoreApi* | [**core_users_delete_create**](docs/CoreApi.md#core_users_delete_create) | **POST** /api/core/users/delete/ | 
*CoreApi* | [**core_users_metadata_proxy_retrieve**](docs/CoreApi.md#core_users_metadata_proxy_retrieve) | **GET** /api/core/users/metadata/proxy/ | 
*CoreApi* | [**core_users_platforms_config_create**](docs/CoreApi.md#core_users_platforms_config_create) | **POST** /api/core/users/platforms/config/ | 
*CoreApi* | [**core_users_platforms_config_retrieve**](docs/CoreApi.md#core_users_platforms_config_retrieve) | **GET** /api/core/users/platforms/config/ | 
*CoreApi* | [**core_users_platforms_create**](docs/CoreApi.md#core_users_platforms_create) | **POST** /api/core/users/platforms/ | 
*CoreApi* | [**core_users_platforms_list**](docs/CoreApi.md#core_users_platforms_list) | **GET** /api/core/users/platforms/ | 
*CoreApi* | [**core_users_platforms_self_link_create**](docs/CoreApi.md#core_users_platforms_self_link_create) | **POST** /api/core/users/platforms/self-link/ | 
*CoreApi* | [**core_users_proxy_bulk_create**](docs/CoreApi.md#core_users_proxy_bulk_create) | **POST** /api/core/users/proxy/bulk/ | 
*CoreApi* | [**core_users_proxy_create**](docs/CoreApi.md#core_users_proxy_create) | **POST** /api/core/users/proxy/ | 
*CoreApi* | [**core_users_proxy_retrieve**](docs/CoreApi.md#core_users_proxy_retrieve) | **GET** /api/core/users/proxy/ | 
*CoreApi* | [**core_users_search_retrieve**](docs/CoreApi.md#core_users_search_retrieve) | **GET** /api/core/users/search/ | 
*CoreApi* | [**departments_orgs_retrieve**](docs/CoreApi.md#departments_orgs_retrieve) | **GET** /api/departments/orgs/{org}/ | 
*CoreApi* | [**roles_platform_orgs_roles_users_desired_roles_retrieve**](docs/CoreApi.md#roles_platform_orgs_roles_users_desired_roles_retrieve) | **GET** /api/roles/platform/orgs/{org}/roles/users/{username}/desired-roles/ | 
*CoreApi* | [**roles_platform_orgs_roles_users_reported_roles_retrieve**](docs/CoreApi.md#roles_platform_orgs_roles_users_reported_roles_retrieve) | **GET** /api/roles/platform/orgs/{org}/roles/users/{username}/reported-roles/ | 
*CoreApi* | [**user_groups_orgs_retrieve**](docs/CoreApi.md#user_groups_orgs_retrieve) | **GET** /api/user-groups/orgs/{key}/ | 
*CredentialsApi* | [**credentials_exim_credentials_course_export_retrieve**](docs/CredentialsApi.md#credentials_exim_credentials_course_export_retrieve) | **GET** /api/credentials/exim/credentials/course/{course_id}/export/ | 
*CredentialsApi* | [**credentials_exim_credentials_course_import_create**](docs/CredentialsApi.md#credentials_exim_credentials_course_import_create) | **POST** /api/credentials/exim/credentials/course/{course_id}/import/ | 
*CredentialsApi* | [**credentials_orgs_users_assertions_bulk_create**](docs/CredentialsApi.md#credentials_orgs_users_assertions_bulk_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/{entity_id}/assertions/bulk/ | 
*CredentialsApi* | [**credentials_orgs_users_assertions_bulk_create2**](docs/CredentialsApi.md#credentials_orgs_users_assertions_bulk_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/{entity_id}/assertions/bulk/ | 
*CredentialsApi* | [**credentials_orgs_users_assertions_create**](docs/CredentialsApi.md#credentials_orgs_users_assertions_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/{entity_id}/assertions/ | 
*CredentialsApi* | [**credentials_orgs_users_assertions_create2**](docs/CredentialsApi.md#credentials_orgs_users_assertions_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/{entity_id}/assertions/ | 
*CredentialsApi* | [**credentials_orgs_users_assertions_over_time_retrieve**](docs/CredentialsApi.md#credentials_orgs_users_assertions_over_time_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/assertions-over-time/ | 
*CredentialsApi* | [**credentials_orgs_users_assertions_over_time_retrieve2**](docs/CredentialsApi.md#credentials_orgs_users_assertions_over_time_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/assertions-over-time/ | 
*CredentialsApi* | [**credentials_orgs_users_assertions_retrieve**](docs/CredentialsApi.md#credentials_orgs_users_assertions_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/assertions/ | 
*CredentialsApi* | [**credentials_orgs_users_assertions_retrieve2**](docs/CredentialsApi.md#credentials_orgs_users_assertions_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/assertions/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_assertions_retrieve3**](docs/CredentialsApi.md#credentials_orgs_users_assertions_retrieve3) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/{entity_id}/assertions/ | 
*CredentialsApi* | [**credentials_orgs_users_assertions_retrieve4**](docs/CredentialsApi.md#credentials_orgs_users_assertions_retrieve4) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/assertions/ | 
*CredentialsApi* | [**credentials_orgs_users_assertions_retrieve5**](docs/CredentialsApi.md#credentials_orgs_users_assertions_retrieve5) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/assertions/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_assertions_retrieve6**](docs/CredentialsApi.md#credentials_orgs_users_assertions_retrieve6) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/{entity_id}/assertions/ | 
*CredentialsApi* | [**credentials_orgs_users_assertions_update**](docs/CredentialsApi.md#credentials_orgs_users_assertions_update) | **PUT** /api/credentials/orgs/{platform_key}/users/{user_id}/assertions/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_assertions_update2**](docs/CredentialsApi.md#credentials_orgs_users_assertions_update2) | **PUT** /api/credentials/orgs/{platform_key}/users/{username}/assertions/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_assignments_destroy**](docs/CredentialsApi.md#credentials_orgs_users_assignments_destroy) | **DELETE** /api/credentials/orgs/{platform_key}/users/{user_id}/assignments/{assignment_id} | 
*CredentialsApi* | [**credentials_orgs_users_assignments_destroy2**](docs/CredentialsApi.md#credentials_orgs_users_assignments_destroy2) | **DELETE** /api/credentials/orgs/{platform_key}/users/{username}/assignments/{assignment_id} | 
*CredentialsApi* | [**credentials_orgs_users_assignments_groups_create**](docs/CredentialsApi.md#credentials_orgs_users_assignments_groups_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/assignments/groups/ | 
*CredentialsApi* | [**credentials_orgs_users_assignments_groups_create2**](docs/CredentialsApi.md#credentials_orgs_users_assignments_groups_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/assignments/groups/ | 
*CredentialsApi* | [**credentials_orgs_users_assignments_groups_retrieve**](docs/CredentialsApi.md#credentials_orgs_users_assignments_groups_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/assignments/groups/ | 
*CredentialsApi* | [**credentials_orgs_users_assignments_groups_retrieve2**](docs/CredentialsApi.md#credentials_orgs_users_assignments_groups_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/assignments/groups/ | 
*CredentialsApi* | [**credentials_orgs_users_assignments_users_create**](docs/CredentialsApi.md#credentials_orgs_users_assignments_users_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/assignments/users/ | 
*CredentialsApi* | [**credentials_orgs_users_assignments_users_create2**](docs/CredentialsApi.md#credentials_orgs_users_assignments_users_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/assignments/users/ | 
*CredentialsApi* | [**credentials_orgs_users_assignments_users_retrieve**](docs/CredentialsApi.md#credentials_orgs_users_assignments_users_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/assignments/users/ | 
*CredentialsApi* | [**credentials_orgs_users_assignments_users_retrieve2**](docs/CredentialsApi.md#credentials_orgs_users_assignments_users_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/assignments/users/ | 
*CredentialsApi* | [**credentials_orgs_users_course_assertions_over_time_retrieve**](docs/CredentialsApi.md#credentials_orgs_users_course_assertions_over_time_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/course-assertions-over-time/ | 
*CredentialsApi* | [**credentials_orgs_users_course_assertions_over_time_retrieve2**](docs/CredentialsApi.md#credentials_orgs_users_course_assertions_over_time_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/course-assertions-over-time/ | 
*CredentialsApi* | [**credentials_orgs_users_course_credentials_list**](docs/CredentialsApi.md#credentials_orgs_users_course_credentials_list) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/course-credentials/ | 
*CredentialsApi* | [**credentials_orgs_users_course_credentials_list2**](docs/CredentialsApi.md#credentials_orgs_users_course_credentials_list2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/course-credentials/ | 
*CredentialsApi* | [**credentials_orgs_users_create**](docs/CredentialsApi.md#credentials_orgs_users_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/ | 
*CredentialsApi* | [**credentials_orgs_users_create2**](docs/CredentialsApi.md#credentials_orgs_users_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/ | 
*CredentialsApi* | [**credentials_orgs_users_credentials_over_time_retrieve**](docs/CredentialsApi.md#credentials_orgs_users_credentials_over_time_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/credentials-over-time/ | 
*CredentialsApi* | [**credentials_orgs_users_credentials_over_time_retrieve2**](docs/CredentialsApi.md#credentials_orgs_users_credentials_over_time_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/credentials-over-time/ | 
*CredentialsApi* | [**credentials_orgs_users_destroy**](docs/CredentialsApi.md#credentials_orgs_users_destroy) | **DELETE** /api/credentials/orgs/{platform_key}/users/{user_id}/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_destroy2**](docs/CredentialsApi.md#credentials_orgs_users_destroy2) | **DELETE** /api/credentials/orgs/{platform_key}/users/{username}/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_external_mapping_create**](docs/CredentialsApi.md#credentials_orgs_users_external_mapping_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/external-mapping/ | 
*CredentialsApi* | [**credentials_orgs_users_external_mapping_create2**](docs/CredentialsApi.md#credentials_orgs_users_external_mapping_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/external-mapping/ | 
*CredentialsApi* | [**credentials_orgs_users_external_mapping_destroy**](docs/CredentialsApi.md#credentials_orgs_users_external_mapping_destroy) | **DELETE** /api/credentials/orgs/{platform_key}/users/{user_id}/external-mapping/ | 
*CredentialsApi* | [**credentials_orgs_users_external_mapping_destroy2**](docs/CredentialsApi.md#credentials_orgs_users_external_mapping_destroy2) | **DELETE** /api/credentials/orgs/{platform_key}/users/{username}/external-mapping/ | 
*CredentialsApi* | [**credentials_orgs_users_external_mapping_retrieve**](docs/CredentialsApi.md#credentials_orgs_users_external_mapping_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/external-mapping/ | 
*CredentialsApi* | [**credentials_orgs_users_external_mapping_retrieve2**](docs/CredentialsApi.md#credentials_orgs_users_external_mapping_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/external-mapping/ | 
*CredentialsApi* | [**credentials_orgs_users_images_create**](docs/CredentialsApi.md#credentials_orgs_users_images_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/images/ | 
*CredentialsApi* | [**credentials_orgs_users_images_create2**](docs/CredentialsApi.md#credentials_orgs_users_images_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/images/ | 
*CredentialsApi* | [**credentials_orgs_users_images_retrieve**](docs/CredentialsApi.md#credentials_orgs_users_images_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/images/ | 
*CredentialsApi* | [**credentials_orgs_users_images_retrieve2**](docs/CredentialsApi.md#credentials_orgs_users_images_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/images/ | 
*CredentialsApi* | [**credentials_orgs_users_issuers_authority_create**](docs/CredentialsApi.md#credentials_orgs_users_issuers_authority_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/issuers/authority/ | 
*CredentialsApi* | [**credentials_orgs_users_issuers_authority_create2**](docs/CredentialsApi.md#credentials_orgs_users_issuers_authority_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/issuers/authority/ | 
*CredentialsApi* | [**credentials_orgs_users_issuers_create**](docs/CredentialsApi.md#credentials_orgs_users_issuers_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/issuers/ | 
*CredentialsApi* | [**credentials_orgs_users_issuers_create2**](docs/CredentialsApi.md#credentials_orgs_users_issuers_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/issuers/ | 
*CredentialsApi* | [**credentials_orgs_users_issuers_destroy**](docs/CredentialsApi.md#credentials_orgs_users_issuers_destroy) | **DELETE** /api/credentials/orgs/{platform_key}/users/{user_id}/issuers/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_issuers_destroy2**](docs/CredentialsApi.md#credentials_orgs_users_issuers_destroy2) | **DELETE** /api/credentials/orgs/{platform_key}/users/{username}/issuers/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_issuers_retrieve**](docs/CredentialsApi.md#credentials_orgs_users_issuers_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/issuers/ | 
*CredentialsApi* | [**credentials_orgs_users_issuers_retrieve2**](docs/CredentialsApi.md#credentials_orgs_users_issuers_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/issuers/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_issuers_retrieve3**](docs/CredentialsApi.md#credentials_orgs_users_issuers_retrieve3) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/issuers/ | 
*CredentialsApi* | [**credentials_orgs_users_issuers_retrieve4**](docs/CredentialsApi.md#credentials_orgs_users_issuers_retrieve4) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/issuers/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_issuers_update**](docs/CredentialsApi.md#credentials_orgs_users_issuers_update) | **PUT** /api/credentials/orgs/{platform_key}/users/{user_id}/issuers/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_issuers_update2**](docs/CredentialsApi.md#credentials_orgs_users_issuers_update2) | **PUT** /api/credentials/orgs/{platform_key}/users/{username}/issuers/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_provider_config_create**](docs/CredentialsApi.md#credentials_orgs_users_provider_config_create) | **POST** /api/credentials/orgs/{platform_key}/users/{user_id}/provider-config/ | 
*CredentialsApi* | [**credentials_orgs_users_provider_config_create2**](docs/CredentialsApi.md#credentials_orgs_users_provider_config_create2) | **POST** /api/credentials/orgs/{platform_key}/users/{username}/provider-config/ | 
*CredentialsApi* | [**credentials_orgs_users_provider_config_destroy**](docs/CredentialsApi.md#credentials_orgs_users_provider_config_destroy) | **DELETE** /api/credentials/orgs/{platform_key}/users/{user_id}/provider-config/ | 
*CredentialsApi* | [**credentials_orgs_users_provider_config_destroy2**](docs/CredentialsApi.md#credentials_orgs_users_provider_config_destroy2) | **DELETE** /api/credentials/orgs/{platform_key}/users/{username}/provider-config/ | 
*CredentialsApi* | [**credentials_orgs_users_provider_config_retrieve**](docs/CredentialsApi.md#credentials_orgs_users_provider_config_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/provider-config/ | 
*CredentialsApi* | [**credentials_orgs_users_provider_config_retrieve2**](docs/CredentialsApi.md#credentials_orgs_users_provider_config_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/provider-config/ | 
*CredentialsApi* | [**credentials_orgs_users_retrieve**](docs/CredentialsApi.md#credentials_orgs_users_retrieve) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/ | 
*CredentialsApi* | [**credentials_orgs_users_retrieve2**](docs/CredentialsApi.md#credentials_orgs_users_retrieve2) | **GET** /api/credentials/orgs/{platform_key}/users/{user_id}/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_retrieve3**](docs/CredentialsApi.md#credentials_orgs_users_retrieve3) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/ | 
*CredentialsApi* | [**credentials_orgs_users_retrieve4**](docs/CredentialsApi.md#credentials_orgs_users_retrieve4) | **GET** /api/credentials/orgs/{platform_key}/users/{username}/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_update**](docs/CredentialsApi.md#credentials_orgs_users_update) | **PUT** /api/credentials/orgs/{platform_key}/users/{user_id}/{entity_id} | 
*CredentialsApi* | [**credentials_orgs_users_update2**](docs/CredentialsApi.md#credentials_orgs_users_update2) | **PUT** /api/credentials/orgs/{platform_key}/users/{username}/{entity_id} | 
*CredentialsApi* | [**credentials_providers_retrieve**](docs/CredentialsApi.md#credentials_providers_retrieve) | **GET** /api/credentials/providers/ | 
*CredentialsApi* | [**credentials_public_assertions_retrieve**](docs/CredentialsApi.md#credentials_public_assertions_retrieve) | **GET** /api/credentials/public/assertions/{entity_id}/ | 
*CreditsApi* | [**credits_sample_action_create**](docs/CreditsApi.md#credits_sample_action_create) | **POST** /credits/sample-action/ | 
*CustomDomainsApi* | [**custom_domains_by_name_status_update**](docs/CustomDomainsApi.md#custom_domains_by_name_status_update) | **PUT** /api/custom-domains/by-name/{domain_name}/status/ | 
*CustomDomainsApi* | [**custom_domains_create_create**](docs/CustomDomainsApi.md#custom_domains_create_create) | **POST** /api/custom-domains/create/ | 
*CustomDomainsApi* | [**custom_domains_delete_destroy**](docs/CustomDomainsApi.md#custom_domains_delete_destroy) | **DELETE** /api/custom-domains/{domain_id}/delete/ | 
*CustomDomainsApi* | [**custom_domains_deleted_status_create**](docs/CustomDomainsApi.md#custom_domains_deleted_status_create) | **POST** /api/custom-domains/{domain_id}/deleted-status/ | 
*CustomDomainsApi* | [**custom_domains_retrieve**](docs/CustomDomainsApi.md#custom_domains_retrieve) | **GET** /api/custom-domains/ | 
*CustomDomainsApi* | [**custom_domains_status_update**](docs/CustomDomainsApi.md#custom_domains_status_update) | **PUT** /api/custom-domains/{domain_id}/status/ | 
*FeaturesApi* | [**features_apps_list**](docs/FeaturesApi.md#features_apps_list) | **GET** /api/features/apps/ | 
*FeaturesApi* | [**features_apps_update_create**](docs/FeaturesApi.md#features_apps_update_create) | **POST** /api/features/apps/update/ | 
*FeaturesApi* | [**features_apps_update_trial_status_create**](docs/FeaturesApi.md#features_apps_update_trial_status_create) | **POST** /api/features/apps/update-trial-status/ | 
*FeaturesApi* | [**features_bulk_config_create**](docs/FeaturesApi.md#features_bulk_config_create) | **POST** /api/features/bulk-config/ | 
*FeaturesApi* | [**features_config_create**](docs/FeaturesApi.md#features_config_create) | **POST** /api/features/config/ | 
*FeaturesApi* | [**features_config_retrieve**](docs/FeaturesApi.md#features_config_retrieve) | **GET** /api/features/config/ | 
*MediaApi* | [**media_orgs_users_media_media_resources_by_item_retrieve**](docs/MediaApi.md#media_orgs_users_media_media_resources_by_item_retrieve) | **GET** /api/media/orgs/{org}/users/{user_id}/media/media-resources/by_item/ | 
*MediaApi* | [**media_orgs_users_media_media_resources_create**](docs/MediaApi.md#media_orgs_users_media_media_resources_create) | **POST** /api/media/orgs/{org}/users/{user_id}/media/media-resources/ | 
*MediaApi* | [**media_orgs_users_media_media_resources_destroy**](docs/MediaApi.md#media_orgs_users_media_media_resources_destroy) | **DELETE** /api/media/orgs/{org}/users/{user_id}/media/media-resources/{id}/ | 
*MediaApi* | [**media_orgs_users_media_media_resources_list**](docs/MediaApi.md#media_orgs_users_media_media_resources_list) | **GET** /api/media/orgs/{org}/users/{user_id}/media/media-resources/ | 
*MediaApi* | [**media_orgs_users_media_media_resources_partial_update**](docs/MediaApi.md#media_orgs_users_media_media_resources_partial_update) | **PATCH** /api/media/orgs/{org}/users/{user_id}/media/media-resources/{id}/ | 
*MediaApi* | [**media_orgs_users_media_media_resources_retrieve**](docs/MediaApi.md#media_orgs_users_media_media_resources_retrieve) | **GET** /api/media/orgs/{org}/users/{user_id}/media/media-resources/{id}/ | 
*MediaApi* | [**media_orgs_users_media_media_resources_search_retrieve**](docs/MediaApi.md#media_orgs_users_media_media_resources_search_retrieve) | **GET** /api/media/orgs/{org}/users/{user_id}/media/media-resources/search/ | 
*MediaApi* | [**media_orgs_users_media_media_resources_update**](docs/MediaApi.md#media_orgs_users_media_media_resources_update) | **PUT** /api/media/orgs/{org}/users/{user_id}/media/media-resources/{id}/ | 
*NotificationsApi* | [**notification_v1_campaigns_unsubscribe_retrieve**](docs/NotificationsApi.md#notification_v1_campaigns_unsubscribe_retrieve) | **GET** /api/notification/v1/campaigns/unsubscribe/{unsubscribe_hash}/ | 
*NotificationsApi* | [**notification_v1_orgs_campaigns_enable_create**](docs/NotificationsApi.md#notification_v1_orgs_campaigns_enable_create) | **POST** /api/notification/v1/orgs/{platform_key}/campaigns/enable/ | 
*NotificationsApi* | [**notification_v1_orgs_campaigns_exclude_create**](docs/NotificationsApi.md#notification_v1_orgs_campaigns_exclude_create) | **POST** /api/notification/v1/orgs/{platform_key}/campaigns/exclude/ | 
*NotificationsApi* | [**notification_v1_orgs_mark_all_as_read_create**](docs/NotificationsApi.md#notification_v1_orgs_mark_all_as_read_create) | **POST** /api/notification/v1/orgs/{platform_key}/mark-all-as-read | 
*NotificationsApi* | [**notification_v1_orgs_notification_builder_context_retrieve**](docs/NotificationsApi.md#notification_v1_orgs_notification_builder_context_retrieve) | **GET** /api/notification/v1/orgs/{platform_key}/notification-builder/context/ | Get notification context data
*NotificationsApi* | [**notification_v1_orgs_notification_builder_preview_create**](docs/NotificationsApi.md#notification_v1_orgs_notification_builder_preview_create) | **POST** /api/notification/v1/orgs/{platform_key}/notification-builder/preview/ | Preview notification
*NotificationsApi* | [**notification_v1_orgs_notification_builder_recipients_list**](docs/NotificationsApi.md#notification_v1_orgs_notification_builder_recipients_list) | **GET** /api/notification/v1/orgs/{platform_key}/notification-builder/{id}/recipients/ | Get build recipients
*NotificationsApi* | [**notification_v1_orgs_notification_builder_send_create**](docs/NotificationsApi.md#notification_v1_orgs_notification_builder_send_create) | **POST** /api/notification/v1/orgs/{platform_key}/notification-builder/send/ | Send notification
*NotificationsApi* | [**notification_v1_orgs_notification_builder_validate_source_create**](docs/NotificationsApi.md#notification_v1_orgs_notification_builder_validate_source_create) | **POST** /api/notification/v1/orgs/{platform_key}/notification-builder/validate_source/ | Validate notification source
*NotificationsApi* | [**notification_v1_orgs_notifications_bulk_update_partial_update**](docs/NotificationsApi.md#notification_v1_orgs_notifications_bulk_update_partial_update) | **PATCH** /api/notification/v1/orgs/{org}/notifications/bulk-update/ | 
*NotificationsApi* | [**notification_v1_orgs_notifications_retrieve**](docs/NotificationsApi.md#notification_v1_orgs_notifications_retrieve) | **GET** /api/notification/v1/orgs/{org}/notifications/ | 
*NotificationsApi* | [**notification_v1_orgs_notifications_update**](docs/NotificationsApi.md#notification_v1_orgs_notifications_update) | **PUT** /api/notification/v1/orgs/{org}/notifications/ | 
*NotificationsApi* | [**notification_v1_orgs_users_notifications_bulk_update_partial_update**](docs/NotificationsApi.md#notification_v1_orgs_users_notifications_bulk_update_partial_update) | **PATCH** /api/notification/v1/orgs/{org}/users/{user_id}/notifications/bulk-update/ | 
*NotificationsApi* | [**notification_v1_orgs_users_notifications_count_retrieve**](docs/NotificationsApi.md#notification_v1_orgs_users_notifications_count_retrieve) | **GET** /api/notification/v1/orgs/{org}/users/{user_id}/notifications-count/ | 
*NotificationsApi* | [**notification_v1_orgs_users_notifications_destroy**](docs/NotificationsApi.md#notification_v1_orgs_users_notifications_destroy) | **DELETE** /api/notification/v1/orgs/{org}/users/{user_id}/notifications/{notification_id}/ | 
*NotificationsApi* | [**notification_v1_orgs_users_notifications_retrieve**](docs/NotificationsApi.md#notification_v1_orgs_users_notifications_retrieve) | **GET** /api/notification/v1/orgs/{org}/users/{user_id}/notifications/ | 
*NotificationsApi* | [**notification_v1_orgs_users_notifications_update**](docs/NotificationsApi.md#notification_v1_orgs_users_notifications_update) | **PUT** /api/notification/v1/orgs/{org}/users/{user_id}/notifications/ | 
*NotificationsApi* | [**notification_v1_platforms_config_test_smtp_create**](docs/NotificationsApi.md#notification_v1_platforms_config_test_smtp_create) | **POST** /api/notification/v1/platforms/{platform_key}/config/test-smtp/ | Test SMTP credentials for a platform
*NotificationsApi* | [**notification_v1_platforms_templates_list**](docs/NotificationsApi.md#notification_v1_platforms_templates_list) | **GET** /api/notification/v1/platforms/{platform_key}/templates/ | List notification templates
*NotificationsApi* | [**notification_v1_platforms_templates_partial_update**](docs/NotificationsApi.md#notification_v1_platforms_templates_partial_update) | **PATCH** /api/notification/v1/platforms/{platform_key}/templates/{notification_type}/ | Update notification template
*NotificationsApi* | [**notification_v1_platforms_templates_reset_create**](docs/NotificationsApi.md#notification_v1_platforms_templates_reset_create) | **POST** /api/notification/v1/platforms/{platform_key}/templates/{notification_type}/reset/ | Reset template to default
*NotificationsApi* | [**notification_v1_platforms_templates_retrieve**](docs/NotificationsApi.md#notification_v1_platforms_templates_retrieve) | **GET** /api/notification/v1/platforms/{platform_key}/templates/{notification_type}/ | Get notification template details
*NotificationsApi* | [**notification_v1_platforms_templates_test_create**](docs/NotificationsApi.md#notification_v1_platforms_templates_test_create) | **POST** /api/notification/v1/platforms/{platform_key}/templates/{notification_type}/test/ | Send test notification
*NotificationsApi* | [**notification_v1_platforms_templates_toggle_partial_update**](docs/NotificationsApi.md#notification_v1_platforms_templates_toggle_partial_update) | **PATCH** /api/notification/v1/platforms/{platform_key}/templates/{notification_type}/toggle/ | Toggle notification preference
*PlatformsApi* | [**platforms_items_access_check_retrieve**](docs/PlatformsApi.md#platforms_items_access_check_retrieve) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/access-check/ | 
*PlatformsApi* | [**platforms_items_checkout_callback_retrieve**](docs/PlatformsApi.md#platforms_items_checkout_callback_retrieve) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/checkout-callback/ | Handle checkout callback
*PlatformsApi* | [**platforms_items_checkout_callback_retrieve2**](docs/PlatformsApi.md#platforms_items_checkout_callback_retrieve2) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/checkout-callback/{checkout_session_id}/ | Handle checkout callback
*PlatformsApi* | [**platforms_items_checkout_create**](docs/PlatformsApi.md#platforms_items_checkout_create) | **POST** /platforms/{platform_key}/items/{item_type}/{item_id}/checkout/ | Create checkout session
*PlatformsApi* | [**platforms_items_checkout_guest_create**](docs/PlatformsApi.md#platforms_items_checkout_guest_create) | **POST** /platforms/{platform_key}/items/{item_type}/{item_id}/checkout-guest/ | Create guest checkout session
*PlatformsApi* | [**platforms_items_paywall_create**](docs/PlatformsApi.md#platforms_items_paywall_create) | **POST** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/ | Create or update paywall configuration
*PlatformsApi* | [**platforms_items_paywall_destroy**](docs/PlatformsApi.md#platforms_items_paywall_destroy) | **DELETE** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/ | Disable paywall configuration
*PlatformsApi* | [**platforms_items_paywall_prices_create**](docs/PlatformsApi.md#platforms_items_paywall_prices_create) | **POST** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/ | Create a price
*PlatformsApi* | [**platforms_items_paywall_prices_destroy**](docs/PlatformsApi.md#platforms_items_paywall_prices_destroy) | **DELETE** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/{price_id}/ | Delete a price
*PlatformsApi* | [**platforms_items_paywall_prices_list**](docs/PlatformsApi.md#platforms_items_paywall_prices_list) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/ | List prices
*PlatformsApi* | [**platforms_items_paywall_prices_retrieve**](docs/PlatformsApi.md#platforms_items_paywall_prices_retrieve) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/{price_id}/ | Get price details
*PlatformsApi* | [**platforms_items_paywall_prices_update**](docs/PlatformsApi.md#platforms_items_paywall_prices_update) | **PUT** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/prices/{price_id}/ | Update a price
*PlatformsApi* | [**platforms_items_paywall_retrieve**](docs/PlatformsApi.md#platforms_items_paywall_retrieve) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/ | Get paywall configuration
*PlatformsApi* | [**platforms_items_paywall_update**](docs/PlatformsApi.md#platforms_items_paywall_update) | **PUT** /platforms/{platform_key}/items/{item_type}/{item_id}/paywall/ | Update paywall configuration
*PlatformsApi* | [**platforms_items_pricing_retrieve**](docs/PlatformsApi.md#platforms_items_pricing_retrieve) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/pricing/ | Get public pricing
*PlatformsApi* | [**platforms_items_subscribers_list**](docs/PlatformsApi.md#platforms_items_subscribers_list) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/subscribers/ | List item subscribers
*PlatformsApi* | [**platforms_items_subscription_cancel_create**](docs/PlatformsApi.md#platforms_items_subscription_cancel_create) | **POST** /platforms/{platform_key}/items/{item_type}/{item_id}/subscription/cancel/ | Cancel subscription
*PlatformsApi* | [**platforms_items_subscription_retrieve**](docs/PlatformsApi.md#platforms_items_subscription_retrieve) | **GET** /platforms/{platform_key}/items/{item_type}/{item_id}/subscription/ | Get user subscription
*PlatformsApi* | [**platforms_my_subscriptions_list**](docs/PlatformsApi.md#platforms_my_subscriptions_list) | **GET** /platforms/{platform_key}/my-subscriptions/ | List user subscriptions
*PlatformsApi* | [**platforms_paywalls_list**](docs/PlatformsApi.md#platforms_paywalls_list) | **GET** /platforms/{platform_key}/paywalls/ | List all platform paywall configurations
*PlatformsApi* | [**platforms_revenue_retrieve**](docs/PlatformsApi.md#platforms_revenue_retrieve) | **GET** /platforms/{platform_key}/revenue/ | Platform sales summary
*PlatformsApi* | [**platforms_subscribers_list**](docs/PlatformsApi.md#platforms_subscribers_list) | **GET** /platforms/{platform_key}/subscribers/ | List all platform subscribers
*RecommendationsApi* | [**recommendations_orgs_users_retrieve**](docs/RecommendationsApi.md#recommendations_orgs_users_retrieve) | **GET** /api/recommendations/orgs/{org}/users/{user_id}/ | 
*ReportsApi* | [**reports_platforms_download_retrieve**](docs/ReportsApi.md#reports_platforms_download_retrieve) | **GET** /api/reports/platforms/{key}/{task_id}/download | Download report
*ReportsApi* | [**reports_platforms_new_create**](docs/ReportsApi.md#reports_platforms_new_create) | **POST** /api/reports/platforms/{key}/new | 
*ReportsApi* | [**reports_platforms_retrieve**](docs/ReportsApi.md#reports_platforms_retrieve) | **GET** /api/reports/platforms/{key}/ | 
*ReportsApi* | [**reports_platforms_retrieve2**](docs/ReportsApi.md#reports_platforms_retrieve2) | **GET** /api/reports/platforms/{key}/{report_name} | 
*ScimApi* | [**add_group_members**](docs/ScimApi.md#add_group_members) | **POST** /api/orgs/{platform_key}/scim/v2/Groups/{id}/add_members | Add members to an existing RBAC group
*ScimApi* | [**create_user**](docs/ScimApi.md#create_user) | **POST** /api/orgs/{platform_key}/scim/v2/Users | Create a new user in the system
*ScimApi* | [**delete_group**](docs/ScimApi.md#delete_group) | **DELETE** /api/orgs/{platform_key}/scim/v2/Groups/{id} | Delete an existing RBAC group
*ScimApi* | [**delete_group2**](docs/ScimApi.md#delete_group2) | **DELETE** /api/orgs/{platform_key}/scim/v2/Groups/{id}/ | Delete an existing RBAC group
*ScimApi* | [**delete_user**](docs/ScimApi.md#delete_user) | **DELETE** /api/orgs/{platform_key}/scim/v2/Users/{id} | Delete a user (not supported)
*ScimApi* | [**delete_user2**](docs/ScimApi.md#delete_user2) | **DELETE** /api/orgs/{platform_key}/scim/v2/Users/{id}/ | Delete a user (not supported)
*ScimApi* | [**list_groups**](docs/ScimApi.md#list_groups) | **GET** /api/orgs/{platform_key}/scim/v2/Groups | List existing RBAC groups
*ScimApi* | [**list_users**](docs/ScimApi.md#list_users) | **GET** /api/orgs/{platform_key}/scim/v2/Users | List users in the system
*ScimApi* | [**manage_group**](docs/ScimApi.md#manage_group) | **POST** /api/orgs/{platform_key}/scim/v2/Groups | Manage existing user group
*ScimApi* | [**partial_update_group**](docs/ScimApi.md#partial_update_group) | **PATCH** /api/orgs/{platform_key}/scim/v2/Groups/{id} | Partially update an existing RBAC group
*ScimApi* | [**partial_update_group2**](docs/ScimApi.md#partial_update_group2) | **PATCH** /api/orgs/{platform_key}/scim/v2/Groups/{id}/ | Partially update an existing RBAC group
*ScimApi* | [**partial_update_user**](docs/ScimApi.md#partial_update_user) | **PATCH** /api/orgs/{platform_key}/scim/v2/Users/{id} | Partially update an existing user
*ScimApi* | [**partial_update_user2**](docs/ScimApi.md#partial_update_user2) | **PATCH** /api/orgs/{platform_key}/scim/v2/Users/{id}/ | Partially update an existing user
*ScimApi* | [**remove_group_members**](docs/ScimApi.md#remove_group_members) | **POST** /api/orgs/{platform_key}/scim/v2/Groups/{id}/remove_members | Remove members from an existing RBAC group
*ScimApi* | [**retrieve_group**](docs/ScimApi.md#retrieve_group) | **GET** /api/orgs/{platform_key}/scim/v2/Groups/{id} | Get details of a specific RBAC group
*ScimApi* | [**retrieve_group2**](docs/ScimApi.md#retrieve_group2) | **GET** /api/orgs/{platform_key}/scim/v2/Groups/{id}/ | Get details of a specific RBAC group
*ScimApi* | [**retrieve_user**](docs/ScimApi.md#retrieve_user) | **GET** /api/orgs/{platform_key}/scim/v2/Users/{id} | Get details of a specific user
*ScimApi* | [**retrieve_user2**](docs/ScimApi.md#retrieve_user2) | **GET** /api/orgs/{platform_key}/scim/v2/Users/{id}/ | Get details of a specific user
*ScimApi* | [**update_group**](docs/ScimApi.md#update_group) | **PUT** /api/orgs/{platform_key}/scim/v2/Groups/{id} | Update an existing RBAC group
*ScimApi* | [**update_group2**](docs/ScimApi.md#update_group2) | **PUT** /api/orgs/{platform_key}/scim/v2/Groups/{id}/ | Update an existing RBAC group
*ScimApi* | [**update_user**](docs/ScimApi.md#update_user) | **PUT** /api/orgs/{platform_key}/scim/v2/Users/{id} | Update a user
*ScimApi* | [**update_user2**](docs/ScimApi.md#update_user2) | **PUT** /api/orgs/{platform_key}/scim/v2/Users/{id}/ | Update a user
*SearchApi* | [**search_ai_search_retrieve**](docs/SearchApi.md#search_ai_search_retrieve) | **GET** /api/search/ai-search/ | 
*SearchApi* | [**search_catalog_retrieve**](docs/SearchApi.md#search_catalog_retrieve) | **GET** /api/search/catalog/ | 
*SearchApi* | [**search_mentors_documents_retrieve**](docs/SearchApi.md#search_mentors_documents_retrieve) | **GET** /api/search/mentors/{mentor_unique_id}/documents/ | 
*SearchApi* | [**search_mentors_retrieve**](docs/SearchApi.md#search_mentors_retrieve) | **GET** /api/search/mentors/ | 
*SearchApi* | [**search_orgs_users_mentors_retrieve**](docs/SearchApi.md#search_orgs_users_mentors_retrieve) | **GET** /api/search/orgs/{org}/users/{username}/mentors/ | 
*SearchApi* | [**search_orgs_users_prompts_retrieve**](docs/SearchApi.md#search_orgs_users_prompts_retrieve) | **GET** /api/search/orgs/{org}/users/{username}/prompts/ | 
*SearchApi* | [**search_orgs_users_recommended_retrieve**](docs/SearchApi.md#search_orgs_users_recommended_retrieve) | **GET** /api/search/orgs/{org}/users/{username}/recommended/ | 
*SearchApi* | [**search_personalized_catalog_retrieve**](docs/SearchApi.md#search_personalized_catalog_retrieve) | **GET** /api/search/personalized-catalog/{username}/ | 
*SearchApi* | [**search_prompts_retrieve**](docs/SearchApi.md#search_prompts_retrieve) | **GET** /api/search/prompts/ | 
*SearchApi* | [**search_users_orgs_users_retrieve**](docs/SearchApi.md#search_users_orgs_users_retrieve) | **GET** /api/search/users/orgs/{org}/users/{username}/ | 
*SkillsApi* | [**skills_orgs_skills_list**](docs/SkillsApi.md#skills_orgs_skills_list) | **GET** /api/skills/orgs/{org}/skills | 
*SkillsApi* | [**skills_orgs_skills_percentile_list**](docs/SkillsApi.md#skills_orgs_skills_percentile_list) | **GET** /api/skills/orgs/{org}/skills/percentile/ | 
*SkillsApi* | [**skills_orgs_skills_percentile_retrieve**](docs/SkillsApi.md#skills_orgs_skills_percentile_retrieve) | **GET** /api/skills/orgs/{org}/skills/{skill_id}/percentile/ | 
*SkillsApi* | [**skills_orgs_skills_retrieve**](docs/SkillsApi.md#skills_orgs_skills_retrieve) | **GET** /api/skills/orgs/{org}/skills/{skill_name}/ | 
*SkillsApi* | [**skills_orgs_skills_thresholds_create**](docs/SkillsApi.md#skills_orgs_skills_thresholds_create) | **POST** /api/skills/orgs/{org}/skills/thresholds/ | 
*SkillsApi* | [**skills_orgs_skills_thresholds_destroy**](docs/SkillsApi.md#skills_orgs_skills_thresholds_destroy) | **DELETE** /api/skills/orgs/{org}/skills/thresholds/ | 
*SkillsApi* | [**skills_orgs_skills_thresholds_partial_update**](docs/SkillsApi.md#skills_orgs_skills_thresholds_partial_update) | **PATCH** /api/skills/orgs/{org}/skills/thresholds/ | 
*SkillsApi* | [**skills_orgs_skills_thresholds_retrieve**](docs/SkillsApi.md#skills_orgs_skills_thresholds_retrieve) | **GET** /api/skills/orgs/{org}/skills/thresholds/ | 
*SkillsApi* | [**skills_orgs_skills_users_desired_skills_retrieve**](docs/SkillsApi.md#skills_orgs_skills_users_desired_skills_retrieve) | **GET** /api/skills/orgs/{org}/skills/users/{user_id}/desired-skills/ | 
*SkillsApi* | [**skills_orgs_skills_users_point_percentile_retrieve**](docs/SkillsApi.md#skills_orgs_skills_users_point_percentile_retrieve) | **GET** /api/skills/orgs/{org}/skills/users/{user_id}/point-percentile/ | 
*SkillsApi* | [**skills_orgs_skills_users_reported_skills_retrieve**](docs/SkillsApi.md#skills_orgs_skills_users_reported_skills_retrieve) | **GET** /api/skills/orgs/{org}/skills/users/{user_id}/reported-skills/ | 
*SkillsApi* | [**skills_orgs_skills_users_retrieve**](docs/SkillsApi.md#skills_orgs_skills_users_retrieve) | **GET** /api/skills/orgs/{org}/skills/users/{user_id}/ | 
*TransactionsApi* | [**transactions_retrieve**](docs/TransactionsApi.md#transactions_retrieve) | **GET** /transactions/ | List transaction history

