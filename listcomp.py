number_list=[x**2 for x in range(10) if x%2==0]
print(number_list)


#list comprehension lab
num=[x for x in range(11) if x%2==0]
print(num)

city=["Seoul", "New York", "London", "Shanghai", "Paris", "Tokyo"]
s_city=[c for c in city if c.startswith("S")]
print(s_city)