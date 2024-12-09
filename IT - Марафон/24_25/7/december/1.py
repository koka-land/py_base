d = int(input())
x = int(input())

a = ((365 - 75 / (d**3)) / (3 * d**2 - d)) * 5
b = ((412 - 125 / (d**3)) / (2 * d**2 - d)) * 4

print(int((a + b) * x))