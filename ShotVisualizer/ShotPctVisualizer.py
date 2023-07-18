import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
class ShotPctVisualizer:
    def __init__(self, shotTuple: tuple[int, int, float]) -> None:
        
        self.totalShots = shotTuple[0]
        self.totalGoals = shotTuple[1]
        self.shotPCT = shotTuple[2]
        self.colour = ["#ADD8E6","#90EE90"]
        self.labels = ["Non-Converted Shots", "Converted Shots"]

    def piePlot(self):
        fig, ax = plt.subplots(figsize = (10,10))
        labels = [" ".join([self.labels[0],"{:.2%}".format(1-self.shotPCT)]), " ".join([self.labels[1],"{:.2%}".format(self.shotPCT)])]
        ax.pie(x=[self.totalShots - self.totalGoals, self.totalGoals], colors=self.colour, wedgeprops=dict(width=0.5),startangle=-40)
        
        ax.legend(labels=labels)
        #from https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html
        # bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        # kw = dict(arrowprops=dict(arrowstyle="-"),
        #         bbox=bbox_props, zorder=0, va="center")

        # for i, p in enumerate(wedges):
        #     ang = (p.theta2 - p.theta1)/2. + p.theta1
        #     y = np.sin(np.deg2rad(ang))
        #     x = np.cos(np.deg2rad(ang))
        #     horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        #     connectionstyle = f"angle,angleA=0,angleB={ang}"
        #     kw["arrowprops"].update({"connectionstyle": connectionstyle})
        #     ax.annotate(self.label[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
        #                 horizontalalignment=horizontalalignment, **kw)
        return fig