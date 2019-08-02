kilometer= [39,40,41]
feet1 = map(lambda x: float(3280) * x, kilometer)

print(list(feet1))

#better:
feet2= [float(3280) * x for x in kilometer]

print(feet2)