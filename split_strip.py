"""Puedes usar .strip() y sus variantes, .rstrip() y .lstrip(),
para eliminar espacios en blanco de la cadena, incluidos 
caracteres de tabulación y de nueva línea. 
Esto es especialmente útil cuando estás leyendo un archivo 
de texto que necesitas analizar."""


#ELIMINAR CON .STRIP()
#ELIMINA ESPACIOS EN BLANCO AL INICIO Y AL FINAL DE LA CADENA

text_with_spaces = ' Hola, mundo!  '
stripped_text = text_with_spaces.strip()
print(f"Original: '{text_with_spaces}")
print(f"Sin espacios: '{stripped_text}")


#EJEMPLO CON .RSTRIP()
#ELIMINA ESPACIOS EN BLANCO SOLO AL FINAL DE LA CADENA

text_with_trailing_spaces = 'Hola, mundo!  '
right_stripped_text = text_with_trailing_spaces.rsplit()
print(f"Original: '{text_with_trailing_spaces}'")
print(f"Sin espacios al final: '{right_stripped_text}'")


#EJEMPLO CON .LSTRIP()
#ELIMINA ESPACIOS EN BLANCO SOLO AL INICIO DE LA CADENA

text_with_leading_spaces = '    hola, mundo!'
left_stripped_text = text_with_leading_spaces.lstrip()
print(f"Original: '{text_with_leading_spaces}'")
print(f"Sin espacios al inicio: '{left_stripped_text}'")