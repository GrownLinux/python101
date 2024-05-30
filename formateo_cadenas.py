'''El formateo de cadenas o sustitución de 
cadenas es cuando deseas insertar una cadena
 dentro de otra cadena.'''


name = 'Mike'
print('my name is %s' % name)


age = 18
print('You must be at least %s to continue' % age)
print('Hello %s, You must be at least %i to continue!' % (name, age))
#El %i indica que vas a pasar un entero.

print('Hello %(first_name)s. You must be at least %(age)i to continue!' % {'first_name': name, 'age': age})















