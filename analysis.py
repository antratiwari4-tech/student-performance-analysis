
import pandas as pd
import matplotlib.pyplot as plt

# Sample student marks
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Maths": [85, 72, 90, 65, 78],
    "Science": [88, 75, 92, 70, 82],
    "English": [80, 85, 87, 74, 79]
}

df = pd.DataFrame(data)

# Calculate average marks for each student
subjects = ["Maths", "Science", "English"]
df["Average"] = df[subjects].mean(axis=1)

print("Student Performance Analysis")
print(df.round(2))

# Find the highest overall average
top_student = df.loc[df["Average"].idxmax()]
print("\nHighest average:", top_student["Student"])
print("Average marks:", round(top_student["Average"], 2))

# Plot a graph
df.plot(
    x="Student",
    y="Average",
    kind="bar",
    legend=False,
    title="Average Marks by Student"
)

plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("student_averages.png")
plt.show()
