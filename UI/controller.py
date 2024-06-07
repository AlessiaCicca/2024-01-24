import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        ann="201"
        for i in range(5,9):
            anno=ann+str(i)
            self._view.ddyear.options.append(ft.dropdown.Option(f"{anno}"))
        metodi=self._model.metodi
        for metodo in metodi:
            self._view.ddmetodo.options.append(ft.dropdown.Option(f"{metodo.Order_method_type}"))



    def handle_graph(self, e):
        grafo = self._model.creaGrafo(self._view.ddmetodo.value, int(self._view.ddyear.value), float(self._view.txtS.value))
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        self._view.update_page()



    def handle_prodotti(self, e):
        redditizi=self._model.redditizi()
        self._view.txt_result.controls.append(ft.Text(f"I prodotti più redditizi sono"))
        for tupla in redditizi:
            self._view.txt_result.controls.append(ft.Text(f"Prodotto {tupla[0].Product_number}  Archi Entranti={tupla[1]} Ricavo={tupla[2]}"))
        self._view.update_page()



    def handle_path(self, e):
        pass
