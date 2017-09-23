def travel_distance():
    total_distance = 0

    file_id = open("./parser/travel.log")
    content = file_id.readlines()
    file_id.close()

    for entry in content:
        frequency, travel_from, travel_to, distance = entry.split(",")

        # print ("processed: %s->%s (%s km): %s times" % (travel_from, travel_to, distance[:-1], frequency))
        total_distance += int(distance[:-1]) * int(frequency)

    print("Travelling distance is %i km" % total_distance)
