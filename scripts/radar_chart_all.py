from math import pi
import matplotlib.pyplot as plt




color=["red","orange","green","darkblue"]

# Set data
performances = ['Temps de convergence', 'Consommation energetique', 'Temps de latence', 'Taux de perte de paquets']
#The values are found using the mean_variance statistic test, and taking the best results
values_NULL_RDC = [8, 0.175,63, 10]
values_Contiki_MAC = [8,0.16,149,30]
values_TSCH = [30,0.17,300,20]

N = len(performances)

x_as = [n / float(N) * 2 * pi for n in range(N)]

# Because our chart will be circular we need to append a copy of the first 
# value of each list at the end of each list with data
values_NULL_RDC += values_NULL_RDC[:1]
values_Contiki_MAC += values_Contiki_MAC[:1]
values_TSCH += values_TSCH[:1]



x_as += x_as[:1]


# Set color of axes
plt.rc('axes', linewidth=0.5, edgecolor="black")


# Create polar plot
ax = plt.subplot(111, polar=True)


# Set clockwise rotation. That is:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)


# Set position of y-labels
ax.set_rlabel_position(0)


# Set color and linestyle of grid
ax.xaxis.grid(True, color="grey", linestyle='solid', linewidth=0.5)
ax.yaxis.grid(True, color="grey", linestyle='solid', linewidth=0.5)


# Set number of radial axes and remove labels
plt.xticks(x_as[:-1], [])

# Set yticks
plt.yticks([50, 100, 200,300], ["50","100","200","300"])


# Plot data
ax.plot(x_as, values_NULL_RDC,'-y', linestyle='solid', zorder=3, label = 'NULL RDC')
ax.plot(x_as,values_Contiki_MAC,'-b', linestyle='solid',zorder=3, label ='Contiki MAC')
ax.plot(x_as,values_TSCH,'-r', linestyle='solid',zorder=3, label ='TSCH')





plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)



# Fill area
ax.fill(x_as, values_NULL_RDC, 'yellow', alpha=0.3)
ax.fill(x_as,values_Contiki_MAC, 'blue', alpha=0.3)
ax.fill(x_as,values_TSCH, 'red', alpha=0.3)




# Set axes limits
plt.ylim(0, 300)


# Draw ytick labels to make sure they fit properly
for i in range(N):
    angle_rad = i / float(N) * 2 * pi

    if angle_rad == 0:
        ha, distance_ax = "center", 10
    elif 0 < angle_rad < pi:
        ha, distance_ax = "left", 1
    elif angle_rad == pi:
        ha, distance_ax = "center", 1
    else:
        ha, distance_ax = "right", 1

    ax.text(angle_rad, 300 + distance_ax, performances[i], size=10,color=color[i], horizontalalignment=ha, verticalalignment="center")

    ax.set_title("Compraison des performances du protocole RPL en fonction de la couche MAC pour le Border Router   ")

# Show polar plot
plt.show()
