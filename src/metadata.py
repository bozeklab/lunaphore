import os
import pandas as pd
from pathlib import Path
from utils import get_base_dir

class metadata:
    
# updated for cookiecutter use... good luck to us

    def __init__(self):
        self.base_dir = get_base_dir()
        self.subfolders = {
            'images'      : 'data/raw',
            'bg_removed'  : 'data/interim/bg_removed',
            'illumination': 'data/interim/illumination_correction',
            'segmented'   : 'data/interim/segmented',
            'regionprops' : 'data/interim/regionprops'
        }

        self.folders = {k:os.path.join(self.base_dir, v) for k,v in self.subfolders.items()}

        
        for f in self.folders.values():
            Path(f).mkdir(exist_ok=True, parents=True)

        
        # self.markers = {
        #     # 'DAPI1':'DAPI',
        #     # 'tritc':'TRITC AF',
        #     # 'cy5'  :'Cy5 AF',
        #     'DAPI2':'DAPI', 
        #     'ecad' :'E-Cadherin 36E',
        #     'c-myc':'c-Myc (Y69)',
        #     'DAPI3':'DAPI', 
        #     'vim'  :'Vimentin V9',
        #     'gfp'  :'GFP D5.1',
        #     'DAPI4':'DAPI', 
        #     'ki67' :'Ki67 MIB-1',
        #     'ccasp':'Cleaved Caspase3 D175',
        #     'DAPI5':'DAPI', 
        #     'ck'   :'CK AE1/AE3',
        #     'slug' :'SLUG C19G7',
        #     # 'DAPI6':'DAPI',
        #     # 'fibro':'Fibronectin E5H6X'

        # }

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
            