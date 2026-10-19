# Initialize a mock score to test the conditional logic rules
score = 75

# Approach A: The clean, compact Python conditional expression variant
status_inline = "Pass" if score >= 60 else "Fail"
print(f"Inline evaluation output: {status_inline}")

# Approach B: The standard multi-line block pattern (Note the mandatory ':' path)
if score >= 60:
    status_block = "Pass"
else:
    status_block = "Fail"

print(f"Block indentation output: {status_block}")
