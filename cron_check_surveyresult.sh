#!/bin/bash
cd "$(dirname "$(realpath "$0")")";
. $HOME/miniconda3/bin/activate base
python check_surveyresult.py -c jobcfg.json >> survey_log2.log