#!/bin/bash
. $HOME/miniconda3/bin/activate base
cd /srv/easemailing
python job.py -c jobcfg.json >> survey_log.log
