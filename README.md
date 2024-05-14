# Budapesti Gazdasági Egyetem
## Üzleti Intelligencia
Mesterséges intelligencia alkalmazásai üzleti kontextusban. 

## Feldolgozott témák a kurzus alatt

- Bevezetés
1. Verziókezelés: `1_git_dok`
- Megerősítéses tanulás
2. Bevezetés a megerősítéses tanulásba: `2_reinforcement_learning`
3. Markov döntési folyamatok megoldása: `3_solving_mdp`
4. Sztochasztikus becslés: `4_mc_td`
5. Q-tanulás: `5_ql`
6. Megerősítéses mélytanulás: `6_dql`
- Mélytanulás
7. Bevezetés a mesterséges mélytanulásba: `7_dl`
8. Objektum detekció: `8_od`
9. Egyed szegmentáicó: `9_instance`
10. Visszacsatolásos neurális hálózatok: `10_recurrent`
11. Transzformáló archtiketkúrák: `11_transformer`

## Mappák struktúrája
A gyökérmappában található scriptek:  
- `merge_pdfs.py`: Konkatenálja az összes pdf-et egy dokumentummá a gyökérmappába.  
- `render_graph.py`: Renderel minden dot gráfot az összes mappában.  
- `render_pdf.py`: Renderel minden LaTeX fájlt pdf formátumba.  
    
Minden mappában két almappa található:  
- `code`: Esettanulány, ami megvalósítja a tanult témakört.  
- `doc`: Dokumentáció LaTeX és pdf formátumban.  
	- `images`: Diagramok és képek a dokumentációban. Itt megtalálható egy témának megfelelően elnevezeett Jupyter notebook, ami a képek generálásáért felelős. Az itt található programkód publikus és szabadon felhasználható az órai munka során.  
	- `graphs` (opcionális): Gráfok dot formátumban, amit a Graphviz szoftver segítségével lehet lerenderelni.   
