# P1nG
My super awesome programming language made all by myself and eventually I'll recruit others to help me in my journey of making the perfect programming language

# Syntax
the syntax is pretty simple to understand:
variable=command{data/paramaters/file}
or
command{data/paramaters/file/empty}

# Commands
ask: prompts the user for input and assigns the input to a variable. Syntax: variable=ask{What's your name}
math: performs a mathematical operation and assigns the result to a variable. Syntax: variable=math{5+5}
paste: prints the value of a variable or a string. Syntax: paste{Hello, {variable}.}
end: exits the program. Syntax: end{!}
read: allows you to read .json files. Syntax: /path/to/json=read{}
write: allows you to write .json files. Syntax: /path/to/json=write{data, stuff, age}
win: Allows you to create an application window. Syntax: win{500x500}
int: Allows you to open a website. Syntax: int{https://www.google.com}
wint: Allows you to put text on a pre-existing application window. Syntax: wint{Text}

# Examples
paste{hello} Responce: hello
variable=ask{How old are you? } Responce: How old are you?
paste{You're {variable} years old!} Responce: You're 1 years old! (variable=1)
variable=math{5*2} Responce:
paste{{variable}} Responce: 10
end{!} Responce: *Ends program*
file.json=write{Name: John, LName: Doe, Age: 50} Responce: Written succesfully
file.json=read{} Responce: DATA: Name: John, LName: Doe, Age: 50
win{500-500} Responce: Creates 500x500 sized window
int{https://www.google.com} Responce: Opens up https://www.google.com in your default browser
wint{Hello World} Responce: Puts the text 'Hello World' on the screen

# Website
https://gpage.neocities.org/p1ng/
