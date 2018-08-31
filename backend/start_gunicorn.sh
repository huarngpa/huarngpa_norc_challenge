#!/bin/bash

APPNAME=surveybackend
APPDIR=/home/ubuntu/huarngpa_norc_challenge/backend/$APPNAME/

LOGFILE=$APPDIR'gunicorn.log'
ERRORFILE=$APPDIR'gunicorn-error.log'

NUM_WORKERS=3

ADDRESS=0.0.0.0:8000

cd $APPDIR

source ~/.bashrc
source /home/ubuntu/huarngpa_norc_challenge/env/bin/activate

exec gunicorn $APPNAME.wsgi:application \
-w $NUM_WORKERS --bind=$ADDRESS \
--log-level=debug
