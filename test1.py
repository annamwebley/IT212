# Project 4b
# Anna Markiewicz
# May 25
# test1.py

from onlinestudent import OnlineStudent


mcarter = OnlineStudent("1234","mcarter","Carter","Marilyn","312/473-4837",1,"mcarter@coolmail.net")
def test__init__():
    print(f"Test to verify __init__, student is = {mcarter}")

def testEmail():
    print(f"Test to verify email, email = {mcarter.email}")

def testAddGroupMember():
    mcarter.add_group_member("ggraber")
    print(f"Test to verify add_group_member(), group member = {mcarter.study_group}")

if __name__ == "__main__":
    test__init__()
    testEmail()
    testAddGroupMember()

