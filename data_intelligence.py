import data_scrapper
from functools import reduce
from my_errors import NoTeamException


def get_bonus_list(match, team):
    bonus_list = ""
    team_researched = team
    team_home = match['data']['teamHome']['name']
    team_away = match['data']['teamAway']['name']

    bonus = match['data']['bonus']

    if team_home == team_researched or team_away == team_researched :
        if not bonus:
            return None
        else:
            try:
                if team_home == team_researched :
                    bonus_home = bonus["home"]
                    bonus_list += get_bonus(bonus_home)
                if team_away == team_researched :
                    bonus_away = bonus["away"]
                    bonus_list += get_bonus(bonus_away)
            except KeyError:
                pass
        return bonus_list


def get_bonus_list_left(bonus, results):
    n = len(bonus)
    for i in range(n - 1, -1, -1):
        if bonus[i] in results:
            results.remove(bonus[i])
            del bonus[i]


def get_bonus(json):
    bonuses = {
        1: 'Valise',
        2: 'Zahia',
        3: 'Suarez',
        4: 'Uber Eats',
        5: 'Miroir',
        6: 'Chapron',
        7: 'Pat Evra'
    }
    return bonuses[json['type']]


def get_last_season(token, league):
    palmares = data_scrapper.get_palmares(token, league)
    if not palmares:
        return 1
    else:
        return max(palmares['winners'], key=lambda item: item['season'])['season'] + 1


def get_teams_list(match):
    teams_list = []
    team_home = match['data']['teamHome']['name']
    teams_list.append(team_home)
    team_away = match['data']['teamAway']['name']
    teams_list.append(team_away)
    return teams_list


def check_team(teams, team):
    list_teams = reduce(lambda x,y: x+y, teams)
    try:
        if team not in list_teams:
            raise NoTeamException('The team '+team+' is not present in the league')
    except NoTeamException as nte:
        exit(nte.msg)