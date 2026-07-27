USE ROLE USERADMIN;

CREATE ROLE job_ads_dbt_role;

GRANT ROLE job_ads_dbt_role TO USER transformer;
GRANT ROLE job_ads_dbt_role TO USER ; -- Add your own user name here
