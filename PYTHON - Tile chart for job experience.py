import matplotlib.pyplot as plt
import squarify

# Data for the tile chart
roles = [
    ("Business Analyst", 1),
    ("Biz Ops Consultant", 5),
    ("Project Coordinator", 1),
    ("Order Manager", 5),
    ("Reporting Specialist", 1),
    ("InfoSec Analyst", 2),
    ("IT Incident Analyst", 3),
    ("Trainer", 1),
    ("Temp & Student Jobs", 8)
]

# Extract labels and sizes
labels = [f"{role}\n{years} yrs" for role, years in roles]
sizes = [years for _, years in roles]

# Create the tile chart
plt.figure(figsize=(10, 6))
squarify.plot(sizes=sizes, label=labels, alpha=0.7, edgecolor="black")
plt.axis("off")
plt.title("Tile Chart of Richard's Work Experience")
plt.show()
