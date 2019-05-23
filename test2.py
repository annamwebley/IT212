# Project 4b
# Anna Markiewicz
# May 25
# test2.py

import unittest
from onlinestudent import OnlineStudent

class TestOnlineStudent(unittest.TestCase):
    def test__init__():
        mcarter = OnlineStudent("1234","mcarter","Carter","Marilyn","312/473-4837",1,"mcarter@coolmail.net")
        expected_result = '"1234","mcarter","Carter","Marilyn","312/473-4837",1,"mcarter@coolmail.net"'
        self.assertEqual(mcarter, expected_result)
    
    def testEmail():
        mcarter = OnlineStudent("1234","mcarter","Carter","Marilyn","312/473-4837",1,"mcarter@coolmail.net")
        expected_result = "mcarter@coolmail.net"
        self.assertEqual(mcarter.email, expected_result)

    def testAddGroupMember():
        group_member = OnlineStudent("ggraber")
        expected_result = "ggraber"
        self.assertEqual(group_member, expected_result)

if __name__ == "__main__":
    unittest.main()