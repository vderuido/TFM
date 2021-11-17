import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Circle
img = plt.imread("/home/vic/Documents/git_repos/TFM/imagenes/auditorio_butacas.jpg")
fig, ax = plt.subplots()

xt=1.5*2+2*6+1.32*2
yt=1.5*2+2*11
ax.imshow(img,extent=[0,xt,yt,0])

fuentex=xt/2
fuentey=0.5+2
radio=np.array([21,20,19,18,17,13,10,8,6])
colores=np.array(["blue","red","yellow","green","black","white","orange","gray","pink"])

for i in range(radio.size):
    circ=Circle((fuentex,fuentey),radio[i],color=colores[i])
    ax.add_patch(circ)
plt.show()
