import sqlite3
from student import Student
from cohort import Cohort
from exercise import Exercise
from instructor import Instructor


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/ajbyr/workspace/python/StudentExercises/studentexercises.db"

    

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            [print(s) for s in all_students]

    def all_cohorts(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Cohort(
                row[1]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT * 
            FROM Cohort c
            """)

            all_cohorts = db_cursor.fetchall()

            for c in all_cohorts:
                print(c.Name)

    def all_exercises(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercise(
               row[1], row[2] 
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT *
            FROM Exercise e
            """)

            all_exercises = db_cursor.fetchall()

            for e in all_exercises:
                print(f'Exercise: {e.name} Language: {e.language}')

    def javascript_exercises(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercise(
               row[0], row[1] 
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.exercise_name, e.exercise_language
            FROM Exercise e
            WHERE e.exercise_language = 'JavaScript'        
            """)

            all_exercises = db_cursor.fetchall()

            for e in all_exercises:
                print(f'{e.name} is an exercise in {e.language}')

    def python_exercises(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercise(
               row[0], row[1] 
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.exercise_name, e.exercise_language
            FROM Exercise e
            WHERE e.exercise_language = 'Python'        
            """)

            all_exercises = db_cursor.fetchall()

            for e in all_exercises:
                print(f'{e.name} is an exercise in {e.language}')

    def sql_exercises(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercise(
               row[0], row[1] 
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.exercise_name, e.exercise_language
            FROM Exercise e
            WHERE e.exercise_language = 'SQL'        
            """)

            all_exercises = db_cursor.fetchall()

            for e in all_exercises:
                print(f'{e.name} is an exercise in {e.language}')

    def all_instructors(self):

        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[5]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.first_name,
                i.last_name,
                i.slack_handle,
                i.CohortId,
                c.Name
            from Instructor i
            join Cohort c on i.CohortId = c.Id
            order by i.CohortId
            """)

            all_instructors = db_cursor.fetchall()

            [print(i) for i in all_instructors]


reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_exercises()
reports.javascript_exercises()
reports.python_exercises()
reports.sql_exercises()
reports.all_instructors()
