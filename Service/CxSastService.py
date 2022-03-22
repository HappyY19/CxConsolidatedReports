from CheckmarxPythonSDK.CxRestAPISDK import TeamAPI

all_teams = TeamAPI().get_all_teams()


def get_team_by_full_name(team_full_name):
    """

    Args:
        team_full_name (str):

    Returns:
        CxTeam
    """
    if not isinstance(team_full_name, str):
        raise ValueError("parameter team_full_name type should be str")

    team_list = [team for team in all_teams if team.full_name == team_full_name]
    if not team_list:
        return None
    return team_list[0]


def get_descendant_teams_by_parent_id(parent_id):
    """

    Args:
        parent_id (int):

    Returns:
        list[CxTeam]
    """
    if not isinstance(parent_id, int):
        raise ValueError("parameter parent_id type should be int")
    teams = [team for team in all_teams if team.parent_id == parent_id]
    for team in teams:
        teams.extend(get_descendant_teams_by_parent_id(parent_id=team.team_id))
    return teams


def get_team_with_descendants(team_full_name):
    """

    Args:
        team_full_name (str):

    Returns:
        list[CxTeam]
    """

    team = get_team_by_full_name(team_full_name)
    if not team:
        return []

    child_teams = get_descendant_teams_by_parent_id(parent_id=team.team_id)
    child_teams.append(team)
    return child_teams
