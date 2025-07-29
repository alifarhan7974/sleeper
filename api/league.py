from api.utils import get, build_url
from api.path_constants import BASE_URL, MATCHUPS, ROSTERS, TRADED_PICKS, USERS, VERSION, LEAGUE



class League: 

    def __init__(self, league_id: int): 
        self.league_id = league_id

    def __str__(self): 
        return f"League id: {self.league_id}"

    def get_league(self) -> dict: 
        """Makes an get request to 
        https://api.sleeper.app/v1/league/<league_id>"""

        full_url = build_url(BASE_URL, VERSION, LEAGUE, self.league_id)
        return get(full_url)


    def get_league_rosters(self) -> dict: 
        """Makes an get request to 
        https://api.sleeper.app/v1/league/<league_id>/rosters"""

        full_url = build_url(BASE_URL, VERSION, LEAGUE, self.league_id, ROSTERS)
        return get(full_url)

    def get_league_users(self) -> dict: 
        """Makes an get request to 
        https://api.sleeper.app/v1/league/<league_id>/users"""

        full_url = build_url(BASE_URL, VERSION, LEAGUE, self.league_id, USERS)
        return get(full_url)

    def get_league_matchups(self, week: int) -> dict: 
        """Makes an get request to 
        https://api.sleeper.app/v1/league/<league_id>/matchups/<week>"""

        full_url = build_url(BASE_URL, VERSION, LEAGUE, self.league_id, MATCHUPS, USERS, week)
        return get(full_url)
    

    def get_traded_picks(self) -> dict: 
        """Makes a get request to 
        https://api.sleeper.app/v1/league/<league_id>/traded_picks"""

        full_url = build_url(BASE_URL, VERSION, LEAGUE, self.league_id, TRADED_PICKS)
        return get(full_url)