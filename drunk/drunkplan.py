import drunk

#"as" is the abbrevation. It's easy to call the function using shorttened form.
#for example:
#fig=matplotlib.pyplot.figure(figsize=(10,10)) could be used as:
#fig=plt.figure(figsize=(10,10))
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import csv

# Open up 'drunk.plan.txt' file and load the map.
tMap = []
f = open('drunk.plan.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
for row in reader:
	rowlist=[]
	for value in row:
		rowlist.append(int(value))
	tMap.append(rowlist)
f.close()


stepNums = []  #Create an empty list which records drunk's steps.
#Create an empty list which records drunk's route. It includes every drunk's passing points. 
#For example: if 10th drunk passing through [A,B,C,D], and 20th drunk passing through [A,E,F]. The content of the list is [[A,B,C,D],[A,E,F]]
drunkRoutes = [] 
for drunkId in range(10,255,10):
    #
	drunkRoutes.append(drunk.Drunk(drunkId).move()) 
	stepNums.append(len(drunk.Drunk(drunkId).move())) #object=drunk.Drunk(drunkId)，then object.move().It means create an object and use move methods on this object.

def get_Drunk_Step(dkId, i): # Get dkId for drunk's ith steps. In this way, dkId goes from 0 to 24, which is，(0,1,2,3...)
	if i < len(drunkRoutes[dkId]): 
		return drunkRoutes[dkId][i]
	else:
        # For example: Some drunks might walk 20steps back home and some might needs 50 steps. It needs to refresh at the most steps drunks walked. If using 20 steps to refresh, the drunks with 50 steps home can't make it to their home.
        # If uses 50 steps, some drunks with 20 steps could stay at home and the portion of 21 to 50 steps keeps refresh.
		return drunkRoutes[dkId][-1] 

# It records drunk's density map. The initial is at 0.
density = np.zeros((300, 300), dtype = int) # It records drunk's density map. The initial is at 0.
for route in drunkRoutes:
	for i in range(0, len(route)):
		density[route[i][0]][route[i][1]] += 1

#Save density as txt files.
np.savetxt('density.txt', density, fmt = '%d', delimiter = ',')  #Save density as txt files.

fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0, 0, 1, 1])


def update(step_number):
	plt.clf()
	for dkId in range(0, len(drunkRoutes)):
		tMap[get_Drunk_Step(dkId, step_number)[0]][get_Drunk_Step(dkId, step_number)[1]] = (dkId*10 + 10)  # Record drunk's steps and give them an ID value.
	plt.xlim(0,300)
	plt.ylim(0,300)
	plt.imshow(tMap)



def run():
    # Use update's function. Frame is an array that is (0, how many steps to drunk's home). The value inside the the () will be used for update function.
	animation = anim.FuncAnimation(fig, update, frames=range(0, max(stepNums))) 
	canvas.draw()

root = tk.Tk()  # Use tkinter's User Interface
root.wm_title('DrunkPlan')
canvas = FigureCanvasTkAgg(fig, master = root)
canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

menu_bar = tk.Menu(root)   #Sets the menu bar.
root.config(menu = menu_bar)
model_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label = 'Model', menu = model_menu)
model_menu.add_command(label = 'Run model', command = run) # Make an command called 'Run model' to run the model.
model_menu.add_command(label="Close Window", command= root.destroy)  # Close the tkinter window.
tk.mainloop()