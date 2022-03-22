# configuration


```json
{
  "checkmarx": {
    "base_url": "http://HappyY-Laptop",
    "username": "CxConsolidatedReport",
    "password": "Password01!",
    "grant_type": "password",
    "scope": "sast_rest_api",
    "client_id": "resource_owner_client",
    "client_secret": "014DF517-39D1-4453-B7B3-9930C563627C"
  },
  "CxReporting": {
    "base_url": "http://HappyY-Laptop",
    "reporting_client_url": "http://HappyY-Laptop:5001",
    "username": "CxConsolidatedReport",
    "password": "Password01!",
    "grant_type": "password",
    "scope": "reporting_api",
    "client_id": "reporting_service_api",
    "client_secret": "014DF517-39D1-4453-B7B3-9930C563627C"
  },
  "SMTP": {
    "smtp_server": "smtp.163.com",
    "port": 25,
    "send_from_address": "yang2149@163.com",
    "send_from_display_name": "CxConsolidatedReportNoReply",
    "use_default_credentials": false,
    "username": "yang2149@163.com",
    "password": "**"
  },
  "CxConsolidatedReports": {
    "reports_folder": "",
    "report_rotation_days": 30,
    "log_folder": "",
    "log_rotation_days": 30,
    "recursive_level": 3,
    "team_mapping": [
      {
        "team_full_name": "/CxServer/SP",
        "search_team_recursive": true,
        "emails": [
          "happy.yang@checkmarx.com",
          "james.bostock@checkmarx.com"
        ]
      }
    ]
  }
}
```