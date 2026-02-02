import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def populate_dd(self):
        """ Metodo per popolare il dropdown """
        # 1. Svuoto le opzioni attuali
        self._view.dd_anno.options.clear()

        # 2. Ottengo la lista
        lista_anni = self._model.get_all_year_team()

        # 3. Popolo il dropdown
        for anno in lista_anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(key=str(anno), text=str(anno)))

        self._view.update()

    def handle_team(self, e):
        anno_selezionato = self._view.dd_anno.value

        self._view.txt_out_squadre.controls.clear()

        lista_team = self._model.get_team(anno_selezionato)

        n_team = len(lista_team)

        self._view.txt_out_squadre.controls.append(ft.Text(f"Numero di squadre: {n_team} "))

        for n in lista_team:
            sigla = n['team_code']
            nome_team = n['name']
            self._view.txt_out_squadre.controls.append(ft.Text(f"{sigla} ({nome_team})"))

        self._view.update()

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        # 1. Recupero l'anno selezionato (serve al model per filtrare i team)
        anno_selezionato = self._view.dd_anno.value

        # 2. Carico i dati dal Model che lavorano per la costruzione del grafo
        self._model.get_team(anno_selezionato)
        self._model.get_id_team_salary()

        # POPOLA IL SECONDO DROPDOWN DOPO LA CREAZIONE
        self.populate_squadra()

        # 3. Creo il grafo in memoria
        self._model.creazione_grafo()

        # 4. Aggiorno la pagina per confermare l'interazione (senza stampare nulla)
        self._view.update()

    def populate_squadra(self):
        self._view.dd_squadra.options.clear()

        lista_team = self._model.lista_team

        for n in lista_team:
            self._view.dd_squadra.options.append(ft.dropdown.Option(key=str(n['id']), text=n['name']))

        self._view.update()


    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        # TODO
        # 1. Recupero l'id della squadra selezionata dal dropdown
        id_selezionato = self._view.dd_squadra.value

        # Converto l'ID in intero perché i nodi nel grafo sono int
        id_squadra = int(id_selezionato)

        # 2. Chiedo al model i vicini ordinati
        vicini_ordinati = self._model.get_adiacenti_ordinati(id_squadra)

        self._view.txt_risultato.controls.clear()

        # Creiamo una mappa veloce per mostrare i nomi invece dei soli ID
        mappa_nomi = {team['id']: team['name'] for team in self._model.lista_team}

        for vicino_id, peso in vicini_ordinati:
            nome_vicino = mappa_nomi.get(vicino_id, "Sconosciuto")
            self._view.txt_risultato.controls.append(
                ft.Text(f"-> {nome_vicino} | Peso: {peso}")
            )

        self._view.update()

    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO