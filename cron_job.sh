#!/bin/bash
cd "$(dirname "$(realpath "$0")")";
. $HOME/miniconda3/bin/activate base
python job.py -c jobcfg.json >> survey_log.log
