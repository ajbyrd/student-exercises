from exercise import Exercise 
from student import Student
from cohort import Cohort
# from instructor import Instructor

# Creating Exercises
chickenMonkey = Exercise("ChickenMonkey", "Python")
urbanPlanner = Exercise("Urban Planner", "Python")
kennel = Exercise("Kennel", "JavaScript")
welcomeToNashville = Exercise("Welcome to Nashville", "HTML")

# Creating Cohorts
cohort36 = Cohort("Day Cohort 36")
cohort37 = Cohort("Day Cohort 37")
cohort20 = Cohort("Evening Cohort 20")

# Creating Students

adam = Student("Adam", "Byrd", "ajbyrd", cohort36)
sophia = Student("Sophia", "Hoffman", "sophiahoffman", cohort36)
corri = Student("Corri", "Golden", "corrigolden", cohort37)
sully = Student("Sullivan", "Pierce", "sullypierce", cohort20)

