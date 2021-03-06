BEGIN;
TRUNCATE "oauth2_provider_refreshtoken", "auth_permission", "auth_group", "miller_document", "auth_user_user_permissions", "social_auth_nonce", "django_site", "miller_caption", "django_content_type", "miller_mention", "django_session", "auth_user_groups", "miller_story_tags", "miller_comment", "captcha_captchastore", "miller_profile", "django_admin_log", "auth_group_permissions", "miller_review", "oauth2_provider_accesstoken", "actstream_action", "miller_story_authors", "auth_user", "oauth2_provider_application", "social_auth_usersocialauth", "actstream_follow", "templated_email_savedemail", "miller_story", "miller_story_covers", "social_auth_association", "social_auth_code", "miller_page", "miller_author", "miller_tag", "oauth2_provider_grant";
SELECT setval(pg_get_serial_sequence('"django_admin_log"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"auth_permission"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"auth_group"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"auth_user"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"django_content_type"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"django_site"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"social_auth_usersocialauth"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"social_auth_nonce"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"social_auth_association"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"social_auth_code"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"oauth2_provider_application"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"oauth2_provider_grant"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"oauth2_provider_accesstoken"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"oauth2_provider_refreshtoken"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"templated_email_savedemail"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"captcha_captchastore"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"miller_profile"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"miller_tag"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"miller_document"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"miller_author"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"miller_story"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"miller_caption"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"miller_mention"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"miller_comment"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"miller_review"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"miller_page"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"actstream_follow"','id'), 1, false);
SELECT setval(pg_get_serial_sequence('"actstream_action"','id'), 1, false);
COMMIT;
