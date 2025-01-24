import sqlite3
import json

class GamePersistence:

  def __init__(self, dbName="game.db"):
    # Initialize the database connection and cursor
    self.db = sqlite3.connect(dbName)
    self.cursor = self.db.cursor()

    # Check if the 'game_saves' table exists, if not, create it
    res = self.cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='game_saves'"
    )
    if res.fetchone() is None:
      self.initSchema('game_saves')

    # Check if the 'text_saves' table exists, if not, create it
    res = self.cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='text_saves'"
    )
    if res.fetchone() is None:
      self.initSchema('text_saves')

  def initSchema(self, name):
    # Create a table with the given name and columns for id, name, data, and date_created
    self.cursor.execute(
        f"CREATE TABLE {name}(id INTEGER PRIMARY KEY, name TEXT NOT NULL, data TEXT, date_created TEXT NOT NULL)"
    )
    # Other tables like rooms, items, can be initialized here

  def saveGame(self, name, game_data):
    # Insert a new game save into the 'game_saves' table
    self.cursor.execute(
        "INSERT INTO game_saves(name, data, date_created) VALUES(?, ?, datetime('now'))",
        (name, json.dumps(game_data, default=vars)))
    self.db.commit()

  def loadGame(self, save_name):
    # Load a game save from the 'game_saves' table by name
    self.cursor.execute("SELECT data FROM game_saves WHERE name=?",
                        (save_name, ))
    data = self.cursor.fetchone()
    if data is None:
      return None
    return json.loads(data[0])
  
  def saveData(self, name, data, table_name):
    # Insert data into the specified table
    self.cursor.execute(
        f"INSERT INTO {table_name}(name, data, date_created) VALUES(?, ?, datetime('now'))",
        (name, json.dumps(data, default=vars)))
    self.db.commit()

  def loadData(self, save_name, table_name):
    # Load data from the specified table by name
    self.cursor.execute(f"SELECT data FROM {table_name} WHERE name=?",
                        (save_name, ))
    data = self.cursor.fetchone()
    if data is None:
      return None
    return json.loads(data[0])

  def deleteGame(self, id):
    # Delete a game save from the 'game_saves' table by id
    self.cursor.execute("DELETE FROM game_saves WHERE id=?", (id, ))
    self.db.commit()

  def getGameIds(self):
    # Get all game save ids and names from the 'game_saves' table
    self.cursor.execute("SELECT id, name FROM game_saves")
    return [(row[0], row[1]) for row in self.cursor.fetchall()]
