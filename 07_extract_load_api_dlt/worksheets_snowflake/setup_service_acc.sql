-- ref: https://docs.coalesce.io/docs/setup-your-project/connection-guides/snowflake/snowflake-service-accounts


-- Use a role with sufficient privileges to create roles and users (e.g., USERADMIN or SECURITYADMIN)
USE ROLE ACCOUNTADMIN; 


-- Create the dbt role
CREATE ROLE IF NOT EXISTS JOB_ADS_DBT_ROLE;


-- Create the dlt service user with the public key
-- Replace '<YOUR_PUBLIC_KEY_STRING_HERE>' with the actual public key from rsa_key.pub (without headers/footers)
CREATE USER IF NOT EXISTS extract_loader
TYPE = SERVICE
RSA_PUBLIC_KEY = '<YOUR_PUBLIC_KEY_STRING_HERE>' 
DEFAULT_ROLE = JOB_ADS_DBT_ROLE
DEFAULT_WAREHOUSE = DEV_WH
COMMENT = "Service user for dlt pipeline";
-- check user config
DESC USER extract_loader;


-- Grant dlt role to the dlt service user
GRANT ROLE JOB_ADS_DLT_ROLE TO USER extract_loader;
GRANT ROLE JOB_ADS_DLT_ROLE TO USER ;


-- Grant the dlt role to the SYSADMIN role (or another administrative role) 
-- This allows administrators to manage and troubleshoot the role setup.
GRANT ROLE JOB_ADS_DLT_ROLE TO ROLE SYSADMIN;


-- grant privileges to role
GRANT USAGE ON WAREHOUSE dev_wh TO ROLE job_ads_dlt_role;
GRANT USAGE ON DATABASE job_ads TO ROLE job_ads_dlt_role;
GRANT USAGE ON SCHEMA job_ads.staging TO ROLE job_ads_dlt_role;
GRANT CREATE TABLE ON SCHEMA job_ads.staging TO ROLE job_ads_dlt_role;

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA job_ads.staging TO ROLE job_ads_dlt_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON FUTURE TABLES IN SCHEMA job_ads.staging TO ROLE job_ads_dlt_role;