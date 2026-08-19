# Setup

Video on snowflake and snowsql setup [TO BE UPDATED] :point_down:

[![setup snowflake](https://github.com/kokchun/assets/blob/main/data_warehouse/setup_snowflake_video.png?raw=true)](https://www.youtube.com/watch?v=i454nHjdMAc)

This setup requires that you have the following prerequisites already setup

- visual studio code
- git
- git bash (for windows)
- github account

If you don't know how to work with git, and github, follow this [tutorial series](https://www.youtube.com/watch?v=3RjQznt-8kE&list=PL4cUxeGkcC9goXbgTDQ0n_4TBzOO0ocPR). 

## 1. Snowflake account

Now we will create a [snowflake free trial account](https://signup.snowflake.com/), which can be used for 30 days, with $400 credits. After the 30 days, you can use the same email to create a new free trial account. You just need to create again necessary users, roles, databases, etc., for your pipelines. 

> [!NOTE]
> Pick enterprise version, Microsoft Azure and West Europe (Netherlands).

<img width = "400" src="https://github.com/kokchun/assets/blob/main/data_warehouse/snowflake_free_trial.png?raw=true"/>


> [!NOTE]
> It is recommended to set up MFA for all *human* accounts. With MFA, there will be some additional steps in logging into SnowSQL though. 


## 2. Snowflake extension

Now install snowflake extension on vscode by searching for Snowflake on vscode extensions marketplace. After installation, you can click on the Snowflake icon on vscode to connect to your snowflake account. You will be asked to provide:

### accountname
`accountname` is composed of `Account Locator`. `Region` and `Cloud Platform` of your Snowflake account. If you follows our steps above, `Region` is *west-europe* and `Cloud platform` is *azure*. 

To find your `Account Locator`:
- log into your account on Snowflake web interface
- open the account selector on the left bottom corner
- click on *View account details* to find your `Account Locator`

### username and password
Use the username and password to fill in when setting up your account. You can also find the user name in the homepage of your Snowflake account: go into `Governance and Security` and then `users & roles` to find your user.


## 3. Create a github repository

Now we will create a github repository online, then clone it, so that you can work with it locally. Name your github repository as follows and make it public

```
data_warehouse_<first_name>_<last_name>_<class>
```

> [!IMPORTANT]
> Add the python .gitignore to your repository in order to not track certain files in version control.

Clone the repository to a local directory of your choice, e.g. `documents/github`.

Now create the following directories to organize your files: 

- exercises 
- code-alongs
- explorations


## 4. Test connection

Navigate to your repository and create a file called `test_snowsql.sql` and add a few statements 

```sql
SHOW databases;

USE SCHEMA snowflake_sample_data.tpch_sf1;

SHOW TABLES;

SELECT * FROM CUSTOMER;
```

> [!NOTE]
> You might need to change the language mode to snowflake SQL if it isn't set by default

> [!NOTE]
> Use ctrl+enter or cmd+enter to run each sql statements through snowflake.

## Other videos :video_camera:

- [How to use SnowSQL | Install, Config & Query - Kahan Data Solutions (2023)](https://www.youtube.com/watch?v=ogg9SLBRZ9A)


## Read more :eyeglasses:

- [install snowsql](https://docs.snowflake.com/en/user-guide/snowsql-install-config)  
- [configure snowsql](https://docs.snowflake.com/en/user-guide/snowsql-config)