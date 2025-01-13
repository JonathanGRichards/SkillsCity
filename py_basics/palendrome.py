string = "bob"
reversed= ""

for char in string:
  reversed = char + reversed

result = "this isn't a palendrome";
if string == reversed:
  result = "this is a palendrome"
print(result)