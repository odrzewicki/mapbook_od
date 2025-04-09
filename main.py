users:list=[
            {"name":"Oliwier","location":"Zamość","posts":2},
            {"name":"Kuba","location":"Zamość","posts":3},
            {"name":"Konrad","location":"Zamość","posts":500},
            {"name":"Johny","location":"Zamość","posts":10},
]



def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f"Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów.")

get_user_info(users)