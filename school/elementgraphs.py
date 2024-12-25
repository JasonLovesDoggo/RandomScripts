# Add edges between elements in the same period
periods = [
	['H', 'He'],
	['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne'],
	['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar'],
	['K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr']
]
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # We'll use Seaborn for the heatmap

# Electronegativity values (same as before)
electronegativity_values = {
	'H': 2.20, 'He': 0,
	'Li': 0.98, 'Be': 1.57, 'B': 2.04, 'C': 2.55, 'N': 3.04, 'O': 3.44, 'F': 3.98, 'Ne': 0,
	'Na': 0.93, 'Mg': 1.31, 'Al': 1.61, 'Si': 1.90, 'P': 2.19, 'S': 2.58, 'Cl': 3.16, 'Ar': 0,
	'K': 0.82, 'Ca': 1.00, 'Sc': 1.36, 'Ti': 1.54, 'V': 1.63, 'Cr': 1.66, 'Mn': 1.55, 'Fe': 1.83, 'Co': 1.88, 'Ni': 1.91, 'Cu': 1.90, 'Zn': 1.65, 'Ga': 1.81, 'Ge': 2.01, 'As': 2.18, 'Se': 2.55, 'Br': 2.96, 'Kr': 3.00
}

# Create a 2D numpy array to represent the periodic table
data = np.zeros((4, 18))  # 4 periods, 18 groups (maximum)

# Fill the array with electronegativity values
elements = list(electronegativity_values.keys())
for i in range(4):
	for j in range(len(periods[i])):
		element = periods[i][j]
		data[i, j] = electronegativity_values[element]

# Create the heatmap using Seaborn
plt.figure(figsize=(10, 5))
sns.heatmap(data, annot=True, fmt=".2f", cmap="YlGnBu", cbar_kws={'label': 'Electronegativity'})

# Set axis labels and ticks
plt.xlabel('Group')
plt.ylabel('Period')
plt.xticks(np.arange(18) + 0.5, range(1, 19))
plt.yticks(np.arange(4) + 0.5, range(1, 5))

# Set title
plt.title('Periodic Trends in Electronegativity (Heatmap)')

plt.show()
