score = 72
status = "Pass" if score >= 60 else "Fail"
print(f"score={score} status={status}")

# Boundary check list
score = 60
status = "Pass" if score >= 60 else "Fail"
print(f"Boundary check: score={score} status={status}")
