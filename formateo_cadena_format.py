#{[field_name][!conversion][:format_spec]}

#field_name: Especifica el objeto cuyo valor se va a insertar.
#conversion: Especifica una conversión de tipo (opcional), utilizando !s, !r, o !a.
#format_spec: Especifica el formato del valor (opcional).


#REFERENCIAS A ARGUMENTOS POSICIONALES
print("Primero, contaras hasta {0}".format(3))

#REFERENCIA IMPLICITA AL PRIMER ARGUMENTO POSICIONAL
print("traeme un {}".format("pan"))

#REFERENCIA A MULTIPLES ARGUMENTOS POSICIONALES
print("de {} a {}".format("A", "B"))


#age =18
#name = "mike"
#print("Hello {}. You must be at least {} to continue!".format(name, age))


#first_name = "mike"
#print('Hello {first_name}. Why do they call you {first_name}?'.format(first_name=first_name))

age = 18
first_name = 'mike'
greeting = 'Hello {first_name}. you must be at least {age} to continue'
formatted_greeting = greeting.format(first_name=first_name, age=age)
print(formatted_greeting)