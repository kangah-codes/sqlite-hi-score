__author__ = "Joshua Akangah"

import sqlite3
import datetime

class HighScoreModel:
    def __init__(self, name="game.db"):
        """
        init method
        params:
            name: name of the database
        return:
            None
        """
        self.name = name
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

        if self.connection:
            self.connection.close()

    def create_tables(self):
        """
        function to create database tables
        params:
            None
        return: True, sqlite3.OperationalError, Exception
        """
        try:
            self.connection = sqlite3.connect(self.name)
            self.cursor = self.connection.cursor()

            self.cursor.execute("CREATE TABLE GAME_DATA (SCORE INTEGER NOT NULL, DATEOF DATE NOT NULL) ")
            self.connection.commit()
            return True

        except sqlite3.OperationalError as e:
            return e

        finally:
            if self.connection:
                self.connection.close()

    def add_score(self, score, date=datetime.datetime.today().date()):
        """
        Add scores to the database, date is automatically filled in
        params:
            score: score to add
            date: date of adding the score
        return:
            True, sqlite3.OperationalError
        """
        try:
            self.connection = sqlite3.connect(self.name)
            self.cursor = self.connection.cursor()

            self.cursor.execute("INSERT INTO GAME_DATA (SCORE, DATEOF) VALUES (?, ?)", (score, date))
            self.connection.commit()
            return True

        except sqlite3.OperationalError as e:
            return e

        finally:
            if self.connection:
                self.connection.close()

    def get_scores(self):
        """
        returns a list of all scores in the database
        params:
            None
        return:
            list, sqlite3.OperationalError
        """
        try:
            self.connection = sqlite3.connect(self.name)
            self.cursor = self.connection.cursor()

            self.cursor.execute("SELECT * FROM GAME_DATA")
            return self.cursor.fetchall()

        except sqlite3.OperationalError as e:
            return e

        finally:
            if self.connection:
                self.connection.close()

    def get_max_score(self):
        """
        return the highest score in the database
        params:
            None
        return:
            list, sqlite3.OperationalError
        """
        try:
            self.connection = sqlite3.connect(self.name)
            self.cursor = self.connection.cursor()

            self.cursor.execute("SELECT * FROM GAME_DATA")
            return max(self.cursor.fetchall())

        except sqlite3.OperationalError as e:
            return e

        finally:
            if self.connection:
                self.connection.close()

    def delete_score(self, score):
        """
        delete a particular score from the database
        params:
            score: score to delete
        return:
            True, sqlite3.OperationalError, Exception
        """
        try:
            self.connection = sqlite3.connect(self.name)
            self.cursor = self.connection.cursor()

            self.cursor.execute("DELETE FROM GAME_DATA WHERE SCORE=?", (score,))
            self.connection.commit()
            return True

        except sqlite3.OperationalError as e:
            return e

        finally:
            if self.connection:
                self.connection.close()
