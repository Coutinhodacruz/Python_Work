from pathlib import Path
import csv

path = Path.cwd() / "new_directory" / "consensus.csv"
path.touch()
census = [
    {"name": "Ned",
     "isSingle": False,
     "cohort": 15,
     "status": "COMPLICATED"
     },
    {"name": "Ridwan",
     "isSingle": True,
     "cohort": 15,
     "status": "UNKNOWN"
     },
    {"name": "Timmy",
     "isSingle": True,
     "cohort": 15,
     "status": "UNDISCLOSED"
     },
]

# numbers = [
#     [29, 39, 49, 58, 34, 56],
#     [80, 34, 56, 32, 67, 89],
#     [43, 65, 76, 34, 78, 54]
# ]


with open(path, encoding="utf-8", mode="r+") as file:
    writer = csv.DictWriter(file,
                            fieldnames=["name", "isSingle", "cohort", "status"])
    writer.writeheader()
    writer.writerows(census)

    # writer = csv.writer(file)
    # writer.writerows(numbers)
