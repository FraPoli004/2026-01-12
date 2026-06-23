from model.model import Model

mdl = Model()
mdl.buildGraph(1950,2016)
print(f"Il grafo creato contiene {mdl.get_numnodi()} nodi e "
      f"{mdl.get_numarchi()} archi.")

##mdl.getInfoCompConnessa(1224)