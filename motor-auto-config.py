"""
Script to read questionnaire and automatically load motor configurations
"""

from happi.backends.qs_db import QSBackend
import pmgr.pmgrobj
import pmgr.utilsPlus as up


qs = QSBackend('xcslu5817') # instance of questionnaire for given experiment
pmgr = pmgrobj.pmgrobj('ims_motor', 'xcs') # remove hard coded hutch

# Parse questionnaire: get dictionary of ims motors {PV : config}
exp_mot_configs = {} # dictionary of PVs/configs for given experiment
for PV in qs.db.keys():
    if 'MMS' in PV:
        exp_mot_configs[PV] = qs.db[PV]['stageidentity']

# Load configs with pmgr.utilsPlus
for PV in exp_mot_configs:
    up.setConfig(pmgr, PV, exp_mot_configs[PV])
    up.applyConfig(pmgr, PV)
