USE ROLE job_ads_dlt_role;
USE DATABASE job_ads;

SHOW SCHEMAS;

SHOW TABLES IN SCHEMA staging;

DESC TABLE staging.data_field_job_ads;

USE WAREHOUSE dev_wh;

SELECT
    COUNT(*) -- compare with the total value via browser
FROM staging.data_field_job_ads;

SELECT * FROM staging.data_field_job_ads;
SELECT headline,
       employer__name,
       workplace_address__municipality
FROM staging.data_field_job_ads;
