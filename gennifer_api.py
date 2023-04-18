import os
import pandas as pd

from arboreto.algo import grnboost2, genie3
from arboreto.utils import load_tf_names
from distributed import Client

DATASET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample_data')

def generateInputs(dataset_uri):
    return pd.read_csv(os.path.join(DATASET_PATH, dataset_uri), header=0, index_col=0)

def run(dataset):
    network = MAC_counter(data=inputExpr, max_lag_prop=maxLag, MAC_cutoff=0, file_name="temp", lag_matrix=False, symmetric=False)
    return network

def parseOutput(network):
    return network.to_json(orient='records')
