from click import prompt
from voter import Voter
from candidate import Candidate
from common_db_operations import Operation
import random



v = Voter("Droid-fi Voting System")
op = Operation()

print(op.count_total("voter", "gender", "Male"))
print(op.search_single_entry("voter", "id_number", "id53963"))


# print(v.total_voters())
# print(v.count_registered_per_poling_center("MUS3B"))

# cand_id = input("Enter Candidate ID Number: ")
# position = input("Enter Electoral Position(\'President, Governor, Senetor, MP'): ")