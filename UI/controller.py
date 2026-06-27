import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDyears(self):
        years = self._model.get_all_years()

        self._view._ddAnno.options.clear()

        for year in years:
            self._view._ddAnno.options.append(
                ft.dropdown.Option(str(year))
            )

        self._view._ddAnno.value = None
        self._view.update_page()

    def filltxtOutSquadre(self, anno):
        self._view._txtOutSquadre.controls.clear()

        squadre = self._model.get_all_squadre()

        self._view._txtOutSquadre.controls.append(
            ft.Text(f"Numero squadre: {len(squadre)}")
        )

        for squadra in squadre:
            self._view._txtOutSquadre.controls.append(
                ft.Text(str(squadra))
            )

        self._view.update_page()

    def handleAnnoSelezionato(self, e):
        self._view._txtOutSquadre.controls.clear()
        self._view._ddSquadra.options.clear()

        anno = int(self._view._ddAnno.value)

        self._model.build_graph(anno) #devo chiamare questa altrimenti lista vuota

        squadre = self._model.get_all_squadre()

        self._view._txtOutSquadre.controls.append(
            ft.Text(f"Numero squadre: {len(squadre)}")
        )

        self._view._txtOutSquadre.controls.append(
            ft.Text("Elenco sigle squadre:")
        )

        for squadra in squadre:
            self._view._txtOutSquadre.controls.append(
                ft.Text(str(squadra))
            )

            self._view._ddSquadra.options.append(
                ft.dropdown.Option(
                    key=str(squadra.teamCode),
                    text=str(squadra),
                    data=squadra
                )
            )

        self._view._ddSquadra.value = None
        self._view.update_page()

    def handleCreaGrafo(self, e):

        self._view._txt_result.controls.clear()
        anno = self._view._ddAnno.value

        if anno is None:
            self._view.create_alert("Seleziona anno.")
            return




        n_nodi, n_archi = self._model.build_graph(anno)

        self._view._txt_result.controls.append(
            ft.Text("Grafo correttamente creato.")
        )



        self._view._txt_result.controls.append(
            ft.Text(f"Numero di nodi: {n_nodi}")
        )

        self._view._txt_result.controls.append(
            ft.Text(f"Numero di archi: {n_archi}")
        )

        self._view.update_page()

    def get_selected_item(self, dropdown):
        for option in dropdown.options:
            if str(option.key) == str(dropdown.value):
                return option.data
        return None

    def handleDettagli(self, e):
        self._view._txt_result.controls.clear()

        squadra = self.get_selected_item(self._view._ddSquadra) #recupero oggetto e non stringa

        if squadra is None:
            self._view._txt_result.controls.append(
                ft.Text("Attenzione, per usare questo metodo occorre selezionare una squadra.")
            )
            self._view.update_page()
            return

        viciniT = self._model.getViciniOrdinati(squadra)

        if len(viciniT) == 0:
            self._view._txt_result.controls.append(
                ft.Text("Nessun vicino trovato. Crea prima il grafo.")
            )
            self._view.update_page()
            return

        self._view._txt_result.controls.append(
            ft.Text(f"Squadre adiacenti a {squadra}:")
        )

        for vicino, peso in viciniT:
            self._view._txt_result.controls.append(
                ft.Text(f"{vicino} - peso: {peso}")
            )

        self._view.update_page()

    def handlePercorso(self, e):
        pass

