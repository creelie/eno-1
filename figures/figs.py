import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams.update({"font.family":"serif","mathtext.fontset":"cm","font.size":12})

# Figure 1: the real sphere and a polynomial curve leaving it
fig=plt.figure(figsize=(7.2,5.6)); ax=fig.add_subplot(111,projection="3d")
u=np.linspace(0,2*np.pi,90); v=np.linspace(0,np.pi,60)
X=np.outer(np.cos(u),np.sin(v));Y=np.outer(np.sin(u),np.sin(v));Z=np.outer(np.ones_like(u),np.cos(v))
ax.plot_surface(X,Y,Z,color="#9ecae1",alpha=0.35,linewidth=0,shade=True)
for z0 in np.linspace(-0.8,0.8,5):
    r=np.sqrt(1-z0**2); ax.plot(r*np.cos(u),r*np.sin(u),z0*np.ones_like(u),color="#3182bd",lw=0.6,alpha=0.7)
t=np.linspace(-1.35,1.35,200)
P=np.array([0.0,0.6,-0.8])  # a point of the sphere
c=np.array([t, 0.6+0*t, -0.8+0.9*t**2])
ax.plot(*c,color="#d62728",lw=2.2)
ax.scatter(*P,color="k",s=30)
ax.text(0.1,0.6,-1.05,r"$P$",fontsize=14)
ax.text(1.2,0.6,1.0,r"$t\mapsto \exp(tE)\cdot P$",color="#d62728",fontsize=13)
ax.text(-1.6,-1.2,1.15,r"$x^2+y^2+z^2=1$",color="#08519c",fontsize=13)
ax.set_box_aspect((1,1,1)); ax.set_xlim(-1.4,1.4);ax.set_ylim(-1.4,1.4);ax.set_zlim(-1.2,1.6)
ax.set_axis_off(); ax.view_init(elev=18,azim=-60)
plt.tight_layout(); plt.savefig("fig_sphere.png",dpi=200,facecolor="white",bbox_inches="tight"); plt.close()

# Figure 2: which transcendence degrees of ML* are settled, n = 3 and n = 4
fig=plt.figure(figsize=(8,5)); ax=fig.add_subplot(111,projection="3d")
cols={"A":"#2ca02c","B":"#1f77b4","T":"#9e9e9e","O":"#ff7f0e"}
data=[(3,[("A",0),("A",1),("B",2),("T",3)]),(4,[("A",0),("A",1),("O",2),("B",3),("T",4)])]
for yi,(n,lst) in enumerate(data):
    for (kind,d) in lst:
        h=1.0 if kind!="T" else 0.35
        ax.bar3d(d,yi*1.6,0,0.7,0.7,h,color=cols[kind],alpha=0.9,shade=True,edgecolor="k",linewidth=0.3)
ax.set_xticks([0.35,1.35,2.35,3.35,4.35]); ax.set_xticklabels(["0","1","2","3","4"])
ax.set_yticks([0.35,1.95]); ax.set_yticklabels([r"$n=3$",r"$n=4$"])
ax.set_zticks([]); ax.set_xlabel(r"$\mathrm{tr.deg}_k\,\mathrm{ML}^*(B)$",labelpad=8)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=cols["A"],label="Theorem A"),Patch(color=cols["B"],label="Theorem B"),
  Patch(color=cols["O"],label="open over non-closed $k$"),Patch(color=cols["T"],label="no slice ($\\mathrm{ML}^*=B$)")],
  loc="lower center",bbox_to_anchor=(0.5,-0.02),ncol=2,fontsize=10,frameon=False,bbox_transform=fig.transFigure)
ax.view_init(elev=24,azim=-58)
plt.subplots_adjust(bottom=0.18); plt.savefig("fig_ladder.png",dpi=200,facecolor="white",bbox_inches="tight"); plt.close()

# Figure 3: the subrings in the proof
fig,ax=plt.subplots(figsize=(7.5,4.2))
from matplotlib.patches import Ellipse, FancyArrowPatch
for (w,h,lab,col,yl) in [(7.0,3.8,r"$B=A[s]$","#deebf7",1.62),(5.0,2.7,r"$A=\ker D$","#c6dbef",1.08),(3.0,1.6,r"$R=\mathrm{ML}^*(B)$","#9ecae1",0.48)]:
    ax.add_patch(Ellipse((0,0),w,h,facecolor=col,edgecolor="#08519c",lw=1.2))
    ax.text(0,yl,lab,ha="center",fontsize=13)
ax.text(0,-0.2,r"$E(R)\subseteq R$",ha="center",fontsize=12)
ax.add_patch(FancyArrowPatch((0.55,-0.55),(1.05,-0.25),connectionstyle="arc3,rad=-0.9",arrowstyle="-|>",mutation_scale=14,color="#d62728",lw=1.5))
ax.text(0.35,-0.68,r"$E$",color="#d62728",fontsize=13)
ax.text(0,-2.25,r"$D(s)=1$, every slice derivation kills $R$",fontsize=11,ha="center")
ax.set_xlim(-3.7,3.7);ax.set_ylim(-2.45,2.0);ax.set_aspect("equal");ax.axis("off")
plt.tight_layout(); plt.savefig("fig_rings.png",dpi=200,facecolor="white",bbox_inches="tight"); plt.close()
