import matplotlib.pyplot as plt
import matplotlib.image as img
class ShotPctVisualizer:
    def __init__(self, shotTuple: tuple[int, int, float]) -> None:
        
        self.totalShots = shotTuple[0]
        self.totalGoals = shotTuple[1]
        self.shotPCT = shotTuple[2]
        self.colour = ["#ADD8E6","#90EE90"]
        self.label = ["Total Shot on Net", "Total Goal"]

    def piePlot(self):
        fig, ax = plt.subplots(figsize = (10,10))
        ax.pie(x=[self.totalShots - self.totalGoals, self.totalGoals], colors=self.colour, autopct='%.0f%%', labels=self.label)
        return fig