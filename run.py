"""
This is a tool to send emails with Checkmarx consolidated PDF reports
Author: happy.yang@checkmarx.com
Date: 2022-03-19

read from configuration file to get the information
get team report by using CxReporting service api
send email with the team report
"""
import logging
from datetime import datetime
from CheckmarxPythonSDK.configUtility import get_config, get_config_info_from_config_json_file
from Service.CxReportingService import (
    get_multiple_team_report_file_path,
    get_single_team_report_file_path,
)
from Service.SmtpService import send_mail
from Service.CxSastService import (get_team_by_full_name, get_team_with_descendants)
from Service.LoggingService import set_logger

cx_consolidated_report_config = get_config_info_from_config_json_file(
        section="CxConsolidatedReports",
        option_list=[
            "reports_folder", "report_rotation_days", "log_level", "log_folder", "log_rotation_days",
            "recursive_level", "team_mapping"
        ]
    )

set_logger(
    level=logging.DEBUG,
    log_folder=cx_consolidated_report_config.get("log_folder"),
    when="M",
    backup_count=cx_consolidated_report_config.get("log_rotation_days")
)

logger = logging.getLogger("CxConsolidatedReports")


if __name__ == '__main__':

    CxReporting = {
        "base_url": "***",
        "reporting_client_url": "***",
        "username": "***",
        "password": "***",
        "grant_type": "password",
        "scope": "reporting_api",
        "client_id": "reporting_service_api",
        "client_secret": "014DF517-39D1-4453-B7B3-9930C563627C"
    }

    SMTP = {
        "smtp_server": "***",
        "port": 25,
        "send_from_address": "***",
        "send_from_display_name": "CxConsolidatedReportNoReply",
        "use_default_credentials": False,
        "username": "***",
        "password": "***",
        "use_tls": False
    }

    cx_reporting_config = get_config(config_default=CxReporting, section="CxReporting", prefix="cxreporting_")
    smtp_config = get_config(config_default=SMTP, section="SMTP", prefix="smtp_")

    team_mapping_list = cx_consolidated_report_config.get("team_mapping")
    logger.info("Finished get config data")
    for team_mapping in team_mapping_list:
        team_full_name = team_mapping.get("team_full_name")
        search_team_recursive = team_mapping.get("search_team_recursive")
        email_list = team_mapping.get("emails")
        logger.info("team full name: {}, search_team_recursive: {}".format(team_full_name, search_team_recursive))
        team = get_team_by_full_name(team_full_name)
        if not team:
            logger.info("team with team_full_name: {} not found, skip this team".format(team_full_name))
            continue
        team_name = team_full_name.split("/")[-1]
        output_format = "PDF"
        report_name = team_name + datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')

        if not search_team_recursive:
            file_path = get_single_team_report_file_path(
                team_full_name=team_full_name,
                report_name=report_name,
                output_format=output_format,
                report_folder=cx_consolidated_report_config.get("reports_folder"),
            )
        else:
            team_with_descendants = get_team_with_descendants(
                team_full_name, recursive_level=cx_consolidated_report_config.get("recursive_level")
            )
            team_full_name_list = [team.full_name for team in team_with_descendants]
            file_path = get_multiple_team_report_file_path(
                team_full_name_list=team_full_name_list,
                report_name=report_name,
                output_format=output_format,
                report_folder=cx_consolidated_report_config.get("reports_folder"),
            )
        if file_path:
            send_mail(
                send_from=smtp_config.get("send_from_address"),
                send_to=email_list,
                subject=cx_consolidated_report_config.get("subject", "CxSAST Consolidated Report"),
                message=cx_consolidated_report_config.get("message",
                                                          "Please find attached the consolidated CxSAST report."),
                files=[file_path],
                server=smtp_config.get("smtp_server"),
                port=smtp_config.get("port"),
                username=smtp_config.get("username"),
                password=smtp_config.get("password"),
                use_tls=smtp_config.get("use_tls", True),
            )
