-- NOTE: you should .gitignore this file as it contains credentials
USE ROLE useradmin;
CREATE USER IF NOT EXISTS reporter
    TYPE = SERVICE
    DEFAULT_WAREHOUSE = dev_wh
    DEFAULT_ROLE = job_ads_reporter_role
    RSA_PUBLIC_KEY = '<YOUR_PUBLIC_KEY_STRING_HERE>' 
    COMMENT = "Service user for streamlit";

