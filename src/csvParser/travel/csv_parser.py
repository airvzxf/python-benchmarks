#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Parser CSV with csv module"""

import csv


def csv_parser():
    """This function open the log file and split by commas, then it count the total distances traveled"""
    total_distance = 0

    file_id = open("./travel/travel.log")
    content = file_id.readlines()
    file_id.close()

    for entry in csv.reader(content):
        frequency, travel_from, travel_to, distance = entry

        # print ("processed: %s->%s (%s km): %s times" % (travel_from, travel_to, distance, frequency))
        total_distance += int(distance) * int(frequency)

    print("Travelling distance is %i km" % total_distance)
