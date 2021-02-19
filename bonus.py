import data_scrapper
import data_intelligence
from my_errors import NoTokenException, NoMatchException

def main():
    # Entrez ici vos paramètres
    username = 'xxx@xxx.xx'
    password = 'xxxxxxxx'
    league = 'XXXXXXXX'
    # Nom de la team recherchée
    team = "xxx"

    # Liste des bonus pour une ligue de 10, à modifier si votre ligue a un nombre inférieur de participant
    bonus = [
        'Valise',
        'Zahia',
        'Suarez',
        'Suarez',
        'Uber Eats',
        'Uber Eats',
        'Uber Eats',
        'Miroir',
        'Chapron',
        'Pat Evra'
    ]

    try:
        # Récupération du token de connexion
        token = data_scrapper.get_token(username, password)

        # Test existance de la ligue et récupération des informations
        league_info = data_scrapper.get_league_info(token, league)

        # Journée en cours (dernière ou à venir)
        current_match_day = data_scrapper.get_calendar(token, league)['data']['results']['currentMatchDay']

        # Récupération de la saison en cours
        season = data_intelligence.get_last_season(token, league)

        print("----")
        print("Ligue " + league_info['leagueName'] + " | Saison "+str(season))
        print("----")

        # Vérification existance de l'équipe dans la ligue
        teams_list = []
        teams = data_scrapper.get_teamplayers(token, league)
        for i in range(0, int(league_info['players'])):
            teams_list.append(teams["teamsid"][i]['name'])
        data_intelligence.check_team(teams_list, team)

        # Listage des bonus utilisés
        results = []
        no_more_matches = False
        match_number = (int(league_info['players']/2))
        print(team + " a utilisé : ")
        for day in range(1, current_match_day+1):
            for match in range(1, match_number+1):
                try:
                    match = data_scrapper.get_match_summary(token, league, str(season)+"_"+str(day)+"_"+str(match))
                    result = data_intelligence.get_bonus_list(match, team)
                    if result != None :
                        if result != "" :
                            results.append(result)
                            print('Journée '+str(day)+' : 1 '+result)
                except NoMatchException:
                    no_more_matches = True
                    break
            if no_more_matches:
                break
        
        # Listage des bonus restants
        if results or results==[] :
            data_intelligence.get_bonus_list_left(bonus, results)
            print('\nIl reste à '+str(team)+' :')
            print('1 '+'\n1 '.join(bonus))
        else :
            print("\n"+str(team)+" n'a plus aucun bonus.")

    except NoTokenException as nte:
        print(nte.msg)

if __name__ == '__main__':
    main()
