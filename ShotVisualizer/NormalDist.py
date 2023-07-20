import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

class NormalDist:

    def createPDFDist(self, field: str, results: list[dict], playerStats: int | None = None):

        fieldStr = str.upper(field[0])+field[1:]
        fig, ax = plt.subplots(figsize = (10,5))
        valList = np.array([result[field] for result in results])
        valList.sort()
        mean = np.mean(valList)
        sd = np.std(valList)
        dist = norm.pdf(valList,mean,sd)
        offsets = max(dist) / 10
        ax.set_xlim(0,valList[-1] + 10)
        ax.set_ylim((0-2*offsets),(max(dist) + 1.5 * offsets))


        ax.plot(valList,dist, color = "lightblue")
        bbox = dict(boxstyle ="round", fc ="0.8")

        ax.vlines(x=mean,ymin=-offsets,ymax = max(dist), color = "blue")
        ax.annotate("Mean (%s): %d"%(fieldStr,mean),
                    (mean,-offsets),
                    bbox = bbox,
                    ha='center')

        if playerStats:
            pctile = norm.cdf(playerStats,mean,sd)
            prob = norm.pdf(playerStats,mean,sd)

            ax.annotate("Percentile (%s): %s"%(fieldStr,'{:.2%}'.format(pctile)),
                        (playerStats,prob+offsets),        
                        bbox = bbox,
                        ha='center')
            ax.fill_between(valList,dist, where=((valList >= valList[0]) & (valList <= playerStats)), color="lightblue", alpha=0.5)

            ax.annotate("Total %s: %d"%(fieldStr,playerStats),
                    (playerStats,prob/2),
                    xytext =(playerStats+(valList[-1]+valList[0])/50,prob/2),
                    bbox = bbox,
                    ha='left')
            ax.vlines(x=playerStats,ymin=min(dist),ymax = prob+offsets, color = "blue")
        ax.spines['bottom'].set_position('zero')
        ax.set(yticks = [],xticks = [])
        ax.spines[['right', 'top']].set_visible(False)

        return fig
        
