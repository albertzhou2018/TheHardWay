type_of_people = 10 #创建一个变量type_of_people，并赋值10
x = f"There are {type_of_people} types of people." #创建变量x，赋值一串字符串

binary = "binary"#创建变量binary，赋值“binary”
do_not = "don't"#创建变量do_not，赋值”don't“”
y = f"Those who know {binary} and those who {do_not}."#创建变量y，赋值一串字符串

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)
