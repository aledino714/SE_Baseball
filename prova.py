from database.dao import DAO

lista_team = [
    {'id': 2776, 'year': 2015, 'team_code': 'ARI', 'name': 'Arizona Diamondbacks'},
    {'id': 2777, 'year': 2015, 'team_code': 'ATL', 'name': 'Atlanta Braves'}
]

lista_salari_per_ogni_id_team = [
    {'idteam': 1918, 'peso': 14807000.0},
    {'idteam': 1919, 'peso': 11560712.0},
    {'idteam': 1920, 'peso': 10897560.0}
]

mappa_salari = {}
for riga in lista_salari_per_ogni_id_team:
    id_squadra = riga['idteam']
    valore_peso = riga['peso']
    mappa_salari[id_squadra] = valore_peso

print(mappa_salari)







