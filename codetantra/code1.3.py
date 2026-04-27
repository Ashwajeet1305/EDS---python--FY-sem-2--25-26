from datetime import date
from datetime import datetime

# Input dates
date1 = input()
date2 = input()

# Convert string to date format
d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")

# Calculate difference
difference = (d2 - d1).days

# Output number of days
print(difference)
