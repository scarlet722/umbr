text = "This is a more advanced comprehension exercise to practice"
result = [word[::-1] for word in text.split() if len(word) >= 5]
print(result)
