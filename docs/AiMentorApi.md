# iblai.AiMentorApi

All URIs are relative to *https://base.manager.iblai.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_mentor_orgs_all_triggers_retrieve**](AiMentorApi.md#ai_mentor_orgs_all_triggers_retrieve) | **GET** /api/ai-mentor/orgs/{org}/all-triggers/ | 
[**ai_mentor_orgs_mentors_email_inbox_list**](AiMentorApi.md#ai_mentor_orgs_mentors_email_inbox_list) | **GET** /api/ai-mentor/orgs/{org}/mentors/{mentor}/email-inbox/ | 
[**ai_mentor_orgs_mentors_email_inbox_retrieve**](AiMentorApi.md#ai_mentor_orgs_mentors_email_inbox_retrieve) | **GET** /api/ai-mentor/orgs/{org}/mentors/{mentor}/email-inbox/{email_prompt_id}/ | 
[**ai_mentor_orgs_mentors_email_inbox_summary_retrieve**](AiMentorApi.md#ai_mentor_orgs_mentors_email_inbox_summary_retrieve) | **GET** /api/ai-mentor/orgs/{org}/mentors/{mentor}/email-inbox-summary/ | 
[**ai_mentor_orgs_mentors_link_course_create**](AiMentorApi.md#ai_mentor_orgs_mentors_link_course_create) | **POST** /api/ai-mentor/orgs/{org}/mentors/{mentor}/link-course/ | 
[**ai_mentor_orgs_mentors_link_course_retrieve**](AiMentorApi.md#ai_mentor_orgs_mentors_link_course_retrieve) | **GET** /api/ai-mentor/orgs/{org}/mentors/{mentor}/link-course/ | 
[**ai_mentor_orgs_metadata_create**](AiMentorApi.md#ai_mentor_orgs_metadata_create) | **POST** /api/ai-mentor/orgs/{org}/metadata/ | 
[**ai_mentor_orgs_quiz_customizer_create**](AiMentorApi.md#ai_mentor_orgs_quiz_customizer_create) | **POST** /api/ai-mentor/orgs/{org}/quiz-customizer/ | 
[**ai_mentor_orgs_quiz_customizer_retrieve**](AiMentorApi.md#ai_mentor_orgs_quiz_customizer_retrieve) | **GET** /api/ai-mentor/orgs/{org}/quiz-customizer/ | 
[**ai_mentor_orgs_sessions_create**](AiMentorApi.md#ai_mentor_orgs_sessions_create) | **POST** /api/ai-mentor/orgs/{org}/sessions/ | 
[**ai_mentor_orgs_trigger_create**](AiMentorApi.md#ai_mentor_orgs_trigger_create) | **POST** /api/ai-mentor/orgs/{org}/trigger/ | 
[**ai_mentor_orgs_trigger_deletion_create**](AiMentorApi.md#ai_mentor_orgs_trigger_deletion_create) | **POST** /api/ai-mentor/orgs/{org}/trigger/{slug}/deletion/ | 
[**ai_mentor_orgs_trigger_retrieve**](AiMentorApi.md#ai_mentor_orgs_trigger_retrieve) | **GET** /api/ai-mentor/orgs/{org}/trigger/{slug}/ | 
[**ai_mentor_orgs_trigger_templates_retrieve**](AiMentorApi.md#ai_mentor_orgs_trigger_templates_retrieve) | **GET** /api/ai-mentor/orgs/{org}/trigger-templates/ | 
[**ai_mentor_orgs_users_ai_generated_images_destroy**](AiMentorApi.md#ai_mentor_orgs_users_ai_generated_images_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-generated-images/{id}/ | 
[**ai_mentor_orgs_users_ai_generated_images_list**](AiMentorApi.md#ai_mentor_orgs_users_ai_generated_images_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-generated-images/ | 
[**ai_mentor_orgs_users_ai_generated_images_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_ai_generated_images_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-generated-images/{id}/ | 
[**ai_mentor_orgs_users_ai_user_profile_memory_create**](AiMentorApi.md#ai_mentor_orgs_users_ai_user_profile_memory_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-user-profile-memory/ | 
[**ai_mentor_orgs_users_ai_user_profile_memory_destroy**](AiMentorApi.md#ai_mentor_orgs_users_ai_user_profile_memory_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-user-profile-memory/{tag}/ | 
[**ai_mentor_orgs_users_ai_user_profile_memory_list**](AiMentorApi.md#ai_mentor_orgs_users_ai_user_profile_memory_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/ai-user-profile-memory/ | 
[**ai_mentor_orgs_users_assumed_knowledge_create**](AiMentorApi.md#ai_mentor_orgs_users_assumed_knowledge_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/assumed-knowledge/ | 
[**ai_mentor_orgs_users_assumed_knowledge_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_assumed_knowledge_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/assumed-knowledge/ | 
[**ai_mentor_orgs_users_audio_to_text_create**](AiMentorApi.md#ai_mentor_orgs_users_audio_to_text_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/audio-to-text/ | 
[**ai_mentor_orgs_users_available_template_mentors_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_available_template_mentors_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/available-template-mentors/ | 
[**ai_mentor_orgs_users_call_configurations_create**](AiMentorApi.md#ai_mentor_orgs_users_call_configurations_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/call-configurations/ | 
[**ai_mentor_orgs_users_call_configurations_list**](AiMentorApi.md#ai_mentor_orgs_users_call_configurations_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/call-configurations/ | 
[**ai_mentor_orgs_users_call_configurations_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_call_configurations_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/call-configurations/{id}/ | 
[**ai_mentor_orgs_users_call_configurations_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_call_configurations_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/call-configurations/{id}/ | 
[**ai_mentor_orgs_users_call_configurations_update**](AiMentorApi.md#ai_mentor_orgs_users_call_configurations_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/call-configurations/{id}/ | 
[**ai_mentor_orgs_users_category_groups_create**](AiMentorApi.md#ai_mentor_orgs_users_category_groups_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/category-groups/ | 
[**ai_mentor_orgs_users_category_groups_destroy**](AiMentorApi.md#ai_mentor_orgs_users_category_groups_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/category-groups/{id}/ | 
[**ai_mentor_orgs_users_category_groups_list**](AiMentorApi.md#ai_mentor_orgs_users_category_groups_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/category-groups/ | 
[**ai_mentor_orgs_users_category_groups_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_category_groups_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/category-groups/{id}/ | 
[**ai_mentor_orgs_users_category_groups_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_category_groups_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/category-groups/{id}/ | 
[**ai_mentor_orgs_users_category_groups_update**](AiMentorApi.md#ai_mentor_orgs_users_category_groups_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/category-groups/{id}/ | 
[**ai_mentor_orgs_users_clean_vector_results_create**](AiMentorApi.md#ai_mentor_orgs_users_clean_vector_results_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/clean-vector-results/{session_id}/ | 
[**ai_mentor_orgs_users_clean_vector_results_list**](AiMentorApi.md#ai_mentor_orgs_users_clean_vector_results_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/clean-vector-results/{session_id}/ | 
[**ai_mentor_orgs_users_clear_chathistory_destroy**](AiMentorApi.md#ai_mentor_orgs_users_clear_chathistory_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/clear-chathistory | Delete User Chat History
[**ai_mentor_orgs_users_course_creation_component_create**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_component_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/component/ | 
[**ai_mentor_orgs_users_course_creation_component_destroy**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_component_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/component/{id}/ | 
[**ai_mentor_orgs_users_course_creation_component_draft_content_create**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_component_draft_content_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/component/{id}/draft-content/ | 
[**ai_mentor_orgs_users_course_creation_component_draft_content_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_component_draft_content_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/component/{id}/draft-content/ | 
[**ai_mentor_orgs_users_course_creation_component_list**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_component_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/component/ | 
[**ai_mentor_orgs_users_course_creation_component_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_component_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/component/{id}/ | 
[**ai_mentor_orgs_users_course_creation_component_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_component_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/component/{id}/ | 
[**ai_mentor_orgs_users_course_creation_component_update**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_component_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/component/{id}/ | 
[**ai_mentor_orgs_users_course_creation_course_destroy**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/ | 
[**ai_mentor_orgs_users_course_creation_course_draft_content_for_all_units_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_draft_content_for_all_units_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/draft-content-for-all-units/ | 
[**ai_mentor_orgs_users_course_creation_course_full_structure_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_full_structure_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/full-structure/ | 
[**ai_mentor_orgs_users_course_creation_course_list**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/ | 
[**ai_mentor_orgs_users_course_creation_course_load_from_edx_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_load_from_edx_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/load-from-edx/ | 
[**ai_mentor_orgs_users_course_creation_course_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/ | 
[**ai_mentor_orgs_users_course_creation_course_sync_to_edx_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_course_sync_to_edx_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/sync-to-edx/ | 
[**ai_mentor_orgs_users_course_creation_files_create**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_files_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/files/ | 
[**ai_mentor_orgs_users_course_creation_files_destroy**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_files_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/files/{id}/ | 
[**ai_mentor_orgs_users_course_creation_files_list**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_files_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/files/ | 
[**ai_mentor_orgs_users_course_creation_files_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_files_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/files/{id}/ | 
[**ai_mentor_orgs_users_course_creation_files_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_files_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/files/{id}/ | 
[**ai_mentor_orgs_users_course_creation_files_update**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_files_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/files/{id}/ | 
[**ai_mentor_orgs_users_course_creation_section_create**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_section_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/section/ | 
[**ai_mentor_orgs_users_course_creation_section_destroy**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_section_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/section/{id}/ | 
[**ai_mentor_orgs_users_course_creation_section_list**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_section_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/section/ | 
[**ai_mentor_orgs_users_course_creation_section_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_section_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/section/{id}/ | 
[**ai_mentor_orgs_users_course_creation_section_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_section_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/section/{id}/ | 
[**ai_mentor_orgs_users_course_creation_section_update**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_section_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/section/{id}/ | 
[**ai_mentor_orgs_users_course_creation_subsection_create**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_subsection_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/subsection/ | 
[**ai_mentor_orgs_users_course_creation_subsection_destroy**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_subsection_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/subsection/{id}/ | 
[**ai_mentor_orgs_users_course_creation_subsection_list**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_subsection_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/subsection/ | 
[**ai_mentor_orgs_users_course_creation_subsection_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_subsection_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/subsection/{id}/ | 
[**ai_mentor_orgs_users_course_creation_subsection_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_subsection_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/subsection/{id}/ | 
[**ai_mentor_orgs_users_course_creation_subsection_update**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_subsection_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/subsection/{id}/ | 
[**ai_mentor_orgs_users_course_creation_task_files_create**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_task_files_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-task-files/ | 
[**ai_mentor_orgs_users_course_creation_task_files_destroy**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_task_files_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-task-files/{id}/ | 
[**ai_mentor_orgs_users_course_creation_task_files_list**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_task_files_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-task-files/ | 
[**ai_mentor_orgs_users_course_creation_task_files_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_task_files_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-task-files/{id}/ | 
[**ai_mentor_orgs_users_course_creation_task_files_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_task_files_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-task-files/{id}/ | 
[**ai_mentor_orgs_users_course_creation_task_files_update**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_task_files_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-task-files/{id}/ | 
[**ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/{id}/cancel/ | 
[**ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve2**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve2) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/{id}/cancel/ | 
[**ai_mentor_orgs_users_course_creation_tasks_create**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/ | 
[**ai_mentor_orgs_users_course_creation_tasks_create2**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create2) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/ | 
[**ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/{id}/create-course-outline/ | 
[**ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create2**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create2) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/{id}/create-course-outline/ | 
[**ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/{id}/create-course-outline/ | 
[**ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve2**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve2) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/{id}/create-course-outline/ | 
[**ai_mentor_orgs_users_course_creation_tasks_destroy**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/{id}/ | 
[**ai_mentor_orgs_users_course_creation_tasks_destroy2**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_destroy2) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/{id}/ | 
[**ai_mentor_orgs_users_course_creation_tasks_list**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/ | 
[**ai_mentor_orgs_users_course_creation_tasks_list2**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_list2) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/ | 
[**ai_mentor_orgs_users_course_creation_tasks_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/{id}/ | 
[**ai_mentor_orgs_users_course_creation_tasks_retrieve2**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_retrieve2) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/{id}/ | 
[**ai_mentor_orgs_users_course_creation_tasks_start_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_start_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation-tasks/{id}/start/ | 
[**ai_mentor_orgs_users_course_creation_tasks_start_retrieve2**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_tasks_start_retrieve2) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/tasks/{id}/start/ | 
[**ai_mentor_orgs_users_course_creation_unit_create**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_unit_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/unit/ | 
[**ai_mentor_orgs_users_course_creation_unit_destroy**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_unit_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/unit/{id}/ | 
[**ai_mentor_orgs_users_course_creation_unit_draft_content_create**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_unit_draft_content_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/unit/{id}/draft-content/ | 
[**ai_mentor_orgs_users_course_creation_unit_draft_content_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_unit_draft_content_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/unit/{id}/draft-content/ | 
[**ai_mentor_orgs_users_course_creation_unit_list**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_unit_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/unit/ | 
[**ai_mentor_orgs_users_course_creation_unit_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_unit_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/unit/{id}/ | 
[**ai_mentor_orgs_users_course_creation_unit_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_unit_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/unit/{id}/ | 
[**ai_mentor_orgs_users_course_creation_unit_update**](AiMentorApi.md#ai_mentor_orgs_users_course_creation_unit_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/unit/{id}/ | 
[**ai_mentor_orgs_users_create**](AiMentorApi.md#ai_mentor_orgs_users_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/ | 
[**ai_mentor_orgs_users_create_mentor_wizard_create**](AiMentorApi.md#ai_mentor_orgs_users_create_mentor_wizard_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/create-mentor-wizard/ | 
[**ai_mentor_orgs_users_custom_instruction_create**](AiMentorApi.md#ai_mentor_orgs_users_custom_instruction_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/custom-instruction/ | 
[**ai_mentor_orgs_users_custom_instruction_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_custom_instruction_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/custom-instruction/ | 
[**ai_mentor_orgs_users_custom_instruction_update**](AiMentorApi.md#ai_mentor_orgs_users_custom_instruction_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/custom-instruction/ | 
[**ai_mentor_orgs_users_destroy**](AiMentorApi.md#ai_mentor_orgs_users_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/{name}/ | 
[**ai_mentor_orgs_users_downloads_tasks_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_downloads_tasks_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/downloads/tasks/{task_id}/ | 
[**ai_mentor_orgs_users_edx_memory_destroy**](AiMentorApi.md#ai_mentor_orgs_users_edx_memory_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/edx-memory/{id}/ | 
[**ai_mentor_orgs_users_edx_memory_list**](AiMentorApi.md#ai_mentor_orgs_users_edx_memory_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/edx-memory/ | 
[**ai_mentor_orgs_users_edx_memory_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_edx_memory_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/edx-memory/{id}/ | 
[**ai_mentor_orgs_users_elevenlabs_voice_create**](AiMentorApi.md#ai_mentor_orgs_users_elevenlabs_voice_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/elevenlabs-voice/ | 
[**ai_mentor_orgs_users_elevenlabs_voice_destroy**](AiMentorApi.md#ai_mentor_orgs_users_elevenlabs_voice_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/elevenlabs-voice/{voice_name}/ | 
[**ai_mentor_orgs_users_elevenlabs_voice_list**](AiMentorApi.md#ai_mentor_orgs_users_elevenlabs_voice_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/elevenlabs-voice/ | 
[**ai_mentor_orgs_users_export_chathistory_create**](AiMentorApi.md#ai_mentor_orgs_users_export_chathistory_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/export-chathistory/ | 
[**ai_mentor_orgs_users_free_usage_count_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_free_usage_count_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/free-usage-count | 
[**ai_mentor_orgs_users_list**](AiMentorApi.md#ai_mentor_orgs_users_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/ | 
[**ai_mentor_orgs_users_mcp_servers_create**](AiMentorApi.md#ai_mentor_orgs_users_mcp_servers_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-servers/ | 
[**ai_mentor_orgs_users_mcp_servers_destroy**](AiMentorApi.md#ai_mentor_orgs_users_mcp_servers_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-servers/{id}/ | 
[**ai_mentor_orgs_users_mcp_servers_list**](AiMentorApi.md#ai_mentor_orgs_users_mcp_servers_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-servers/ | 
[**ai_mentor_orgs_users_mcp_servers_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_mcp_servers_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-servers/{id}/ | 
[**ai_mentor_orgs_users_mcp_servers_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mcp_servers_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-servers/{id}/ | 
[**ai_mentor_orgs_users_mcp_servers_update**](AiMentorApi.md#ai_mentor_orgs_users_mcp_servers_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mcp-servers/{id}/ | 
[**ai_mentor_orgs_users_mentor_audience_create**](AiMentorApi.md#ai_mentor_orgs_users_mentor_audience_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/audience/ | 
[**ai_mentor_orgs_users_mentor_audience_destroy**](AiMentorApi.md#ai_mentor_orgs_users_mentor_audience_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/audience/ | 
[**ai_mentor_orgs_users_mentor_audience_list**](AiMentorApi.md#ai_mentor_orgs_users_mentor_audience_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/audience/ | 
[**ai_mentor_orgs_users_mentor_categories_create**](AiMentorApi.md#ai_mentor_orgs_users_mentor_categories_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/categories/ | 
[**ai_mentor_orgs_users_mentor_categories_destroy**](AiMentorApi.md#ai_mentor_orgs_users_mentor_categories_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/categories/ | 
[**ai_mentor_orgs_users_mentor_categories_list**](AiMentorApi.md#ai_mentor_orgs_users_mentor_categories_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/categories/ | 
[**ai_mentor_orgs_users_mentor_feedback_create_create**](AiMentorApi.md#ai_mentor_orgs_users_mentor_feedback_create_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-feedback/create/ | 
[**ai_mentor_orgs_users_mentor_feedback_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentor_feedback_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-feedback/{feedback_id}/ | 
[**ai_mentor_orgs_users_mentor_feedback_update**](AiMentorApi.md#ai_mentor_orgs_users_mentor_feedback_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-feedback/{feedback_id}/ | 
[**ai_mentor_orgs_users_mentor_from_template_create**](AiMentorApi.md#ai_mentor_orgs_users_mentor_from_template_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-from-template/ | 
[**ai_mentor_orgs_users_mentor_llms_list**](AiMentorApi.md#ai_mentor_orgs_users_mentor_llms_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-llms/ | 
[**ai_mentor_orgs_users_mentor_seed_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentor_seed_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor/seed/ | 
[**ai_mentor_orgs_users_mentor_tools_list**](AiMentorApi.md#ai_mentor_orgs_users_mentor_tools_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-tools/ | 
[**ai_mentor_orgs_users_mentor_with_settings_create**](AiMentorApi.md#ai_mentor_orgs_users_mentor_with_settings_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentor-with-settings/ | 
[**ai_mentor_orgs_users_mentors_available_tools_list**](AiMentorApi.md#ai_mentor_orgs_users_mentors_available_tools_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/available-tools/ | 
[**ai_mentor_orgs_users_mentors_create_call_credentials_create**](AiMentorApi.md#ai_mentor_orgs_users_mentors_create_call_credentials_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/create-call-credentials/ | 
[**ai_mentor_orgs_users_mentors_current_memory_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_current_memory_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/current-memory/ | 
[**ai_mentor_orgs_users_mentors_current_memory_update**](AiMentorApi.md#ai_mentor_orgs_users_mentors_current_memory_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/current-memory/ | 
[**ai_mentor_orgs_users_mentors_custom_voice_create**](AiMentorApi.md#ai_mentor_orgs_users_mentors_custom_voice_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/custom-voice/ | 
[**ai_mentor_orgs_users_mentors_custom_voice_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_custom_voice_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/custom-voice/ | 
[**ai_mentor_orgs_users_mentors_custom_voice_tts_create**](AiMentorApi.md#ai_mentor_orgs_users_mentors_custom_voice_tts_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/custom-voice-tts/ | 
[**ai_mentor_orgs_users_mentors_edit_scenarios_update**](AiMentorApi.md#ai_mentor_orgs_users_mentors_edit_scenarios_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/edit-scenarios/ | 
[**ai_mentor_orgs_users_mentors_fork_create**](AiMentorApi.md#ai_mentor_orgs_users_mentors_fork_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/fork/ | 
[**ai_mentor_orgs_users_mentors_historical_memory_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_historical_memory_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/historical-memory/ | 
[**ai_mentor_orgs_users_mentors_memory_progress_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_memory_progress_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/memory-progress/ | 
[**ai_mentor_orgs_users_mentors_memory_settings_create**](AiMentorApi.md#ai_mentor_orgs_users_mentors_memory_settings_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/memory-settings/ | 
[**ai_mentor_orgs_users_mentors_memory_settings_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_memory_settings_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/memory-settings/ | 
[**ai_mentor_orgs_users_mentors_mentor_eval_create**](AiMentorApi.md#ai_mentor_orgs_users_mentors_mentor_eval_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/mentor-eval/ | 
[**ai_mentor_orgs_users_mentors_mentor_eval_execution_create**](AiMentorApi.md#ai_mentor_orgs_users_mentors_mentor_eval_execution_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/mentor-eval-execution/ | 
[**ai_mentor_orgs_users_mentors_mentor_eval_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_mentor_eval_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/mentor-eval/ | 
[**ai_mentor_orgs_users_mentors_public_settings_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_public_settings_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/public-settings/ | 
[**ai_mentor_orgs_users_mentors_reports_mentor_eval_report_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_reports_mentor_eval_report_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/reports/{report_id}/mentor-eval-report/ | 
[**ai_mentor_orgs_users_mentors_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/ | 
[**ai_mentor_orgs_users_mentors_scenarios_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_scenarios_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/scenarios/ | 
[**ai_mentor_orgs_users_mentors_settings_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_settings_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/settings/ | Retrieve Mentor Settings
[**ai_mentor_orgs_users_mentors_settings_update**](AiMentorApi.md#ai_mentor_orgs_users_mentors_settings_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/settings/ | Update Mentor Settings
[**ai_mentor_orgs_users_mentors_spaced_repetition_question_stats_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_spaced_repetition_question_stats_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/spaced-repetition-question-stats/ | 
[**ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_list**](AiMentorApi.md#ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/spaced-repetition-recommended-paths/ | 
[**ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_update**](AiMentorApi.md#ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/spaced-repetition-recommended-paths/ | 
[**ai_mentor_orgs_users_mentors_star_create**](AiMentorApi.md#ai_mentor_orgs_users_mentors_star_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/star/ | 
[**ai_mentor_orgs_users_mentors_star_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_mentors_star_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/star/ | 
[**ai_mentor_orgs_users_mentors_unstar_create**](AiMentorApi.md#ai_mentor_orgs_users_mentors_unstar_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/mentors/{mentor}/unstar/ | 
[**ai_mentor_orgs_users_metadata_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_metadata_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/metadata | 
[**ai_mentor_orgs_users_moderation_logs_destroy**](AiMentorApi.md#ai_mentor_orgs_users_moderation_logs_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/moderation-logs/{id}/ | 
[**ai_mentor_orgs_users_moderation_logs_list**](AiMentorApi.md#ai_mentor_orgs_users_moderation_logs_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/moderation-logs/ | 
[**ai_mentor_orgs_users_moderation_logs_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_moderation_logs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/moderation-logs/{id}/ | 
[**ai_mentor_orgs_users_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/{name}/ | 
[**ai_mentor_orgs_users_periodic_agent_logs_list**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agent_logs_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agent-logs/ | 
[**ai_mentor_orgs_users_periodic_agent_logs_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agent_logs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agent-logs/{id}/ | 
[**ai_mentor_orgs_users_periodic_agents_create**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/ | 
[**ai_mentor_orgs_users_periodic_agents_destroy**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/{id}/ | 
[**ai_mentor_orgs_users_periodic_agents_list**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/ | 
[**ai_mentor_orgs_users_periodic_agents_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/{id}/ | 
[**ai_mentor_orgs_users_periodic_agents_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/{id}/ | 
[**ai_mentor_orgs_users_periodic_agents_update**](AiMentorApi.md#ai_mentor_orgs_users_periodic_agents_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/periodic-agents/{id}/ | 
[**ai_mentor_orgs_users_pin_message_create**](AiMentorApi.md#ai_mentor_orgs_users_pin_message_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/pin-message/ | 
[**ai_mentor_orgs_users_pin_message_destroy**](AiMentorApi.md#ai_mentor_orgs_users_pin_message_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/pin-message/ | 
[**ai_mentor_orgs_users_pin_message_list**](AiMentorApi.md#ai_mentor_orgs_users_pin_message_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/pin-message/ | 
[**ai_mentor_orgs_users_planned_jobs_list**](AiMentorApi.md#ai_mentor_orgs_users_planned_jobs_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/planned-jobs/ | 
[**ai_mentor_orgs_users_planned_jobs_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_planned_jobs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/planned-jobs/{id}/ | 
[**ai_mentor_orgs_users_playwright_scripts_create**](AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/ | 
[**ai_mentor_orgs_users_playwright_scripts_destroy**](AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/{id}/ | 
[**ai_mentor_orgs_users_playwright_scripts_list**](AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/ | 
[**ai_mentor_orgs_users_playwright_scripts_partial_update**](AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_partial_update) | **PATCH** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/{id}/ | 
[**ai_mentor_orgs_users_playwright_scripts_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/{id}/ | 
[**ai_mentor_orgs_users_playwright_scripts_update**](AiMentorApi.md#ai_mentor_orgs_users_playwright_scripts_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/playwright-scripts/{id}/ | 
[**ai_mentor_orgs_users_predictive_analytics_create**](AiMentorApi.md#ai_mentor_orgs_users_predictive_analytics_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/predictive-analytics/ | 
[**ai_mentor_orgs_users_recent_messages_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_recent_messages_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/recent-messages/ | 
[**ai_mentor_orgs_users_recently_accessed_mentors_list**](AiMentorApi.md#ai_mentor_orgs_users_recently_accessed_mentors_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/recently-accessed-mentors/ | 
[**ai_mentor_orgs_users_recommend_courses_block_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_recommend_courses_block_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/recommend-courses-block/ | 
[**ai_mentor_orgs_users_recommend_courses_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_recommend_courses_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/recommend-courses/ | 
[**ai_mentor_orgs_users_resources_web_create**](AiMentorApi.md#ai_mentor_orgs_users_resources_web_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/resources/web/ | 
[**ai_mentor_orgs_users_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/{name}/ | 
[**ai_mentor_orgs_users_safety_logs_destroy**](AiMentorApi.md#ai_mentor_orgs_users_safety_logs_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/safety-logs/{id}/ | 
[**ai_mentor_orgs_users_safety_logs_list**](AiMentorApi.md#ai_mentor_orgs_users_safety_logs_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/safety-logs/ | 
[**ai_mentor_orgs_users_safety_logs_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_safety_logs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/safety-logs/{id}/ | 
[**ai_mentor_orgs_users_session_detail_mentors_list**](AiMentorApi.md#ai_mentor_orgs_users_session_detail_mentors_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/session-detail/mentors/{mentor}/ | 
[**ai_mentor_orgs_users_sessionid_list**](AiMentorApi.md#ai_mentor_orgs_users_sessionid_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessionid/ | 
[**ai_mentor_orgs_users_sessions_browser_screenshot_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_sessions_browser_screenshot_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/browser-screenshot/ | 
[**ai_mentor_orgs_users_sessions_create**](AiMentorApi.md#ai_mentor_orgs_users_sessions_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/ | 
[**ai_mentor_orgs_users_sessions_destroy**](AiMentorApi.md#ai_mentor_orgs_users_sessions_destroy) | **DELETE** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/ | 
[**ai_mentor_orgs_users_sessions_download_session_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_sessions_download_session_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/download-session | 
[**ai_mentor_orgs_users_sessions_memory_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_sessions_memory_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/memory/ | 
[**ai_mentor_orgs_users_sessions_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_sessions_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/ | Retrieve Chat Messages
[**ai_mentor_orgs_users_sessions_shell_logs_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_sessions_shell_logs_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/shell-logs/ | 
[**ai_mentor_orgs_users_sessions_suggestion_list**](AiMentorApi.md#ai_mentor_orgs_users_sessions_suggestion_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/suggestion | 
[**ai_mentor_orgs_users_sessions_tasks_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_sessions_tasks_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/tasks/{task_id}/ | 
[**ai_mentor_orgs_users_sessions_update**](AiMentorApi.md#ai_mentor_orgs_users_sessions_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/sessions/{session_id}/ | 
[**ai_mentor_orgs_users_settings_tenant_llm_create**](AiMentorApi.md#ai_mentor_orgs_users_settings_tenant_llm_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/settings/tenant-llm/ | 
[**ai_mentor_orgs_users_settings_tenant_llm_list**](AiMentorApi.md#ai_mentor_orgs_users_settings_tenant_llm_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/settings/tenant-llm/ | 
[**ai_mentor_orgs_users_starred_mentors_list**](AiMentorApi.md#ai_mentor_orgs_users_starred_mentors_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/starred-mentors/ | 
[**ai_mentor_orgs_users_tasks_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_tasks_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/tasks/{task_id} | 
[**ai_mentor_orgs_users_tasks_sessions_create**](AiMentorApi.md#ai_mentor_orgs_users_tasks_sessions_create) | **POST** /api/ai-mentor/orgs/{org}/users/{user_id}/tasks/sessions/{session_id}/ | 
[**ai_mentor_orgs_users_update**](AiMentorApi.md#ai_mentor_orgs_users_update) | **PUT** /api/ai-mentor/orgs/{org}/users/{user_id}/{name}/ | 
[**ai_mentor_orgs_users_voices_list**](AiMentorApi.md#ai_mentor_orgs_users_voices_list) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/voices/ | 
[**ai_mentor_orgs_users_voices_retrieve**](AiMentorApi.md#ai_mentor_orgs_users_voices_retrieve) | **GET** /api/ai-mentor/orgs/{org}/users/{user_id}/voices/{id}/ | 
[**ai_mentor_orgs_webhooks_azure_trigger_create**](AiMentorApi.md#ai_mentor_orgs_webhooks_azure_trigger_create) | **POST** /api/ai-mentor/orgs/{org}/webhooks/azure/trigger/{slug}/ | 
[**ai_mentor_orgs_webhooks_github_pullrequest_create**](AiMentorApi.md#ai_mentor_orgs_webhooks_github_pullrequest_create) | **POST** /api/ai-mentor/orgs/{org}/webhooks/github/pullrequest/ | 
[**ai_mentor_webhooks_azure_emailchat_create**](AiMentorApi.md#ai_mentor_webhooks_azure_emailchat_create) | **POST** /api/ai-mentor/webhooks/azure/emailchat/ | 


# **ai_mentor_orgs_all_triggers_retrieve**
> ai_mentor_orgs_all_triggers_retrieve(org)



List all triggers for an organization.  Args:     request: The HTTP request.     org: The organization/tenant identifier.  Returns:     Response: A list of trigger slugs for the organization.  Raises:     BadRequest: If the request is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.ai_mentor_orgs_all_triggers_retrieve(org)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_all_triggers_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of trigger slugs |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_mentors_email_inbox_list**
> PaginatedEmailPromptListList ai_mentor_orgs_mentors_email_inbox_list(mentor, org, page=page, page_size=page_size, search=search)



Retrieve a list of emails in a mentor's inbox.  The list can be filtered using the 'search' query parameter to search for specific terms in the email content or subject.  Args:     mentor: The unique identifier of the mentor.  Returns:     Response: A paginated list of emails in the mentor's inbox.  Raises:     NotFound: If the specified mentor does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_email_prompt_list_list import PaginatedEmailPromptListList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str | Search term to filter emails by content or subject (optional)

try:
    api_response = api_instance.ai_mentor_orgs_mentors_email_inbox_list(mentor, org, page=page, page_size=page_size, search=search)
    print("The response of AiMentorApi->ai_mentor_orgs_mentors_email_inbox_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_mentors_email_inbox_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| Search term to filter emails by content or subject | [optional] 

### Return type

[**PaginatedEmailPromptListList**](PaginatedEmailPromptListList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Mentor not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_mentors_email_inbox_retrieve**
> EmailPromptDetail ai_mentor_orgs_mentors_email_inbox_retrieve(email_prompt_id, mentor, org)



Retrieve details of a specific email in a mentor's inbox.  Args:     request: The HTTP request.     email_prompt_id: The ID of the email to retrieve.  Returns:     Response: The detailed information about the email.  Raises:     NotFound: If the specified email does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.email_prompt_detail import EmailPromptDetail
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
email_prompt_id = 56 # int | 
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_mentors_email_inbox_retrieve(email_prompt_id, mentor, org)
    print("The response of AiMentorApi->ai_mentor_orgs_mentors_email_inbox_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_mentors_email_inbox_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_prompt_id** | **int**|  | 
 **mentor** | **str**|  | 
 **org** | **str**|  | 

### Return type

[**EmailPromptDetail**](EmailPromptDetail.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Email not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_mentors_email_inbox_summary_retrieve**
> EmailPromptSummary ai_mentor_orgs_mentors_email_inbox_summary_retrieve(mentor, org)



Retrieve a summary of a mentor's email inbox.  Args:     request: The HTTP request.     mentor: The unique identifier of the mentor.  Returns:     Response: A summary of the mentor's email inbox statistics.  Raises:     NotFound: If the specified mentor does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.email_prompt_summary import EmailPromptSummary
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_mentors_email_inbox_summary_retrieve(mentor, org)
    print("The response of AiMentorApi->ai_mentor_orgs_mentors_email_inbox_summary_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_mentors_email_inbox_summary_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 

### Return type

[**EmailPromptSummary**](EmailPromptSummary.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Mentor not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_mentors_link_course_create**
> LinkCourseResponse ai_mentor_orgs_mentors_link_course_create(mentor, org, link_course_request)



API endpoint to link mentor with a course and enable guided mode.  Permissions:     - Accessible to tenant admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.link_course_request import LinkCourseRequest
from iblai.models.link_course_response import LinkCourseResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
link_course_request = iblai.LinkCourseRequest() # LinkCourseRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_mentors_link_course_create(mentor, org, link_course_request)
    print("The response of AiMentorApi->ai_mentor_orgs_mentors_link_course_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_mentors_link_course_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **link_course_request** | [**LinkCourseRequest**](LinkCourseRequest.md)|  | 

### Return type

[**LinkCourseResponse**](LinkCourseResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_mentors_link_course_retrieve**
> LinkCourseResponse ai_mentor_orgs_mentors_link_course_retrieve(mentor, org)



API endpoint to link mentor with a course and enable guided mode.  Permissions:     - Accessible to tenant admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.link_course_response import LinkCourseResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_mentors_link_course_retrieve(mentor, org)
    print("The response of AiMentorApi->ai_mentor_orgs_mentors_link_course_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_mentors_link_course_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 

### Return type

[**LinkCourseResponse**](LinkCourseResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_metadata_create**
> MentorMetadata ai_mentor_orgs_metadata_create(org, mentor_metadata)



Create or update metadata for a mentor.  Args:     request: The HTTP request containing the metadata.     org: The organization/tenant identifier.  Returns:     Response: The created or updated mentor metadata.  Raises:     BadRequest: If the provided data is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_metadata import MentorMetadata
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
mentor_metadata = {"metadata":{"specialty":"machine learning","experience_level":"expert","languages":["English","Spanish"]},"mentor_id":123} # MentorMetadata | 

try:
    api_response = api_instance.ai_mentor_orgs_metadata_create(org, mentor_metadata)
    print("The response of AiMentorApi->ai_mentor_orgs_metadata_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_metadata_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **mentor_metadata** | [**MentorMetadata**](MentorMetadata.md)|  | 

### Return type

[**MentorMetadata**](MentorMetadata.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_quiz_customizer_create**
> QuestionResponse ai_mentor_orgs_quiz_customizer_create(org, question_request)



Generate follow-up questions based on initial questions.  Args:     request: The HTTP request containing the initial questions.  Returns:     Response: The generated follow-up questions.  Raises:     BadRequest: If the provided data is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.question_request import QuestionRequest
from iblai.models.question_response import QuestionResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
question_request = {"username":"johndoe","initial_questions":[{"text":"What is machine learning?","difficulty_level":2,"possible_answers":[{"text":"A type of artificial intelligence"},{"text":"A programming language"}]}],"question_count":5,"subject":"Artificial Intelligence"} # QuestionRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_quiz_customizer_create(org, question_request)
    print("The response of AiMentorApi->ai_mentor_orgs_quiz_customizer_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_quiz_customizer_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **question_request** | [**QuestionRequest**](QuestionRequest.md)|  | 

### Return type

[**QuestionResponse**](QuestionResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_quiz_customizer_retrieve**
> ai_mentor_orgs_quiz_customizer_retrieve(org)



Retrieve existing questions.  Args:     request: The HTTP request.  Returns:     Response: The existing questions.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.ai_mentor_orgs_quiz_customizer_retrieve(org)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_quiz_customizer_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_sessions_create**
> ChatSessionResponse ai_mentor_orgs_sessions_create(org, chat_session_request)



Retrieve or create a chat session with a mentor.  Passing `null` as `tools` results in using all tools assigned to the mentor. To specify that no tools be used, pass an empty list.  Args:     request: HTTP request containing mentor details.     org: Organization key identifier.     user_id (optional): Username for authentication (if required by the mentor).  Returns:     Response: JSON object containing the session ID.  Raises:     Http404: If the mentor is not found.     ValidationError: If the username is invalid.     ValidationError: If one or more tool slugs are invalid.

### Example


```python
import iblai
from iblai.models.chat_session_request import ChatSessionRequest
from iblai.models.chat_session_response import ChatSessionResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
chat_session_request = {"mentor":"ai-mentor"} # ChatSessionRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_sessions_create(org, chat_session_request)
    print("The response of AiMentorApi->ai_mentor_orgs_sessions_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_sessions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **chat_session_request** | [**ChatSessionRequest**](ChatSessionRequest.md)|  | 

### Return type

[**ChatSessionResponse**](ChatSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_trigger_create**
> TriggerResponse ai_mentor_orgs_trigger_create(org, trigger_request)



Create or modify a trigger.  Args:     request: The HTTP request containing the trigger data.     org: The organization/tenant identifier.  Returns:     Response: The created or updated trigger details.  Raises:     BadRequest: If the provided data is invalid or missing required parameters.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.trigger_request import TriggerRequest
from iblai.models.trigger_response import TriggerResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
trigger_request = {"slug":"trggr-slug-1","template":"url_to_email_everyday","parameters":{"recipients":["tcook@apple.com"],"trigger_url":"https://google.com"}} # TriggerRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_trigger_create(org, trigger_request)
    print("The response of AiMentorApi->ai_mentor_orgs_trigger_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_trigger_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **trigger_request** | [**TriggerRequest**](TriggerRequest.md)|  | 

### Return type

[**TriggerResponse**](TriggerResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data or missing required parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_trigger_deletion_create**
> ai_mentor_orgs_trigger_deletion_create(org, slug)



Delete a specific trigger.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     slug: The unique slug identifier of the trigger to delete.  Returns:     Response: A confirmation of the deletion status.  Raises:     BadRequest: If the specified trigger does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
slug = 'slug_example' # str | 

try:
    api_instance.ai_mentor_orgs_trigger_deletion_create(org, slug)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_trigger_deletion_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Trigger successfully deleted |  -  |
**400** | Trigger not found or invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_trigger_retrieve**
> TriggerResponse ai_mentor_orgs_trigger_retrieve(org, slug)



Retrieve details of a specific trigger.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     slug: The unique slug identifier of the trigger.  Returns:     Response: The details of the specified trigger.  Raises:     Http404: If the specified trigger does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.trigger_response import TriggerResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
slug = 'slug_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_trigger_retrieve(org, slug)
    print("The response of AiMentorApi->ai_mentor_orgs_trigger_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_trigger_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **slug** | **str**|  | 

### Return type

[**TriggerResponse**](TriggerResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Trigger not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_trigger_templates_retrieve**
> ai_mentor_orgs_trigger_templates_retrieve(org)



Retrieve available trigger templates.  Args:     request: The HTTP request.     org: The organization/tenant identifier.  Returns:     Response: A dictionary of available trigger templates and their required parameters.  Raises:     BadRequest: If the request is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.ai_mentor_orgs_trigger_templates_retrieve(org)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_trigger_templates_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dictionary of trigger templates and their required parameters |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_ai_generated_images_destroy**
> ai_mentor_orgs_users_ai_generated_images_destroy(id, org, user_id)



Endpoint to view and delete AI generated images for a user.  AI Generated images are images generated during chat with AI. They are cached to allow retrieval and deletion.  optional filtering parameters allowed are - username: The username of the user for which this image was stored. - provider: The provider used to generate the image. eg. openai, nvidia (nim), replicate. - model: the text to image model on the provider used to generate the image.  This endpoint is accessible to both students and platform admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this ai generated image.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_ai_generated_images_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_ai_generated_images_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ai generated image. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_ai_generated_images_list**
> PaginatedAIGeneratedImageList ai_mentor_orgs_users_ai_generated_images_list(org, user_id, model=model, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, username=username)



Endpoint to view and delete AI generated images for a user.  AI Generated images are images generated during chat with AI. They are cached to allow retrieval and deletion.  optional filtering parameters allowed are - username: The username of the user for which this image was stored. - provider: The provider used to generate the image. eg. openai, nvidia (nim), replicate. - model: the text to image model on the provider used to generate the image.  This endpoint is accessible to both students and platform admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_ai_generated_image_list import PaginatedAIGeneratedImageList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
model = 'model_example' # str |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
provider = 'provider_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_ai_generated_images_list(org, user_id, model=model, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, username=username)
    print("The response of AiMentorApi->ai_mentor_orgs_users_ai_generated_images_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_ai_generated_images_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **model** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedAIGeneratedImageList**](PaginatedAIGeneratedImageList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_ai_generated_images_retrieve**
> AIGeneratedImage ai_mentor_orgs_users_ai_generated_images_retrieve(id, org, user_id)



Endpoint to view and delete AI generated images for a user.  AI Generated images are images generated during chat with AI. They are cached to allow retrieval and deletion.  optional filtering parameters allowed are - username: The username of the user for which this image was stored. - provider: The provider used to generate the image. eg. openai, nvidia (nim), replicate. - model: the text to image model on the provider used to generate the image.  This endpoint is accessible to both students and platform admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.ai_generated_image import AIGeneratedImage
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this ai generated image.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_ai_generated_images_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_ai_generated_images_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_ai_generated_images_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this ai generated image. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**AIGeneratedImage**](AIGeneratedImage.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_ai_user_profile_memory_create**
> AIUserProfileMemoryRelation ai_mentor_orgs_users_ai_user_profile_memory_create(org, user_id, ai_user_profile_request)



Endpoint to create an AI user profile memory entry.  Sample request: ``` {\"favorite-animal\": \"my favorite animal is cat\"} ``` Sample Response (the same as request data): ``` {\"favorite-animal\": \"my favorite animal is cat\"} ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.ai_user_profile_memory_relation import AIUserProfileMemoryRelation
from iblai.models.ai_user_profile_request import AIUserProfileRequest
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
ai_user_profile_request = iblai.AIUserProfileRequest() # AIUserProfileRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_users_ai_user_profile_memory_create(org, user_id, ai_user_profile_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_ai_user_profile_memory_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_ai_user_profile_memory_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **ai_user_profile_request** | [**AIUserProfileRequest**](AIUserProfileRequest.md)|  | 

### Return type

[**AIUserProfileMemoryRelation**](AIUserProfileMemoryRelation.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_ai_user_profile_memory_destroy**
> ai_mentor_orgs_users_ai_user_profile_memory_destroy(org, tag, user_id)



The endpoint to delete an AI user profile memory entry.  No query parameters or JSON parameters are required.  The response is always empty. Successful request will be responded with status 204, and failed request will be responded with status 404.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
tag = 'tag_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_ai_user_profile_memory_destroy(org, tag, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_ai_user_profile_memory_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **tag** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_ai_user_profile_memory_list**
> List[AIUserProfileMemoryRelation] ai_mentor_orgs_users_ai_user_profile_memory_list(org, user_id)



Endpoint to get a list of AI user profile memory entries or to add an entry.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.ai_user_profile_memory_relation import AIUserProfileMemoryRelation
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_ai_user_profile_memory_list(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_ai_user_profile_memory_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_ai_user_profile_memory_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[AIUserProfileMemoryRelation]**](AIUserProfileMemoryRelation.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_assumed_knowledge_create**
> AssumedKnowledge ai_mentor_orgs_users_assumed_knowledge_create(org, user_id, assumed_knowledge)



Update assumed knowledge levels.  Args:     request: The HTTP request containing the updated knowledge levels.     org: The organization/tenant identifier.     user_id: The ID of the user to update assumed knowledge for.  Returns:     Response: The updated assumed knowledge levels.  Raises:     BadRequest: If the provided data is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.assumed_knowledge import AssumedKnowledge
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
assumed_knowledge = {"levels":[{"category":"Programming","level":"Advanced"},{"category":"Mathematics","level":"Advanced"},{"category":"Statistics","level":"Intermediate"}]} # AssumedKnowledge | 

try:
    api_response = api_instance.ai_mentor_orgs_users_assumed_knowledge_create(org, user_id, assumed_knowledge)
    print("The response of AiMentorApi->ai_mentor_orgs_users_assumed_knowledge_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_assumed_knowledge_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **assumed_knowledge** | [**AssumedKnowledge**](AssumedKnowledge.md)|  | 

### Return type

[**AssumedKnowledge**](AssumedKnowledge.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_assumed_knowledge_retrieve**
> AssumedKnowledge ai_mentor_orgs_users_assumed_knowledge_retrieve(org, user_id)



Retrieve assumed knowledge levels.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user to retrieve assumed knowledge for.  Returns:     Response: The assumed knowledge levels for different categories.  Raises:     NotFound: If no assumed knowledge exists for the user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.assumed_knowledge import AssumedKnowledge
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_assumed_knowledge_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_assumed_knowledge_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_assumed_knowledge_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**AssumedKnowledge**](AssumedKnowledge.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Assumed knowledge not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_audio_to_text_create**
> AudioToTextResponse ai_mentor_orgs_users_audio_to_text_create(org, user_id, file)



Convert an uploaded audio file to text.  Args:     request: The HTTP request containing the audio file.     org: The organization/tenant identifier.     user_id: The ID of the user uploading the audio.  Returns:     Response: The transcribed text from the audio file.  Raises:     BadRequest: If the audio file is invalid or cannot be processed.     NotFound: If the API key for the tenant is not found.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.audio_to_text_response import AudioToTextResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
file = 'file_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_audio_to_text_create(org, user_id, file)
    print("The response of AiMentorApi->ai_mentor_orgs_users_audio_to_text_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_audio_to_text_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **file** | **str**|  | 

### Return type

[**AudioToTextResponse**](AudioToTextResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid audio file or processing error |  -  |
**404** | API key not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_available_template_mentors_retrieve**
> TemplateMentor ai_mentor_orgs_users_available_template_mentors_retrieve(org, user_id)



This endpoint list available template mentors for a tenant  Returns:      200 : List of Tool objects

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.template_mentor import TemplateMentor
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_available_template_mentors_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_available_template_mentors_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_available_template_mentors_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**TemplateMentor**](TemplateMentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_call_configurations_create**
> CallConfiguration ai_mentor_orgs_users_call_configurations_create(org, user_id, call_configuration)



API ViewSet for managing call configurations.  This ViewSet provides endpoints to retrieve, create, and update call configurations for mentors. Call configurations define how voice calls are handled for a mentor.  Permissions:     - Accessible only to platform admins.  Endpoints:     GET /api/org/{org}/mentors/{mentor_pk}/call-configurations/         - List all call configurations for a specific mentor         - Returns paginated list of call configurations      POST /api/org/{org}/mentors/{mentor_pk}/call-configurations/         - Create a new call configuration for a mentor         - Requires call configuration data in request body      PUT /api/org/{org}/mentors/{mentor_pk}/call-configurations/{id}/         - Update an existing call configuration         - Requires call configuration data in request body  Query Parameters:     - mentor: Filter configurations by mentor ID  Returns:     - CallConfigurationSerializer data

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.call_configuration import CallConfiguration
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
call_configuration = iblai.CallConfiguration() # CallConfiguration | 

try:
    api_response = api_instance.ai_mentor_orgs_users_call_configurations_create(org, user_id, call_configuration)
    print("The response of AiMentorApi->ai_mentor_orgs_users_call_configurations_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_call_configurations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **call_configuration** | [**CallConfiguration**](CallConfiguration.md)|  | 

### Return type

[**CallConfiguration**](CallConfiguration.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_call_configurations_list**
> List[CallConfiguration] ai_mentor_orgs_users_call_configurations_list(org, user_id, mentor=mentor, mode=mode, ordering=ordering, search=search)



API ViewSet for managing call configurations.  This ViewSet provides endpoints to retrieve, create, and update call configurations for mentors. Call configurations define how voice calls are handled for a mentor.  Permissions:     - Accessible only to platform admins.  Endpoints:     GET /api/org/{org}/mentors/{mentor_pk}/call-configurations/         - List all call configurations for a specific mentor         - Returns paginated list of call configurations      POST /api/org/{org}/mentors/{mentor_pk}/call-configurations/         - Create a new call configuration for a mentor         - Requires call configuration data in request body      PUT /api/org/{org}/mentors/{mentor_pk}/call-configurations/{id}/         - Update an existing call configuration         - Requires call configuration data in request body  Query Parameters:     - mentor: Filter configurations by mentor ID  Returns:     - CallConfigurationSerializer data

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.call_configuration import CallConfiguration
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor = 56 # int |  (optional)
mode = 'mode_example' # str | * `realtime` - Realtime * `inference` - Inference (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
search = 'search_example' # str | A search term. (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_call_configurations_list(org, user_id, mentor=mentor, mode=mode, ordering=ordering, search=search)
    print("The response of AiMentorApi->ai_mentor_orgs_users_call_configurations_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_call_configurations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor** | **int**|  | [optional] 
 **mode** | **str**| * &#x60;realtime&#x60; - Realtime * &#x60;inference&#x60; - Inference | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**List[CallConfiguration]**](CallConfiguration.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_call_configurations_partial_update**
> CallConfiguration ai_mentor_orgs_users_call_configurations_partial_update(id, org, user_id, patched_call_configuration=patched_call_configuration)



API ViewSet for managing call configurations.  This ViewSet provides endpoints to retrieve, create, and update call configurations for mentors. Call configurations define how voice calls are handled for a mentor.  Permissions:     - Accessible only to platform admins.  Endpoints:     GET /api/org/{org}/mentors/{mentor_pk}/call-configurations/         - List all call configurations for a specific mentor         - Returns paginated list of call configurations      POST /api/org/{org}/mentors/{mentor_pk}/call-configurations/         - Create a new call configuration for a mentor         - Requires call configuration data in request body      PUT /api/org/{org}/mentors/{mentor_pk}/call-configurations/{id}/         - Update an existing call configuration         - Requires call configuration data in request body  Query Parameters:     - mentor: Filter configurations by mentor ID  Returns:     - CallConfigurationSerializer data

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.call_configuration import CallConfiguration
from iblai.models.patched_call_configuration import PatchedCallConfiguration
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this call configuration.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
patched_call_configuration = iblai.PatchedCallConfiguration() # PatchedCallConfiguration |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_call_configurations_partial_update(id, org, user_id, patched_call_configuration=patched_call_configuration)
    print("The response of AiMentorApi->ai_mentor_orgs_users_call_configurations_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_call_configurations_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this call configuration. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **patched_call_configuration** | [**PatchedCallConfiguration**](PatchedCallConfiguration.md)|  | [optional] 

### Return type

[**CallConfiguration**](CallConfiguration.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_call_configurations_retrieve**
> CallConfiguration ai_mentor_orgs_users_call_configurations_retrieve(id, org, user_id)



API ViewSet for managing call configurations.  This ViewSet provides endpoints to retrieve, create, and update call configurations for mentors. Call configurations define how voice calls are handled for a mentor.  Permissions:     - Accessible only to platform admins.  Endpoints:     GET /api/org/{org}/mentors/{mentor_pk}/call-configurations/         - List all call configurations for a specific mentor         - Returns paginated list of call configurations      POST /api/org/{org}/mentors/{mentor_pk}/call-configurations/         - Create a new call configuration for a mentor         - Requires call configuration data in request body      PUT /api/org/{org}/mentors/{mentor_pk}/call-configurations/{id}/         - Update an existing call configuration         - Requires call configuration data in request body  Query Parameters:     - mentor: Filter configurations by mentor ID  Returns:     - CallConfigurationSerializer data

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.call_configuration import CallConfiguration
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this call configuration.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_call_configurations_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_call_configurations_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_call_configurations_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this call configuration. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CallConfiguration**](CallConfiguration.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_call_configurations_update**
> CallConfiguration ai_mentor_orgs_users_call_configurations_update(id, org, user_id, call_configuration)



API ViewSet for managing call configurations.  This ViewSet provides endpoints to retrieve, create, and update call configurations for mentors. Call configurations define how voice calls are handled for a mentor.  Permissions:     - Accessible only to platform admins.  Endpoints:     GET /api/org/{org}/mentors/{mentor_pk}/call-configurations/         - List all call configurations for a specific mentor         - Returns paginated list of call configurations      POST /api/org/{org}/mentors/{mentor_pk}/call-configurations/         - Create a new call configuration for a mentor         - Requires call configuration data in request body      PUT /api/org/{org}/mentors/{mentor_pk}/call-configurations/{id}/         - Update an existing call configuration         - Requires call configuration data in request body  Query Parameters:     - mentor: Filter configurations by mentor ID  Returns:     - CallConfigurationSerializer data

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.call_configuration import CallConfiguration
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this call configuration.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
call_configuration = iblai.CallConfiguration() # CallConfiguration | 

try:
    api_response = api_instance.ai_mentor_orgs_users_call_configurations_update(id, org, user_id, call_configuration)
    print("The response of AiMentorApi->ai_mentor_orgs_users_call_configurations_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_call_configurations_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this call configuration. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **call_configuration** | [**CallConfiguration**](CallConfiguration.md)|  | 

### Return type

[**CallConfiguration**](CallConfiguration.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_category_groups_create**
> MentorCategoryGroup ai_mentor_orgs_users_category_groups_create(org, user_id, mentor_category_group_create)



Create a new Mentor Category Group. Only accessible to Platform Admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_category_group import MentorCategoryGroup
from iblai.models.mentor_category_group_create import MentorCategoryGroupCreate
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_category_group_create = {"name":"STEM","description":"Science, Technology, Engineering, and Mathematics","audience":3,"audiences":[1,2,3]} # MentorCategoryGroupCreate | 

try:
    api_response = api_instance.ai_mentor_orgs_users_category_groups_create(org, user_id, mentor_category_group_create)
    print("The response of AiMentorApi->ai_mentor_orgs_users_category_groups_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_category_groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_category_group_create** | [**MentorCategoryGroupCreate**](MentorCategoryGroupCreate.md)|  | 

### Return type

[**MentorCategoryGroup**](MentorCategoryGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_category_groups_destroy**
> ai_mentor_orgs_users_category_groups_destroy(id, org, user_id)



Mentor Category Groups offer parent grouping for mentor category objects.  The parameter `audience` is deprecated and is currently left behind for backward compatibility.  Permissions:     GET: Accessible to both Platform Admins and Students     POST, DELETE, PATCH, PUT: Accessible to only Platform Admins

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this mentor category group.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_category_groups_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_category_groups_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this mentor category group. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_category_groups_list**
> List[MentorCategoryGroup] ai_mentor_orgs_users_category_groups_list(org, user_id, audience=audience, audience__name=audience__name, ordering=ordering, search=search)



Retrieve a list of Mentor Category Groups.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_category_group import MentorCategoryGroup
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
audience = 56 # int |  (optional)
audience__name = 'audience__name_example' # str |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
search = 'search_example' # str | A search term. (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_category_groups_list(org, user_id, audience=audience, audience__name=audience__name, ordering=ordering, search=search)
    print("The response of AiMentorApi->ai_mentor_orgs_users_category_groups_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_category_groups_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **audience** | **int**|  | [optional] 
 **audience__name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**List[MentorCategoryGroup]**](MentorCategoryGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_category_groups_partial_update**
> MentorCategoryGroupCreate ai_mentor_orgs_users_category_groups_partial_update(id, org, user_id, patched_mentor_category_group_create=patched_mentor_category_group_create)



Mentor Category Groups offer parent grouping for mentor category objects.  The parameter `audience` is deprecated and is currently left behind for backward compatibility.  Permissions:     GET: Accessible to both Platform Admins and Students     POST, DELETE, PATCH, PUT: Accessible to only Platform Admins

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_category_group_create import MentorCategoryGroupCreate
from iblai.models.patched_mentor_category_group_create import PatchedMentorCategoryGroupCreate
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this mentor category group.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
patched_mentor_category_group_create = iblai.PatchedMentorCategoryGroupCreate() # PatchedMentorCategoryGroupCreate |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_category_groups_partial_update(id, org, user_id, patched_mentor_category_group_create=patched_mentor_category_group_create)
    print("The response of AiMentorApi->ai_mentor_orgs_users_category_groups_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_category_groups_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this mentor category group. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **patched_mentor_category_group_create** | [**PatchedMentorCategoryGroupCreate**](PatchedMentorCategoryGroupCreate.md)|  | [optional] 

### Return type

[**MentorCategoryGroupCreate**](MentorCategoryGroupCreate.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_category_groups_retrieve**
> MentorCategoryGroup ai_mentor_orgs_users_category_groups_retrieve(id, org, user_id)



Mentor Category Groups offer parent grouping for mentor category objects.  The parameter `audience` is deprecated and is currently left behind for backward compatibility.  Permissions:     GET: Accessible to both Platform Admins and Students     POST, DELETE, PATCH, PUT: Accessible to only Platform Admins

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_category_group import MentorCategoryGroup
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this mentor category group.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_category_groups_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_category_groups_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_category_groups_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this mentor category group. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorCategoryGroup**](MentorCategoryGroup.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_category_groups_update**
> MentorCategoryGroupCreate ai_mentor_orgs_users_category_groups_update(id, org, user_id, mentor_category_group_create)



Mentor Category Groups offer parent grouping for mentor category objects.  The parameter `audience` is deprecated and is currently left behind for backward compatibility.  Permissions:     GET: Accessible to both Platform Admins and Students     POST, DELETE, PATCH, PUT: Accessible to only Platform Admins

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_category_group_create import MentorCategoryGroupCreate
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this mentor category group.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_category_group_create = iblai.MentorCategoryGroupCreate() # MentorCategoryGroupCreate | 

try:
    api_response = api_instance.ai_mentor_orgs_users_category_groups_update(id, org, user_id, mentor_category_group_create)
    print("The response of AiMentorApi->ai_mentor_orgs_users_category_groups_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_category_groups_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this mentor category group. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_category_group_create** | [**MentorCategoryGroupCreate**](MentorCategoryGroupCreate.md)|  | 

### Return type

[**MentorCategoryGroupCreate**](MentorCategoryGroupCreate.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_clean_vector_results_create**
> List[VectorResult] ai_mentor_orgs_users_clean_vector_results_create(org, session_id, user_id, vector_result)



Clean up provided vector results.  This endpoint allows users to submit specific vector results for cleaning, which is useful when there are particular documents that need to be processed.  Args:     request: The HTTP request containing the vector results to clean.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.  Returns:     Response: The cleaned vector results.  Raises:     BadRequest: If the API key for the cleaning provider is not found or the provided data is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.vector_result import VectorResult
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 
vector_result = [[{"type":"document","title":"Introduction to Machine Learning","snippet":"Machine learning is a subset of artificial intelligence that focuses on developing systems that can learn from data.","source":"https://example.com/ml-intro","score":0.92,"confidence_level":0.85}]] # List[VectorResult] | 

try:
    api_response = api_instance.ai_mentor_orgs_users_clean_vector_results_create(org, session_id, user_id, vector_result)
    print("The response of AiMentorApi->ai_mentor_orgs_users_clean_vector_results_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_clean_vector_results_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 
 **vector_result** | [**List[VectorResult]**](VectorResult.md)|  | 

### Return type

[**List[VectorResult]**](VectorResult.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | API key not found or invalid data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_clean_vector_results_list**
> List[VectorResult] ai_mentor_orgs_users_clean_vector_results_list(org, session_id, user_id)



Retrieve and clean up vector results from a specific session.  This endpoint retrieves the documents last used by the mentor to answer the most recent query from the user in the specified session, and cleans them to remove any inappropriate content.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.     session_id: The ID of the session to retrieve vector results from.  Returns:     Response: The cleaned vector results.  Raises:     BadRequest: If the API key for the cleaning provider is not found.     NotFound: If no vector results are found for the session.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.vector_result import VectorResult
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_clean_vector_results_list(org, session_id, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_clean_vector_results_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_clean_vector_results_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[VectorResult]**](VectorResult.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | API key not found |  -  |
**404** | Session or results not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_clear_chathistory_destroy**
> ai_mentor_orgs_users_clear_chathistory_destroy(org, user_id)

Delete User Chat History

Endpoint to clear a user's chat history.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Delete User Chat History
    api_instance.ai_mentor_orgs_users_clear_chathistory_destroy(org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_clear_chathistory_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_component_create**
> Unit ai_mentor_orgs_users_course_creation_component_create(org, user_id, unit)



API viewset for managing course units.  This viewset allows platform administrators to retrieve and manage units within course subsections, and generate content for them.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.unit import Unit
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
unit = iblai.Unit() # Unit | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_component_create(org, user_id, unit)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_component_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_component_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **unit** | [**Unit**](Unit.md)|  | 

### Return type

[**Unit**](Unit.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_component_destroy**
> ai_mentor_orgs_users_course_creation_component_destroy(id, org, user_id)



API viewset for managing course units.  This viewset allows platform administrators to retrieve and manage units within course subsections, and generate content for them.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this unit.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_component_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_component_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this unit. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_component_draft_content_create**
> ai_mentor_orgs_users_course_creation_component_draft_content_create(id, org, user_id, unit)



Generate draft content for a specific unit.  This action starts a background task to create draft content for the specified unit using AI.  Args:     request: The HTTP request.     pk: The primary key of the unit to generate content for.  Returns:     Response: A confirmation that the content generation task has been started.  Raises:     NotFound: If the specified unit does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.unit import Unit
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this unit.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
unit = iblai.Unit() # Unit | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_component_draft_content_create(id, org, user_id, unit)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_component_draft_content_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this unit. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **unit** | [**Unit**](Unit.md)|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Content creation started successfully |  -  |
**404** | Unit not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_component_draft_content_retrieve**
> ai_mentor_orgs_users_course_creation_component_draft_content_retrieve(id, org, user_id)



Generate draft content for a specific unit.  This action starts a background task to create draft content for the specified unit using AI.  Args:     request: The HTTP request.     pk: The primary key of the unit to generate content for.  Returns:     Response: A confirmation that the content generation task has been started.  Raises:     NotFound: If the specified unit does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this unit.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_component_draft_content_retrieve(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_component_draft_content_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this unit. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Content creation started successfully |  -  |
**404** | Unit not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_component_list**
> PaginatedUnitList ai_mentor_orgs_users_course_creation_component_list(org, user_id, course=course, ordering=ordering, page=page, page_size=page_size, search=search, section=section, subsection=subsection, task=task)



API viewset for managing course units.  This viewset allows platform administrators to retrieve and manage units within course subsections, and generate content for them.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_unit_list import PaginatedUnitList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
course = 56 # int |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str | A search term. (optional)
section = 56 # int |  (optional)
subsection = 56 # int |  (optional)
task = 56 # int |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_component_list(org, user_id, course=course, ordering=ordering, page=page, page_size=page_size, search=search, section=section, subsection=subsection, task=task)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_component_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_component_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **course** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **section** | **int**|  | [optional] 
 **subsection** | **int**|  | [optional] 
 **task** | **int**|  | [optional] 

### Return type

[**PaginatedUnitList**](PaginatedUnitList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_component_partial_update**
> Unit ai_mentor_orgs_users_course_creation_component_partial_update(id, org, user_id, patched_unit=patched_unit)



API viewset for managing course units.  This viewset allows platform administrators to retrieve and manage units within course subsections, and generate content for them.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_unit import PatchedUnit
from iblai.models.unit import Unit
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this unit.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
patched_unit = iblai.PatchedUnit() # PatchedUnit |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_component_partial_update(id, org, user_id, patched_unit=patched_unit)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_component_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_component_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this unit. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **patched_unit** | [**PatchedUnit**](PatchedUnit.md)|  | [optional] 

### Return type

[**Unit**](Unit.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_component_retrieve**
> Unit ai_mentor_orgs_users_course_creation_component_retrieve(id, org, user_id)



API viewset for managing course units.  This viewset allows platform administrators to retrieve and manage units within course subsections, and generate content for them.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.unit import Unit
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this unit.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_component_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_component_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_component_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this unit. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Unit**](Unit.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_component_update**
> Unit ai_mentor_orgs_users_course_creation_component_update(id, org, user_id, unit)



API viewset for managing course units.  This viewset allows platform administrators to retrieve and manage units within course subsections, and generate content for them.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.unit import Unit
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this unit.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
unit = iblai.Unit() # Unit | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_component_update(id, org, user_id, unit)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_component_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_component_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this unit. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **unit** | [**Unit**](Unit.md)|  | 

### Return type

[**Unit**](Unit.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_course_destroy**
> ai_mentor_orgs_users_course_creation_course_destroy(id, org, user_id)



API viewset for managing EdX courses.  This viewset allows platform administrators to retrieve, delete, and perform various operations on EdX courses that were created through course creation tasks.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this edx course.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_course_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_course_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edx course. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_course_draft_content_for_all_units_retrieve**
> ai_mentor_orgs_users_course_creation_course_draft_content_for_all_units_retrieve(id, org, user_id)



Generate draft content for all units in a course.  This action starts a background task to create draft content for all units in the course using AI.  Args:     request: The HTTP request.     pk: The primary key of the course to generate content for.  Returns:     Response: A confirmation that the content generation task has been started.  Raises:     NotFound: If the specified course does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this edx course.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_course_draft_content_for_all_units_retrieve(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_course_draft_content_for_all_units_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edx course. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Content creation started successfully |  -  |
**404** | Course not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_course_full_structure_retrieve**
> FullCourse ai_mentor_orgs_users_course_creation_course_full_structure_retrieve(id, org, user_id)



Retrieve the full structure of a course.  This action returns the complete hierarchical structure of the course, including all sections, subsections, units, and components.  Args:     request: The HTTP request.     pk: The primary key of the course to retrieve.  Returns:     Response: The full structure of the course.  Raises:     NotFound: If the specified course does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.full_course import FullCourse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this edx course.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_course_full_structure_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_course_full_structure_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_course_full_structure_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edx course. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**FullCourse**](FullCourse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Course not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_course_list**
> PaginatedEdxCourseList ai_mentor_orgs_users_course_creation_course_list(org, user_id, ordering=ordering, page=page, page_size=page_size, search=search, task=task)



API viewset for managing EdX courses.  This viewset allows platform administrators to retrieve, delete, and perform various operations on EdX courses that were created through course creation tasks.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_edx_course_list import PaginatedEdxCourseList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str | A search term. (optional)
task = 56 # int |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_course_list(org, user_id, ordering=ordering, page=page, page_size=page_size, search=search, task=task)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_course_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_course_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **task** | **int**|  | [optional] 

### Return type

[**PaginatedEdxCourseList**](PaginatedEdxCourseList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_course_load_from_edx_retrieve**
> ai_mentor_orgs_users_course_creation_course_load_from_edx_retrieve(id, org, user_id)



Load existing course structure from OpenEdX.  This action starts a background task to pull the course structure from the EdX platform into the database.  Args:     request: The HTTP request.     pk: The primary key of the course to load.  Returns:     Response: A confirmation that the load task has been started.  Raises:     NotFound: If the specified course does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this edx course.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_course_load_from_edx_retrieve(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_course_load_from_edx_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edx course. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Course load started successfully |  -  |
**404** | Course not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_course_retrieve**
> EdxCourse ai_mentor_orgs_users_course_creation_course_retrieve(id, org, user_id)



API viewset for managing EdX courses.  This viewset allows platform administrators to retrieve, delete, and perform various operations on EdX courses that were created through course creation tasks.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.edx_course import EdxCourse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this edx course.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_course_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_course_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_course_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edx course. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**EdxCourse**](EdxCourse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_course_sync_to_edx_retrieve**
> ai_mentor_orgs_users_course_creation_course_sync_to_edx_retrieve(id, org, user_id)



Synchronize the course structure to EdX.  This action starts a background task to push the course structure from the database to the EdX platform.  Args:     request: The HTTP request.     pk: The primary key of the course to synchronize.  Returns:     Response: A confirmation that the sync task has been started.  Raises:     NotFound: If the specified course does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this edx course.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_course_sync_to_edx_retrieve(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_course_sync_to_edx_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edx course. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Course sync started successfully |  -  |
**404** | Course not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_files_create**
> CourseCreationTaskFile ai_mentor_orgs_users_course_creation_files_create(org, user_id, id, course_creation_task, file, date_created, last_modified)



Endpoint to fetch update and delete files associated with course creation tasks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task_file import CourseCreationTaskFile
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
id = 56 # int | 
course_creation_task = 56 # int | 
file = 'file_example' # str | 
date_created = '2013-10-20T19:20:30+01:00' # datetime | 
last_modified = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_files_create(org, user_id, id, course_creation_task, file, date_created, last_modified)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_files_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_files_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **id** | **int**|  | 
 **course_creation_task** | **int**|  | 
 **file** | **str**|  | 
 **date_created** | **datetime**|  | 
 **last_modified** | **datetime**|  | 

### Return type

[**CourseCreationTaskFile**](CourseCreationTaskFile.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_files_destroy**
> ai_mentor_orgs_users_course_creation_files_destroy(id, org, user_id)



Endpoint to fetch update and delete files associated with course creation tasks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task file.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_files_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_files_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task file. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_files_list**
> PaginatedCourseCreationTaskFileList ai_mentor_orgs_users_course_creation_files_list(org, user_id, page=page, page_size=page_size)



Endpoint to fetch update and delete files associated with course creation tasks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_course_creation_task_file_list import PaginatedCourseCreationTaskFileList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_files_list(org, user_id, page=page, page_size=page_size)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_files_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_files_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedCourseCreationTaskFileList**](PaginatedCourseCreationTaskFileList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_files_partial_update**
> CourseCreationTaskFile ai_mentor_orgs_users_course_creation_files_partial_update(id, org, user_id, id2=id2, course_creation_task=course_creation_task, file=file, date_created=date_created, last_modified=last_modified)



Endpoint to fetch update and delete files associated with course creation tasks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task_file import CourseCreationTaskFile
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task file.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
id2 = 56 # int |  (optional)
course_creation_task = 56 # int |  (optional)
file = 'file_example' # str |  (optional)
date_created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
last_modified = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_files_partial_update(id, org, user_id, id2=id2, course_creation_task=course_creation_task, file=file, date_created=date_created, last_modified=last_modified)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_files_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_files_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task file. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **id2** | **int**|  | [optional] 
 **course_creation_task** | **int**|  | [optional] 
 **file** | **str**|  | [optional] 
 **date_created** | **datetime**|  | [optional] 
 **last_modified** | **datetime**|  | [optional] 

### Return type

[**CourseCreationTaskFile**](CourseCreationTaskFile.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_files_retrieve**
> CourseCreationTaskFile ai_mentor_orgs_users_course_creation_files_retrieve(id, org, user_id)



Endpoint to fetch update and delete files associated with course creation tasks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task_file import CourseCreationTaskFile
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task file.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_files_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_files_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_files_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task file. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CourseCreationTaskFile**](CourseCreationTaskFile.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_files_update**
> CourseCreationTaskFile ai_mentor_orgs_users_course_creation_files_update(id, org, user_id, id2, course_creation_task, file, date_created, last_modified)



Endpoint to fetch update and delete files associated with course creation tasks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task_file import CourseCreationTaskFile
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task file.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
id2 = 56 # int | 
course_creation_task = 56 # int | 
file = 'file_example' # str | 
date_created = '2013-10-20T19:20:30+01:00' # datetime | 
last_modified = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_files_update(id, org, user_id, id2, course_creation_task, file, date_created, last_modified)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_files_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_files_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task file. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **id2** | **int**|  | 
 **course_creation_task** | **int**|  | 
 **file** | **str**|  | 
 **date_created** | **datetime**|  | 
 **last_modified** | **datetime**|  | 

### Return type

[**CourseCreationTaskFile**](CourseCreationTaskFile.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_section_create**
> Section ai_mentor_orgs_users_course_creation_section_create(org, user_id, section)



API viewset for managing course sections.  This viewset allows platform administrators to retrieve and manage sections within EdX courses.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.section import Section
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
section = iblai.Section() # Section | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_section_create(org, user_id, section)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_section_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_section_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **section** | [**Section**](Section.md)|  | 

### Return type

[**Section**](Section.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_section_destroy**
> ai_mentor_orgs_users_course_creation_section_destroy(id, org, user_id)



API viewset for managing course sections.  This viewset allows platform administrators to retrieve and manage sections within EdX courses.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this section.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_section_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_section_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this section. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_section_list**
> PaginatedSectionList ai_mentor_orgs_users_course_creation_section_list(org, user_id, course=course, ordering=ordering, page=page, page_size=page_size, search=search, task=task)



API viewset for managing course sections.  This viewset allows platform administrators to retrieve and manage sections within EdX courses.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_section_list import PaginatedSectionList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
course = 56 # int |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str | A search term. (optional)
task = 56 # int |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_section_list(org, user_id, course=course, ordering=ordering, page=page, page_size=page_size, search=search, task=task)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_section_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_section_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **course** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **task** | **int**|  | [optional] 

### Return type

[**PaginatedSectionList**](PaginatedSectionList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_section_partial_update**
> Section ai_mentor_orgs_users_course_creation_section_partial_update(id, org, user_id, patched_section=patched_section)



API viewset for managing course sections.  This viewset allows platform administrators to retrieve and manage sections within EdX courses.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_section import PatchedSection
from iblai.models.section import Section
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this section.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
patched_section = iblai.PatchedSection() # PatchedSection |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_section_partial_update(id, org, user_id, patched_section=patched_section)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_section_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_section_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this section. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **patched_section** | [**PatchedSection**](PatchedSection.md)|  | [optional] 

### Return type

[**Section**](Section.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_section_retrieve**
> Section ai_mentor_orgs_users_course_creation_section_retrieve(id, org, user_id)



API viewset for managing course sections.  This viewset allows platform administrators to retrieve and manage sections within EdX courses.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.section import Section
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this section.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_section_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_section_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_section_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this section. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Section**](Section.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_section_update**
> Section ai_mentor_orgs_users_course_creation_section_update(id, org, user_id, section)



API viewset for managing course sections.  This viewset allows platform administrators to retrieve and manage sections within EdX courses.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.section import Section
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this section.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
section = iblai.Section() # Section | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_section_update(id, org, user_id, section)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_section_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_section_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this section. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **section** | [**Section**](Section.md)|  | 

### Return type

[**Section**](Section.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_subsection_create**
> SubSection ai_mentor_orgs_users_course_creation_subsection_create(org, user_id, sub_section)



API viewset for managing course subsections.  This viewset allows platform administrators to retrieve and manage subsections within course sections.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.sub_section import SubSection
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
sub_section = iblai.SubSection() # SubSection | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_subsection_create(org, user_id, sub_section)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_subsection_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_subsection_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **sub_section** | [**SubSection**](SubSection.md)|  | 

### Return type

[**SubSection**](SubSection.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_subsection_destroy**
> ai_mentor_orgs_users_course_creation_subsection_destroy(id, org, user_id)



API viewset for managing course subsections.  This viewset allows platform administrators to retrieve and manage subsections within course sections.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this sub section.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_subsection_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_subsection_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sub section. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_subsection_list**
> PaginatedSubSectionList ai_mentor_orgs_users_course_creation_subsection_list(org, user_id, course=course, ordering=ordering, page=page, page_size=page_size, search=search, section=section, task=task)



API viewset for managing course subsections.  This viewset allows platform administrators to retrieve and manage subsections within course sections.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_sub_section_list import PaginatedSubSectionList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
course = 56 # int |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str | A search term. (optional)
section = 56 # int |  (optional)
task = 56 # int |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_subsection_list(org, user_id, course=course, ordering=ordering, page=page, page_size=page_size, search=search, section=section, task=task)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_subsection_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_subsection_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **course** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **section** | **int**|  | [optional] 
 **task** | **int**|  | [optional] 

### Return type

[**PaginatedSubSectionList**](PaginatedSubSectionList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_subsection_partial_update**
> SubSection ai_mentor_orgs_users_course_creation_subsection_partial_update(id, org, user_id, patched_sub_section=patched_sub_section)



API viewset for managing course subsections.  This viewset allows platform administrators to retrieve and manage subsections within course sections.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_sub_section import PatchedSubSection
from iblai.models.sub_section import SubSection
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this sub section.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
patched_sub_section = iblai.PatchedSubSection() # PatchedSubSection |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_subsection_partial_update(id, org, user_id, patched_sub_section=patched_sub_section)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_subsection_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_subsection_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sub section. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **patched_sub_section** | [**PatchedSubSection**](PatchedSubSection.md)|  | [optional] 

### Return type

[**SubSection**](SubSection.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_subsection_retrieve**
> SubSection ai_mentor_orgs_users_course_creation_subsection_retrieve(id, org, user_id)



API viewset for managing course subsections.  This viewset allows platform administrators to retrieve and manage subsections within course sections.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.sub_section import SubSection
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this sub section.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_subsection_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_subsection_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_subsection_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sub section. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**SubSection**](SubSection.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_subsection_update**
> SubSection ai_mentor_orgs_users_course_creation_subsection_update(id, org, user_id, sub_section)



API viewset for managing course subsections.  This viewset allows platform administrators to retrieve and manage subsections within course sections.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.sub_section import SubSection
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this sub section.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
sub_section = iblai.SubSection() # SubSection | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_subsection_update(id, org, user_id, sub_section)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_subsection_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_subsection_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sub section. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **sub_section** | [**SubSection**](SubSection.md)|  | 

### Return type

[**SubSection**](SubSection.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_task_files_create**
> CourseCreationTaskFile ai_mentor_orgs_users_course_creation_task_files_create(org, user_id, id, course_creation_task, file, date_created, last_modified)



Endpoint to fetch update and delete files associated with course creation tasks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task_file import CourseCreationTaskFile
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
id = 56 # int | 
course_creation_task = 56 # int | 
file = 'file_example' # str | 
date_created = '2013-10-20T19:20:30+01:00' # datetime | 
last_modified = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_task_files_create(org, user_id, id, course_creation_task, file, date_created, last_modified)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_task_files_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_task_files_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **id** | **int**|  | 
 **course_creation_task** | **int**|  | 
 **file** | **str**|  | 
 **date_created** | **datetime**|  | 
 **last_modified** | **datetime**|  | 

### Return type

[**CourseCreationTaskFile**](CourseCreationTaskFile.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_task_files_destroy**
> ai_mentor_orgs_users_course_creation_task_files_destroy(id, org, user_id)



Endpoint to fetch update and delete files associated with course creation tasks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task file.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_task_files_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_task_files_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task file. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_task_files_list**
> PaginatedCourseCreationTaskFileList ai_mentor_orgs_users_course_creation_task_files_list(org, user_id, page=page, page_size=page_size)



Endpoint to fetch update and delete files associated with course creation tasks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_course_creation_task_file_list import PaginatedCourseCreationTaskFileList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_task_files_list(org, user_id, page=page, page_size=page_size)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_task_files_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_task_files_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedCourseCreationTaskFileList**](PaginatedCourseCreationTaskFileList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_task_files_partial_update**
> CourseCreationTaskFile ai_mentor_orgs_users_course_creation_task_files_partial_update(id, org, user_id, id2=id2, course_creation_task=course_creation_task, file=file, date_created=date_created, last_modified=last_modified)



Endpoint to fetch update and delete files associated with course creation tasks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task_file import CourseCreationTaskFile
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task file.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
id2 = 56 # int |  (optional)
course_creation_task = 56 # int |  (optional)
file = 'file_example' # str |  (optional)
date_created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
last_modified = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_task_files_partial_update(id, org, user_id, id2=id2, course_creation_task=course_creation_task, file=file, date_created=date_created, last_modified=last_modified)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_task_files_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_task_files_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task file. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **id2** | **int**|  | [optional] 
 **course_creation_task** | **int**|  | [optional] 
 **file** | **str**|  | [optional] 
 **date_created** | **datetime**|  | [optional] 
 **last_modified** | **datetime**|  | [optional] 

### Return type

[**CourseCreationTaskFile**](CourseCreationTaskFile.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_task_files_retrieve**
> CourseCreationTaskFile ai_mentor_orgs_users_course_creation_task_files_retrieve(id, org, user_id)



Endpoint to fetch update and delete files associated with course creation tasks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task_file import CourseCreationTaskFile
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task file.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_task_files_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_task_files_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_task_files_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task file. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CourseCreationTaskFile**](CourseCreationTaskFile.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_task_files_update**
> CourseCreationTaskFile ai_mentor_orgs_users_course_creation_task_files_update(id, org, user_id, id2, course_creation_task, file, date_created, last_modified)



Endpoint to fetch update and delete files associated with course creation tasks.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task_file import CourseCreationTaskFile
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task file.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
id2 = 56 # int | 
course_creation_task = 56 # int | 
file = 'file_example' # str | 
date_created = '2013-10-20T19:20:30+01:00' # datetime | 
last_modified = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_task_files_update(id, org, user_id, id2, course_creation_task, file, date_created, last_modified)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_task_files_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_task_files_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task file. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **id2** | **int**|  | 
 **course_creation_task** | **int**|  | 
 **file** | **str**|  | 
 **date_created** | **datetime**|  | 
 **last_modified** | **datetime**|  | 

### Return type

[**CourseCreationTaskFile**](CourseCreationTaskFile.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve**
> CourseCreationTask ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve(id, org, user_id)



Cancel a course creation task run. ** Conditions Required **: The task must be running or pending. ** Response **: - 200: The course creation task is successfully cancelled. - 400: The course creation task is not in a running or pending state.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task import CourseCreationTask
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CourseCreationTask**](CourseCreationTask.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve2**
> CourseCreationTask ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve2(id, org, user_id)



Cancel a course creation task run. ** Conditions Required **: The task must be running or pending. ** Response **: - 200: The course creation task is successfully cancelled. - 400: The course creation task is not in a running or pending state.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task import CourseCreationTask
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve2(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_cancel_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CourseCreationTask**](CourseCreationTask.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_create**
> CourseCreationTask ai_mentor_orgs_users_course_creation_tasks_create(org, user_id, id, user_id2, student, name, description, target_audience, platform, platform_key, status, course_data, logs, files, date_created, last_modified, publish_course=publish_course, provider=provider, model=model, desired_number_of_sections=desired_number_of_sections)



Create, retrieve and delete course creation tasks  Course creation tasks allow you to schedule the creation of a course on OpenEdx deployment connected to this data manager.  The course is created entirely by an ai model (as specified in your inputs).  The llm decides on the content of the course based on the name, description, target audience and other parameters. Bigger and newer models tend to outperform smaller once.  Clear and unambiguous parameters are more likely to produce better results.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task import CourseCreationTask
from iblai.models.course_creation_task_file import CourseCreationTaskFile
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
id = 56 # int | 
user_id2 = 'user_id_example' # str | 
student = 56 # int | edX user ID
name = 'name_example' # str | 
description = 'description_example' # str | Description of the course to create and its requirements
target_audience = 'target_audience_example' # str | The intended audience for the course. eg. Grade 11 students.
platform = 56 # int | 
platform_key = 'platform_key_example' # str | 
status = iblai.CourseCreationTaskStatusEnum() # CourseCreationTaskStatusEnum | 
course_data = None # object | 
logs = 'logs_example' # str | 
files = [iblai.CourseCreationTaskFile()] # List[CourseCreationTaskFile] | 
date_created = '2013-10-20T19:20:30+01:00' # datetime | 
last_modified = '2013-10-20T19:20:30+01:00' # datetime | 
publish_course = True # bool |  (optional)
provider = 'provider_example' # str |  (optional)
model = 'model_example' # str |  (optional)
desired_number_of_sections = 56 # int |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_create(org, user_id, id, user_id2, student, name, description, target_audience, platform, platform_key, status, course_data, logs, files, date_created, last_modified, publish_course=publish_course, provider=provider, model=model, desired_number_of_sections=desired_number_of_sections)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **id** | **int**|  | 
 **user_id2** | **str**|  | 
 **student** | **int**| edX user ID | 
 **name** | **str**|  | 
 **description** | **str**| Description of the course to create and its requirements | 
 **target_audience** | **str**| The intended audience for the course. eg. Grade 11 students. | 
 **platform** | **int**|  | 
 **platform_key** | **str**|  | 
 **status** | [**CourseCreationTaskStatusEnum**](CourseCreationTaskStatusEnum.md)|  | 
 **course_data** | [**object**](object.md)|  | 
 **logs** | **str**|  | 
 **files** | [**List[CourseCreationTaskFile]**](CourseCreationTaskFile.md)|  | 
 **date_created** | **datetime**|  | 
 **last_modified** | **datetime**|  | 
 **publish_course** | **bool**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **model** | **str**|  | [optional] 
 **desired_number_of_sections** | **int**|  | [optional] 

### Return type

[**CourseCreationTask**](CourseCreationTask.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_create2**
> CourseCreationTask ai_mentor_orgs_users_course_creation_tasks_create2(org, user_id, id, user_id2, student, name, description, target_audience, platform, platform_key, status, course_data, logs, files, date_created, last_modified, publish_course=publish_course, provider=provider, model=model, desired_number_of_sections=desired_number_of_sections)



Create, retrieve and delete course creation tasks  Course creation tasks allow you to schedule the creation of a course on OpenEdx deployment connected to this data manager.  The course is created entirely by an ai model (as specified in your inputs).  The llm decides on the content of the course based on the name, description, target audience and other parameters. Bigger and newer models tend to outperform smaller once.  Clear and unambiguous parameters are more likely to produce better results.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task import CourseCreationTask
from iblai.models.course_creation_task_file import CourseCreationTaskFile
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
id = 56 # int | 
user_id2 = 'user_id_example' # str | 
student = 56 # int | edX user ID
name = 'name_example' # str | 
description = 'description_example' # str | Description of the course to create and its requirements
target_audience = 'target_audience_example' # str | The intended audience for the course. eg. Grade 11 students.
platform = 56 # int | 
platform_key = 'platform_key_example' # str | 
status = iblai.CourseCreationTaskStatusEnum() # CourseCreationTaskStatusEnum | 
course_data = None # object | 
logs = 'logs_example' # str | 
files = [iblai.CourseCreationTaskFile()] # List[CourseCreationTaskFile] | 
date_created = '2013-10-20T19:20:30+01:00' # datetime | 
last_modified = '2013-10-20T19:20:30+01:00' # datetime | 
publish_course = True # bool |  (optional)
provider = 'provider_example' # str |  (optional)
model = 'model_example' # str |  (optional)
desired_number_of_sections = 56 # int |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_create2(org, user_id, id, user_id2, student, name, description, target_audience, platform, platform_key, status, course_data, logs, files, date_created, last_modified, publish_course=publish_course, provider=provider, model=model, desired_number_of_sections=desired_number_of_sections)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_create2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **id** | **int**|  | 
 **user_id2** | **str**|  | 
 **student** | **int**| edX user ID | 
 **name** | **str**|  | 
 **description** | **str**| Description of the course to create and its requirements | 
 **target_audience** | **str**| The intended audience for the course. eg. Grade 11 students. | 
 **platform** | **int**|  | 
 **platform_key** | **str**|  | 
 **status** | [**CourseCreationTaskStatusEnum**](CourseCreationTaskStatusEnum.md)|  | 
 **course_data** | [**object**](object.md)|  | 
 **logs** | **str**|  | 
 **files** | [**List[CourseCreationTaskFile]**](CourseCreationTaskFile.md)|  | 
 **date_created** | **datetime**|  | 
 **last_modified** | **datetime**|  | 
 **publish_course** | **bool**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **model** | **str**|  | [optional] 
 **desired_number_of_sections** | **int**|  | [optional] 

### Return type

[**CourseCreationTask**](CourseCreationTask.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create**
> FullCourse ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create(id, org, user_id, id2, user_id2, student, name, description, target_audience, platform, platform_key, status, course_data, logs, files, date_created, last_modified, publish_course=publish_course, provider=provider, model=model, desired_number_of_sections=desired_number_of_sections)



This is intended for stepwise approach of course creation.  Use this to intiate generating an outline of the course.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task_file import CourseCreationTaskFile
from iblai.models.full_course import FullCourse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
id2 = 56 # int | 
user_id2 = 'user_id_example' # str | 
student = 56 # int | edX user ID
name = 'name_example' # str | 
description = 'description_example' # str | Description of the course to create and its requirements
target_audience = 'target_audience_example' # str | The intended audience for the course. eg. Grade 11 students.
platform = 56 # int | 
platform_key = 'platform_key_example' # str | 
status = iblai.CourseCreationTaskStatusEnum() # CourseCreationTaskStatusEnum | 
course_data = None # object | 
logs = 'logs_example' # str | 
files = [iblai.CourseCreationTaskFile()] # List[CourseCreationTaskFile] | 
date_created = '2013-10-20T19:20:30+01:00' # datetime | 
last_modified = '2013-10-20T19:20:30+01:00' # datetime | 
publish_course = True # bool |  (optional)
provider = 'provider_example' # str |  (optional)
model = 'model_example' # str |  (optional)
desired_number_of_sections = 56 # int |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create(id, org, user_id, id2, user_id2, student, name, description, target_audience, platform, platform_key, status, course_data, logs, files, date_created, last_modified, publish_course=publish_course, provider=provider, model=model, desired_number_of_sections=desired_number_of_sections)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **id2** | **int**|  | 
 **user_id2** | **str**|  | 
 **student** | **int**| edX user ID | 
 **name** | **str**|  | 
 **description** | **str**| Description of the course to create and its requirements | 
 **target_audience** | **str**| The intended audience for the course. eg. Grade 11 students. | 
 **platform** | **int**|  | 
 **platform_key** | **str**|  | 
 **status** | [**CourseCreationTaskStatusEnum**](CourseCreationTaskStatusEnum.md)|  | 
 **course_data** | [**object**](object.md)|  | 
 **logs** | **str**|  | 
 **files** | [**List[CourseCreationTaskFile]**](CourseCreationTaskFile.md)|  | 
 **date_created** | **datetime**|  | 
 **last_modified** | **datetime**|  | 
 **publish_course** | **bool**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **model** | **str**|  | [optional] 
 **desired_number_of_sections** | **int**|  | [optional] 

### Return type

[**FullCourse**](FullCourse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create2**
> FullCourse ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create2(id, org, user_id, id2, user_id2, student, name, description, target_audience, platform, platform_key, status, course_data, logs, files, date_created, last_modified, publish_course=publish_course, provider=provider, model=model, desired_number_of_sections=desired_number_of_sections)



This is intended for stepwise approach of course creation.  Use this to intiate generating an outline of the course.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task_file import CourseCreationTaskFile
from iblai.models.full_course import FullCourse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
id2 = 56 # int | 
user_id2 = 'user_id_example' # str | 
student = 56 # int | edX user ID
name = 'name_example' # str | 
description = 'description_example' # str | Description of the course to create and its requirements
target_audience = 'target_audience_example' # str | The intended audience for the course. eg. Grade 11 students.
platform = 56 # int | 
platform_key = 'platform_key_example' # str | 
status = iblai.CourseCreationTaskStatusEnum() # CourseCreationTaskStatusEnum | 
course_data = None # object | 
logs = 'logs_example' # str | 
files = [iblai.CourseCreationTaskFile()] # List[CourseCreationTaskFile] | 
date_created = '2013-10-20T19:20:30+01:00' # datetime | 
last_modified = '2013-10-20T19:20:30+01:00' # datetime | 
publish_course = True # bool |  (optional)
provider = 'provider_example' # str |  (optional)
model = 'model_example' # str |  (optional)
desired_number_of_sections = 56 # int |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create2(id, org, user_id, id2, user_id2, student, name, description, target_audience, platform, platform_key, status, course_data, logs, files, date_created, last_modified, publish_course=publish_course, provider=provider, model=model, desired_number_of_sections=desired_number_of_sections)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_create_course_outline_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **id2** | **int**|  | 
 **user_id2** | **str**|  | 
 **student** | **int**| edX user ID | 
 **name** | **str**|  | 
 **description** | **str**| Description of the course to create and its requirements | 
 **target_audience** | **str**| The intended audience for the course. eg. Grade 11 students. | 
 **platform** | **int**|  | 
 **platform_key** | **str**|  | 
 **status** | [**CourseCreationTaskStatusEnum**](CourseCreationTaskStatusEnum.md)|  | 
 **course_data** | [**object**](object.md)|  | 
 **logs** | **str**|  | 
 **files** | [**List[CourseCreationTaskFile]**](CourseCreationTaskFile.md)|  | 
 **date_created** | **datetime**|  | 
 **last_modified** | **datetime**|  | 
 **publish_course** | **bool**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **model** | **str**|  | [optional] 
 **desired_number_of_sections** | **int**|  | [optional] 

### Return type

[**FullCourse**](FullCourse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve**
> FullCourse ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve(id, org, user_id)



This is intended for stepwise approach of course creation.  Use this to intiate generating an outline of the course.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.full_course import FullCourse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**FullCourse**](FullCourse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve2**
> FullCourse ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve2(id, org, user_id)



This is intended for stepwise approach of course creation.  Use this to intiate generating an outline of the course.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.full_course import FullCourse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve2(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_create_course_outline_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**FullCourse**](FullCourse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_destroy**
> ai_mentor_orgs_users_course_creation_tasks_destroy(id, org, user_id)



Create, retrieve and delete course creation tasks  Course creation tasks allow you to schedule the creation of a course on OpenEdx deployment connected to this data manager.  The course is created entirely by an ai model (as specified in your inputs).  The llm decides on the content of the course based on the name, description, target audience and other parameters. Bigger and newer models tend to outperform smaller once.  Clear and unambiguous parameters are more likely to produce better results.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_tasks_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_destroy2**
> ai_mentor_orgs_users_course_creation_tasks_destroy2(id, org, user_id)



Create, retrieve and delete course creation tasks  Course creation tasks allow you to schedule the creation of a course on OpenEdx deployment connected to this data manager.  The course is created entirely by an ai model (as specified in your inputs).  The llm decides on the content of the course based on the name, description, target audience and other parameters. Bigger and newer models tend to outperform smaller once.  Clear and unambiguous parameters are more likely to produce better results.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_tasks_destroy2(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_destroy2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_list**
> PaginatedCourseCreationTaskList ai_mentor_orgs_users_course_creation_tasks_list(org, user_id, page=page, page_size=page_size)



Create, retrieve and delete course creation tasks  Course creation tasks allow you to schedule the creation of a course on OpenEdx deployment connected to this data manager.  The course is created entirely by an ai model (as specified in your inputs).  The llm decides on the content of the course based on the name, description, target audience and other parameters. Bigger and newer models tend to outperform smaller once.  Clear and unambiguous parameters are more likely to produce better results.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_course_creation_task_list import PaginatedCourseCreationTaskList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_list(org, user_id, page=page, page_size=page_size)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedCourseCreationTaskList**](PaginatedCourseCreationTaskList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_list2**
> PaginatedCourseCreationTaskList ai_mentor_orgs_users_course_creation_tasks_list2(org, user_id, page=page, page_size=page_size)



Create, retrieve and delete course creation tasks  Course creation tasks allow you to schedule the creation of a course on OpenEdx deployment connected to this data manager.  The course is created entirely by an ai model (as specified in your inputs).  The llm decides on the content of the course based on the name, description, target audience and other parameters. Bigger and newer models tend to outperform smaller once.  Clear and unambiguous parameters are more likely to produce better results.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_course_creation_task_list import PaginatedCourseCreationTaskList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_list2(org, user_id, page=page, page_size=page_size)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_list2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_list2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedCourseCreationTaskList**](PaginatedCourseCreationTaskList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_retrieve**
> CourseCreationTask ai_mentor_orgs_users_course_creation_tasks_retrieve(id, org, user_id)



Create, retrieve and delete course creation tasks  Course creation tasks allow you to schedule the creation of a course on OpenEdx deployment connected to this data manager.  The course is created entirely by an ai model (as specified in your inputs).  The llm decides on the content of the course based on the name, description, target audience and other parameters. Bigger and newer models tend to outperform smaller once.  Clear and unambiguous parameters are more likely to produce better results.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task import CourseCreationTask
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CourseCreationTask**](CourseCreationTask.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_retrieve2**
> CourseCreationTask ai_mentor_orgs_users_course_creation_tasks_retrieve2(id, org, user_id)



Create, retrieve and delete course creation tasks  Course creation tasks allow you to schedule the creation of a course on OpenEdx deployment connected to this data manager.  The course is created entirely by an ai model (as specified in your inputs).  The llm decides on the content of the course based on the name, description, target audience and other parameters. Bigger and newer models tend to outperform smaller once.  Clear and unambiguous parameters are more likely to produce better results.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task import CourseCreationTask
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_retrieve2(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CourseCreationTask**](CourseCreationTask.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_start_retrieve**
> CourseCreationTask ai_mentor_orgs_users_course_creation_tasks_start_retrieve(id, org, user_id)



Kick start the course creation task. This endpoint should be called once the files for a course creation task has been successfully uploaded.  ** Conditions Required **: - The course creation task must be in a pending state or failed state.  ** Response **: - 200: The course creation task is successfully started. - 400: The course creation task is not in a pending state.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task import CourseCreationTask
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_start_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_start_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_start_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CourseCreationTask**](CourseCreationTask.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_tasks_start_retrieve2**
> CourseCreationTask ai_mentor_orgs_users_course_creation_tasks_start_retrieve2(id, org, user_id)



Kick start the course creation task. This endpoint should be called once the files for a course creation task has been successfully uploaded.  ** Conditions Required **: - The course creation task must be in a pending state or failed state.  ** Response **: - 200: The course creation task is successfully started. - 400: The course creation task is not in a pending state.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.course_creation_task import CourseCreationTask
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this course creation task.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_tasks_start_retrieve2(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_start_retrieve2:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_tasks_start_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this course creation task. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CourseCreationTask**](CourseCreationTask.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_unit_create**
> Unit ai_mentor_orgs_users_course_creation_unit_create(org, user_id, unit)



API viewset for managing course units.  This viewset allows platform administrators to retrieve and manage units within course subsections, and generate content for them.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.unit import Unit
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
unit = iblai.Unit() # Unit | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_unit_create(org, user_id, unit)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_unit_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_unit_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **unit** | [**Unit**](Unit.md)|  | 

### Return type

[**Unit**](Unit.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_unit_destroy**
> ai_mentor_orgs_users_course_creation_unit_destroy(id, org, user_id)



API viewset for managing course units.  This viewset allows platform administrators to retrieve and manage units within course subsections, and generate content for them.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this unit.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_unit_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_unit_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this unit. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_unit_draft_content_create**
> ai_mentor_orgs_users_course_creation_unit_draft_content_create(id, org, user_id, unit)



Generate draft content for a specific unit.  This action starts a background task to create draft content for the specified unit using AI.  Args:     request: The HTTP request.     pk: The primary key of the unit to generate content for.  Returns:     Response: A confirmation that the content generation task has been started.  Raises:     NotFound: If the specified unit does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.unit import Unit
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this unit.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
unit = iblai.Unit() # Unit | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_unit_draft_content_create(id, org, user_id, unit)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_unit_draft_content_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this unit. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **unit** | [**Unit**](Unit.md)|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Content creation started successfully |  -  |
**404** | Unit not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_unit_draft_content_retrieve**
> ai_mentor_orgs_users_course_creation_unit_draft_content_retrieve(id, org, user_id)



Generate draft content for a specific unit.  This action starts a background task to create draft content for the specified unit using AI.  Args:     request: The HTTP request.     pk: The primary key of the unit to generate content for.  Returns:     Response: A confirmation that the content generation task has been started.  Raises:     NotFound: If the specified unit does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this unit.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_course_creation_unit_draft_content_retrieve(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_unit_draft_content_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this unit. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Content creation started successfully |  -  |
**404** | Unit not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_unit_list**
> PaginatedUnitList ai_mentor_orgs_users_course_creation_unit_list(org, user_id, course=course, ordering=ordering, page=page, page_size=page_size, search=search, section=section, subsection=subsection, task=task)



API viewset for managing course units.  This viewset allows platform administrators to retrieve and manage units within course subsections, and generate content for them.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_unit_list import PaginatedUnitList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
course = 56 # int |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str | A search term. (optional)
section = 56 # int |  (optional)
subsection = 56 # int |  (optional)
task = 56 # int |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_unit_list(org, user_id, course=course, ordering=ordering, page=page, page_size=page_size, search=search, section=section, subsection=subsection, task=task)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_unit_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_unit_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **course** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **section** | **int**|  | [optional] 
 **subsection** | **int**|  | [optional] 
 **task** | **int**|  | [optional] 

### Return type

[**PaginatedUnitList**](PaginatedUnitList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_unit_partial_update**
> Unit ai_mentor_orgs_users_course_creation_unit_partial_update(id, org, user_id, patched_unit=patched_unit)



API viewset for managing course units.  This viewset allows platform administrators to retrieve and manage units within course subsections, and generate content for them.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_unit import PatchedUnit
from iblai.models.unit import Unit
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this unit.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
patched_unit = iblai.PatchedUnit() # PatchedUnit |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_unit_partial_update(id, org, user_id, patched_unit=patched_unit)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_unit_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_unit_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this unit. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **patched_unit** | [**PatchedUnit**](PatchedUnit.md)|  | [optional] 

### Return type

[**Unit**](Unit.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_unit_retrieve**
> Unit ai_mentor_orgs_users_course_creation_unit_retrieve(id, org, user_id)



API viewset for managing course units.  This viewset allows platform administrators to retrieve and manage units within course subsections, and generate content for them.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.unit import Unit
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this unit.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_unit_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_unit_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_unit_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this unit. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Unit**](Unit.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_course_creation_unit_update**
> Unit ai_mentor_orgs_users_course_creation_unit_update(id, org, user_id, unit)



API viewset for managing course units.  This viewset allows platform administrators to retrieve and manage units within course subsections, and generate content for them.  Permissions:     - Restricted to platform administrators only

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.unit import Unit
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this unit.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
unit = iblai.Unit() # Unit | 

try:
    api_response = api_instance.ai_mentor_orgs_users_course_creation_unit_update(id, org, user_id, unit)
    print("The response of AiMentorApi->ai_mentor_orgs_users_course_creation_unit_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_course_creation_unit_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this unit. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **unit** | [**Unit**](Unit.md)|  | 

### Return type

[**Unit**](Unit.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_create**
> Mentor ai_mentor_orgs_users_create(org, user_id, mentor_create, department_id=department_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)



Create a new mentor.  Body Parameters:     - name: Mentor name.     - unique_id: Unique identifier.     - platform_key: Associated platform.     - metadata: Additional mentor attributes.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
from iblai.models.mentor_create import MentorCreate
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_create = {"name":"John Doe","unique_id":"1234","platform_key":"main","metadata":{"specialty":"AI"}} # MentorCreate | 
department_id = 56 # int | Department to filter by (optional)
filter_by = 'filter_by_example' # str | Filter options include, date, name, default is date  (optional)
metadata_key = 'metadata_key_example' # str | Metadata key to be queried with (optional)
metadata_value = 'metadata_value_example' # str | Metadata value to be filter for (optional)
return_session_information = True # bool | Declares if session information should be included in the mentor data (optional)
visibility = 'visibility_example' # str | visibility type  to be queried with (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_create(org, user_id, mentor_create, department_id=department_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)
    print("The response of AiMentorApi->ai_mentor_orgs_users_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_create** | [**MentorCreate**](MentorCreate.md)|  | 
 **department_id** | **int**| Department to filter by | [optional] 
 **filter_by** | **str**| Filter options include, date, name, default is date  | [optional] 
 **metadata_key** | **str**| Metadata key to be queried with | [optional] 
 **metadata_value** | **str**| Metadata value to be filter for | [optional] 
 **return_session_information** | **bool**| Declares if session information should be included in the mentor data | [optional] 
 **visibility** | **str**| visibility type  to be queried with | [optional] 

### Return type

[**Mentor**](Mentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_create_mentor_wizard_create**
> Mentor ai_mentor_orgs_users_create_mentor_wizard_create(org, user_id, mentor_wizard)



Create a new mentor using the wizard interface.  Args:     request: The HTTP request containing the mentor data.     org: The organization/tenant identifier.     user_id: The ID of the user creating the mentor.  Returns:     Response: The created mentor.  Raises:     BadRequest: If the provided data is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
from iblai.models.mentor_wizard import MentorWizard
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_wizard = {"name":"Data Science Mentor","description":"A mentor specialized in data science and machine learning concepts."} # MentorWizard | 

try:
    api_response = api_instance.ai_mentor_orgs_users_create_mentor_wizard_create(org, user_id, mentor_wizard)
    print("The response of AiMentorApi->ai_mentor_orgs_users_create_mentor_wizard_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_create_mentor_wizard_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_wizard** | [**MentorWizard**](MentorWizard.md)|  | 

### Return type

[**Mentor**](Mentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Invalid data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_custom_instruction_create**
> CustomInstructionResponse ai_mentor_orgs_users_custom_instruction_create(org, user_id, custom_instruction_response=custom_instruction_response)



Create a new custom instruction for a user.  Args:     request: The HTTP request containing the custom instruction data.     org: The organization/tenant identifier.     user_id: The ID of the user to create custom instructions for.  Returns:     Response: The created custom instruction.  Raises:     BadRequest: If the provided data is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.custom_instruction_response import CustomInstructionResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
custom_instruction_response = {"content":"Always explain concepts in simple terms with examples."} # CustomInstructionResponse |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_custom_instruction_create(org, user_id, custom_instruction_response=custom_instruction_response)
    print("The response of AiMentorApi->ai_mentor_orgs_users_custom_instruction_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_custom_instruction_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **custom_instruction_response** | [**CustomInstructionResponse**](CustomInstructionResponse.md)|  | [optional] 

### Return type

[**CustomInstructionResponse**](CustomInstructionResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Invalid data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_custom_instruction_retrieve**
> CustomInstructionResponse ai_mentor_orgs_users_custom_instruction_retrieve(org, user_id)



Retrieve custom instructions for a specific user.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user to retrieve custom instructions for.  Returns:     Response: The custom instructions for the user.  Raises:     NotFound: If no custom instructions exist for the user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.custom_instruction_response import CustomInstructionResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_custom_instruction_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_custom_instruction_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_custom_instruction_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**CustomInstructionResponse**](CustomInstructionResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Custom instruction not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_custom_instruction_update**
> CustomInstructionResponse ai_mentor_orgs_users_custom_instruction_update(org, user_id, custom_instruction_response=custom_instruction_response)



Update an existing custom instruction for a user.  Args:     request: The HTTP request containing the updated custom instruction data.     org: The organization/tenant identifier.     user_id: The ID of the user to update custom instructions for.  Returns:     Response: The updated custom instruction.  Raises:     BadRequest: If the provided data is invalid.     NotFound: If no custom instruction exists for the user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.custom_instruction_response import CustomInstructionResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
custom_instruction_response = {"content":"Always explain concepts in simple terms with examples and analogies."} # CustomInstructionResponse |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_custom_instruction_update(org, user_id, custom_instruction_response=custom_instruction_response)
    print("The response of AiMentorApi->ai_mentor_orgs_users_custom_instruction_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_custom_instruction_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **custom_instruction_response** | [**CustomInstructionResponse**](CustomInstructionResponse.md)|  | [optional] 

### Return type

[**CustomInstructionResponse**](CustomInstructionResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data |  -  |
**404** | Custom instruction not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_destroy**
> ai_mentor_orgs_users_destroy(name, org, user_id, department_id=department_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)



Soft delete a mentor.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
name = 'name_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | Department to filter by (optional)
filter_by = 'filter_by_example' # str | Filter options include, date, name, default is date  (optional)
metadata_key = 'metadata_key_example' # str | Metadata key to be queried with (optional)
metadata_value = 'metadata_value_example' # str | Metadata value to be filter for (optional)
return_session_information = True # bool | Declares if session information should be included in the mentor data (optional)
visibility = 'visibility_example' # str | visibility type  to be queried with (optional)

try:
    api_instance.ai_mentor_orgs_users_destroy(name, org, user_id, department_id=department_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **department_id** | **int**| Department to filter by | [optional] 
 **filter_by** | **str**| Filter options include, date, name, default is date  | [optional] 
 **metadata_key** | **str**| Metadata key to be queried with | [optional] 
 **metadata_value** | **str**| Metadata value to be filter for | [optional] 
 **return_session_information** | **bool**| Declares if session information should be included in the mentor data | [optional] 
 **visibility** | **str**| visibility type  to be queried with | [optional] 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_downloads_tasks_retrieve**
> ChatHistoryItem ai_mentor_orgs_users_downloads_tasks_retrieve(org, task_id, user_id, to_csv=to_csv)



Retrieves the chat history for a user if the export task is ready.  This Endpoint to download user chathistory.  Accessible to tenant admins and students.  Returns:      200: When task is not ready.      200: chat history object      400: When data is not valid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.chat_history_item import ChatHistoryItem
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
task_id = 'task_id_example' # str | 
user_id = 'user_id_example' # str | 
to_csv = False # bool | Choose download in csv or not (optional) (default to False)

try:
    api_response = api_instance.ai_mentor_orgs_users_downloads_tasks_retrieve(org, task_id, user_id, to_csv=to_csv)
    print("The response of AiMentorApi->ai_mentor_orgs_users_downloads_tasks_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_downloads_tasks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **task_id** | **str**|  | 
 **user_id** | **str**|  | 
 **to_csv** | **bool**| Choose download in csv or not | [optional] [default to False]

### Return type

[**ChatHistoryItem**](ChatHistoryItem.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_edx_memory_destroy**
> ai_mentor_orgs_users_edx_memory_destroy(id, org, user_id)



Endpoints to fetch and delete Edx stored Memory information stored for a user and a corresponding edx course they have interracted with. This information is passed to the corresponding mentor so the mentor has context information about the course and unit that the user last interracted with.  There can be only one UserEdxMemory instance per student and course_id.  Url Args:     org (str): The organization's platform key.     user_id (str): The username  identifier of the individual.  Returns:      200: A paginated list of UserEdxMemory objects  Examples:      - List all memories         GET: /api/ai-mentor/orgs/main/users/johndoe/edx-memory/          Request:        None         Response:       {                             \"count\": 0,                             \"next\": null,                             \"previous\": null,                             \"results\": [{                                 \"student\": 1,                                 \"course_id\": \"course-v1:main+CARBON+2024_Fall\",                                 \"data\": {},                                 \"date_created\": \"2024-06-25T15:30:26.257140\",                                 \"last_modified\": \"2024-06-25T15:30:26.257140\"                             }]                         }     - Get a single UserEdxMemory object         GET: /api/ai-mentor/orgs/main/users/johndoe/edx-memory/1/          Request:        None         Response:       {                             \"student\": 1,                             \"course_id\": \"course-v1:main+CARBON+2024_Fall\",                             \"data\": {},                             \"date_created\": \"2024-06-25T15:30:26.257140\",                             \"last_modified\": \"2024-06-25T15:30:26.257140\"                         }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this user edx memory.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_edx_memory_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_edx_memory_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user edx memory. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_edx_memory_list**
> PaginatedUserEdxMemoryList ai_mentor_orgs_users_edx_memory_list(org, user_id, course_id=course_id, ordering=ordering, page=page, page_size=page_size, student=student, username=username)



Endpoints to fetch and delete Edx stored Memory information stored for a user and a corresponding edx course they have interracted with. This information is passed to the corresponding mentor so the mentor has context information about the course and unit that the user last interracted with.  There can be only one UserEdxMemory instance per student and course_id.  Url Args:     org (str): The organization's platform key.     user_id (str): The username  identifier of the individual.  Returns:      200: A paginated list of UserEdxMemory objects  Examples:      - List all memories         GET: /api/ai-mentor/orgs/main/users/johndoe/edx-memory/          Request:        None         Response:       {                             \"count\": 0,                             \"next\": null,                             \"previous\": null,                             \"results\": [{                                 \"student\": 1,                                 \"course_id\": \"course-v1:main+CARBON+2024_Fall\",                                 \"data\": {},                                 \"date_created\": \"2024-06-25T15:30:26.257140\",                                 \"last_modified\": \"2024-06-25T15:30:26.257140\"                             }]                         }     - Get a single UserEdxMemory object         GET: /api/ai-mentor/orgs/main/users/johndoe/edx-memory/1/          Request:        None         Response:       {                             \"student\": 1,                             \"course_id\": \"course-v1:main+CARBON+2024_Fall\",                             \"data\": {},                             \"date_created\": \"2024-06-25T15:30:26.257140\",                             \"last_modified\": \"2024-06-25T15:30:26.257140\"                         }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_user_edx_memory_list import PaginatedUserEdxMemoryList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
course_id = 'course_id_example' # str |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
student = 56 # int | edX user ID (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_edx_memory_list(org, user_id, course_id=course_id, ordering=ordering, page=page, page_size=page_size, student=student, username=username)
    print("The response of AiMentorApi->ai_mentor_orgs_users_edx_memory_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_edx_memory_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **course_id** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **student** | **int**| edX user ID | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedUserEdxMemoryList**](PaginatedUserEdxMemoryList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_edx_memory_retrieve**
> UserEdxMemory ai_mentor_orgs_users_edx_memory_retrieve(id, org, user_id)



Endpoints to fetch and delete Edx stored Memory information stored for a user and a corresponding edx course they have interracted with. This information is passed to the corresponding mentor so the mentor has context information about the course and unit that the user last interracted with.  There can be only one UserEdxMemory instance per student and course_id.  Url Args:     org (str): The organization's platform key.     user_id (str): The username  identifier of the individual.  Returns:      200: A paginated list of UserEdxMemory objects  Examples:      - List all memories         GET: /api/ai-mentor/orgs/main/users/johndoe/edx-memory/          Request:        None         Response:       {                             \"count\": 0,                             \"next\": null,                             \"previous\": null,                             \"results\": [{                                 \"student\": 1,                                 \"course_id\": \"course-v1:main+CARBON+2024_Fall\",                                 \"data\": {},                                 \"date_created\": \"2024-06-25T15:30:26.257140\",                                 \"last_modified\": \"2024-06-25T15:30:26.257140\"                             }]                         }     - Get a single UserEdxMemory object         GET: /api/ai-mentor/orgs/main/users/johndoe/edx-memory/1/          Request:        None         Response:       {                             \"student\": 1,                             \"course_id\": \"course-v1:main+CARBON+2024_Fall\",                             \"data\": {},                             \"date_created\": \"2024-06-25T15:30:26.257140\",                             \"last_modified\": \"2024-06-25T15:30:26.257140\"                         }

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.user_edx_memory import UserEdxMemory
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this user edx memory.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_edx_memory_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_edx_memory_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_edx_memory_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user edx memory. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserEdxMemory**](UserEdxMemory.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_elevenlabs_voice_create**
> ElevenlabsCustomVoiceResponse ai_mentor_orgs_users_elevenlabs_voice_create(org, user_id, name, files)



Create a new custom Elevenlabs voice.  This endpoint allows users to upload audio files to create a custom voice that can be used with the Elevenlabs text-to-speech service.  Note: The audio files' total length should be longer than 1 minute and the total size should be smaller than 11 MiB.  Args:     request: The HTTP request containing the voice name and audio files.     org: The organization/tenant identifier.     user_id: The ID of the user creating the voice.  Returns:     Response: The created voice configuration.  Raises:     BadRequest: If the provided data is invalid, credentials are not found, or there's an API error.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.elevenlabs_custom_voice_response import ElevenlabsCustomVoiceResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
name = 'name_example' # str | 
files = ['files_example'] # List[str] | 

try:
    api_response = api_instance.ai_mentor_orgs_users_elevenlabs_voice_create(org, user_id, name, files)
    print("The response of AiMentorApi->ai_mentor_orgs_users_elevenlabs_voice_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_elevenlabs_voice_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **name** | **str**|  | 
 **files** | [**List[str]**](str.md)|  | 

### Return type

[**ElevenlabsCustomVoiceResponse**](ElevenlabsCustomVoiceResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data, credentials not found, or API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_elevenlabs_voice_destroy**
> ai_mentor_orgs_users_elevenlabs_voice_destroy(org, user_id, voice_name)



Delete an existing Elevenlabs voice configuration.  This endpoint removes a custom voice configuration both from the local database and from the Elevenlabs remote API if applicable.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user who owns the voice.     voice_name: The name of the voice to delete.  Returns:     Response: A confirmation of the deletion.  Raises:     BadRequest: If the Elevenlabs credentials are not found or there's an API error.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
voice_name = 'voice_name_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_elevenlabs_voice_destroy(org, user_id, voice_name)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_elevenlabs_voice_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **voice_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Voice successfully deleted |  -  |
**400** | Credentials not found or API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_elevenlabs_voice_list**
> List[ElevenlabsCustomVoiceResponse] ai_mentor_orgs_users_elevenlabs_voice_list(org, user_id)



Retrieve a list of Elevenlabs voices available to a user.  This endpoint returns both custom voices created by the user and premade voices available to all users.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user to retrieve voices for.  Returns:     Response: A list of available Elevenlabs voices.  Raises:     NotFound: If the specified user does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.elevenlabs_custom_voice_response import ElevenlabsCustomVoiceResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_elevenlabs_voice_list(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_elevenlabs_voice_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_elevenlabs_voice_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[ElevenlabsCustomVoiceResponse]**](ElevenlabsCustomVoiceResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_export_chathistory_create**
> TaskView ai_mentor_orgs_users_export_chathistory_create(org, user_id)



Initiates a background task to export the user's chat history.  Returns:      200: task id.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.task_view import TaskView
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_export_chathistory_create(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_export_chathistory_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_export_chathistory_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**TaskView**](TaskView.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_free_usage_count_retrieve**
> FreeUsageCount ai_mentor_orgs_users_free_usage_count_retrieve(org, user_id)



Retrieve the count of free usage credits available to a user.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user to check free usage for.  Returns:     Response: The count of free usage credits available.  Raises:     NotFound: If the specified user does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.free_usage_count import FreeUsageCount
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_free_usage_count_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_free_usage_count_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_free_usage_count_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**FreeUsageCount**](FreeUsageCount.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_list**
> PaginatedMentorList ai_mentor_orgs_users_list(org, user_id, department_id=department_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, page=page, page_size=page_size, return_session_information=return_session_information, visibility=visibility)



Retrieve a list of mentors.  Returns:     - List of mentors matching the filters.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_mentor_list import PaginatedMentorList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | Department to filter by (optional)
filter_by = 'filter_by_example' # str | Filter options include, date, name, default is date  (optional)
metadata_key = 'metadata_key_example' # str | Metadata key to be queried with (optional)
metadata_value = 'metadata_value_example' # str | Metadata value to be filter for (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
return_session_information = True # bool | Declares if session information should be included in the mentor data (optional)
visibility = 'visibility_example' # str | visibility type  to be queried with (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_list(org, user_id, department_id=department_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, page=page, page_size=page_size, return_session_information=return_session_information, visibility=visibility)
    print("The response of AiMentorApi->ai_mentor_orgs_users_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **department_id** | **int**| Department to filter by | [optional] 
 **filter_by** | **str**| Filter options include, date, name, default is date  | [optional] 
 **metadata_key** | **str**| Metadata key to be queried with | [optional] 
 **metadata_value** | **str**| Metadata value to be filter for | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **return_session_information** | **bool**| Declares if session information should be included in the mentor data | [optional] 
 **visibility** | **str**| visibility type  to be queried with | [optional] 

### Return type

[**PaginatedMentorList**](PaginatedMentorList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mcp_servers_create**
> MCPServer ai_mentor_orgs_users_mcp_servers_create(org, user_id, mcp_server)



ViewSet for MCP Servers.  Allows platform admins to list, create, retrieve, update, and delete MCP servers.  Permissions:     - Accessible to tenant admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mcp_server import MCPServer
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mcp_server = iblai.MCPServer() # MCPServer | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mcp_servers_create(org, user_id, mcp_server)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mcp_servers_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mcp_servers_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mcp_server** | [**MCPServer**](MCPServer.md)|  | 

### Return type

[**MCPServer**](MCPServer.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mcp_servers_destroy**
> ai_mentor_orgs_users_mcp_servers_destroy(id, org, user_id)



ViewSet for MCP Servers.  Allows platform admins to list, create, retrieve, update, and delete MCP servers.  Permissions:     - Accessible to tenant admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this mcp server.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_mcp_servers_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mcp_servers_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this mcp server. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mcp_servers_list**
> PaginatedMCPServerList ai_mentor_orgs_users_mcp_servers_list(org, user_id, page=page, page_size=page_size, platform=platform, search=search)



List all MCP servers.  Returns a paginated list of MCP servers that can be filtered by platform and searched by name or URL.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_mcp_server_list import PaginatedMCPServerList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
platform = 56 # int |  (optional)
search = 'search_example' # str | A search term. (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_mcp_servers_list(org, user_id, page=page, page_size=page_size, platform=platform, search=search)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mcp_servers_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mcp_servers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **platform** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedMCPServerList**](PaginatedMCPServerList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mcp_servers_partial_update**
> MCPServer ai_mentor_orgs_users_mcp_servers_partial_update(id, org, user_id, patched_mcp_server=patched_mcp_server)



ViewSet for MCP Servers.  Allows platform admins to list, create, retrieve, update, and delete MCP servers.  Permissions:     - Accessible to tenant admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mcp_server import MCPServer
from iblai.models.patched_mcp_server import PatchedMCPServer
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this mcp server.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
patched_mcp_server = iblai.PatchedMCPServer() # PatchedMCPServer |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_mcp_servers_partial_update(id, org, user_id, patched_mcp_server=patched_mcp_server)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mcp_servers_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mcp_servers_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this mcp server. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **patched_mcp_server** | [**PatchedMCPServer**](PatchedMCPServer.md)|  | [optional] 

### Return type

[**MCPServer**](MCPServer.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mcp_servers_retrieve**
> MCPServer ai_mentor_orgs_users_mcp_servers_retrieve(id, org, user_id)



ViewSet for MCP Servers.  Allows platform admins to list, create, retrieve, update, and delete MCP servers.  Permissions:     - Accessible to tenant admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mcp_server import MCPServer
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this mcp server.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mcp_servers_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mcp_servers_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mcp_servers_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this mcp server. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MCPServer**](MCPServer.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mcp_servers_update**
> MCPServer ai_mentor_orgs_users_mcp_servers_update(id, org, user_id, mcp_server)



ViewSet for MCP Servers.  Allows platform admins to list, create, retrieve, update, and delete MCP servers.  Permissions:     - Accessible to tenant admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mcp_server import MCPServer
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this mcp server.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mcp_server = iblai.MCPServer() # MCPServer | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mcp_servers_update(id, org, user_id, mcp_server)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mcp_servers_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mcp_servers_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this mcp server. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mcp_server** | [**MCPServer**](MCPServer.md)|  | 

### Return type

[**MCPServer**](MCPServer.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_audience_create**
> MentorAudience ai_mentor_orgs_users_mentor_audience_create(org, user_id, mentor_audience)



Create a new mentor audience.  Accessible to tenant admins only.  Returns:     - 201: Created mentor audience.     - 401: Unauthorized.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_audience import MentorAudience
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_audience = {"name":"Student","description":"Mentor for student audience"} # MentorAudience | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_audience_create(org, user_id, mentor_audience)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_audience_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_audience_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_audience** | [**MentorAudience**](MentorAudience.md)|  | 

### Return type

[**MentorAudience**](MentorAudience.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**401** | Unauthorized - Only tenant admins can create mentor audiences. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_audience_destroy**
> ai_mentor_orgs_users_mentor_audience_destroy(org, user_id)



Delete a mentor audience.  Accessible to tenant admins only.  Returns:     - 204: No content.     - 400: Bad request if audience name is missing.     - 404: Not found if audience does not exist.     - 401: Unauthorized.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_mentor_audience_destroy(org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_audience_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content - Mentor audience deleted successfully. |  -  |
**400** | Bad Request - Invalid data. |  -  |
**404** | Not Found - Audience does not exist. |  -  |
**401** | Unauthorized - Only tenant admins can delete mentor audiences. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_audience_list**
> List[MentorAudience] ai_mentor_orgs_users_mentor_audience_list(org, user_id)



Retrieve the list of mentor audiences.  Returns:     - 200: List of mentor audiences.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_audience import MentorAudience
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_audience_list(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_audience_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_audience_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[MentorAudience]**](MentorAudience.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_categories_create**
> MentorCategory ai_mentor_orgs_users_mentor_categories_create(org, user_id, mentor_category_create)



Create a new mentor category.  Accessible only to tenant admins.  Returns:     200: Details of the created mentor category.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_category import MentorCategory
from iblai.models.mentor_category_create import MentorCategoryCreate
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_category_create = {"name":"Education","description":"Education testing","audience":1} # MentorCategoryCreate | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_categories_create(org, user_id, mentor_category_create)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_categories_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_categories_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_category_create** | [**MentorCategoryCreate**](MentorCategoryCreate.md)|  | 

### Return type

[**MentorCategory**](MentorCategory.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_categories_destroy**
> ai_mentor_orgs_users_mentor_categories_destroy(org, user_id)



Delete a mentor category.  Accessible only to tenant admins.  Returns:     204: \"No content\" when Delete succeeded.     400: Bad request data received

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_mentor_categories_destroy(org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_categories_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_categories_list**
> List[MentorCategory] ai_mentor_orgs_users_mentor_categories_list(org, user_id)



Retrieve a list of mentor categories.  Returns:     200: A list of mentor categories.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_category import MentorCategory
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_categories_list(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_categories_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_categories_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[MentorCategory]**](MentorCategory.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_feedback_create_create**
> UserChatFeedback ai_mentor_orgs_users_mentor_feedback_create_create(org, user_id, user_chat_feedback)



Create a new user chat feedback entry.  Args:     request: The HTTP request containing the feedback data.     org: The organization/tenant identifier.  Returns:     Response: The created feedback entry.  Raises:     BadRequest: If the provided data is invalid or the mentor does not exist.

### Example


```python
import iblai
from iblai.models.user_chat_feedback import UserChatFeedback
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
user_chat_feedback = {"username":"johndoe","session":"937d3d46-3048-4f9d-aa5c-ce7c51d85332","user_text":"Who is Marc H. Supcoff","ai_response":"Marc H. Supcoff is an Adjunct Professor of Law","reason":"Good reason","additional_feedback":"Good response","rating":1,"mentor":"ai-mentor"} # UserChatFeedback | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_feedback_create_create(org, user_id, user_chat_feedback)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_feedback_create_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_feedback_create_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **user_chat_feedback** | [**UserChatFeedback**](UserChatFeedback.md)|  | 

### Return type

[**UserChatFeedback**](UserChatFeedback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Invalid data or mentor not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_feedback_retrieve**
> UserChatFeedback ai_mentor_orgs_users_mentor_feedback_retrieve(feedback_id, org, user_id)



Retrieve details of a specific user chat feedback entry.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     feedback_id: The ID of the feedback entry to retrieve.  Returns:     Response: The feedback entry details.  Raises:     NotFound: If the specified feedback entry does not exist.

### Example


```python
import iblai
from iblai.models.user_chat_feedback import UserChatFeedback
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
feedback_id = 56 # int | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_feedback_retrieve(feedback_id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_feedback_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_feedback_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **int**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserChatFeedback**](UserChatFeedback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Feedback not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_feedback_update**
> UserChatFeedback ai_mentor_orgs_users_mentor_feedback_update(feedback_id, org, user_id, user_chat_feedback)



Update an existing user chat feedback entry.  Args:     request: The HTTP request containing the updated feedback data.     org: The organization/tenant identifier.     feedback_id: The ID of the feedback entry to update.  Returns:     Response: The updated feedback entry.  Raises:     NotFound: If the specified feedback entry does not exist.     BadRequest: If the provided data is invalid or the mentor does not exist.

### Example


```python
import iblai
from iblai.models.user_chat_feedback import UserChatFeedback
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
feedback_id = 56 # int | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
user_chat_feedback = {"username":"johndoe","session":"937d3d46-3048-4f9d-aa5c-ce7c51d85332","user_text":"Who is Marc H. Supcoff","ai_response":"Marc H. Supcoff is an Adjunct Professor of Law","reason":"Good reason","additional_feedback":"Good response","rating":1,"mentor":"ai-mentor"} # UserChatFeedback | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_feedback_update(feedback_id, org, user_id, user_chat_feedback)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_feedback_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_feedback_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_id** | **int**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **user_chat_feedback** | [**UserChatFeedback**](UserChatFeedback.md)|  | 

### Return type

[**UserChatFeedback**](UserChatFeedback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data or mentor not found |  -  |
**404** | Feedback not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_from_template_create**
> Mentor ai_mentor_orgs_users_mentor_from_template_create(org, user_id, mentor_from_template_request)



View to create a mentor from a template  Accessible to only tenant admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
from iblai.models.mentor_from_template_request import MentorFromTemplateRequest
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_from_template_request = iblai.MentorFromTemplateRequest() # MentorFromTemplateRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_from_template_create(org, user_id, mentor_from_template_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_from_template_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_from_template_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_from_template_request** | [**MentorFromTemplateRequest**](MentorFromTemplateRequest.md)|  | 

### Return type

[**Mentor**](Mentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_llms_list**
> List[LLMResponse] ai_mentor_orgs_users_mentor_llms_list(org, user_id, mentor_id=mentor_id)



Retrieve available LLMs for a user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_response import LLMResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_id = 'mentor_id_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_llms_list(org, user_id, mentor_id=mentor_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_llms_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_llms_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_id** | **str**|  | [optional] 

### Return type

[**List[LLMResponse]**](LLMResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_seed_retrieve**
> SeedMentorsView ai_mentor_orgs_users_mentor_seed_retrieve(org, user_id)



Seed initial mentors in a tenant.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user initiating the seeding.  Returns:     Response: A success message with details about the seeded mentors.  Raises:     BadRequest: If the seeding process fails.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.seed_mentors_view import SeedMentorsView
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_seed_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_seed_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_seed_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**SeedMentorsView**](SeedMentorsView.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Seeding failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_tools_list**
> List[ToolResponse] ai_mentor_orgs_users_mentor_tools_list(org, user_id)



Retrieve the list of available mentor tools.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.tool_response import ToolResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_tools_list(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_tools_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_tools_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[ToolResponse]**](ToolResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentor_with_settings_create**
> Mentor ai_mentor_orgs_users_mentor_with_settings_create(org, user_id, template_name, new_mentor_name, display_name=display_name, description=description, profile_image=profile_image, initial_message=initial_message, suggested_message=suggested_message, theme=theme, user_message_color=user_message_color, mentor_bubble_color=mentor_bubble_color, align_mentor_bubble=align_mentor_bubble, system_prompt=system_prompt, llm_provider=llm_provider, llm_name=llm_name, mentor_visibility=mentor_visibility, enable_image_generation=enable_image_generation, enable_web_browsing=enable_web_browsing, enable_code_interpreter=enable_code_interpreter, metadata=metadata, custom_css=custom_css, uploaded_profile_image=uploaded_profile_image, proactive_response=proactive_response, greeting_method=greeting_method, forkable=forkable, forkable_with_training_data=forkable_with_training_data, categories=categories, tool_slugs=tool_slugs, llm_temperature=llm_temperature, seo_tags=seo_tags, marketing_conversations=marketing_conversations, proactive_prompt=proactive_prompt, moderation_system_prompt=moderation_system_prompt, post_processing_prompt=post_processing_prompt, moderation_response=moderation_response, enable_moderation=enable_moderation, enable_post_processing_system=enable_post_processing_system, enable_openai_assistant=enable_openai_assistant, enable_total_grounding=enable_total_grounding, google_voice=google_voice, openai_voice=openai_voice, enable_suggested_prompts=enable_suggested_prompts, enable_guided_prompts=enable_guided_prompts, mcp_servers=mcp_servers, guided_prompt_instructions=guided_prompt_instructions)



View to create a mentor from a template with settings.  Accessible to tenant admins only.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.greeting_method_enum import GreetingMethodEnum
from iblai.models.mentor import Mentor
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
template_name = 'template_name_example' # str | 
new_mentor_name = 'new_mentor_name_example' # str | 
display_name = 'display_name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
profile_image = 'profile_image_example' # str |  (optional)
initial_message = 'initial_message_example' # str |  (optional)
suggested_message = 'suggested_message_example' # str |  (optional)
theme = 'theme_example' # str |  (optional)
user_message_color = 'user_message_color_example' # str |  (optional)
mentor_bubble_color = 'mentor_bubble_color_example' # str |  (optional)
align_mentor_bubble = 'align_mentor_bubble_example' # str |  (optional)
system_prompt = 'system_prompt_example' # str |  (optional)
llm_provider = 'llm_provider_example' # str |  (optional)
llm_name = 'llm_name_example' # str |  (optional)
mentor_visibility = 'mentor_visibility_example' # str |  (optional)
enable_image_generation = True # bool |  (optional)
enable_web_browsing = True # bool |  (optional)
enable_code_interpreter = True # bool |  (optional)
metadata = None # object |  (optional)
custom_css = 'custom_css_example' # str |  (optional)
uploaded_profile_image = 'uploaded_profile_image_example' # str |  (optional)
proactive_response = 'proactive_response_example' # str |  (optional)
greeting_method = iblai.GreetingMethodEnum() # GreetingMethodEnum |  (optional)
forkable = True # bool |  (optional)
forkable_with_training_data = True # bool |  (optional)
categories = [56] # List[int] |  (optional)
tool_slugs = ['tool_slugs_example'] # List[str] |  (optional)
llm_temperature = 3.4 # float |  (optional)
seo_tags = None # object |  (optional)
marketing_conversations = None # object |  (optional)
proactive_prompt = 'proactive_prompt_example' # str |  (optional)
moderation_system_prompt = 'moderation_system_prompt_example' # str |  (optional)
post_processing_prompt = 'post_processing_prompt_example' # str |  (optional)
moderation_response = 'moderation_response_example' # str |  (optional)
enable_moderation = False # bool |  (optional) (default to False)
enable_post_processing_system = False # bool |  (optional) (default to False)
enable_openai_assistant = True # bool |  (optional)
enable_total_grounding = False # bool |  (optional) (default to False)
google_voice = 56 # int |  (optional)
openai_voice = 56 # int |  (optional)
enable_suggested_prompts = True # bool |  (optional)
enable_guided_prompts = True # bool |  (optional)
mcp_servers = [56] # List[int] |  (optional)
guided_prompt_instructions = 'guided_prompt_instructions_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_mentor_with_settings_create(org, user_id, template_name, new_mentor_name, display_name=display_name, description=description, profile_image=profile_image, initial_message=initial_message, suggested_message=suggested_message, theme=theme, user_message_color=user_message_color, mentor_bubble_color=mentor_bubble_color, align_mentor_bubble=align_mentor_bubble, system_prompt=system_prompt, llm_provider=llm_provider, llm_name=llm_name, mentor_visibility=mentor_visibility, enable_image_generation=enable_image_generation, enable_web_browsing=enable_web_browsing, enable_code_interpreter=enable_code_interpreter, metadata=metadata, custom_css=custom_css, uploaded_profile_image=uploaded_profile_image, proactive_response=proactive_response, greeting_method=greeting_method, forkable=forkable, forkable_with_training_data=forkable_with_training_data, categories=categories, tool_slugs=tool_slugs, llm_temperature=llm_temperature, seo_tags=seo_tags, marketing_conversations=marketing_conversations, proactive_prompt=proactive_prompt, moderation_system_prompt=moderation_system_prompt, post_processing_prompt=post_processing_prompt, moderation_response=moderation_response, enable_moderation=enable_moderation, enable_post_processing_system=enable_post_processing_system, enable_openai_assistant=enable_openai_assistant, enable_total_grounding=enable_total_grounding, google_voice=google_voice, openai_voice=openai_voice, enable_suggested_prompts=enable_suggested_prompts, enable_guided_prompts=enable_guided_prompts, mcp_servers=mcp_servers, guided_prompt_instructions=guided_prompt_instructions)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentor_with_settings_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentor_with_settings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **template_name** | **str**|  | 
 **new_mentor_name** | **str**|  | 
 **display_name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **profile_image** | **str**|  | [optional] 
 **initial_message** | **str**|  | [optional] 
 **suggested_message** | **str**|  | [optional] 
 **theme** | **str**|  | [optional] 
 **user_message_color** | **str**|  | [optional] 
 **mentor_bubble_color** | **str**|  | [optional] 
 **align_mentor_bubble** | **str**|  | [optional] 
 **system_prompt** | **str**|  | [optional] 
 **llm_provider** | **str**|  | [optional] 
 **llm_name** | **str**|  | [optional] 
 **mentor_visibility** | **str**|  | [optional] 
 **enable_image_generation** | **bool**|  | [optional] 
 **enable_web_browsing** | **bool**|  | [optional] 
 **enable_code_interpreter** | **bool**|  | [optional] 
 **metadata** | [**object**](object.md)|  | [optional] 
 **custom_css** | **str**|  | [optional] 
 **uploaded_profile_image** | **str**|  | [optional] 
 **proactive_response** | **str**|  | [optional] 
 **greeting_method** | [**GreetingMethodEnum**](GreetingMethodEnum.md)|  | [optional] 
 **forkable** | **bool**|  | [optional] 
 **forkable_with_training_data** | **bool**|  | [optional] 
 **categories** | [**List[int]**](int.md)|  | [optional] 
 **tool_slugs** | [**List[str]**](str.md)|  | [optional] 
 **llm_temperature** | **float**|  | [optional] 
 **seo_tags** | [**object**](object.md)|  | [optional] 
 **marketing_conversations** | [**object**](object.md)|  | [optional] 
 **proactive_prompt** | **str**|  | [optional] 
 **moderation_system_prompt** | **str**|  | [optional] 
 **post_processing_prompt** | **str**|  | [optional] 
 **moderation_response** | **str**|  | [optional] 
 **enable_moderation** | **bool**|  | [optional] [default to False]
 **enable_post_processing_system** | **bool**|  | [optional] [default to False]
 **enable_openai_assistant** | **bool**|  | [optional] 
 **enable_total_grounding** | **bool**|  | [optional] [default to False]
 **google_voice** | **int**|  | [optional] 
 **openai_voice** | **int**|  | [optional] 
 **enable_suggested_prompts** | **bool**|  | [optional] 
 **enable_guided_prompts** | **bool**|  | [optional] 
 **mcp_servers** | [**List[int]**](int.md)|  | [optional] 
 **guided_prompt_instructions** | **str**|  | [optional] 

### Return type

[**Mentor**](Mentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_available_tools_list**
> List[ToolResponse] ai_mentor_orgs_users_mentors_available_tools_list(mentor, org, user_id)



Retrieve tools available for a particular mentor.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.tool_response import ToolResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_available_tools_list(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_available_tools_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_available_tools_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[ToolResponse]**](ToolResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_create_call_credentials_create**
> CallAuthenticationResponse ai_mentor_orgs_users_mentors_create_call_credentials_create(mentor, org, user_id, call_authentication_request)



Generate IBL Call Pro authentication parameters for audio calls.  This endpoint creates the necessary authentication tokens and parameters for connecting to a IBL Call Pro room for audio communication with a mentor.  Args:     request: The HTTP request object containing the required parameters.     org: The organization/tenant identifier.     user_id: The ID of the user requesting authentication.  Returns:     Response: IBL Call Pro authentication parameters including URL, room name,              participant name, and authentication token.  Raises:     ValidationError: If the request parameters are invalid.     BadRequest: If the IBL Call Pro credentials are not properly configured.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.call_authentication_request import CallAuthenticationRequest
from iblai.models.call_authentication_response import CallAuthenticationResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
call_authentication_request = iblai.CallAuthenticationRequest() # CallAuthenticationRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_create_call_credentials_create(mentor, org, user_id, call_authentication_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_create_call_credentials_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_create_call_credentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **call_authentication_request** | [**CallAuthenticationRequest**](CallAuthenticationRequest.md)|  | 

### Return type

[**CallAuthenticationResponse**](CallAuthenticationResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid request parameters or improperly configured IBL Call Pro credentials |  -  |
**401** | Authentication failed |  -  |
**404** | No mentor or session found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_current_memory_retrieve**
> MemoryComponentResponse ai_mentor_orgs_users_mentors_current_memory_retrieve(mentor, org, user_id)



Retrieve memory components for a specific mentor.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.     mentor: The identifier of the mentor to retrieve memory for.  Returns:     Response: The memory components for the mentor.  Raises:     NotFound: If the specified mentor or memory does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.memory_component_response import MemoryComponentResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_current_memory_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_current_memory_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_current_memory_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MemoryComponentResponse**](MemoryComponentResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Mentor or memory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_current_memory_update**
> QuestionResponse ai_mentor_orgs_users_mentors_current_memory_update(mentor, org, user_id, question_request)



Update memory components for a specific mentor.  Args:     request: The HTTP request containing the updated memory data.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.     mentor: The identifier of the mentor to update memory for.  Returns:     Response: The updated memory components for the mentor.  Raises:     BadRequest: If the provided data is invalid.     NotFound: If the specified mentor does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.question_request import QuestionRequest
from iblai.models.question_response import QuestionResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
question_request = {"username":"johndoe","initial_questions":[{"text":"What is machine learning?","difficulty_level":2,"possible_answers":[{"text":"A type of artificial intelligence"},{"text":"A programming language"}]}],"question_count":5,"subject":"Artificial Intelligence"} # QuestionRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_current_memory_update(mentor, org, user_id, question_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_current_memory_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_current_memory_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **question_request** | [**QuestionRequest**](QuestionRequest.md)|  | 

### Return type

[**QuestionResponse**](QuestionResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data |  -  |
**404** | Mentor not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_custom_voice_create**
> MentorCustomVoiceResponse ai_mentor_orgs_users_mentors_custom_voice_create(mentor, org, user_id, mentor_custom_voice)



Set a custom voice for a mentor.  This endpoint allows setting a custom voice for a specific mentor, either using the default voice provider or Elevenlabs.  Args:     request: The HTTP request containing the voice provider and name.     org: The organization/tenant identifier.     user_id: The ID of the user who owns the mentor link.     mentor: The unique identifier of the mentor.  Returns:     Response: The updated custom voice settings.  Raises:     BadRequest: If the provided data is invalid or the voice does not exist.     NotFound: If the mentor or student does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_custom_voice import MentorCustomVoice
from iblai.models.mentor_custom_voice_response import MentorCustomVoiceResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_custom_voice = {"voice_provider":"default","voice_name":"default"} # MentorCustomVoice | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_custom_voice_create(mentor, org, user_id, mentor_custom_voice)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_custom_voice_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_custom_voice_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_custom_voice** | [**MentorCustomVoice**](MentorCustomVoice.md)|  | 

### Return type

[**MentorCustomVoiceResponse**](MentorCustomVoiceResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data or voice not found |  -  |
**404** | Mentor or student not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_custom_voice_retrieve**
> MentorCustomVoiceResponse ai_mentor_orgs_users_mentors_custom_voice_retrieve(mentor, org, user_id)



Retrieve the current custom voice settings for a mentor.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user who owns the mentor link.     mentor: The unique identifier of the mentor.  Returns:     Response: The current custom voice settings.  Raises:     NotFound: If the specified mentor or student does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_custom_voice_response import MentorCustomVoiceResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_custom_voice_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_custom_voice_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_custom_voice_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorCustomVoiceResponse**](MentorCustomVoiceResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Mentor or student not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_custom_voice_tts_create**
> ai_mentor_orgs_users_mentors_custom_voice_tts_create(mentor, org, user_id)



Generate audio from text using a mentor's custom voice.  This endpoint converts the provided text to speech using the custom voice configured for the specified mentor.  Args:     request: The HTTP request containing the text to convert.     org: The organization/tenant identifier.     user_id: The ID of the user who owns the mentor link.     mentor: The unique identifier of the mentor.  Returns:     Response: An MP3 audio file of the synthesized speech.  Raises:     BadRequest: If the text is empty, credentials are not found, or custom voice is not set.     NotFound: If the mentor or student does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_mentors_custom_voice_tts_create(mentor, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_custom_voice_tts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MP3 audio file |  -  |
**400** | Invalid data, credentials not found, or custom voice not set |  -  |
**404** | Mentor or student not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_edit_scenarios_update**
> MentorScenario ai_mentor_orgs_users_mentors_edit_scenarios_update(mentor, org, user_id, mentor_scenario)



Update scenarios for a specific mentor.  Args:     request: The HTTP request containing the updated scenarios.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.     mentor: The identifier of the mentor to update scenarios for.  Returns:     Response: The updated scenarios for the mentor.  Raises:     BadRequest: If the provided data is invalid.     NotFound: If the specified mentor does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_scenario import MentorScenario
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_scenario = [{"display":"Chat","name":"chat","prompts":[{"summary":"Give Me a Summary","content":"please give me a summary of this topic","icon":"add"},{"summary":"Ask Some Questions","content":"ask the user some questions","icon":"start"}]}] # MentorScenario | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_edit_scenarios_update(mentor, org, user_id, mentor_scenario)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_edit_scenarios_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_edit_scenarios_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_scenario** | [**MentorScenario**](MentorScenario.md)|  | 

### Return type

[**MentorScenario**](MentorScenario.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data |  -  |
**404** | Mentor not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_fork_create**
> Mentor ai_mentor_orgs_users_mentors_fork_create(mentor, org, user_id, mentor_fork)



Fork (clone) an existing mentor.  Args:     request: The HTTP request containing the fork parameters.     org: The organization/tenant identifier.     mentor: The identifier of the mentor to fork.     user_id: The ID of the user initiating the fork.  Returns:     Response: The newly created forked mentor.  Raises:     BadRequest: If the provided data is invalid or the fork operation fails.     NotFound: If the specified mentor does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
from iblai.models.mentor_fork import MentorFork
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_fork = {"new_mentor_name":"Data Science Mentor Clone","destination_platform_key":"secondary","clone_documents":true} # MentorFork | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_fork_create(mentor, org, user_id, mentor_fork)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_fork_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_fork_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_fork** | [**MentorFork**](MentorFork.md)|  | 

### Return type

[**Mentor**](Mentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data or fork failed |  -  |
**404** | Mentor not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_historical_memory_retrieve**
> MemoryComponentMemoryDetail ai_mentor_orgs_users_mentors_historical_memory_retrieve(mentor, org, user_id)



Retrieve memory history entries for a specific mentor and user.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user to retrieve memory history for.     mentor: The identifier of the mentor to retrieve memory history for.  Returns:     Response: The memory history entries for the mentor and user.  Raises:     NotFound: If the specified mentor or memory history does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.memory_component_memory_detail import MemoryComponentMemoryDetail
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_historical_memory_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_historical_memory_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_historical_memory_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MemoryComponentMemoryDetail**](MemoryComponentMemoryDetail.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Mentor or memory history not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_memory_progress_retrieve**
> MemoryProgress ai_mentor_orgs_users_mentors_memory_progress_retrieve(mentor, org, user_id)



Mixin that includes the StudentTokenAuthentication and IsAdminUserOrStudent

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.memory_progress import MemoryProgress
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_memory_progress_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_memory_progress_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_memory_progress_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MemoryProgress**](MemoryProgress.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_memory_settings_create**
> MentorMemorySettingsResponse ai_mentor_orgs_users_mentors_memory_settings_create(mentor, org, user_id, mentor_memory_settings_request=mentor_memory_settings_request)



Endpoint for mentor memory item settings.  Accessible to platform admins and superusers.  Returns:      200: Change mentor memory component item.      400: When request is not valid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_memory_settings_request import MentorMemorySettingsRequest
from iblai.models.mentor_memory_settings_response import MentorMemorySettingsResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_memory_settings_request = {"item_type":"program","item_identifier":"program-v1:edX+DemoProgram","learner_advance_correct_rate":0.5,"learner_advance_question_count":12} # MentorMemorySettingsRequest |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_memory_settings_create(mentor, org, user_id, mentor_memory_settings_request=mentor_memory_settings_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_memory_settings_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_memory_settings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_memory_settings_request** | [**MentorMemorySettingsRequest**](MentorMemorySettingsRequest.md)|  | [optional] 

### Return type

[**MentorMemorySettingsResponse**](MentorMemorySettingsResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data |  -  |
**404** | Mentor not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_memory_settings_retrieve**
> MentorMemorySettingsResponse ai_mentor_orgs_users_mentors_memory_settings_retrieve(mentor, org, user_id)



Retrieve memory settings for a specific mentor.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.     mentor: The identifier of the mentor to retrieve settings for.  Returns:     Response: The memory settings for the mentor.  Raises:     NotFound: If the specified mentor or settings do not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_memory_settings_response import MentorMemorySettingsResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_memory_settings_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_memory_settings_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_memory_settings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorMemorySettingsResponse**](MentorMemorySettingsResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Mentor or settings not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_mentor_eval_create**
> MentorEval ai_mentor_orgs_users_mentors_mentor_eval_create(mentor, org, user_id, mentor_eval_request=mentor_eval_request)



Create or update evaluation criteria for a specific mentor.  Args:     request: The HTTP request containing the evaluation data.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.     mentor: The identifier of the mentor to create/update evaluations for.  Returns:     Response: The created or updated evaluation criteria.  Raises:     BadRequest: If the provided data is invalid or the mentor does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_eval import MentorEval
from iblai.models.mentor_eval_request import MentorEvalRequest
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_eval_request = {"questions":[{"content":"how to explain a computer to a 5 year old?","sample_answer":""},{"content":"how to learn linux well?","sample_answer":""}]} # MentorEvalRequest |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_mentor_eval_create(mentor, org, user_id, mentor_eval_request=mentor_eval_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_mentor_eval_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_mentor_eval_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_eval_request** | [**MentorEvalRequest**](MentorEvalRequest.md)|  | [optional] 

### Return type

[**MentorEval**](MentorEval.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data or mentor not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_mentor_eval_execution_create**
> ai_mentor_orgs_users_mentors_mentor_eval_execution_create(mentor, org, user_id, run_mentor_eval)



Run an evaluation for a specific mentor.  Args:     request: The HTTP request containing the evaluation ID.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.     mentor: The identifier of the mentor to evaluate.  Returns:     Response: The ID of the generated evaluation report.  Raises:     BadRequest: If the evaluation ID is invalid or the mentor does not match.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.run_mentor_eval import RunMentorEval
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
run_mentor_eval = {"id":100} # RunMentorEval | 

try:
    api_instance.ai_mentor_orgs_users_mentors_mentor_eval_execution_create(mentor, org, user_id, run_mentor_eval)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_mentor_eval_execution_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **run_mentor_eval** | [**RunMentorEval**](RunMentorEval.md)|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Evaluation execution started successfully |  -  |
**400** | Invalid evaluation ID or mentor mismatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_mentor_eval_retrieve**
> MentorEval ai_mentor_orgs_users_mentors_mentor_eval_retrieve(mentor, org, user_id)



Retrieve evaluation criteria for a specific mentor.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.     mentor: The identifier of the mentor to retrieve evaluations for.  Returns:     Response: The evaluation criteria for the mentor.  Raises:     NotFound: If the specified mentor or evaluations do not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_eval import MentorEval
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_mentor_eval_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_mentor_eval_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_mentor_eval_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorEval**](MentorEval.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Mentor or evaluations not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_public_settings_retrieve**
> MentorSettingsPublic ai_mentor_orgs_users_mentors_public_settings_retrieve(mentor, org, user_id)



Retrieve public mentor settings.  Args:     request: HTTP request instance.     user_id: The ID of the user requesting settings.     mentor: The mentor identifier (name, slug, or unique_id).     org: The organization key.  Returns:     Response containing the mentor settings or an error message.

### Example


```python
import iblai
from iblai.models.mentor_settings_public import MentorSettingsPublic
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_public_settings_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_public_settings_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_public_settings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorSettingsPublic**](MentorSettingsPublic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Mentor not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_reports_mentor_eval_report_retrieve**
> MentorEvalReport ai_mentor_orgs_users_mentors_reports_mentor_eval_report_retrieve(mentor, org, report_id, user_id)



Retrieve a specific evaluation report.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.     mentor: The identifier of the mentor that was evaluated.     report_id: The ID of the evaluation report to retrieve.  Returns:     Response: The detailed evaluation report.  Raises:     BadRequest: If the report does not exist, does not match the mentor, or is still being generated.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_eval_report import MentorEvalReport
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
report_id = 56 # int | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_reports_mentor_eval_report_retrieve(mentor, org, report_id, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_reports_mentor_eval_report_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_reports_mentor_eval_report_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **report_id** | **int**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorEvalReport**](MentorEvalReport.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Report not found or still being generated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_retrieve**
> Mentor ai_mentor_orgs_users_mentors_retrieve(mentor, org, user_id)



Retrieve details of a specific mentor by slug or name.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Mentor**](Mentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_scenarios_retrieve**
> MentorScenario ai_mentor_orgs_users_mentors_scenarios_retrieve(mentor, org, user_id)



Retrieve available scenarios for a specific mentor.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.     mentor: The identifier of the mentor to retrieve scenarios for.  Returns:     Response: The available scenarios for the mentor.  Raises:     NotFound: If the specified mentor or scenarios do not exist.

### Example


```python
import iblai
from iblai.models.mentor_scenario import MentorScenario
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_scenarios_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_scenarios_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_scenarios_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorScenario**](MentorScenario.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Mentor or scenarios not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_settings_retrieve**
> MentorSettingsPublic ai_mentor_orgs_users_mentors_settings_retrieve(mentor, org, user_id, department_id=department_id)

Retrieve Mentor Settings

Fetch the settings of a mentor within an organization. Only accessible to tenant admins.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_settings_public import MentorSettingsPublic
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | Department to authorize users by (optional)

try:
    # Retrieve Mentor Settings
    api_response = api_instance.ai_mentor_orgs_users_mentors_settings_retrieve(mentor, org, user_id, department_id=department_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_settings_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_settings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **department_id** | **int**| Department to authorize users by | [optional] 

### Return type

[**MentorSettingsPublic**](MentorSettingsPublic.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Mentor not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_settings_update**
> MentorSettings ai_mentor_orgs_users_mentors_settings_update(mentor, org, user_id, department_id=department_id, mentor_name=mentor_name, template_name=template_name, display_name=display_name, profile_image=profile_image, initial_message=initial_message, suggested_message=suggested_message, theme=theme, user_message_color=user_message_color, mentor_bubble_color=mentor_bubble_color, align_mentor_bubble=align_mentor_bubble, system_prompt=system_prompt, llm_provider=llm_provider, llm_name=llm_name, featured=featured, disable_chathistory=disable_chathistory, metadata=metadata, custom_css=custom_css, department_id2=department_id2, mentor_visibility=mentor_visibility, enable_image_generation=enable_image_generation, enable_web_browsing=enable_web_browsing, enable_code_interpreter=enable_code_interpreter, allow_anonymous=allow_anonymous, forkable=forkable, forkable_with_training_data=forkable_with_training_data, mentor_description=mentor_description, uploaded_profile_image=uploaded_profile_image, proactive_response=proactive_response, greeting_method=greeting_method, can_use_tools=can_use_tools, tool_slugs=tool_slugs, llm_temperature=llm_temperature, proactive_prompt=proactive_prompt, moderation_system_prompt=moderation_system_prompt, post_processing_prompt=post_processing_prompt, moderation_response=moderation_response, enable_moderation=enable_moderation, enable_post_processing_system=enable_post_processing_system, enable_openai_assistant=enable_openai_assistant, enable_total_grounding=enable_total_grounding, enable_suggested_prompts=enable_suggested_prompts, enable_guided_prompts=enable_guided_prompts, mcp_servers=mcp_servers, google_voice=google_voice, openai_voice=openai_voice, guided_prompt_instructions=guided_prompt_instructions, safety_system_prompt=safety_system_prompt, safety_response=safety_response, enable_safety_system=enable_safety_system, enable_memory_component=enable_memory_component, enable_spaced_repetition=enable_spaced_repetition, enable_instruction_mode=enable_instruction_mode, enable_socratic_mode=enable_socratic_mode, is_guided_mentor=is_guided_mentor, enable_email_chat=enable_email_chat, categories=categories)

Update Mentor Settings

Update various mentor settings including system prompts, tool permissions, and UI configurations.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.greeting_method_enum import GreetingMethodEnum
from iblai.models.mentor_settings import MentorSettings
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | Department to authorize users by (optional)
mentor_name = 'mentor_name_example' # str |  (optional)
template_name = 'template_name_example' # str |  (optional)
display_name = 'display_name_example' # str |  (optional)
profile_image = 'profile_image_example' # str |  (optional)
initial_message = 'initial_message_example' # str |  (optional)
suggested_message = 'suggested_message_example' # str |  (optional)
theme = 'theme_example' # str |  (optional)
user_message_color = 'user_message_color_example' # str |  (optional)
mentor_bubble_color = 'mentor_bubble_color_example' # str |  (optional)
align_mentor_bubble = 'align_mentor_bubble_example' # str |  (optional)
system_prompt = 'system_prompt_example' # str |  (optional)
llm_provider = 'llm_provider_example' # str |  (optional)
llm_name = 'llm_name_example' # str |  (optional)
featured = True # bool |  (optional)
disable_chathistory = True # bool |  (optional)
metadata = None # object |  (optional)
custom_css = 'custom_css_example' # str |  (optional)
department_id2 = 56 # int | Department to authorize users by (optional)
mentor_visibility = 'mentor_visibility_example' # str |  (optional)
enable_image_generation = True # bool |  (optional)
enable_web_browsing = True # bool |  (optional)
enable_code_interpreter = True # bool |  (optional)
allow_anonymous = True # bool |  (optional)
forkable = True # bool |  (optional)
forkable_with_training_data = True # bool |  (optional)
mentor_description = 'mentor_description_example' # str |  (optional)
uploaded_profile_image = 'uploaded_profile_image_example' # str |  (optional)
proactive_response = 'proactive_response_example' # str |  (optional)
greeting_method = iblai.GreetingMethodEnum() # GreetingMethodEnum |  (optional)
can_use_tools = True # bool |  (optional)
tool_slugs = ['tool_slugs_example'] # List[str] |  (optional)
llm_temperature = 3.4 # float |  (optional)
proactive_prompt = 'proactive_prompt_example' # str |  (optional)
moderation_system_prompt = 'moderation_system_prompt_example' # str |  (optional)
post_processing_prompt = 'post_processing_prompt_example' # str |  (optional)
moderation_response = 'moderation_response_example' # str |  (optional)
enable_moderation = True # bool |  (optional)
enable_post_processing_system = True # bool |  (optional)
enable_openai_assistant = True # bool |  (optional)
enable_total_grounding = True # bool |  (optional)
enable_suggested_prompts = True # bool |  (optional)
enable_guided_prompts = True # bool |  (optional)
mcp_servers = [56] # List[int] |  (optional)
google_voice = 56 # int |  (optional)
openai_voice = 56 # int |  (optional)
guided_prompt_instructions = 'guided_prompt_instructions_example' # str |  (optional)
safety_system_prompt = 'safety_system_prompt_example' # str |  (optional)
safety_response = 'safety_response_example' # str |  (optional)
enable_safety_system = True # bool |  (optional)
enable_memory_component = False # bool |  (optional) (default to False)
enable_spaced_repetition = False # bool |  (optional) (default to False)
enable_instruction_mode = False # bool |  (optional) (default to False)
enable_socratic_mode = False # bool |  (optional) (default to False)
is_guided_mentor = False # bool |  (optional) (default to False)
enable_email_chat = False # bool |  (optional) (default to False)
categories = [56] # List[int] |  (optional)

try:
    # Update Mentor Settings
    api_response = api_instance.ai_mentor_orgs_users_mentors_settings_update(mentor, org, user_id, department_id=department_id, mentor_name=mentor_name, template_name=template_name, display_name=display_name, profile_image=profile_image, initial_message=initial_message, suggested_message=suggested_message, theme=theme, user_message_color=user_message_color, mentor_bubble_color=mentor_bubble_color, align_mentor_bubble=align_mentor_bubble, system_prompt=system_prompt, llm_provider=llm_provider, llm_name=llm_name, featured=featured, disable_chathistory=disable_chathistory, metadata=metadata, custom_css=custom_css, department_id2=department_id2, mentor_visibility=mentor_visibility, enable_image_generation=enable_image_generation, enable_web_browsing=enable_web_browsing, enable_code_interpreter=enable_code_interpreter, allow_anonymous=allow_anonymous, forkable=forkable, forkable_with_training_data=forkable_with_training_data, mentor_description=mentor_description, uploaded_profile_image=uploaded_profile_image, proactive_response=proactive_response, greeting_method=greeting_method, can_use_tools=can_use_tools, tool_slugs=tool_slugs, llm_temperature=llm_temperature, proactive_prompt=proactive_prompt, moderation_system_prompt=moderation_system_prompt, post_processing_prompt=post_processing_prompt, moderation_response=moderation_response, enable_moderation=enable_moderation, enable_post_processing_system=enable_post_processing_system, enable_openai_assistant=enable_openai_assistant, enable_total_grounding=enable_total_grounding, enable_suggested_prompts=enable_suggested_prompts, enable_guided_prompts=enable_guided_prompts, mcp_servers=mcp_servers, google_voice=google_voice, openai_voice=openai_voice, guided_prompt_instructions=guided_prompt_instructions, safety_system_prompt=safety_system_prompt, safety_response=safety_response, enable_safety_system=enable_safety_system, enable_memory_component=enable_memory_component, enable_spaced_repetition=enable_spaced_repetition, enable_instruction_mode=enable_instruction_mode, enable_socratic_mode=enable_socratic_mode, is_guided_mentor=is_guided_mentor, enable_email_chat=enable_email_chat, categories=categories)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_settings_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **department_id** | **int**| Department to authorize users by | [optional] 
 **mentor_name** | **str**|  | [optional] 
 **template_name** | **str**|  | [optional] 
 **display_name** | **str**|  | [optional] 
 **profile_image** | **str**|  | [optional] 
 **initial_message** | **str**|  | [optional] 
 **suggested_message** | **str**|  | [optional] 
 **theme** | **str**|  | [optional] 
 **user_message_color** | **str**|  | [optional] 
 **mentor_bubble_color** | **str**|  | [optional] 
 **align_mentor_bubble** | **str**|  | [optional] 
 **system_prompt** | **str**|  | [optional] 
 **llm_provider** | **str**|  | [optional] 
 **llm_name** | **str**|  | [optional] 
 **featured** | **bool**|  | [optional] 
 **disable_chathistory** | **bool**|  | [optional] 
 **metadata** | [**object**](object.md)|  | [optional] 
 **custom_css** | **str**|  | [optional] 
 **department_id2** | **int**| Department to authorize users by | [optional] 
 **mentor_visibility** | **str**|  | [optional] 
 **enable_image_generation** | **bool**|  | [optional] 
 **enable_web_browsing** | **bool**|  | [optional] 
 **enable_code_interpreter** | **bool**|  | [optional] 
 **allow_anonymous** | **bool**|  | [optional] 
 **forkable** | **bool**|  | [optional] 
 **forkable_with_training_data** | **bool**|  | [optional] 
 **mentor_description** | **str**|  | [optional] 
 **uploaded_profile_image** | **str**|  | [optional] 
 **proactive_response** | **str**|  | [optional] 
 **greeting_method** | [**GreetingMethodEnum**](GreetingMethodEnum.md)|  | [optional] 
 **can_use_tools** | **bool**|  | [optional] 
 **tool_slugs** | [**List[str]**](str.md)|  | [optional] 
 **llm_temperature** | **float**|  | [optional] 
 **proactive_prompt** | **str**|  | [optional] 
 **moderation_system_prompt** | **str**|  | [optional] 
 **post_processing_prompt** | **str**|  | [optional] 
 **moderation_response** | **str**|  | [optional] 
 **enable_moderation** | **bool**|  | [optional] 
 **enable_post_processing_system** | **bool**|  | [optional] 
 **enable_openai_assistant** | **bool**|  | [optional] 
 **enable_total_grounding** | **bool**|  | [optional] 
 **enable_suggested_prompts** | **bool**|  | [optional] 
 **enable_guided_prompts** | **bool**|  | [optional] 
 **mcp_servers** | [**List[int]**](int.md)|  | [optional] 
 **google_voice** | **int**|  | [optional] 
 **openai_voice** | **int**|  | [optional] 
 **guided_prompt_instructions** | **str**|  | [optional] 
 **safety_system_prompt** | **str**|  | [optional] 
 **safety_response** | **str**|  | [optional] 
 **enable_safety_system** | **bool**|  | [optional] 
 **enable_memory_component** | **bool**|  | [optional] [default to False]
 **enable_spaced_repetition** | **bool**|  | [optional] [default to False]
 **enable_instruction_mode** | **bool**|  | [optional] [default to False]
 **enable_socratic_mode** | **bool**|  | [optional] [default to False]
 **is_guided_mentor** | **bool**|  | [optional] [default to False]
 **enable_email_chat** | **bool**|  | [optional] [default to False]
 **categories** | [**List[int]**](int.md)|  | [optional] 

### Return type

[**MentorSettings**](MentorSettings.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid request data |  -  |
**404** | Mentor not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_spaced_repetition_question_stats_retrieve**
> SpacedRepetitionQuestionStats ai_mentor_orgs_users_mentors_spaced_repetition_question_stats_retrieve(mentor, org, user_id)



Retrieve spaced repetition question statistics.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user to retrieve statistics for.     mentor: The unique identifier of the mentor.  Returns:     Response: Statistics about the user's performance on spaced repetition questions.  Raises:     NotFound: If the mentor or student does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.spaced_repetition_question_stats import SpacedRepetitionQuestionStats
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_spaced_repetition_question_stats_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_spaced_repetition_question_stats_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_spaced_repetition_question_stats_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**SpacedRepetitionQuestionStats**](SpacedRepetitionQuestionStats.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Mentor or student not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_list**
> List[QuestionCardTag] ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_list(mentor, org, user_id)



Retrieve a list of learning paths associated with a specific mentor and student.  This endpoint uses the memory component to establish the learning context for a student under the guidance of a mentor. It verifies that the provided organization identifier matches the mentor's platform key, and then retrieves learning path tags associated with the student's question cards. Each tag is annotated with the total number of question cards and the count of cards with successful repetitions (i.e., correct answers). The learning paths are ordered by the number of correct answers and limited to the top five entries.  Args:     request: The HTTP request containing the necessary context.     org (str): The organization identifier/platform key.     user_id (str): The username of the student.     mentor (str): The unique identifier of the mentor.     *args: Additional positional arguments.     **kwargs: Additional keyword arguments.  Returns:     Resp200onse: memory component detail infomrmation  Raises:     NotFound: If the memory component for the specified mentor and student cannot be found,               or if the organization identifier does not match the mentor's platform key.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.question_card_tag import QuestionCardTag
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_list(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[QuestionCardTag]**](QuestionCardTag.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Mentor or student not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_update**
> SpacedRepetitionLearningPath ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_update(mentor, org, user_id, spaced_repetition_learning_path)



Set a specific learning path for spaced repetition.  Args:     request: The HTTP request containing the learning path.     org: The organization/tenant identifier.     user_id: The ID of the user to set the learning path for.     mentor: The unique identifier of the mentor.  Returns:     Response: The set learning path.  Raises:     BadRequest: If the provided data is invalid.     NotFound: If the learning path, mentor, or student does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.spaced_repetition_learning_path import SpacedRepetitionLearningPath
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
spaced_repetition_learning_path = {"learning_path":"python-programming"} # SpacedRepetitionLearningPath | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_update(mentor, org, user_id, spaced_repetition_learning_path)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_spaced_repetition_recommended_paths_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **spaced_repetition_learning_path** | [**SpacedRepetitionLearningPath**](SpacedRepetitionLearningPath.md)|  | 

### Return type

[**SpacedRepetitionLearningPath**](SpacedRepetitionLearningPath.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid data |  -  |
**404** | Learning path, mentor, or student not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_star_create**
> StarMentor ai_mentor_orgs_users_mentors_star_create(mentor, org, user_id)



Endpoint for starring a mentor.  Accessible to students and admins.   Returns:      200: Star status.      400: When request is not valid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.star_mentor import StarMentor
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_star_create(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_star_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_star_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**StarMentor**](StarMentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_star_retrieve**
> StarMentor ai_mentor_orgs_users_mentors_star_retrieve(mentor, org, user_id)



Endpoint for getting the star status of a mentor.  Accessible to students and admins.   Returns:      200: Star status.      400: When request is not valid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.star_mentor import StarMentor
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_star_retrieve(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_star_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_star_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**StarMentor**](StarMentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_mentors_unstar_create**
> StarMentor ai_mentor_orgs_users_mentors_unstar_create(mentor, org, user_id)



Remove a mentor from a user's starred list.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user unstarring the mentor.     mentor: The identifier of the mentor to unstar.  Returns:     Response: The updated star status of the mentor.  Raises:     NotFound: If the specified mentor or student does not exist.     BadRequest: If the request is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.star_mentor import StarMentor
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_mentors_unstar_create(mentor, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_mentors_unstar_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_mentors_unstar_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**StarMentor**](StarMentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid request |  -  |
**404** | Mentor or student not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_metadata_retrieve**
> MentorMetadata ai_mentor_orgs_users_metadata_retrieve(org, user_id)



Retrieve metadata for a mentor.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.  Returns:     Response: The mentor metadata.  Raises:     NotFound: If no metadata exists for the specified mentor.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_metadata import MentorMetadata
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_metadata_retrieve(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_metadata_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_metadata_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MentorMetadata**](MentorMetadata.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Metadata not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_moderation_logs_destroy**
> ai_mentor_orgs_users_moderation_logs_destroy(id, org, user_id)



Endpoint to view and delete Moderation Logs for a tenant.  These can be filtered by username, platform_key and  mentor id   A search query can be conducted to search through the prompts and reason for the moderation catch event.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this moderation log.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_moderation_logs_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_moderation_logs_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this moderation log. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_moderation_logs_list**
> PaginatedModerationLogList ai_mentor_orgs_users_moderation_logs_list(org, user_id, mentor=mentor, ordering=ordering, page=page, page_size=page_size, platform_key=platform_key, search=search, target_system=target_system, username=username)



Endpoint to view and delete Moderation Logs for a tenant.  These can be filtered by username, platform_key and  mentor id   A search query can be conducted to search through the prompts and reason for the moderation catch event.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_moderation_log_list import PaginatedModerationLogList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor = 56 # int |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
platform_key = 'platform_key_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
target_system = 'target_system_example' # str | * `Safety System` - Safety System * `Moderation System` - Moderation System (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_moderation_logs_list(org, user_id, mentor=mentor, ordering=ordering, page=page, page_size=page_size, platform_key=platform_key, search=search, target_system=target_system, username=username)
    print("The response of AiMentorApi->ai_mentor_orgs_users_moderation_logs_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_moderation_logs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **platform_key** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **target_system** | **str**| * &#x60;Safety System&#x60; - Safety System * &#x60;Moderation System&#x60; - Moderation System | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedModerationLogList**](PaginatedModerationLogList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_moderation_logs_retrieve**
> ModerationLog ai_mentor_orgs_users_moderation_logs_retrieve(id, org, user_id)



Endpoint to view and delete Moderation Logs for a tenant.  These can be filtered by username, platform_key and  mentor id   A search query can be conducted to search through the prompts and reason for the moderation catch event.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.moderation_log import ModerationLog
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this moderation log.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_moderation_logs_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_moderation_logs_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_moderation_logs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this moderation log. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ModerationLog**](ModerationLog.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_partial_update**
> MentorCreate ai_mentor_orgs_users_partial_update(name, org, user_id, department_id=department_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility, patched_mentor_create=patched_mentor_create)



API ViewSet for managing mentors.  Provides endpoints to retrieve, create, update, and delete mentor data.  Permissions:     - Accessible to both tenant admins and students.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor_create import MentorCreate
from iblai.models.patched_mentor_create import PatchedMentorCreate
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
name = 'name_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | Department to filter by (optional)
filter_by = 'filter_by_example' # str | Filter options include, date, name, default is date  (optional)
metadata_key = 'metadata_key_example' # str | Metadata key to be queried with (optional)
metadata_value = 'metadata_value_example' # str | Metadata value to be filter for (optional)
return_session_information = True # bool | Declares if session information should be included in the mentor data (optional)
visibility = 'visibility_example' # str | visibility type  to be queried with (optional)
patched_mentor_create = iblai.PatchedMentorCreate() # PatchedMentorCreate |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_partial_update(name, org, user_id, department_id=department_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility, patched_mentor_create=patched_mentor_create)
    print("The response of AiMentorApi->ai_mentor_orgs_users_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **department_id** | **int**| Department to filter by | [optional] 
 **filter_by** | **str**| Filter options include, date, name, default is date  | [optional] 
 **metadata_key** | **str**| Metadata key to be queried with | [optional] 
 **metadata_value** | **str**| Metadata value to be filter for | [optional] 
 **return_session_information** | **bool**| Declares if session information should be included in the mentor data | [optional] 
 **visibility** | **str**| visibility type  to be queried with | [optional] 
 **patched_mentor_create** | [**PatchedMentorCreate**](PatchedMentorCreate.md)|  | [optional] 

### Return type

[**MentorCreate**](MentorCreate.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_periodic_agent_logs_list**
> PaginatedPeriodicAgentLogList ai_mentor_orgs_users_periodic_agent_logs_list(org, user_id, ordering=ordering, page=page, page_size=page_size, parent_mentor_id=parent_mentor_id, parent_session_id=parent_session_id, periodic_agent=periodic_agent, search=search, status=status, username=username)



Endpoint to view logs for periodic agent runs.  These logs contain the full mentor output for each run for debugging. Logs are ordered from newest to oldest. However this can be changed.  You can also filter logs for a PeriodicAgent by passing the `periodic_agent` query parameter in the URL.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_periodic_agent_log_list import PaginatedPeriodicAgentLogList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
parent_mentor_id = 'parent_mentor_id_example' # str |  (optional)
parent_session_id = 'parent_session_id_example' # str |  (optional)
periodic_agent = 56 # int |  (optional)
search = 'search_example' # str | A search term. (optional)
status = 'status_example' # str | * `success` - Success * `error` - Error * `running` - Running (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agent_logs_list(org, user_id, ordering=ordering, page=page, page_size=page_size, parent_mentor_id=parent_mentor_id, parent_session_id=parent_session_id, periodic_agent=periodic_agent, search=search, status=status, username=username)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agent_logs_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agent_logs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **parent_mentor_id** | **str**|  | [optional] 
 **parent_session_id** | **str**|  | [optional] 
 **periodic_agent** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **status** | **str**| * &#x60;success&#x60; - Success * &#x60;error&#x60; - Error * &#x60;running&#x60; - Running | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedPeriodicAgentLogList**](PaginatedPeriodicAgentLogList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_periodic_agent_logs_retrieve**
> PeriodicAgentLog ai_mentor_orgs_users_periodic_agent_logs_retrieve(id, org, user_id)



Endpoint to view logs for periodic agent runs.  These logs contain the full mentor output for each run for debugging. Logs are ordered from newest to oldest. However this can be changed.  You can also filter logs for a PeriodicAgent by passing the `periodic_agent` query parameter in the URL.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.periodic_agent_log import PeriodicAgentLog
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this periodic agent log.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agent_logs_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agent_logs_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agent_logs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this periodic agent log. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**PeriodicAgentLog**](PeriodicAgentLog.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_periodic_agents_create**
> PeriodicAgentCreate ai_mentor_orgs_users_periodic_agents_create(org, user_id, periodic_agent_create)



Endpoint to create and view, update and delete periodic agents.  Periodic agents are schedulers issued for mentors. These are configured with input prompt (if any) as well as a cron schedule to trigger the periodic agent.  Access to these are restricted to platform admins and tenant administrators  Session information for running the periodic agent will be generated with the credentials of the user (platform administrator) who created the agent.  A Periodic Agent is allowed to have a `callback_url` and `callback_secret`. When a `callback_url` is set for a Periodic Agent, a post request with data entries containing the log and timestamp of the run will be made to the callback_url provided. Here is the payload structure:         ```         {             \"timestamp\": \"timestamp when the run completed\",             \"status\": \"status of the periodic agent\",             \"prompt\": \"input prompt to agent,             \"agent_output\": \"...final response of agent\",             \"log\": \"... full agent run log\",             \"log_id\": periodic agent log id.,         }         ``` The payload is encrypted using the `callback_secret` provided.  You can validate the payload using the X-Hub-Signature-256 signature header for request data. This is a Sha256 encoded HMAC hex digest of the payload body.  ```python import hmac import haslib  def validate_payload(request: HttpRequest, callback_secret: str):     # Get the X-Hub-Signature-256 header from the request     received_signature = request.META.get(\"HTTP_X_HUB_SIGNATURE_256\", \"\")      if not received_signature.startswith(\"sha256=\"):         # Invalid signature format         return False      received_signature = received_signature[len(\"sha256=\") :]      try:         # Get the raw request body         payload = request.body          # Compute the expected signature using the app_secret         expected_signature = hmac.new(             callback_secret.encode(), payload, hashlib.sha256         ).hexdigest()          if hmac.compare_digest(received_signature, expected_signature):             # Signatures match, the payload is genuine             return True         else:             # Signatures don't match             return False     except Exception as e:         # Handle any errors that may occur during validation         return False  ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.periodic_agent_create import PeriodicAgentCreate
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
periodic_agent_create = iblai.PeriodicAgentCreate() # PeriodicAgentCreate | 

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agents_create(org, user_id, periodic_agent_create)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agents_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agents_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **periodic_agent_create** | [**PeriodicAgentCreate**](PeriodicAgentCreate.md)|  | 

### Return type

[**PeriodicAgentCreate**](PeriodicAgentCreate.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_periodic_agents_destroy**
> ai_mentor_orgs_users_periodic_agents_destroy(id, org, user_id)



Endpoint to create and view, update and delete periodic agents.  Periodic agents are schedulers issued for mentors. These are configured with input prompt (if any) as well as a cron schedule to trigger the periodic agent.  Access to these are restricted to platform admins and tenant administrators  Session information for running the periodic agent will be generated with the credentials of the user (platform administrator) who created the agent.  A Periodic Agent is allowed to have a `callback_url` and `callback_secret`. When a `callback_url` is set for a Periodic Agent, a post request with data entries containing the log and timestamp of the run will be made to the callback_url provided. Here is the payload structure:         ```         {             \"timestamp\": \"timestamp when the run completed\",             \"status\": \"status of the periodic agent\",             \"prompt\": \"input prompt to agent,             \"agent_output\": \"...final response of agent\",             \"log\": \"... full agent run log\",             \"log_id\": periodic agent log id.,         }         ``` The payload is encrypted using the `callback_secret` provided.  You can validate the payload using the X-Hub-Signature-256 signature header for request data. This is a Sha256 encoded HMAC hex digest of the payload body.  ```python import hmac import haslib  def validate_payload(request: HttpRequest, callback_secret: str):     # Get the X-Hub-Signature-256 header from the request     received_signature = request.META.get(\"HTTP_X_HUB_SIGNATURE_256\", \"\")      if not received_signature.startswith(\"sha256=\"):         # Invalid signature format         return False      received_signature = received_signature[len(\"sha256=\") :]      try:         # Get the raw request body         payload = request.body          # Compute the expected signature using the app_secret         expected_signature = hmac.new(             callback_secret.encode(), payload, hashlib.sha256         ).hexdigest()          if hmac.compare_digest(received_signature, expected_signature):             # Signatures match, the payload is genuine             return True         else:             # Signatures don't match             return False     except Exception as e:         # Handle any errors that may occur during validation         return False  ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this periodic agent.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_periodic_agents_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agents_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this periodic agent. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_periodic_agents_list**
> PaginatedPeriodicAgentList ai_mentor_orgs_users_periodic_agents_list(org, user_id, enabled=enabled, ordering=ordering, page=page, page_size=page_size, parent_mentor_id=parent_mentor_id, parent_session_id=parent_session_id, previous_agent=previous_agent, previous_agent_status=previous_agent_status, search=search, status=status, title=title, username=username)



Endpoint to create and view, update and delete periodic agents.  Periodic agents are schedulers issued for mentors. These are configured with input prompt (if any) as well as a cron schedule to trigger the periodic agent.  Access to these are restricted to platform admins and tenant administrators  Session information for running the periodic agent will be generated with the credentials of the user (platform administrator) who created the agent.  A Periodic Agent is allowed to have a `callback_url` and `callback_secret`. When a `callback_url` is set for a Periodic Agent, a post request with data entries containing the log and timestamp of the run will be made to the callback_url provided. Here is the payload structure:         ```         {             \"timestamp\": \"timestamp when the run completed\",             \"status\": \"status of the periodic agent\",             \"prompt\": \"input prompt to agent,             \"agent_output\": \"...final response of agent\",             \"log\": \"... full agent run log\",             \"log_id\": periodic agent log id.,         }         ``` The payload is encrypted using the `callback_secret` provided.  You can validate the payload using the X-Hub-Signature-256 signature header for request data. This is a Sha256 encoded HMAC hex digest of the payload body.  ```python import hmac import haslib  def validate_payload(request: HttpRequest, callback_secret: str):     # Get the X-Hub-Signature-256 header from the request     received_signature = request.META.get(\"HTTP_X_HUB_SIGNATURE_256\", \"\")      if not received_signature.startswith(\"sha256=\"):         # Invalid signature format         return False      received_signature = received_signature[len(\"sha256=\") :]      try:         # Get the raw request body         payload = request.body          # Compute the expected signature using the app_secret         expected_signature = hmac.new(             callback_secret.encode(), payload, hashlib.sha256         ).hexdigest()          if hmac.compare_digest(received_signature, expected_signature):             # Signatures match, the payload is genuine             return True         else:             # Signatures don't match             return False     except Exception as e:         # Handle any errors that may occur during validation         return False  ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_periodic_agent_list import PaginatedPeriodicAgentList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
enabled = True # bool |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
parent_mentor_id = 56 # int |  (optional)
parent_session_id = 'parent_session_id_example' # str |  (optional)
previous_agent = 56 # int |  (optional)
previous_agent_status = 'previous_agent_status_example' # str | The status that the previous agent must be in before this agent gets scheduled.  * `success` - Success * `error` - Error * `running` - Running * `pending` - Pending (optional)
search = 'search_example' # str | A search term. (optional)
status = 'status_example' # str | * `success` - Success * `error` - Error * `running` - Running * `pending` - Pending (optional)
title = 'title_example' # str |  (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agents_list(org, user_id, enabled=enabled, ordering=ordering, page=page, page_size=page_size, parent_mentor_id=parent_mentor_id, parent_session_id=parent_session_id, previous_agent=previous_agent, previous_agent_status=previous_agent_status, search=search, status=status, title=title, username=username)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agents_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agents_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **enabled** | **bool**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **parent_mentor_id** | **int**|  | [optional] 
 **parent_session_id** | **str**|  | [optional] 
 **previous_agent** | **int**|  | [optional] 
 **previous_agent_status** | **str**| The status that the previous agent must be in before this agent gets scheduled.  * &#x60;success&#x60; - Success * &#x60;error&#x60; - Error * &#x60;running&#x60; - Running * &#x60;pending&#x60; - Pending | [optional] 
 **search** | **str**| A search term. | [optional] 
 **status** | **str**| * &#x60;success&#x60; - Success * &#x60;error&#x60; - Error * &#x60;running&#x60; - Running * &#x60;pending&#x60; - Pending | [optional] 
 **title** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedPeriodicAgentList**](PaginatedPeriodicAgentList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_periodic_agents_partial_update**
> PeriodicAgentCreate ai_mentor_orgs_users_periodic_agents_partial_update(id, org, user_id, patched_periodic_agent_create=patched_periodic_agent_create)



Endpoint to create and view, update and delete periodic agents.  Periodic agents are schedulers issued for mentors. These are configured with input prompt (if any) as well as a cron schedule to trigger the periodic agent.  Access to these are restricted to platform admins and tenant administrators  Session information for running the periodic agent will be generated with the credentials of the user (platform administrator) who created the agent.  A Periodic Agent is allowed to have a `callback_url` and `callback_secret`. When a `callback_url` is set for a Periodic Agent, a post request with data entries containing the log and timestamp of the run will be made to the callback_url provided. Here is the payload structure:         ```         {             \"timestamp\": \"timestamp when the run completed\",             \"status\": \"status of the periodic agent\",             \"prompt\": \"input prompt to agent,             \"agent_output\": \"...final response of agent\",             \"log\": \"... full agent run log\",             \"log_id\": periodic agent log id.,         }         ``` The payload is encrypted using the `callback_secret` provided.  You can validate the payload using the X-Hub-Signature-256 signature header for request data. This is a Sha256 encoded HMAC hex digest of the payload body.  ```python import hmac import haslib  def validate_payload(request: HttpRequest, callback_secret: str):     # Get the X-Hub-Signature-256 header from the request     received_signature = request.META.get(\"HTTP_X_HUB_SIGNATURE_256\", \"\")      if not received_signature.startswith(\"sha256=\"):         # Invalid signature format         return False      received_signature = received_signature[len(\"sha256=\") :]      try:         # Get the raw request body         payload = request.body          # Compute the expected signature using the app_secret         expected_signature = hmac.new(             callback_secret.encode(), payload, hashlib.sha256         ).hexdigest()          if hmac.compare_digest(received_signature, expected_signature):             # Signatures match, the payload is genuine             return True         else:             # Signatures don't match             return False     except Exception as e:         # Handle any errors that may occur during validation         return False  ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_periodic_agent_create import PatchedPeriodicAgentCreate
from iblai.models.periodic_agent_create import PeriodicAgentCreate
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this periodic agent.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
patched_periodic_agent_create = iblai.PatchedPeriodicAgentCreate() # PatchedPeriodicAgentCreate |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agents_partial_update(id, org, user_id, patched_periodic_agent_create=patched_periodic_agent_create)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agents_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agents_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this periodic agent. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **patched_periodic_agent_create** | [**PatchedPeriodicAgentCreate**](PatchedPeriodicAgentCreate.md)|  | [optional] 

### Return type

[**PeriodicAgentCreate**](PeriodicAgentCreate.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_periodic_agents_retrieve**
> PeriodicAgent ai_mentor_orgs_users_periodic_agents_retrieve(id, org, user_id)



Endpoint to create and view, update and delete periodic agents.  Periodic agents are schedulers issued for mentors. These are configured with input prompt (if any) as well as a cron schedule to trigger the periodic agent.  Access to these are restricted to platform admins and tenant administrators  Session information for running the periodic agent will be generated with the credentials of the user (platform administrator) who created the agent.  A Periodic Agent is allowed to have a `callback_url` and `callback_secret`. When a `callback_url` is set for a Periodic Agent, a post request with data entries containing the log and timestamp of the run will be made to the callback_url provided. Here is the payload structure:         ```         {             \"timestamp\": \"timestamp when the run completed\",             \"status\": \"status of the periodic agent\",             \"prompt\": \"input prompt to agent,             \"agent_output\": \"...final response of agent\",             \"log\": \"... full agent run log\",             \"log_id\": periodic agent log id.,         }         ``` The payload is encrypted using the `callback_secret` provided.  You can validate the payload using the X-Hub-Signature-256 signature header for request data. This is a Sha256 encoded HMAC hex digest of the payload body.  ```python import hmac import haslib  def validate_payload(request: HttpRequest, callback_secret: str):     # Get the X-Hub-Signature-256 header from the request     received_signature = request.META.get(\"HTTP_X_HUB_SIGNATURE_256\", \"\")      if not received_signature.startswith(\"sha256=\"):         # Invalid signature format         return False      received_signature = received_signature[len(\"sha256=\") :]      try:         # Get the raw request body         payload = request.body          # Compute the expected signature using the app_secret         expected_signature = hmac.new(             callback_secret.encode(), payload, hashlib.sha256         ).hexdigest()          if hmac.compare_digest(received_signature, expected_signature):             # Signatures match, the payload is genuine             return True         else:             # Signatures don't match             return False     except Exception as e:         # Handle any errors that may occur during validation         return False  ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.periodic_agent import PeriodicAgent
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this periodic agent.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agents_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agents_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agents_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this periodic agent. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**PeriodicAgent**](PeriodicAgent.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_periodic_agents_update**
> PeriodicAgentCreate ai_mentor_orgs_users_periodic_agents_update(id, org, user_id, periodic_agent_create)



Endpoint to create and view, update and delete periodic agents.  Periodic agents are schedulers issued for mentors. These are configured with input prompt (if any) as well as a cron schedule to trigger the periodic agent.  Access to these are restricted to platform admins and tenant administrators  Session information for running the periodic agent will be generated with the credentials of the user (platform administrator) who created the agent.  A Periodic Agent is allowed to have a `callback_url` and `callback_secret`. When a `callback_url` is set for a Periodic Agent, a post request with data entries containing the log and timestamp of the run will be made to the callback_url provided. Here is the payload structure:         ```         {             \"timestamp\": \"timestamp when the run completed\",             \"status\": \"status of the periodic agent\",             \"prompt\": \"input prompt to agent,             \"agent_output\": \"...final response of agent\",             \"log\": \"... full agent run log\",             \"log_id\": periodic agent log id.,         }         ``` The payload is encrypted using the `callback_secret` provided.  You can validate the payload using the X-Hub-Signature-256 signature header for request data. This is a Sha256 encoded HMAC hex digest of the payload body.  ```python import hmac import haslib  def validate_payload(request: HttpRequest, callback_secret: str):     # Get the X-Hub-Signature-256 header from the request     received_signature = request.META.get(\"HTTP_X_HUB_SIGNATURE_256\", \"\")      if not received_signature.startswith(\"sha256=\"):         # Invalid signature format         return False      received_signature = received_signature[len(\"sha256=\") :]      try:         # Get the raw request body         payload = request.body          # Compute the expected signature using the app_secret         expected_signature = hmac.new(             callback_secret.encode(), payload, hashlib.sha256         ).hexdigest()          if hmac.compare_digest(received_signature, expected_signature):             # Signatures match, the payload is genuine             return True         else:             # Signatures don't match             return False     except Exception as e:         # Handle any errors that may occur during validation         return False  ```

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.periodic_agent_create import PeriodicAgentCreate
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this periodic agent.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
periodic_agent_create = iblai.PeriodicAgentCreate() # PeriodicAgentCreate | 

try:
    api_response = api_instance.ai_mentor_orgs_users_periodic_agents_update(id, org, user_id, periodic_agent_create)
    print("The response of AiMentorApi->ai_mentor_orgs_users_periodic_agents_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_periodic_agents_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this periodic agent. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **periodic_agent_create** | [**PeriodicAgentCreate**](PeriodicAgentCreate.md)|  | 

### Return type

[**PeriodicAgentCreate**](PeriodicAgentCreate.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_pin_message_create**
> PinnedMessageCreate ai_mentor_orgs_users_pin_message_create(org, user_id, pinned_message_request)



Create a pinned message for a user session.  Args:     request: The HTTP request containing session details.     org: Organization key identifier.     user_id: The username of the student.  Returns:     Response: Status 201 on success.  Raises:     NotFound: If the student does not exist.     ValidationError: If request data is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.pinned_message_create import PinnedMessageCreate
from iblai.models.pinned_message_request import PinnedMessageRequest
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
pinned_message_request = {"session_id":"550e8400-e29b-41d4-a716-446655440000"} # PinnedMessageRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_users_pin_message_create(org, user_id, pinned_message_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_pin_message_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_pin_message_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **pinned_message_request** | [**PinnedMessageRequest**](PinnedMessageRequest.md)|  | 

### Return type

[**PinnedMessageCreate**](PinnedMessageCreate.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_pin_message_destroy**
> Dict[str, object] ai_mentor_orgs_users_pin_message_destroy(org, user_id)



Delete a pinned message for a user.  Args:     request: The HTTP request containing session details.     org: Organization key identifier.     user_id: The username of the student.  Returns:     Response: Status 204 on success.  Raises:     NotFound: If the student or pinned message does not exist.     ValidationError: If request data is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_pin_message_destroy(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_pin_message_destroy:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_pin_message_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_pin_message_list**
> List[PinnedMessageGet] ai_mentor_orgs_users_pin_message_list(org, session_id, user_id)



Retrieve pinned messages for a user.  Args:     request: The HTTP request.     org: Organization key identifier.     user_id: The username of the student.  Returns:     Response: Paginated list of pinned messages.  Raises:     NotFound: If the student or session does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.pinned_message_get import PinnedMessageGet
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | Session id of the message to pin
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_pin_message_list(org, session_id, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_pin_message_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_pin_message_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**| Session id of the message to pin | 
 **user_id** | **str**|  | 

### Return type

[**List[PinnedMessageGet]**](PinnedMessageGet.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_planned_jobs_list**
> PaginatedJobRunList ai_mentor_orgs_users_planned_jobs_list(org, user_id, active=active, ordering=ordering, page=page, page_size=page_size, search=search, session=session)



Endpoints for viewing jobs and their status A job run refers to a task with steps that an agent is going to undertake. You can filter job runs by their status. Note that for a single user and a specified session, at most only one JobRun instance is active at any point in time.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_job_run_list import PaginatedJobRunList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
active = True # bool |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str | A search term. (optional)
session = 'session_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_planned_jobs_list(org, user_id, active=active, ordering=ordering, page=page, page_size=page_size, search=search, session=session)
    print("The response of AiMentorApi->ai_mentor_orgs_users_planned_jobs_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_planned_jobs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **active** | **bool**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **session** | **str**|  | [optional] 

### Return type

[**PaginatedJobRunList**](PaginatedJobRunList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_planned_jobs_retrieve**
> JobRun ai_mentor_orgs_users_planned_jobs_retrieve(id, org, user_id)



Endpoints for viewing jobs and their status A job run refers to a task with steps that an agent is going to undertake. You can filter job runs by their status. Note that for a single user and a specified session, at most only one JobRun instance is active at any point in time.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.job_run import JobRun
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this job run.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_planned_jobs_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_planned_jobs_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_planned_jobs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this job run. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**JobRun**](JobRun.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_playwright_scripts_create**
> PlayWrightScript ai_mentor_orgs_users_playwright_scripts_create(org, user_id, play_wright_script)



Endpoints for viewing playwright scripts and updating playwright scripts for a tenant and user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.play_wright_script import PlayWrightScript
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
play_wright_script = iblai.PlayWrightScript() # PlayWrightScript | 

try:
    api_response = api_instance.ai_mentor_orgs_users_playwright_scripts_create(org, user_id, play_wright_script)
    print("The response of AiMentorApi->ai_mentor_orgs_users_playwright_scripts_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_playwright_scripts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **play_wright_script** | [**PlayWrightScript**](PlayWrightScript.md)|  | 

### Return type

[**PlayWrightScript**](PlayWrightScript.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_playwright_scripts_destroy**
> ai_mentor_orgs_users_playwright_scripts_destroy(id, org, user_id)



Endpoints for viewing playwright scripts and updating playwright scripts for a tenant and user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this play wright script.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_playwright_scripts_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_playwright_scripts_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this play wright script. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_playwright_scripts_list**
> PaginatedPlayWrightScriptList ai_mentor_orgs_users_playwright_scripts_list(org, user_id, is_public=is_public, ordering=ordering, page=page, page_size=page_size, search=search, student=student)



Endpoints for viewing playwright scripts and updating playwright scripts for a tenant and user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_play_wright_script_list import PaginatedPlayWrightScriptList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
is_public = True # bool |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str | A search term. (optional)
student = 56 # int | edX user ID (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_playwright_scripts_list(org, user_id, is_public=is_public, ordering=ordering, page=page, page_size=page_size, search=search, student=student)
    print("The response of AiMentorApi->ai_mentor_orgs_users_playwright_scripts_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_playwright_scripts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **is_public** | **bool**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **student** | **int**| edX user ID | [optional] 

### Return type

[**PaginatedPlayWrightScriptList**](PaginatedPlayWrightScriptList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_playwright_scripts_partial_update**
> PlayWrightScript ai_mentor_orgs_users_playwright_scripts_partial_update(id, org, user_id, patched_play_wright_script=patched_play_wright_script)



Endpoints for viewing playwright scripts and updating playwright scripts for a tenant and user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.patched_play_wright_script import PatchedPlayWrightScript
from iblai.models.play_wright_script import PlayWrightScript
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this play wright script.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
patched_play_wright_script = iblai.PatchedPlayWrightScript() # PatchedPlayWrightScript |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_playwright_scripts_partial_update(id, org, user_id, patched_play_wright_script=patched_play_wright_script)
    print("The response of AiMentorApi->ai_mentor_orgs_users_playwright_scripts_partial_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_playwright_scripts_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this play wright script. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **patched_play_wright_script** | [**PatchedPlayWrightScript**](PatchedPlayWrightScript.md)|  | [optional] 

### Return type

[**PlayWrightScript**](PlayWrightScript.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_playwright_scripts_retrieve**
> PlayWrightScript ai_mentor_orgs_users_playwright_scripts_retrieve(id, org, user_id)



Endpoints for viewing playwright scripts and updating playwright scripts for a tenant and user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.play_wright_script import PlayWrightScript
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this play wright script.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_playwright_scripts_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_playwright_scripts_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_playwright_scripts_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this play wright script. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**PlayWrightScript**](PlayWrightScript.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_playwright_scripts_update**
> PlayWrightScript ai_mentor_orgs_users_playwright_scripts_update(id, org, user_id, play_wright_script)



Endpoints for viewing playwright scripts and updating playwright scripts for a tenant and user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.play_wright_script import PlayWrightScript
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this play wright script.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
play_wright_script = iblai.PlayWrightScript() # PlayWrightScript | 

try:
    api_response = api_instance.ai_mentor_orgs_users_playwright_scripts_update(id, org, user_id, play_wright_script)
    print("The response of AiMentorApi->ai_mentor_orgs_users_playwright_scripts_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_playwright_scripts_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this play wright script. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **play_wright_script** | [**PlayWrightScript**](PlayWrightScript.md)|  | 

### Return type

[**PlayWrightScript**](PlayWrightScript.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_predictive_analytics_create**
> PredictiveAnalyticsResponse ai_mentor_orgs_users_predictive_analytics_create(org, user_id, predictive_analytics_request)



Retrieve predictive analytics based on historical data variables.  Args:     request: HTTP request containing predictive analytics input.     org: Organization key identifier.  Returns:     - 200: Object containing predicted data.     - 400: When AI response cannot be loaded into JSON.     - 404: When OpenAI key for the tenant is not set.     - 429: When OpenAI request exceeds the rate limit.  Example:     **POST** `/api/ai-prompt/orgs/main/users/johndoe/predictive-analytics/`

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.predictive_analytics_request import PredictiveAnalyticsRequest
from iblai.models.predictive_analytics_response import PredictiveAnalyticsResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
predictive_analytics_request = {"prompt":{"data_variables":[{"variable_name":"registered_users","data_set":{"2023-10-06":4,"2023-10-07":1,"2023-10-08":0,"2023-10-09":5,"2023-10-10":4},"number_of_data_points":5},{"variable_name":"courses_enrolled","data_set":{"2023-08-09":0,"2023-08-10":0,"2023-08-11":0,"2023-08-12":0,"2023-08-13":0},"number_of_data_points":6}]}} # PredictiveAnalyticsRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_users_predictive_analytics_create(org, user_id, predictive_analytics_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_predictive_analytics_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_predictive_analytics_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **predictive_analytics_request** | [**PredictiveAnalyticsRequest**](PredictiveAnalyticsRequest.md)|  | 

### Return type

[**PredictiveAnalyticsResponse**](PredictiveAnalyticsResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_recent_messages_retrieve**
> ai_mentor_orgs_users_recent_messages_retrieve(org, user_id)



Retrieves recent chat messages based on provided query parameters.  Returns:     200: Paginated List of chat messages.     400: Invalid query parameters.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_recent_messages_retrieve(org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_recent_messages_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_recently_accessed_mentors_list**
> List[RecentlyAccessedMentor] ai_mentor_orgs_users_recently_accessed_mentors_list(org, user_id)



Endpoint for listing most recently accessed mentors.  Accessible to students and admins.   Returns:      200: List of most recently accessed mentors.      400: When request is not valid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.recently_accessed_mentor import RecentlyAccessedMentor
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_recently_accessed_mentors_list(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_recently_accessed_mentors_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_recently_accessed_mentors_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[RecentlyAccessedMentor]**](RecentlyAccessedMentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_recommend_courses_block_retrieve**
> RecommendCourseBlock ai_mentor_orgs_users_recommend_courses_block_retrieve(org, user_id, include_learner_skills=include_learner_skills, include_main_courses=include_main_courses, rank_by_difficulty=rank_by_difficulty, return_course_data=return_course_data, return_number=return_number, search_terms=search_terms)



Retrieve recommended course blocks for a specific user.  Args:     request: The HTTP request containing query parameters.     org: The organization/tenant identifier.     user_id: The ID of the user to get recommendations for.  Returns:     Response: A list of recommended course blocks.  Raises:     BadRequest: If the query parameters are invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.recommend_course_block import RecommendCourseBlock
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
include_learner_skills = True # bool | Include available learner skills for search (optional) (default to True)
include_main_courses = True # bool | Include courses from the main tenant (optional) (default to True)
rank_by_difficulty = False # bool | Rank by course difficulty (optional) (default to False)
return_course_data = False # bool | Return course data (optional) (default to False)
return_number = 56 # int | Number of courses to return (optional)
search_terms = 'search_terms_example' # str | Terms to be searched (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_recommend_courses_block_retrieve(org, user_id, include_learner_skills=include_learner_skills, include_main_courses=include_main_courses, rank_by_difficulty=rank_by_difficulty, return_course_data=return_course_data, return_number=return_number, search_terms=search_terms)
    print("The response of AiMentorApi->ai_mentor_orgs_users_recommend_courses_block_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_recommend_courses_block_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **include_learner_skills** | **bool**| Include available learner skills for search | [optional] [default to True]
 **include_main_courses** | **bool**| Include courses from the main tenant | [optional] [default to True]
 **rank_by_difficulty** | **bool**| Rank by course difficulty | [optional] [default to False]
 **return_course_data** | **bool**| Return course data | [optional] [default to False]
 **return_number** | **int**| Number of courses to return | [optional] 
 **search_terms** | **str**| Terms to be searched | [optional] 

### Return type

[**RecommendCourseBlock**](RecommendCourseBlock.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid query parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_recommend_courses_retrieve**
> RecommendCourseResponse ai_mentor_orgs_users_recommend_courses_retrieve(org, user_id, include_learner_skills=include_learner_skills, include_main_courses=include_main_courses, rank_by_difficulty=rank_by_difficulty, return_course_data=return_course_data, return_number=return_number, search_terms=search_terms)



Retrieve recommended courses for a specific user.  Args:     request: The HTTP request containing query parameters.     org: The organization/tenant identifier.     user_id: The ID of the user to get recommendations for.  Returns:     Response: A list of recommended courses.  Raises:     BadRequest: If the query parameters are invalid.     NotFound: If the OpenAI API key for the tenant is not found.     TooManyRequests: If rate limits are exceeded.     ServerError: If there's an error processing the AI response.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.recommend_course_response import RecommendCourseResponse
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
include_learner_skills = True # bool | Include available learner skills for search (optional) (default to True)
include_main_courses = True # bool | Include courses from the main tenant (optional) (default to True)
rank_by_difficulty = False # bool | Rank by course difficulty (optional) (default to False)
return_course_data = False # bool | Return course data (optional) (default to False)
return_number = 56 # int | Number of courses to return (optional)
search_terms = 'search_terms_example' # str | Terms to be searched (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_recommend_courses_retrieve(org, user_id, include_learner_skills=include_learner_skills, include_main_courses=include_main_courses, rank_by_difficulty=rank_by_difficulty, return_course_data=return_course_data, return_number=return_number, search_terms=search_terms)
    print("The response of AiMentorApi->ai_mentor_orgs_users_recommend_courses_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_recommend_courses_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **include_learner_skills** | **bool**| Include available learner skills for search | [optional] [default to True]
 **include_main_courses** | **bool**| Include courses from the main tenant | [optional] [default to True]
 **rank_by_difficulty** | **bool**| Rank by course difficulty | [optional] [default to False]
 **return_course_data** | **bool**| Return course data | [optional] [default to False]
 **return_number** | **int**| Number of courses to return | [optional] 
 **search_terms** | **str**| Terms to be searched | [optional] 

### Return type

[**RecommendCourseResponse**](RecommendCourseResponse.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid query parameters |  -  |
**404** | API key not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Server error processing AI response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_resources_web_create**
> List[WebResource] ai_mentor_orgs_users_resources_web_create(org, user_id, web_resources_query)



Search for web resources based on a query.  Args:     request: The HTTP request containing the search query.     org: The organization/tenant identifier.     user_id: The ID of the user making the request.  Returns:     Response: A list of web resources matching the query.  Raises:     ValidationError: If the search fails or returns no results.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.web_resource import WebResource
from iblai.models.web_resources_query import WebResourcesQuery
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
web_resources_query = {"query":"ibl education"} # WebResourcesQuery | 

try:
    api_response = api_instance.ai_mentor_orgs_users_resources_web_create(org, user_id, web_resources_query)
    print("The response of AiMentorApi->ai_mentor_orgs_users_resources_web_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_resources_web_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **web_resources_query** | [**WebResourcesQuery**](WebResourcesQuery.md)|  | 

### Return type

[**List[WebResource]**](WebResource.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Failed to fetch web resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_retrieve**
> Mentor ai_mentor_orgs_users_retrieve(name, org, user_id, department_id=department_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)



API ViewSet for managing mentors.  Provides endpoints to retrieve, create, update, and delete mentor data.  Permissions:     - Accessible to both tenant admins and students.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
name = 'name_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
department_id = 56 # int | Department to filter by (optional)
filter_by = 'filter_by_example' # str | Filter options include, date, name, default is date  (optional)
metadata_key = 'metadata_key_example' # str | Metadata key to be queried with (optional)
metadata_value = 'metadata_value_example' # str | Metadata value to be filter for (optional)
return_session_information = True # bool | Declares if session information should be included in the mentor data (optional)
visibility = 'visibility_example' # str | visibility type  to be queried with (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_retrieve(name, org, user_id, department_id=department_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)
    print("The response of AiMentorApi->ai_mentor_orgs_users_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **department_id** | **int**| Department to filter by | [optional] 
 **filter_by** | **str**| Filter options include, date, name, default is date  | [optional] 
 **metadata_key** | **str**| Metadata key to be queried with | [optional] 
 **metadata_value** | **str**| Metadata value to be filter for | [optional] 
 **return_session_information** | **bool**| Declares if session information should be included in the mentor data | [optional] 
 **visibility** | **str**| visibility type  to be queried with | [optional] 

### Return type

[**Mentor**](Mentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_safety_logs_destroy**
> ai_mentor_orgs_users_safety_logs_destroy(id, org, user_id)



Endpoint to view and delete Safety System Logs for a tenant.  These can be filtered by username, platform_key and  mentor id   A search query can be conducted to search through the prompts and reason for the moderation catch event.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this moderation log.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_safety_logs_destroy(id, org, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_safety_logs_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this moderation log. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_safety_logs_list**
> PaginatedModerationLogList ai_mentor_orgs_users_safety_logs_list(org, user_id, mentor=mentor, ordering=ordering, page=page, page_size=page_size, platform_key=platform_key, search=search, target_system=target_system, username=username)



Endpoint to view and delete Safety System Logs for a tenant.  These can be filtered by username, platform_key and  mentor id   A search query can be conducted to search through the prompts and reason for the moderation catch event.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_moderation_log_list import PaginatedModerationLogList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor = 56 # int |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
platform_key = 'platform_key_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
target_system = 'target_system_example' # str | * `Safety System` - Safety System * `Moderation System` - Moderation System (optional)
username = 'username_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_safety_logs_list(org, user_id, mentor=mentor, ordering=ordering, page=page, page_size=page_size, platform_key=platform_key, search=search, target_system=target_system, username=username)
    print("The response of AiMentorApi->ai_mentor_orgs_users_safety_logs_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_safety_logs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **platform_key** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **target_system** | **str**| * &#x60;Safety System&#x60; - Safety System * &#x60;Moderation System&#x60; - Moderation System | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedModerationLogList**](PaginatedModerationLogList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_safety_logs_retrieve**
> ModerationLog ai_mentor_orgs_users_safety_logs_retrieve(id, org, user_id)



Endpoint to view and delete Safety System Logs for a tenant.  These can be filtered by username, platform_key and  mentor id   A search query can be conducted to search through the prompts and reason for the moderation catch event.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.moderation_log import ModerationLog
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this moderation log.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_safety_logs_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_safety_logs_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_safety_logs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this moderation log. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ModerationLog**](ModerationLog.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_session_detail_mentors_list**
> List[SessionDetail] ai_mentor_orgs_users_session_detail_mentors_list(mentor, org, user_id, page=page)



Retrieve session details including message counts and timestamps.  Query Parameters:     page (optional, int): Page number for pagination.  Returns:     - 200: Paginated list of session details.     - 404: Session not found.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.session_detail import SessionDetail
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
mentor = 'mentor_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
page = 56 # int | Page number for pagination (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_session_detail_mentors_list(mentor, org, user_id, page=page)
    print("The response of AiMentorApi->ai_mentor_orgs_users_session_detail_mentors_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_session_detail_mentors_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mentor** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **page** | **int**| Page number for pagination | [optional] 

### Return type

[**List[SessionDetail]**](SessionDetail.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Session not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_sessionid_list**
> List[ChatHistorySessionId] ai_mentor_orgs_users_sessionid_list(org, user_id, end_date=end_date, start_date=start_date)



Retrieve user sessions filtered by start date and end date.  Query Parameters:     start_date (optional, ISO format): Start date for filtering sessions.     end_date (optional, ISO format): End date for filtering sessions.  Returns:     - 200: List of session IDs with insertion timestamps.     - 400: Invalid request parameters.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.chat_history_session_id import ChatHistorySessionId
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
end_date = 'end_date_example' # str |  (optional)
start_date = 'start_date_example' # str |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_sessionid_list(org, user_id, end_date=end_date, start_date=start_date)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessionid_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessionid_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **end_date** | **str**|  | [optional] 
 **start_date** | **str**|  | [optional] 

### Return type

[**List[ChatHistorySessionId]**](ChatHistorySessionId.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_sessions_browser_screenshot_retrieve**
> SessionBrowserScreenshot ai_mentor_orgs_users_sessions_browser_screenshot_retrieve(org, session_id, user_id)



Endpoint to fetch the logs of a session. Logs are cached for up to 1 hour of their creation: accessing the logs after an hour will result in an empty data.  This is intentional and made to avoid cases where logs bloat our in-memory db.  Accessible to tenant admins and students.  Url Args:     org (str): The organization's platform key.     user_id (str): The username  identifier of the individual.     session_id (str): The session id.  Returns:      200: a SessionBrowserScreenshot object

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.session_browser_screenshot import SessionBrowserScreenshot
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_browser_screenshot_retrieve(org, session_id, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_browser_screenshot_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_browser_screenshot_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**SessionBrowserScreenshot**](SessionBrowserScreenshot.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Session or screenshots not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_sessions_create**
> ChatSessionResponse ai_mentor_orgs_users_sessions_create(org, user_id, chat_session_request)



Retrieve or create a chat session with a mentor.  Passing `null` as `tools` results in using all tools assigned to the mentor. To specify that no tools be used, pass an empty list.  Args:     request: HTTP request containing mentor details.     org: Organization key identifier.     user_id (optional): Username for authentication (if required by the mentor).  Returns:     Response: JSON object containing the session ID.  Raises:     Http404: If the mentor is not found.     ValidationError: If the username is invalid.     ValidationError: If one or more tool slugs are invalid.

### Example


```python
import iblai
from iblai.models.chat_session_request import ChatSessionRequest
from iblai.models.chat_session_response import ChatSessionResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
chat_session_request = {"mentor":"ai-mentor"} # ChatSessionRequest | 

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_create(org, user_id, chat_session_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **chat_session_request** | [**ChatSessionRequest**](ChatSessionRequest.md)|  | 

### Return type

[**ChatSessionResponse**](ChatSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_sessions_destroy**
> Dict[str, object] ai_mentor_orgs_users_sessions_destroy(org, session_id, user_id)



Deletes all messages in a chat session.

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_destroy(org, session_id, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_destroy:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_sessions_download_session_retrieve**
> ai_mentor_orgs_users_sessions_download_session_retrieve(org, session_id, user_id)



Retrieves the chat history for a session as a plain text file.  Returns:     200: txt file containing coversation

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_instance.ai_mentor_orgs_users_sessions_download_session_retrieve(org, session_id, user_id)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_download_session_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_sessions_memory_retrieve**
> SessionMemoryStorage ai_mentor_orgs_users_sessions_memory_retrieve(org, session_id, user_id)



Retrieve memory data for a specific session.  This endpoint returns the memory components (knowledge gaps, lessons learned, help requests) that were generated during the specified chat session.  Args:     org: The organization/tenant identifier.     user_id: The ID of the user who owns the session.     session_id: The ID of the session to retrieve memory for.  Returns:     Response: The memory data associated with the session.  Raises:     NotFound: If the session does not exist or does not belong to the user.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.session_memory_storage import SessionMemoryStorage
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_memory_retrieve(org, session_id, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_memory_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_memory_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**SessionMemoryStorage**](SessionMemoryStorage.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Session not found or does not belong to user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_sessions_retrieve**
> MessageView ai_mentor_orgs_users_sessions_retrieve(org, session_id, user_id, share=share)

Retrieve Chat Messages

Fetches chat messages for a specific session.

### Example


```python
import iblai
from iblai.models.message_view import MessageView
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 
share = False # bool |  (optional) (default to False)

try:
    # Retrieve Chat Messages
    api_response = api_instance.ai_mentor_orgs_users_sessions_retrieve(org, session_id, user_id, share=share)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 
 **share** | **bool**|  | [optional] [default to False]

### Return type

[**MessageView**](MessageView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_sessions_shell_logs_retrieve**
> ShellLogs ai_mentor_orgs_users_sessions_shell_logs_retrieve(org, session_id, user_id)



Retrieve shell logs for a specific session.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user who owns the session.     session_id: The ID of the session to retrieve logs for.  Returns:     Response: The shell logs for the specified session.  Raises:     NotFound: If the specified session does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.shell_logs import ShellLogs
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_shell_logs_retrieve(org, session_id, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_shell_logs_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_shell_logs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ShellLogs**](ShellLogs.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Session not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_sessions_suggestion_list**
> List[RelatedText] ai_mentor_orgs_users_sessions_suggestion_list(org, session_id, user_id, num_questions=num_questions)



Retrieve a list of related questions based on a chat session.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.related_text import RelatedText
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 
num_questions = 3 # int |  (optional) (default to 3)

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_suggestion_list(org, session_id, user_id, num_questions=num_questions)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_suggestion_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_suggestion_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 
 **num_questions** | **int**|  | [optional] [default to 3]

### Return type

[**List[RelatedText]**](RelatedText.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_sessions_tasks_retrieve**
> ChatHistoryItem ai_mentor_orgs_users_sessions_tasks_retrieve(org, session_id, task_id, user_id, to_csv=to_csv)



Retrieves the chat history for a given session if the export task is ready.  Returns:      200: When task is not ready.      200: chat history object      400: When data is not valid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.chat_history_item import ChatHistoryItem
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
task_id = 'task_id_example' # str | 
user_id = 'user_id_example' # str | 
to_csv = False # bool | Choose download in csv or not (optional) (default to False)

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_tasks_retrieve(org, session_id, task_id, user_id, to_csv=to_csv)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_tasks_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_tasks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **task_id** | **str**|  | 
 **user_id** | **str**|  | 
 **to_csv** | **bool**| Choose download in csv or not | [optional] [default to False]

### Return type

[**ChatHistoryItem**](ChatHistoryItem.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_sessions_update**
> MessageViewUpdatResponse ai_mentor_orgs_users_sessions_update(org, session_id, user_id, message_view_request=message_view_request)



Update the title of a chat session and its tools

### Example


```python
import iblai
from iblai.models.message_view_request import MessageViewRequest
from iblai.models.message_view_updat_response import MessageViewUpdatResponse
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 
message_view_request = {"title":"New Title","tools":["web-search","image-generation"]} # MessageViewRequest |  (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_sessions_update(org, session_id, user_id, message_view_request=message_view_request)
    print("The response of AiMentorApi->ai_mentor_orgs_users_sessions_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_sessions_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 
 **message_view_request** | [**MessageViewRequest**](MessageViewRequest.md)|  | [optional] 

### Return type

[**MessageViewUpdatResponse**](MessageViewUpdatResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_settings_tenant_llm_create**
> LLMModelForTenant ai_mentor_orgs_users_settings_tenant_llm_create(org, user_id, llm_model_for_tenant)



Create or update an LLM model for a tenant.  Accessible only to tenant administrators.  Args:     request: The HTTP request containing LLM model details.     org: The unique identifier of the tenant.  Returns:     Response: Details of the newly created or updated LLM model.  Raises:     ValidationError: If request data is invalid.     NotFound: If the tenant does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_model_for_tenant import LLMModelForTenant
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
llm_model_for_tenant = {"tenant":"example-tenant","model_name":"gpt-4","configuration":{"max_tokens":2000,"temperature":0.8,"top_p":0.85}} # LLMModelForTenant | 

try:
    api_response = api_instance.ai_mentor_orgs_users_settings_tenant_llm_create(org, user_id, llm_model_for_tenant)
    print("The response of AiMentorApi->ai_mentor_orgs_users_settings_tenant_llm_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_settings_tenant_llm_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **llm_model_for_tenant** | [**LLMModelForTenant**](LLMModelForTenant.md)|  | 

### Return type

[**LLMModelForTenant**](LLMModelForTenant.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_settings_tenant_llm_list**
> List[LLMModelForTenant] ai_mentor_orgs_users_settings_tenant_llm_list(org, user_id)



Retrieve all LLM models assigned to a specific tenant.  Args:     request: The HTTP request.     org: The unique identifier of the tenant.  Returns:     Response: A list of LLM models assigned to the tenant.  Raises:     NotFound: If the specified tenant does not have any associated models.     ValidationError: If an unexpected error occurs.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.llm_model_for_tenant import LLMModelForTenant
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_settings_tenant_llm_list(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_settings_tenant_llm_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_settings_tenant_llm_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[LLMModelForTenant]**](LLMModelForTenant.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_starred_mentors_list**
> List[StarMentor] ai_mentor_orgs_users_starred_mentors_list(org, user_id)



Retrieve a list of mentors starred by a specific user.  Args:     request: The HTTP request.     org: The organization/tenant identifier.     user_id: The ID of the user to retrieve starred mentors for.  Returns:     Response: A list of the user's starred mentors, sorted by most recently accessed.  Raises:     NotFound: If the specified student does not exist.     BadRequest: If the request is invalid.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.star_mentor import StarMentor
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_starred_mentors_list(org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_starred_mentors_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_starred_mentors_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[StarMentor]**](StarMentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid request |  -  |
**404** | Student not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_tasks_retrieve**
> RetrieveTask ai_mentor_orgs_users_tasks_retrieve(org, task_id, user_id)



Retrieves the status of a task using its task ID.  Accessible to both tenant admins and students.  Returns:      200: task id

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.retrieve_task import RetrieveTask
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
task_id = 'task_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_tasks_retrieve(org, task_id, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_tasks_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_tasks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **task_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**RetrieveTask**](RetrieveTask.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_tasks_sessions_create**
> TaskView ai_mentor_orgs_users_tasks_sessions_create(org, session_id, user_id, task_view)



Export chat history for a session.  Returns:     200: Task ID for the export operation.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.task_view import TaskView
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
session_id = 'session_id_example' # str | 
user_id = 'user_id_example' # str | 
task_view = {"task_id":"307be194-2351-44ff-8d7b-24660fd9ec34"} # TaskView | 

try:
    api_response = api_instance.ai_mentor_orgs_users_tasks_sessions_create(org, session_id, user_id, task_view)
    print("The response of AiMentorApi->ai_mentor_orgs_users_tasks_sessions_create:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_tasks_sessions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **session_id** | **str**|  | 
 **user_id** | **str**|  | 
 **task_view** | [**TaskView**](TaskView.md)|  | 

### Return type

[**TaskView**](TaskView.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_update**
> Mentor ai_mentor_orgs_users_update(name, org, user_id, mentor_create, department_id=department_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)



Update a mentor's details with RBAC enforcement and custom serializer handling.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.mentor import Mentor
from iblai.models.mentor_create import MentorCreate
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
name = 'name_example' # str | 
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
mentor_create = {"name":"John Doe","unique_id":"1234","platform_key":"main","metadata":{"specialty":"AI Research"}} # MentorCreate | 
department_id = 56 # int | Department to filter by (optional)
filter_by = 'filter_by_example' # str | Filter options include, date, name, default is date  (optional)
metadata_key = 'metadata_key_example' # str | Metadata key to be queried with (optional)
metadata_value = 'metadata_value_example' # str | Metadata value to be filter for (optional)
return_session_information = True # bool | Declares if session information should be included in the mentor data (optional)
visibility = 'visibility_example' # str | visibility type  to be queried with (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_update(name, org, user_id, mentor_create, department_id=department_id, filter_by=filter_by, metadata_key=metadata_key, metadata_value=metadata_value, return_session_information=return_session_information, visibility=visibility)
    print("The response of AiMentorApi->ai_mentor_orgs_users_update:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **mentor_create** | [**MentorCreate**](MentorCreate.md)|  | 
 **department_id** | **int**| Department to filter by | [optional] 
 **filter_by** | **str**| Filter options include, date, name, default is date  | [optional] 
 **metadata_key** | **str**| Metadata key to be queried with | [optional] 
 **metadata_value** | **str**| Metadata value to be filter for | [optional] 
 **return_session_information** | **bool**| Declares if session information should be included in the mentor data | [optional] 
 **visibility** | **str**| visibility type  to be queried with | [optional] 

### Return type

[**Mentor**](Mentor.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_voices_list**
> PaginatedVoiceList ai_mentor_orgs_users_voices_list(org, user_id, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search)



Retrieve a list of available voice options.  Args:     request: The HTTP request.  Returns:     Response: A list of available voice options.  Raises:     NotFound: If no voice options are available.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.paginated_voice_list import PaginatedVoiceList
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
provider = 'provider_example' # str | * `openai` - Openai * `google` - Google * `elevenlabs` - Elevenlabs (optional)
search = 'search_example' # str | A search term. (optional)

try:
    api_response = api_instance.ai_mentor_orgs_users_voices_list(org, user_id, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search)
    print("The response of AiMentorApi->ai_mentor_orgs_users_voices_list:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_voices_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **user_id** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider** | **str**| * &#x60;openai&#x60; - Openai * &#x60;google&#x60; - Google * &#x60;elevenlabs&#x60; - Elevenlabs | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedVoiceList**](PaginatedVoiceList.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Voice options not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_users_voices_retrieve**
> Voice ai_mentor_orgs_users_voices_retrieve(id, org, user_id)



Retrieve details of a specific voice option.  Args:     request: The HTTP request.     pk: The primary key of the voice option to retrieve.  Returns:     Response: The details of the specified voice option.  Raises:     NotFound: If the specified voice option does not exist.

### Example

* Api Key Authentication (PlatformApiKeyAuthentication):

```python
import iblai
from iblai.models.voice import Voice
from iblai.rest import ApiException
from pprint import pprint

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# The APIs use bearer tokens for authentication with a prefix of: `Api-Key`
# You can generate an authenticated client using the following helper method
client = get_platform_api_client(
    host="https://base.manager.iblai.app", 
    key=os.environ["API_KEY"]
)

# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
id = 56 # int | A unique integer value identifying this voice.
org = 'org_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.ai_mentor_orgs_users_voices_retrieve(id, org, user_id)
    print("The response of AiMentorApi->ai_mentor_orgs_users_voices_retrieve:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_users_voices_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this voice. | 
 **org** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**Voice**](Voice.md)

### Authorization

[PlatformApiKeyAuthentication](../README.md#PlatformApiKeyAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Voice option not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_webhooks_azure_trigger_create**
> ai_mentor_orgs_webhooks_azure_trigger_create(org, slug)



### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 
slug = 'slug_example' # str | 

try:
    api_instance.ai_mentor_orgs_webhooks_azure_trigger_create(org, slug)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_webhooks_azure_trigger_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 
 **slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_orgs_webhooks_github_pullrequest_create**
> ai_mentor_orgs_webhooks_github_pullrequest_create(org)



Handle incoming POST requests from GitHub webhook for pull requests.  Args:     request: The HTTP request object containing the webhook payload.     org: the organizaion name.  Returns:     Response: A response indicating the result of processing the webhook event.

### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)
org = 'org_example' # str | 

try:
    api_instance.ai_mentor_orgs_webhooks_github_pullrequest_create(org)
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_orgs_webhooks_github_pullrequest_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_mentor_webhooks_azure_emailchat_create**
> ai_mentor_webhooks_azure_emailchat_create()



### Example


```python
import iblai
from iblai.rest import ApiException
from pprint import pprint


# Create an instance of the API class
api_instance = iblai.AiMentorApi(api_client)

try:
    api_instance.ai_mentor_webhooks_azure_emailchat_create()
except Exception as e:
    print("Exception when calling AiMentorApi->ai_mentor_webhooks_azure_emailchat_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

