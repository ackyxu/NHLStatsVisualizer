from matplotlib import pyplot as plt
from scipy import stats

class Graphs:
    percentileColour = {0:'lightblue',20:'skyblue',40:'deepskyblue',60:'cornflowerblue',80:'royalblue'}
    font = {'fontname':'Helvetica'}
    def __init__(self, fig=None,ax = None):
        if ax and fig:
            self.ax,self.fig = ax,fig
        else:
            self.fig, self.ax = plt.subplots(figsize = (8,2))
    


    def CreateGraph(self, field: str, results: list[dict], playerStats: int | float | None = None):
        # creates a graph
        pass

    def DefinePercentileColor(self, pct: float) -> str:

        keys = list(self.percentileColour.keys())
        keys.sort()
        prev = 0
        for key in keys:
            if pct < key:
                return self.percentileColour[prev]
            else:
                prev = key

        return self.percentileColour[80]

    def getPercentile(self, dataSet: list[int], value: int) -> float:
        return stats.percentileofscore(dataSet, value)

    def CreatePercentileGuide(self):
        ax = self.ax
        size = 10
        height = 0.3
        colours = list(self.percentileColour.values())
        pct = list(self.percentileColour.keys())
        x = [i for i in range(0,len(pct)*size,size)]
        ax.bar(x=x, height=height,width=size, color=colours)
        for i,p in enumerate(pct):
            n = pct[i+1] if i < len(pct) - 1 else 100 
            ax.annotate("%d-%d%%"%(p,n),
                (x[i],height/2),
                ha="center", 
                **self.font,
                c="white",
                fontweight='bold',
                fontsize='x-large')



        ax.set_xlim(x[0]-size/2, x[-1]+size/2)
        ax.set_ylim(0, 0.5)
        ax.set(yticks = [],xticks = [])
        ax.spines[['right', 'top','bottom','left']].set_visible(False)
        ax.set_xlabel("Percentile Colour Guide", **self.font)

        self.fig.subplots_adjust(left=0, bottom=0, right=1, top=0.5, wspace=0, hspace=0.5)
        return self.fig
            