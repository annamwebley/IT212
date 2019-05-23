# Project 4b
# Anna Markiewicz
# May 25
# onlinestudent.py

from student import Student

class OnlineStudent(Student):
    def __init__(self, _id, username, last_name, first_name, phone, year, email):
        super().__init__(_id, username, last_name, first_name, phone, year)
        self.email = email
        self.study_group = []

    # def __str__(self):
    #     pass

    # def __repr__(self):
    #     pass

    def __lt__(self, other):
        return self.username < other.name

    def add_group_member(self, username):
        self.study_group.append(username)




if __name__ == "__main__":

    online_student1 = OnlineStudent(
        _id = 1111,
        username = "CarterMarilyn",
        last_name = "Carter",
        first_name = "Marilyn",
        phone =  "312/473-4837",
        year = 1,
        email = "cartermarilyn@mail.depaul.edu"
        )

    online_student1.add_group_member("Katemosfgui")   
    online_student1.add_group_member("fungi") 
    print(online_student1.study_group)
    