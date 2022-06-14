# Deployment Guide

This is a CLI tool (run.exe) targeting for Windows Platform to generate Checkmarx reports by using CxReporting Rest API.  

## Prerequisites

### Software 

* CxSAST
* CxReporting

CxSAST and CxReporting should be installed as prerequisites. You might need to install the CxReportingService authorization
setup again, e.g. rerun the PowerShell Script (cx-reporting-auth-setup.ps1) if you upgraded your CxSAST version.

### Least Permission Required for the CxSAST user

- Generate Application Report
- Generate Executive Report
- Generate Project Report
- Generate Scan Report
- Generate Team Report
- View Results

You can create a role named "SAST Reporting", and assign this role to a user, for example a user with name CxConsolidatedReport

### Team of the CxSAST user

The user should be in the root team "/CxServer". So it can have access to all the teams.

### Add Generic Credentials in Windows Credential Manager

#### Accessing Credential Manager
1. To open Credential Manager, type credential manager in the search box on the taskbar and select Credential Manager Control panel. 
2. Select Web Credentials or Windows Credentials to access the credentials you want to manage.

#### Create Generic Credential

Click the "Add a generic credential" link, to open the credential form

Internet or network address: 
User name:
Password: 

Please create 3 credentials with "Internet or network address" as checkmarx, CxReporting, SMTP. The CLI will get the password if an
environment variable "use_keyring" is defined.

### Environment Variable

Please set environment variable "use_keyring", for example "use_keyring = yes". The value of "use_keyring" can be anything you prefer. 
The CLI only check if such an environment variable exist or not.

### Configuration File

Please create a `config.json` file in a `.Checkmarx` folder in your home directory, for example C:\Users\<UserName>
Put the following content in the json file, and make modification as your need.
```json
{
  "checkmarx": {
    "base_url": "http://HappyY-Laptop",
    "username": "CxConsolidatedReport",
    "password": "****",
    "grant_type": "password",
    "scope": "sast_rest_api",
    "client_id": "resource_owner_client",
    "client_secret": "014DF517-39D1-4453-B7B3-9930C563627C"
  },
  "CxReporting": {
    "base_url": "http://HappyY-Laptop",
    "reporting_client_url": "http://HappyY-Laptop:5001",
    "username": "CxConsolidatedReport",
    "password": "****",
    "grant_type": "password",
    "scope": "reporting_api",
    "client_id": "reporting_service_api",
    "client_secret": "014DF517-39D1-4453-B7B3-9930C563627C"
  },
  "SMTP": {
    "smtp_server": "smtp.***.com",
    "port": 25,
    "send_from_address": "***",
    "send_from_display_name": "CxConsolidatedReportNoReply",
    "use_default_credentials": false,
    "username": "***",
    "password": "***",
    "use_tls": false
  },
  "CxConsolidatedReports": {
    "reports_folder": "",
    "report_rotation_days": 30,
    "log_level":  "info",
    "log_folder": "",
    "log_rotation_days": 30,
    "recursive_level": 3,
    "team_mapping": [
      {
        "team_full_name": "/CxServer",
        "search_team_recursive": true,
        "emails": [
          "someone@somedomain.com"
        ]
      },
      {
        "team_full_name": "/CxServer/SP/Company1",
        "search_team_recursive": false,
        "emails": [
          "someone@somedomain.com"
        ]
      }
    ]
  }
}
```

# Run the CLI as Windows Scheduled Task
Copy the CLI to any Windows Server that can reach to CxSAST and CxReporting.
Create a Windows scheduled task.