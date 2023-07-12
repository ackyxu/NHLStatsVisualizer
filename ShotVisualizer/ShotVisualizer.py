import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import seaborn as sns  

class ShotVisualizer:
    """
    Takes in a valid query (in list[dict]) for GamePlays
    """
    rinkImg = r"Resource\nhlrink.png"
    shotEvents = ['STOP', 'MISSED_SHOT','BLOCKED_SHOT', 'GOAL']
    def __init__(self, gamePlays: list[dict]):
        self.gamePlays = gamePlays


    def filterShotEvents(self):
        shotList = []
        for event in self.gamePlays:
            if event["playType"] in self.shotEvents:
                shotList.append(event)
        return shotList


    def filterShotEvents(self, playType: list[str] = None) -> list[dict]:
        shotList = []
        #default arg, where we want all the shot events
        if not playType:
            playType = self.shotEvents
        for event in self.gamePlays:
            if event["playType"] in playType:
                shotList.append(event)
        return shotList


    def rinkPlot(self,events: list[dict], graphType = None):
        cleanedEvents = self.processCoordinates(events)
        coorXs, coorYs  = [event["coorX"] for event in cleanedEvents],[event["coorY"] for event in cleanedEvents]
        eventType = [event["playType"] for event in cleanedEvents]
        im = img.imread(self.rinkImg)
        plt.figure(figsize = (10,10))
        plt.axis('off')

        
        if graphType in ["heat","HEAT","Heat"]:
            sns.kdeplot(x=coorYs, y=coorXs, fill=True, thresh=0.05,  alpha = 0.65)
            implot = plt.imshow(im, extent=(-42.5,42.5,0,100))    

        else:
            
            plt.scatter(x=coorYs, y=coorXs, c="r", s=60)
            plt.xlim(-42.5,42.5)
            plt.ylim(0, 100)
            plt.xticks(np.arange(-42.5,42.5+1,0.1))
            plt.yticks(np.arange(0, 100+1,0.1))
            implot = plt.imshow(im, extent=(-42.5,42.5,0,100))

    def processCoordinates(self, events: list[dict]):
        output = []
        for event in events:
            try:
                event["coorY"],event["coorX"]  = float(event["coorY"]),float(event["coorX"])
            except:
                print(event)
                break
            if event["coorX"] < 0:
                event["coorY"],event["coorX"] = -event["coorY"],-event["coorX"]
            output.append(event)

        return output