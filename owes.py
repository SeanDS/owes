def calculateOwes(owes):
  """
  Calculates from the inserted OWES matrix (list of lists) who owes whom
  by minimising payments
  """
  
  # get list of indices in OWES
  N = range(len(owes))
  
  """
  First step: subtract for each person OWES from OWED where OWES is
  smaller than OWED. This makes the matrix triangular.
  """
  
  for i in N:
    for j in N:
      if i != j and owes[i][j] > owes[j][i]:
	# subtract B OWES A from A OWES B
	owes[i][j] -= owes[j][i]
	
	# set B OWES A to zero
	owes[j][i] = 0

  """
  Second step: debts between A and B where debts between A and B and
  A and C exist are cancelled by increasing/decreasing the relevant debt
  to C.
  """
  
  for k in N:
    for i in N:
      for j in N:
	if k == i or i == j or k == j:
	  continue
	if owes[j][k] > owes[i][j]:
	  owes[i][k] += owes[i][j]
	  owes[j][k] -= owes[i][j]
	  owes[i][j] = 0

  return owes

def printOwes(owes, names):
  """
  Prints who owes whom from OWES using names defined in NAMES
  """
  
  for i in range(0, len(owes)):
    for j in range(0, len(owes[i])):
      if owes[i][j] > 0:
        print u"{0} owes {1} \u00A3{2}".format(names[i], names[j], owes[i][j])

# example usage
owes = [
  #	Sean	Jan	Gareth	Neil	Martin
  [	0,	38.55,	61.52,	68.78,	0	], # Sean owes
  [	112.32,	0,	61.52,	68.78,	0	], # Jan owes
  [	112.32,	38.55,	0,	68.78,	0	], # Gareth owes
  [	112.32,	38.55,	61.52,	0,	0	], # Neil owes
  [	93.97,	0,	61.52,	18.96,	0	]  # Martin owes
]

printOwes(calculateOwes(owes), ["Sean", "Jan", "Gareth", "Neil", "Martin"])