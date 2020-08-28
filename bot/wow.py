import os
import aiohttp

from dotenv import load_dotenv
load_dotenv()
WOW_ID =  os.getenv("WOW_CLIENT_ID")
WOW_SECRET = os.getenv("WOW_CLIENT_SECRET")

# Fetch OAuth Token
async def get_oauth_token():
    auth_path = "https://eu.battle.net/oauth/token"

    auth = aiohttp.BasicAuth(
        login = WOW_ID,
        password = WOW_SECRET
    )

    try:
        async with aiohttp.ClientSession(auth=auth) as client:
            async with client.get(
                auth_path, params={"grant_type": "client_credentials"}
            ) as auth_response:
                assert auth_response.status == 200
                json = await auth_response.json()
                return json["access_token"]

    except Exception:
        return "error_auth"

# Fetch character data from WoW API
async def get_data(auth_token, name):
    base_api_path = "https://eu.api.blizzard.com"
    
    try:
        async with aiohttp.ClientSession() as client:
            api_path = ( "%s/profile/wow/character/silvermoon/%s?namespace=profile-eu&locale=en_GB&access_token=%s" 
                        % (base_api_path, name, auth_token) )
            
            #print(api_path, flush = True)
            
            async with client.get(
                api_path
            ) as api_response:
                print(api_response, flush = True)
                if api_response.status == 200:
                    
                    api_json = await api_response.json()
                    return api_json
                
                elif api_response.status == 404:
                    print("Character is not found")
                    return "not_found"

    except Exception as error:
        print(error)
        print("Error: Connection error when retrieving game data.")
        return "connection_error"

# Get character info 
async def get_character_info(name):
    auth_token = await get_oauth_token()

    info = await get_data(auth_token, name)

    if info == "not_found":
        return info

    else:
        character_sheet = {
            "name": info["name"],
            "level": info["level"],
            "class": info["character_class"]["id"],
            "spec": info["active_spec"]["name"],
            "ilvl": info["equipped_item_level"]
        }

    
    return character_sheet