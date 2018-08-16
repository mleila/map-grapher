import json
import urllib.request

try:
    __IPYTHON__
except NameError:
    import matplotlib
    matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from shapely.geometry import shape, MultiPolygon, LineString, MultiLineString

from .constants import GEOJSON_COUNTIES, GEOJSON_STATES, STATES_CODE, COLORS


def load_data(file):
    url = GEOJSON_STATES if file == 'states' else GEOJSON_COUNTIES
    url = urllib.request.urlopen(url)
    data = json.loads(url.read().decode(encoding = "ISO-8859-1"))
    return data

def get_county(data, target_state):
    county_feats = []
    feats = data['features']
    for feat in feats:
        state = feat['properties']['STATE']
        if STATES_CODE[state] == target_state:
            county_feats.append(feat)
    if county_feats:
        data['features'] = county_feats
        return data
    raise NameError('State {} does not exist'.format(target_state))

def load_map_data(map_name):
    if map_name == 'States':
        data = load_data('states')
    else:
        data = load_data('counties')
        data = get_county(data, map_name)
    return data

def adjacency_test(county1, county2):
    return not county1.intersection(county2).is_empty

def build_adjmat(data):
    features = data['features']
    nb_counties = len(features)
    idx_name_map = {}
    mat = []
    for idx in range(nb_counties):
        county_name = features[idx]['properties']['NAME']
        idx_name_map[idx] = county_name
        county_geo = shape(features[idx]['geometry'])
        lst = []
        for other_idx in range(nb_counties):
            other_geo = shape(features[other_idx]['geometry'])
            if adjacency_test(county_geo, other_geo):
                lst.append(1)
            else:
                lst.append(0)
        mat.append(lst)
    return mat

def color_map(data, vertex_color_pairs):
    features = data['features']
    for feat, pair in zip(features, vertex_color_pairs):
        color = COLORS[pair[1]]
        feat['properties']['color'] = color
    return data

def plot_map(data, map_title):
    fig, ax = plt.subplots(figsize=(8, 8))
    features = data['features']
    shapes = [shape(feat['geometry']) for feat in data['features']]
    properties = [feat['properties'] for feat in data['features']]
    polygons = MultiPolygon(shapes)
    for prop, polygon in zip(properties, polygons):
        facecolor = prop['color'] if 'color' in prop else 'gray'
        mpl_poly = Polygon(np.array(polygon.exterior), facecolor=facecolor, linewidth=5.0, alpha=0.5, edgecolor='black')
        ax.add_patch(mpl_poly)
    ax.relim()
    ax.autoscale()
    ax.axis('off')
    ax.set_title(map_title)
    return fig

def save_to_file(fig, fname):
    fig.savefig(fname)

