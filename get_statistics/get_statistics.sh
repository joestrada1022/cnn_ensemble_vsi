#!/bin/bash

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH
cd $SCRIPTPATH

python QUFVD_ds_initial_csv_readr.py --main_path /home/cslfiu/dev/cnn_vscf/NSF-REU-2024_VSCF/cnn_ensemble_vsi --csvs_folder statistics
python most_common_predicted_label_by_videos.py --main_path /home/cslfiu/dev/cnn_vscf/NSF-REU-2024_VSCF/cnn_ensemble_vsi --csvs_folder statistics
python percentage_video_level_devices.py --main_path /home/cslfiu/dev/cnn_vscf/NSF-REU-2024_VSCF/cnn_ensemble_vsi --csvs_folder statistics