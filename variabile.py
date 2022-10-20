# variabila = zona din memorie a unui calculator care tine date
# variabila = cutiuta in care punem valori

# am declarat si initializat variabila  marca
marca_masina = 'Volvo'
model_masina = 'XC 60'

# nu putem pune spatiu in numele variabile
# o variabila incepe cu litera mica

# loosely typed - nu trebuie sa specificam tipurile

print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul : {model_masina}')

# suprascriere
model_masina = 'XC 60 facelift'

print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul : {model_masina}')

nume = 'Cociuba'
prenume = 'Denisa'
varsta = 26
print(prenume + ' ' + nume)
print(f'{prenume} {nume} si varsta de {varsta}')