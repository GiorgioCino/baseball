import networkx as nx

from database.DAO import DAO


class Model:


    def __init__(self):
        self._all_years = DAO.getAllYears()
        self._all_teams = DAO.getAllTeams()
        self._id_map_teams = {}
        for team in self._all_teams:
            self._id_map_teams[team.teamCode] = team
        self._graph = nx.Graph()

    def build_graph(self, anno):
        self._graph.clear()

        nodes = DAO.getAllNodes(anno, self._id_map_teams)
        self._graph.add_nodes_from(nodes)

        salari = DAO.getSalariSquadre(anno)

        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):

                squadra1 = nodes[i]
                squadra2 = nodes[j]

                salario1 = 0
                salario2 = 0

                if squadra1.teamCode in salari:
                    salario1 = salari[squadra1.teamCode]

                if squadra2.teamCode in salari:
                    salario2 = salari[squadra2.teamCode]

                peso = salario1 + salario2

                self._graph.add_edge(squadra1, squadra2, weight=peso)

        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def get_all_years(self):
        return list(self._all_years)

    def get_all_squadre(self):
        return list(self._graph.nodes)

    def getViciniOrdinati(self, squadra):
        if not self._graph.has_node(squadra):
            return []

        viciniT = []

        for v in self._graph.neighbors(squadra):
            peso = self._graph[squadra][v]["weight"]
            viciniT.append((v, peso))

        viciniT.sort(key=lambda x: x[1], reverse=True)

        return viciniT


