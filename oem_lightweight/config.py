# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from easydict import EasyDict

C = EasyDict()
config = C

# image config
C.num_classes = 8
C.stats = {'mean': [0.4325, 0.4483, 0.3879], 'std': [0.0195, 0.0169, 0.0179]}
C.class_names = ["bareland", "rangeland", "developed space", "road", "tree", "water", "agriculture land", "buildings"]
C.class_colors = [[128, 0, 0],
                  [0, 255, 0],
                  [192, 192, 192],
                  [255, 255, 255],
                  [49, 139, 87],
                  [0, 0, 255],
                  [127, 255, 0],
                  [255, 0, 0]
                  ]

# eval config
C.use_tta = True # TTA evaluation
