import os

import psycopg2 as pg
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2.extras

class Database:
    async def connect(self, user, password, host, port, db):
        #print(user, flush = True)
        try:
            self.connection = pg.connect(user = user,
                                        password = password,
                                        host = host,
                                        port = port,
                                        dbname = db)
        except Exception as e:
            print("Error connecting to database.", flush = True)
            print(e, flush = True)
            raise e
        
        print("Connected to database fine.", flush = True)
    

    # Dict = True (Use Dictionary cursor)
    async def set_cursor(self, dict):
        if dict == True:
            self.cursor = self.connection.cursor(cursor_factory=pg.extras.DictCursor)
        else:
            self.cursor = self.connection.cursor()

    # Add discord user
    async def add_user(self, discord):
        print("Adding user", flush = True)
        
        # Check if discord user id exists
        result = await self.user_exists(discord)

        if result == True:
            return True
        else:
            try:
                self.cursor.execute("INSERT INTO users (discord_id) VALUES (%s)", [discord,])

            except Exception as e:
                print(e, flush = True)
                self.connection.rollback()

    # Retrieve user
    async def user_exists(self, discord):
        try:
            self.cursor.execute("SELECT discord_id FROM users WHERE discord_id = %s", [discord])
            result = self.cursor.fetchone()
            
            if result == None:
                return False
            else:
                return True

        except Exception as e:
            print(e, flush = True)
            self.connection.rollback()
    
    # Add character
    async def add_character(self, discord, character):
        print(discord, flush = True)
        print(character, flush = True)

        await self.add_user(discord)

        # Check if user already has a main character
        try:
            self.cursor.execute("SELECT main FROM user_characters WHERE main = %s", [True])
            result = self.cursor.fetchone()

            # if None add as temporary character which is main (true), else as an alt (false)
            if result == None:
                main_char = True
            else:
                main_char = False

            self.cursor.execute("INSERT INTO user_characters (discord_id, character_name, main, temporary) VALUES (%s, %s, %s, %s)", [discord, character["name"], main_char, True])

        except Exception as e:
            print(e, flush = True)
            self.connection.rollback()

    # Clean up resources
    async def exit(self):
        try:
            self.cursor.close()
        except:
            print("No cursor attribute", flush = True)
        self.connection.commit()
        self.connection.close()