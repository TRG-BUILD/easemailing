#!/bin/bash
. $HOME/miniconda3/bin/activate base
cd /srv/easemailing
python check_surveyresult.py -c jobcfg.json >> survey_log2.log