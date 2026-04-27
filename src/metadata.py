import os
import pandas as pd
from pathlib import Path
from utils import get_base_dir

class metadata:
    
# updated for cookiecutter use... good luck to us

    def __init__(self):
        self.cookiecutter_dir = '/projects/ag-bozek/sugliano/lunaphore'
        self.subfolders = {
            'images'      : 'data/raw',
            'bg_removed'  : 'data/interim/bg_removed',
            'illumination': 'data/interim/illumination_correction',
            'segmented'   : 'data/interim/segmented',
            'regionprops' : 'data/interim/regionprops'
        }

        self.folders = {
            k:os.path.join(self.cookiecutter_dir, v) 
            for k,v in self.subfolders.items()
        }
        
        for f in self.folders.values():
            if not os.path.exists(f):
                Path(f).mkdir(parents=True)

        self.markers = {
            'DAPI'  : 'DAPI',
            'cy5'   : 'Cy5 AF',
            'tritc' : 'TRITC AF',
            'c-myc' : 'c-Myc (Y69)',
            'ecad'  : 'E-Cadherin 36/E',
            'gfp'   : 'GFP D5.1',
            'vim'   : 'Vimentin V9',
            'ccasp' : 'Cleaved Caspase3 D175',
            'ki67'  : 'Ki67 MIB-1',
            'slug'  : 'SLUG C19G7',
            'ck'    : 'CK AE1/AE3',
            'fibro' : 'Fibronectin E5H6X'
        }

        self.marker_channels = {
            'DAPI'  : 'DAPI',
            'cy5'   : 'cy5',
            'tritc' : 'tritc',
            'c-myc' : 'cy5',
            'ecad'  : 'tritc',
            'gfp'   : 'cy5',
            'vim'   : 'tritc',
            'ccasp' : 'cy5',
            'ki67'  : 'tritc',
            'slug'  : 'cy5',
            'ck'    : 'tritc',
            'fibro' : 'cy5'
        }

        self.classification_colormap = {
            'triple_negative'   : '#333333',
            'e-cad_positive'    : '#A72C09',
            'vimentin_positive' : '#3A76DB',
            'double_positive'   : '#FF00FC'
        }

        self.classification_colormap_alt = {
            'triple_negative'   : '#333333',
            'e-cad_positive'    : '#2C72B8',
            'vimentin_positive' : '#2FBD45',
            'double_positive'   : '#32E5ED'
        }

