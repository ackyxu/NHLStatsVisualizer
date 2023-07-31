from ShotVisualizer.Graphs import Graphs
import numpy as np

class BarGraph(Graphs):
    def __init__(self, fig=None, ax=None):
        super().__init__(fig, ax)


    def CreateGraph(self, field: str, results: list[dict], playerStats: int | float | None = None, alignLeft=False):
        return self.createBarGraph(field, results, playerStats,alignLeft)


    def createBarGraph(self, field: str, results: list[dict], playerStats: int | float | None = None, alignLeft = False):
        fieldStr = (str.upper(field[0])+field[1:]).replace("_", " ")
        valList = np.array([result[field] for result in results])
        valList.sort()
        mean = np.mean(valList)
        if alignLeft:
            xflip = 1
            alignment = "left"
        else:
            xflip = -1
            alignment = "right"
        x = [0]
        y =  [mean]
        colour = [self.percentileColour[40]]
        if playerStats:
            x.append(0.6)
            y.append(playerStats)
            pct = self.getPercentile(valList, playerStats)
            colour.append(self.DefinePercentileColor(pct))
            self.ax.annotate("Total %s\n%.2f"%(fieldStr,playerStats),
                (playerStats,x[1]),
                ha=alignment, 
                **self.font,
                textcoords="offset pixels",
                xytext=(5 * xflip, 5))
    

        self.ax.annotate("Mean %s\n%.2f"%(fieldStr,mean),
            (mean,x[0]),
            ha=alignment, 
            **self.font,
            textcoords="offset pixels",
            xytext=(5 * xflip, 5))
        

        self.ax.barh (x, y, height = 0.5,color=colour,align='edge')
        self.ax.set(yticks = []) # ,xticks = []
        self.ax.set_xlim(0,valList[-1])
        # self.ax.set_ylim(0,x[-1])

        if not alignLeft:
            self.ax.invert_xaxis()
        self.ax.spines[['right', 'top','bottom','left']].set_visible(False)
        self.ax.set_title(fieldStr, loc=alignment, **self.font, fontsize=30)
        
        return self.fig