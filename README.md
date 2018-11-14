# timeDelete
## Purpose
Monitors a folder and deletes files that are older than a specified time.

## Background
I have a instance at work where a program creates files and saves them in a temp directory every time a 
website is accessed. The information can be re-generated quickly and easily but the data needs to be stored for 
a specified amount of time. Obviously, if left unchecked, the directory would eventually become massive and the disk 
would fill up from generated reports. I also realize that this directory could be cleared out by a daily cron job. 
However, I thought it would be a better solution to only delete old files instead of just blindly deleting 
everything in the directory. A cron job would also present problems if a report is generated near midnight (or 
whatever set time the cron job runs) and deletes the file before it could be downloaded. 

Hardcoded vairables for time before deletion and directory to monitor could be used if it was only for this 
single application but since I am making this public, I will be adding optional arguments to the program.

