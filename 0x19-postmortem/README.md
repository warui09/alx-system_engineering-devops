# BeiPoa Incident Report

This is an incident report of the downtime experienced by BeiPoa users on Wednesday 17th January 2024. Some API endpoints were unresponsive and thus several services were unavailable, users got a 500 HTTP response. Here is a short list for the meaning of HTTP error codes that we hope you will find useful.

## Issue summary

From 11:36 PM to 01:48 AM East African time some requests to BeiPoa API endpoints got an error response with code 500 indicating an internal server error. 100% of write requests and 50% of read requests failed because the ORM library running on the server affected could not connect to the database, which is the source database. This was caused by an update to the ORM library that broke the configuration file. This being the source database server meant that all write requests could not be completed. The 50% of the successful read requests were completed by another server that was unaffected by the ORM update. In total 50% of all  users were affected.

## Timeline (all times East African time)

- 11:32 PM: ORM library updated 
- 11:36 PM: App cannot connect to database
- 11:36 PM: Pager alerts engineers to the problem
- 11:38 PM: On call engineer begins troubleshooting
- 00:13 AM: Engineer looks at load balancer logs
- 00:32 AM: Engineer tracks the problem to the web server
- 00:33 AM: Engineer goes through web server's log files
- 00:54 AM: Previous config files retrieved from backup
- 00:57 AM: Affected config files fixed
- 01:02 AM: Server restarted
- 01:48 AM: All services fully restored 

## Root cause

The ORM library that connects the back-end code to the database was updated at 11:32 PM East African time. This update changed the config file and the app couldn't connect with the database. This being the source database, it handles all write requests and 50% of the read requests. These are the requests that returned an error message with HTTP code 500.
Initially the problem was thought to be with the loadbalancer but examination of the log files showed this was not the case.
This update should have been carried out in the testing environment first and later pushed to production. This image captures the essence of the events that transpired.

## Resolution

The previous config file was retrieved from back up, a copy was made and the new configuration properties were added. A backup of the new file was then created and the server restarted.
This was first done in the testing environment and once the team was confident the problem was solved, the new config file was pushed to production.

## Corrective and Preventive measures

To prevent a repeat of this incident these are the preventive measures we have implemented:
New updates to made in the testing environment first before rollout to the production servers
Updates and other maintenance activities to be carried out during low traffic hours and users duly informed.
More rigorous process for testing high risk configuration options for all systems.
Improve rollback process to make it quicker and more robust.

We would like to thank our users for their patience while we worked to restore services. We remain committed to providing our users with excellent service.
