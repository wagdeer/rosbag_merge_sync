import rosbag
import rospy
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog = 'rosbag_timeshift.py',
        description = 'Reset the timestamps of messages in a ROS bag using an offset')
    parser.add_argument('-o', type=str, help='name of the output file', default=None, metavar='output_file')
    parser.add_argument('-i', type=str, help='name of the input file', default=None, metavar='input_file')
    parser.add_argument('-s', type=float, help='output_time = input_time +/- shift_time', default=0, metavar='time_shift')
    args = parser.parse_args()
    print('output_file: ', args.o, 'input_file: ', args.i, 'timeshift: ', args.s)

    time_shift = rospy.Duration(args.s)

    with rosbag.Bag(args.o, 'w') as outbag:
        for topic, msg, t in rosbag.Bag(args.i, 'r').read_messages():
            ''' The logic here is that the timestamp in the message and 
                the timestamp of the message record are different, and the
                time shift should be handled separately. '''
            new_t = t + time_shift
            msg.header.stamp = msg.header.stamp + time_shift
            outbag.write(topic, msg, new_t)

    print('Done!')
