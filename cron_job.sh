#!/bin/bash
. $HOME/miniconda3/bin/activate base
python job.py -c jobcfg.json >> survey_log.log
