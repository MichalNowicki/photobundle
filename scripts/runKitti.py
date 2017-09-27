#
#	author: Michal Nowicki
#
from subprocess import call
import sys
import os
import fileinput


# Path to save main results - create if needed
if not os.path.exists("results"):
    os.makedirs("results");
else:
    call('rm results/*', shell=True);


sequences = [
    '00', \
    '01', \
    '02', \
    '03', \
    '04', \
    '05', \
    '06', \
    '07', \
    '08', \
    '09', \
    '10', \
    ];

cfgs = [
    'kitti_stereo_00.cfg', \
    'kitti_stereo_01.cfg', \
    'kitti_stereo_02.cfg', \
    'kitti_stereo_03.cfg', \
    'kitti_stereo_04.cfg', \
    'kitti_stereo_05.cfg', \
    'kitti_stereo_06.cfg', \
    'kitti_stereo_07.cfg', \
    'kitti_stereo_08.cfg', \
    'kitti_stereo_09.cfg', \
    'kitti_stereo_10.cfg', \
    ];

runsPerSequence = 1;


mainDatasetPath = '/mnt/data/Datasets/kitti/sequences';

print 'mainDatasetPath: ' + mainDatasetPath

# For all selected sequences
for seq, cfg in zip(sequences, cfgs):
    print("Current sequence: " + seq);

	# We call this command
    print('cp ../config/' + str(cfg) + ' ../config/kitti_stereo.cfg');

    # Run code
    call('cp ../config/' + str(cfg) + ' ../config/kitti_stereo.cfg', shell=True);

    # We call this command
    print('./run_kitti');

    # Run code
    call('./run_kitti', shell=True);

    # Copy results
    call('mv refined_poses.txt results/' + str(seq) + '.txt', shell=True);
