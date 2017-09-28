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
    # '00', \
    # '01', \
    # '02', \
    # '03', \
    # '04', \
    # '05', \
    # '06', \
    # '07', \
    # '08', \
    '09', \
    # '10', \
    ];

# cfgs = [
#     'poor/kitti_stereo_poor_00.cfg', \
#     'poor/kitti_stereo_poor_01.cfg', \
#     'poor/kitti_stereo_poor_02.cfg', \
#     'poor/kitti_stereo_poor_03.cfg', \
#     'poor/kitti_stereo_poor_04.cfg', \
#     'poor/kitti_stereo_poor_05.cfg', \
#     'poor/kitti_stereo_poor_06.cfg', \
#     'poor/kitti_stereo_poor_07.cfg', \
#     'poor/kitti_stereo_poor_08.cfg', \
#     'poor/kitti_stereo_poor_09.cfg', \
#     'poor/kitti_stereo_poor_10.cfg', \
#     ];

# cfgs = [
#     'orbslam2/kitti_stereo_orbslam2_00.cfg', \
#     'orbslam2/kitti_stereo_orbslam2_01.cfg', \
#     'orbslam2/kitti_stereo_orbslam2_02.cfg', \
#     'orbslam2/kitti_stereo_orbslam2_03.cfg', \
#     'orbslam2/kitti_stereo_orbslam2_04.cfg', \
#     'orbslam2/kitti_stereo_orbslam2_05.cfg', \
#     'orbslam2/kitti_stereo_orbslam2_06.cfg', \
#     'orbslam2/kitti_stereo_orbslam2_07.cfg', \
#     'orbslam2/kitti_stereo_orbslam2_08.cfg', \
#     'orbslam2/kitti_stereo_orbslam2_09.cfg', \
#     'orbslam2/kitti_stereo_orbslam2_10.cfg', \
#     ];

cfgs = [
    # 'perfect/kitti_stereo_perfect_00.cfg', \
    # 'perfect/kitti_stereo_perfect_01.cfg', \
    # 'perfect/kitti_stereo_perfect_02.cfg', \
    # 'perfect/kitti_stereo_perfect_03.cfg', \
    # 'perfect/kitti_stereo_perfect_04.cfg', \
    # 'perfect/kitti_stereo_perfect_05.cfg', \
    # 'perfect/kitti_stereo_perfect_06.cfg', \
    # 'perfect/kitti_stereo_perfect_07.cfg', \
    # 'perfect/kitti_stereo_perfect_08.cfg', \
    'perfect/kitti_stereo_perfect_09.cfg', \
    # 'perfect/kitti_stereo_perfect_10.cfg', \
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
