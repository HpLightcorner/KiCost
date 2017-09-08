# -*- coding: utf-8 -*-

__author__ = 'XESS Corporation'
__email__ = 'info@xess.com'

from .mouser import *

# Place information about this distributor into the distributor dictionary.
from .. import distributors
distributors.update(
    {
        'mouser': {
            'scrape': 'web',
            'label': 'Mouser',
            'order_cols': ['part_num', 'purch', 'refs'],
            'order_delimiter': ' ',
            'wrk_hdr_format': {
                'font_size': 14,
                'font_color': 'white',
                'bold': True,
                'align': 'center',
                'valign': 'vcenter',
                'bg_color': '#004A85'  # Mouser blue.
            }
        }
    }
)
