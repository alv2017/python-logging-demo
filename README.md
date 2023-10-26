# Python Logging Demo

Logging provides insights into what the system is doing. Without proper logging we have
no idea why our application fails, and we have no clue how to fix the problem.

This project demonstrates useful Python logging principles.

## Simple File Logger

The simple file logger captures log message of the predefined level, and stores the to the log file.

Demo script: *ex01_simple_file_logger.py*

## Rotating Logs

If you are developing a long-running 24/7 service, it might be a good idea to split the log into smaller pieces.

Rotating log strategy says that when a log file reaches a certain size, it must be rotated (i.e the old log file 
is backed up and a brand-new log file is created.)

Demo script: *ex02_rotating_logs.py*

## Time Rotating Logs

It is also possible to rotate logs on time basis, in this case the logs will be rotated at pre-defined time
frequency.

Demo scripts: *ex03_time_rotating_logs.py*

## Importance of Appropriate Log Levels

When it comes to logging of distinct events in our application, not everything will carry the same weight in
terms of importance. We might be willing to handle fatal errors separately. This can be achieved by using
different log handlers.

Demo script: *ex04_log_levels.py*