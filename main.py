import pandas as pd

print("hello")
# Create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 22],
    "Score": [85, 90, 78]
}

df = pd.DataFrame(data)

# Add a new column
df["Passed"] = df["Score"] >= 80

# Print the DataFrame
print(df)
