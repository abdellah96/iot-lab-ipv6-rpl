import numpy as np
import matplotlib.pyplot as plt
import sys
import os


def moyenne(tableau):
    return sum(tableau, 0.0) / len(tableau)

def variance(tableau):
    m=moyenne(tableau)
    return moyenne([(x-m)**2 for x in tableau])

def ecartype(tableau):
    return variance(tableau)**0.5

	
def plot_mean_variance(*argv):
	
	#####  PLOT LATENCY ##### 

	latency = [[],[],[],[],[]]
	#LOSS PAQUET RATIO
	lpq = [0,0,0,0,0]

	experiences = ['experience1','experience2','experience3','experience4','experience5']	
	x_pos = np.arange(len(experiences))
	y=[]
	y_ecartype=[]
	i=0
	
	for fichier in os.listdir(sys.argv[1]):
		j=0
		with open(sys.argv[1]+'/'+fichier) as input_plot_file:
        	        for line in input_plot_file:
        	       	 	for s in line.split():
					if(float(s) !=0):
						latency[i].append(float(s))
					else : #if latency is null,there is a paquet loss
						j+=1 
								                
		#print(latency[i])
		#calculate the loss ratio
		lpq[i] = j*100/(j+len(latency[i]))
		
		y.append(moyenne(latency[i]))	
		y_ecartype.append(ecartype(latency[i]))	
		i+=1
		
	print(lpq)

	fig, axs = plt.subplots(nrows=1,ncols=2,sharex=True)
	ax = axs[0]
	ax.bar(x_pos, y , yerr=y_ecartype, align='center', alpha=0.5, ecolor='black', capsize=10)
	ax.set_ylabel('Moyenne')
	ax.set_xticks(x_pos)
	ax.set_xticklabels(experiences)
	ax.set_title('Latency de cinq echantillons de taille 150')
	ax.yaxis.grid(True)
	
	##### PLOT ENERGY CONSUMPTION ##### 
	y=[]
        y_ecartype=[]
	i =0
	energy=[[],[],[],[],[]]
	for fichier in os.listdir(sys.argv[2]):
                with open(sys.argv[2]+'/'+fichier) as input_plot_file:
			for line in input_plot_file:
		            	if line.strip() == '':
	                                break	
			for line in input_plot_file:
				
				try: values=[float(s) for s in line.split()]
				except ValueError:
					print('ValueError')
				#print(len(values))
				if(len(values) > 7):
					#print(values[5])
                                        energy[i].append(float(values[5]))
					

                #print(energy[i])
                y.append(moyenne(energy[i]))
                y_ecartype.append(ecartype(energy[i]))
                i+=1
		

	
	ax = axs[1]
	ax.bar(x_pos, y , yerr=y_ecartype, align='center', alpha=0.5, ecolor='black', capsize=10)
	ax.set_ylabel('Moyenne')
	ax.set_xticks(x_pos)
	ax.set_xticklabels(experiences)
	ax.set_title('Consommation energetique de cinq echantillons de taille'+str(len(energy[0])))
	ax.yaxis.grid(True)
	'''
	ax = axs[1,0]
	ax.bar(x_pos, y , yerr=y_ecartype, align='center', alpha=0.5, ecolor='black', capsize=10)
	ax.set_ylabel('Moyenne')
	ax.set_xticks(x_pos)
	ax.set_xticklabels(experiences)
	ax.set_title('latence de deux echantillons de taille 8')
	ax.yaxis.grid(True)

	ax = axs[1,1]
	ax.bar(x_pos, y , yerr=y_ecartype, align='center', alpha=0.5, ecolor='black', capsize=10)
	ax.set_ylabel('Moyenne')
	ax.set_xticks(x_pos)
	ax.set_xticklabels(experiences)
	ax.set_title('ratio perte de paquets de deux echantillons de taille 8')
	ax.yaxis.grid(True)
	'''
	#plt.tight_layout()
	#plt.savefig('bar_plot_with_error_bars.png')
	
	plt.show()


if __name__ == "__main__":
    plot_mean_variance()
