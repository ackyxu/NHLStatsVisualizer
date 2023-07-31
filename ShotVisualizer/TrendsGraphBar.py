from ShotVisualizer.Graphs import Graphs


class TrendsGraphBar(Graphs):
    def __init__(self, fig=None, ax=None):
        super().__init__(fig, ax)

    def CreateGraph(self, field: str, results: list[dict], playerStats: int | float | None = None):
        self.createTrendGraphBar(field,results,playerStats)


    def createTrendGraphBar(self, field: str, results: list[dict], playerStats: int | float | None = None):
        pass