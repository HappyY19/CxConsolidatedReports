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


def get_child_teams_by_parent_team(parent_teams):
    """

    Args:
        parent_teams (list[CxTeam]):

    Returns:
        list[CxTeam]
    """
    parent_team_list = parent_teams.copy()

    def get_descendants():
        nonlocal parent_team_list
        descendant_teams = []
        for team in all_teams:
            for member in parent_team_list:
                if team.parent_id == member.team_id:
                    descendant_teams.append(team)
        parent_team_list = descendant_teams
        return descendant_teams

    return get_descendants


def get_team_with_descendants(team_full_name, recursive_level=3):
    """

    Args:
        team_full_name (str):
        recursive_level (int):

    Returns:
        list[CxTeam]
    """

    team = get_team_by_full_name(team_full_name)
    if not team:
        return []

    teams = [team]

    get_child_teams_func = get_child_teams_by_parent_team(teams)
    while recursive_level > 1:
        teams.extend(get_child_teams_func())
        recursive_level -= 1

    return teams
