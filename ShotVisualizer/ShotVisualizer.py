import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import seaborn as sns

from ShotVisualizer.Graphs import Graphs  

class ShotVisualizer(Graphs):
    
    """
    Takes in a valid query (in list[dict]) for GamePlays
    """
    rinkImg = r"Resource\nhlrink.png"
    shotEvents = ['SHOT', 'MISSED_SHOT','BLOCKED_SHOT', 'GOAL']
    blueColours = ['darkturquoise','dodgerblue','cyan','powderblue','lightblue','skyblue','deepskyblue','cornflowerblue','royalblue']
    def __init__(self, gamePlays: list[dict]):
        self.gamePlays = gamePlays




    def filterShotEvents(self, playType: list[str] = None) -> list[dict]:
        shotList = []
        #default arg, where we want all the shot events
        if not playType:
            playType = self.shotEvents
        for event in self.gamePlays:
            if event["playType"] in playType:
                shotList.append(event)
        return shotList


    def rinkPlot(self, graphType = None):
        cleanedEvents = self.processCoordinates(self.gamePlays)
        coorXs, coorYs  = [event["coorX"] for event in cleanedEvents],[event["coorY"] for event in cleanedEvents]
        eventType = [event["playType"] for event in cleanedEvents]
        im = img.imread(self.rinkImg)

        fig, ax = plt.subplots(figsize = (10,10))
        ax.axis('off')
        ax.set_xlim(-42.5,42.5)
        ax.set_ylim(0, 100)
        ax.set_xticks(np.arange(-42.5,42.5+1,0.1))
        ax.set_yticks(np.arange(0, 100+1,0.1))
    
        if graphType in ["heat","HEAT","Heat"]:
            sns.kdeplot(x=coorYs, y=coorXs, fill=True, thresh=0.05,  alpha = 0.65, clip=((-42.5,42.5),(0,100)))
            implot = ax.imshow(im, extent=(-42.5,42.5,0,100))    

        else:
            
            ax.scatter(x=coorYs, y=coorXs, c="cornflowerblue", s=60)
            implot = ax.imshow(im, extent=(-42.5,42.5,0,100))

        return fig

    def ShotTypePie(self):
        
        fig, ax = plt.subplots(figsize = (10,10))
     
        freqDict = {}
        for event in self.gamePlays:
            if event["playTypeSec"] in freqDict:
                freqDict[event["playTypeSec"]] += 1
            else:
                freqDict[event["playTypeSec"]] = 1

        totalShots = sum(list(freqDict.values()))       
        ax.pie(x=list(freqDict.values()), wedgeprops=dict(width=0.5),startangle=-40, colors=self.blueColours)
        legends = [f'{l} {(100*s/totalShots):0.2f}%' for l,s in zip(list(freqDict.keys()), freqDict.values())]

        
        ax.legend(labels=legends,loc='lower center',ncol= 4,fontsize="large",prop={f"family":self.font['fontname']})

        return fig

    def processCoordinates(self, events: list[dict]):
        output = []
        for event in events:
            try:
                event["coorY"],event["coorX"]  = float(event["coorY"]),float(event["coorX"])
            except:
                print(event)
                break
            if event["coorX"] < 0:
                event["coorY"],event["coorX"] = event["coorY"],-event["coorX"]
            output.append(event)

        return output