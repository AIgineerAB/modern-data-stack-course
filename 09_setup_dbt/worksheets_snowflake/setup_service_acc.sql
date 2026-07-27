-- NOTE: you should .gitignore this file as it contains credentials

USE ROLE useradmin;

CREATE USER IF NOT EXISTS transformer
    TYPE = SERVICE
    RSA_PUBLIC_KEY = '<YOUR_PUBLIC_KEY_STRING_HERE>'     
    DEFAULT_ROLE = JOB_ADS_DBT_ROLE
    DEFAULT_WAREHOUSE = DEV_WH
    COMMENT = "Service user for dbt pipeline";


