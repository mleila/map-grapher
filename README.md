# map_grapher
Vertex Coloring is a well known problem in Operations Research where the goal is to find the minimum number of colores required to color vertices of an undirected graph such that no two adjacent vertices have the same color.

Coloring maps is a famous application of the vertex cologing problem. Maps can be modeled as undirected graph where vertices represent bordered entities. If two entities are adjacent in the map, their corresponding vertices are connected by an edge.

This package provides an easy interface to model US national and state maps as an undirected graph represented by an adjacency matrix. The graph model can be passed to an external solver to obtain a solution. The package will then reconstruct a colored map from the solution.

# Install
```bash
git clone https://github.com/mleila/map-grapher
pip install -e map-grapher
```

# Usage
import the library

```python
from map_grapher.core import load_map_data, plot_map, color_map, save_to_file, build_adjmat
```
choose a map
```
map_name = 'Arizona'
arizona = load_map_data(map_name) #map data
```

model as an undirected graph
```
matrix = build_adjmat(arizona)
print(matrix)

> [[1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
 [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
 [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
 [1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
 [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
 [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
 [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
 [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
 [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
 [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
 [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
 [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
 [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1]]
```

save the map as a png file
```python
fig = plot_map(arizona, 'Arizona')
save_to_file (fig, 'arizona')
```
