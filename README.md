# Description

This robot demonstrates three different ways to run the [metarobot](https://github.com/vjmp/metarobot/tree/trunk) bot using Robocorp's cloud orchestration while maintaining all code, logs, etc. in your local environment.

# Prerequisets

1. You will need to have an account of [Robocorp's Control Room](https://cloud.robocorp.com) so that you can upload and run this bot from the cloud.
1. You will need to have downloaded the [metarobot](https://github.com/vjmp/metarobot/tree/trunk) and followed the instructions in that `Readme` before running this bot.
1. A worker on your test/local system installed via [Setup Utility](https://robocorp.com/docs/control-room/setup-utility)
   **NOTE:** If you are using Windows you can setup either a `Windows Worker` or `Demo worker` while testing. If you are on MacOS then you will need to setup a `Demo Worker`.
1.

# Installation steps

1. Clone this repository
1. There are three instances of a hard coded path (lines 10, 19, and 26) that need to be replaced with the path to the [metarobot](https://github.com/vjmp/metarobot/tree/trunk) that you installed in the prerequisets section.
1. Once you have updated the paths you can 1) Publish this bot to your Git repository of choice and then link that repository to Control Room to create a Task 2) Upload the bot directly to Control Room via VS Code.

# Why is this bot necessary

A robot like this is necessary for many highly regulated organizations and as organizations of all sizes become more security / privacy focused. This bot can be useful to you because of the type of organization that you work in, for risk controls, and finally because masking the logs causes redundant work for your developers.

Examples include:

- Organization Type:
  - you work in the healthcare space and you are automating the input of sensitive client infomation into a secure web portal and want to ensure that you are not violating any laws if a developer fails to properly leave data out of the logs
  - you are in the banking sector and are automating the filing of your AML reports and are concerned that a server may be in another country
- Risk Controls:
  - your company / team has high developer turn over the skill level of the team is primarily junior developers
  - you are in the banking sector and are automating the filing of your AML reports and are concerned that the details of that report may not be masked properly by the developer
- Redundant Work:
  - you work with sensitive data and the masking of that data or removal of that infomation from the logs would make it difficult or impossible to troubleshoot / resolve issues in bot runs
  - if you are masking logs before they are pushed to cloud but are also writing your own log so that you can ingest it into an internal system like Splunk

The best part is that while keeping your data "in house" you are still getting the power of Robocorp's cloud orchestration as well as the ability to rerun failed work items!

**NOTE:** I acknowledge that there are more effecient ways to implement this bot, such as creating a global variable for the path instead of hard coding it three times. Before taking this into production please consider reviewing it to be inline with best practices.
