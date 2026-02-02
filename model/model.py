import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.lista_anni = []
        self.lista_team = []
        self.lista_salari_per_ogni_id_team = []

    def get_all_year_team(self):
        self.lista_anni.clear()

        a = DAO.read_year_team()

        for n in a:
            anno = n['year']
            self.lista_anni.append(anno)

        return self.lista_anni

    def get_team(self, anno_selezionato):
        self.lista_team.clear()

        a = DAO.read_team()

        for n in a:
            if str(anno_selezionato) == str(n['year']):
                self.lista_team.append(n)

        return self.lista_team

    def get_id_team_salary(self):
        self.lista_salari_per_ogni_id_team.clear()

        a = DAO.read_id_team_salary()

        for n in a:
            self.lista_salari_per_ogni_id_team.append(n)

        return self.lista_salari_per_ogni_id_team

    def creazione_grafo(self):
        self.grafo.clear()

        # NODI
        nodi = []
        for n in self.lista_team:
            nodi.append(n['id'])

        self.grafo.add_nodes_from(nodi)

        # ARCHI
        mappa_salari = {}
        for n in self.lista_salari_per_ogni_id_team:
            id_squadra = n['idteam']
            valore_peso = n['peso']
            mappa_salari[id_squadra] = valore_peso

        for i in range(len(self.lista_team)):
            for j in range(i + 1, len(self.lista_team)):
                u = self.lista_team[i]
                v = self.lista_team[j]

                peso_u = mappa_salari.get(u['id'], 0)
                peso_v = mappa_salari.get(v['id'], 0)
                peso_tot = peso_u + peso_v

                self.grafo.add_edge(u['id'], v['id'], weight=peso_tot)

        return self.lista_team

    def get_adiacenti_ordinati(self, id_squadra):
        # 1. Recupero i vicini e il peso dell'arco che li collega
        # self.grafo.neighbors(n) restituisce i nodi adiacenti
        vicini_con_peso = []

        # Itero sugli archi incidenti al nodo selezionato
        for vicino in self.grafo.neighbors(id_squadra):
            peso = self.grafo[id_squadra][vicino]['weight']
            vicini_con_peso.append((vicino, peso))

        # 2. Ordino la lista per peso decrescente (il peso è in posizione index 1)
        vicini_con_peso.sort(key=lambda x: x[1], reverse=True)

        return vicini_con_peso