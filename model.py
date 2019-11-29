import sqlite3
import datetime


"""
Databse model for storing game highscores
"""

class HighScore:
	def __init__(self, name="game.db"):
		self.name = name

		self.connection = sqlite3.connect(self.name)
		self.cursor = self.connection.cursor()


		try:
			self.cursor.execute(
				"""
					CREATE TABLE HIGHSCORE (SCORE INTEGER NOT NULL, DATEOF DATE NOT NULL, USER TEXT NOT NULL)
				"""
			)

		except sqlite3.OperationalError:
			pass

		finally:
			self.connection.commit()
			if self.connection:
				self.connection.close()

	def add_highscore(self, user, score, date=datetime.datetime.today().date()):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()

			self.cursor.execute(
				"""
					INSERT INTO HIGHSCORE (SCORE, DATEOF, USER) VALUES (?, ?, ?)
				""",
			(score, date, user))

		except sqlite3.OperationalError as e:
			return e

		else:
			self.connection.commit()
			return True

		finally:
			if self.connection:
				self.connection.close()

	def retrieve_highscores(self):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()
			scores = []

			self.cursor.execute(
				"""
					SELECT * FROM HIGHSCORE ORDER BY SCORE DESC
				"""
			)

		except sqlite3.OperationalError as e:
			return e

		else:
			for _ in self.cursor.fetchall():
				scores.append(_)
			return scores

		finally:
			if self.connection:
				self.connection.close()

	def retrieve_max_highscore(self):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()
			scores = []

			self.cursor.execute(
				"""
					SELECT COUNT(*) FROM HIGHSCORE
				"""
			)

		except sqlite3.OperationalError as e:
			return e

		else:
			for _ in self.cursor.fetchall():
				scores.append(_)
			return max(scores)

		finally:
			if self.connection:
				self.connection.close()

	def trim_scores(self):
		try:
			self.connection = sqlite3.connect(self.name)
			self.cursor = self.connection.cursor()
			scores = []

			self.cursor.execute(
				"""
					SELECT COUNT(*) FROM HIGHSCORE
				"""
			)

			if self.cursor.fetchone()[0] >= 10:
				self.cursor.execute(
					"""
						SELECT * FROM HIGHSCORE ORDER BY SCORE ASC
					"""
				)

				for _ in self.cursor.fetchall():
					scores.append(_)
				scores = scores[0:10]
				print(scores)

				self.cursor.execute(
					"""
						DELETE FROM HIGHSCORE
					"""
				)


				for _ in scores:
					# self.add_highscore(scores[2], scores[1], scores[1])
					# add_highscore(self, user, score, date)
					self.cursor.execute(
						"""
							INSERT INTO HIGHSCORE (SCORE, DATEOF, USER) VALUES (?, ?, ?)
						""",
					(_[2], _[0], _[1]))

			return True



		except sqlite3.OperationalError as e:
			return e

		finally:
			self.connection.commit()
			if self.connection:
				self.connection.close()


a = HighScore()
#print(a.add_highscore(123,"LOL"))
print(a.trim_scores())
