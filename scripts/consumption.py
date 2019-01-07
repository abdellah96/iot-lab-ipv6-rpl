import matplotlib.pyplot as plt
import sys

def consumption(*argv):

	time,power = [], []
	values=[]
	with open(str(sys.argv[1])) as input_plot_file:
		for line in input_plot_file:
			if line.strip() == '':				
				break
		
		for line in input_plot_file:
			
			
			try: values = [float(s) for s in line.split()]
			except ValueError: print('Value Error')
		     	#print(values)
			if(len(values) > 5): 
				time.append(values[3])	
				power.append(values[5])
			else :
				break
			
	plt.plot(time,power)
	plt.ylabel('Puissance energetique(W)')
	plt.xlabel('Temps(s)')
	plt.title('Efficacite energetique du noeud')
	plt.show()
	
if __name__ == "__main__":
	consumption()
