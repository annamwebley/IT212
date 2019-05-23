# Project 4a 
# Anna Markiewicz
# May 19
# student.py

class Student:
    def __init__(self, _id, username, last_name, first_name, phone, year):
        self._id = _id
        self.username = username
        self.last_name = last_name
        self.first_name = first_name
        self.phone = phone

        if year < 1:
            self.year = 1
        elif year > 4:
            self.year = 4
        elif 1 <= year <= 4:
            self.year = year

    def __str__(self):
        return f"Student('_id':{self._id}, 'username':{self.username}, 'last_name':{self.last_name}, 'first_name':{self.first_name}, 'phone':{self.phone}, 'year':{self.year})"
        
    def __repr__(self):
        return {
            '_id':self._id,
            'username':self.username,
            'last_name':self.last_name,
            'first_name':self.first_name,
            'phone':self.phone,
            'year':self.year
        }

    def update_year(self):
        if self.year < 4:
            self.year += 1


if __name__ == "__main__":
    carter = Student(
        _id = 1111,
        username = "CarterMarilyn",
        last_name = "Carter",
        first_name = "Marilyn",
        phone =  "312/473-4837",
        year = 1)
    print(carter)
    carter.update_year()




