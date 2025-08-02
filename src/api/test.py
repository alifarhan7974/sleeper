from api.league import League

def generate_user_map(league_id) -> dict: 
    Mhs = League(league_id)
    #Json response is a list of dicts each one abt each user 
    users = Mhs.get_league_users()
    return {u["display_name"] : u["user_id"] for u in users} 

def main(): 
    Mhs_grad_id = 1226686814018879488
    #draft_id = 1226686815126163456
    #user_map = generate_user_map(Mhs_grad_id)

    Mhs = League(Mhs_grad_id)
    rosters = Mhs.get_league_rosters()
    print(rosters)
    

if __name__ == "__main__": 
    main() 