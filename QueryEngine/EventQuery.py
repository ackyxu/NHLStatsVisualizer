from QueryEngine.InfoQuery import InfoQuery
from QueryEngine.QueryEngine import QueryEngine


class EventQuery(InfoQuery):
    selectFrom = " SELECT * FROM GamePlays"
    def __init__(self, qe: QueryEngine):
        super().__init__(qe)

    