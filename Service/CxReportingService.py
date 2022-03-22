import os
from datetime import datetime
from os.path import normpath, join, dirname, exists

from CheckmarxPythonSDK.CxReporting.dto import CreateReportDTO, FilterDTO
from CheckmarxPythonSDK.CxReporting.api import get_report


def create_report_and_get_report_file_path(template_id, entity_id, report_name, output_format="PDF", report_folder=None):

    report_request = CreateReportDTO(
        template_id=template_id,
        output_format=output_format,
        entity_id=entity_id,
        report_name=report_name,
    )
    report_content = get_report(report_request=report_request)
    if not report_content:
        return ""

    if not report_folder or not exists(report_folder):
        report_folder = os.getcwd()
    file_name = normpath(join(report_folder, report_name + "." + output_format))
    with open(str(file_name), "wb") as f_out:
        f_out.write(report_content)
    return file_name


def get_single_team_report_file_path(team_full_name, report_name, output_format="PDF", report_folder=None):
    """
    Args:
        team_full_name (str):
        report_name (str):
        output_format (str):
        report_folder (str, optional):

    Returns:
        file_path (str)
    """

    return create_report_and_get_report_file_path(
        template_id=4,
        entity_id=[team_full_name],
        report_name=report_name,
        output_format=output_format,
        report_folder=report_folder,
    )


def get_multiple_team_report_file_path(team_full_name_list, report_name, output_format="PDF", report_folder=None):
    """
    Args:
        team_full_name_list (list[str]):
        report_name (str):
        output_format (str):
        report_folder (str, optional):

    Returns:
        file_path (str)
    """

    return create_report_and_get_report_file_path(
        template_id=5,
        entity_id=team_full_name_list,
        report_name=report_name,
        output_format=output_format,
        report_folder=report_folder,
    )
