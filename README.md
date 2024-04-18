This repository provides a tool for merging multiple ROS bag files into a single bag file. 
---
Before merging ROS bags:
 1. Ensure timestamps are consistent:
If the timestamps of messages in the different ROS bags are not consistent, you will need to correct them before merging the bags. 
 1. You can use rosbag_timeshift.py to shift(seconds) timestamp of messages:  
```bash
    python rosbag_timeshift.py -o output.bag -i input.bag -s 10.0
```
Merge Multiple rosbags:  
1. To merge multiple ROS bags, use the following command:
```bash
    python merge.py -o output.bag -i input0.bag input1.bag
```
2. Then you can check the result by running:
```bash
    rqt_bag output.bag
```
---
Credits
---  
* [rosbag-tools](https://github.com/Kautenja/rosbag-tools)
