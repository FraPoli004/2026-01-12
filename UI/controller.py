import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDsYears(self):
        anni = self._model.getAnni()
        for a in anni:
            self._view._ddAnno1.options.append(
                ft.dropdown.Option(text=a, data=a)
            )
            self._view._ddAnno2.options.append(
                ft.dropdown.Option(text=a, data=a)
            )
        self._view.update_page()


    def handleCreaGrafo(self,e):
        ai = self._view._ddAnno1.value
        af = self._view._ddAnno2.value

        if ai is None and af is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("inserire un range valido!!!", color="red"))
            self._view.update_page()
            return

        if ai is None or af is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("inserire un range valido!!!", color="red"))
            self._view.update_page()
            return

        ai = int(ai)
        af = int(af)

        if ai > af:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("inserire un valore minimo minore di quello massimo!!!", color="red"))
            self._view.update_page()
            return

        self._model.buildGraph(ai, af)

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("grafo creato correttamente", color="green"))
        self._view.txt_result.controls.append(ft.Text(f'il grafo ha {self._model.get_numnodi()} nodi'))


    def handleDettagli(self, e):
        pass

    def handleCerca(self, e):
        pass

