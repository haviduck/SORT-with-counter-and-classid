# this is so not an example.. but you hopefully get the gist
# when you get your detections, do your stuff.
#
import sort
import tracker

sorter = sort()
history_tracker = ObjectTracker()

# yeah i yanked this out of a project. had to rename etc so probably bugged. i do mapping for object id to color etc, but thats in a utils file and im having an argument with that file at the moment.
# it has counting by tripline counting so added that. it might have remnants of other stuff so sorry bout that but then again not sorry



def getSortCoordinates(detections):
    object_list = []
    linep1 = (pt1x, pt1y)
    linep2 = (pt2x, pt2y)

    for label, confidence, detection in detections:
        det_type = label
        x, y, w, h = detection
        c = int(float(confidence))
        # map your own
        # dnum = det_type_to_number_mapping[det_type]
        xmin, ymin, xmax, ymax, c = getSorted(float(x), float(y), float(w), float(h), c)
        object_list.append([xmin, ymin, xmax, ymax, c, dnum])

    np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
    np1 = np.array(object_list)
    trackers = self.salm_sorter.update(np1)
    for d in trackers:
        d = np.array(d, dtype=np.float32)
        pt1 = (d[0], d[1])
        pt2 = (d[2], d[3])  # from here on out yuou know..
        pt1 = (d[0], d[1])
        pt2 = (d[2], d[3])
        obj_id = d[4]

        c_curr = (int(d[0] + abs(d[0] - d[2]) / 2), int(d[1] + abs(d[1] - d[3]) / 2))
        cv2.rectangle(img, linep1, linep2, (255, 255, 255), 1)
        tracker.set_trajectory(c_curr, int(obj_id), "classname")
        check = tracker.get_trajectory(int(obj_id), "classname")
        lastx = check[0][0]
        lasty = check[0][1]

        if (int(c_curr[0]) > int(pt1x)) and int(c_curr[0]) < int(pt2x):
            if (pt1y > c_curr[1]) and (pt1y < lasty):
                self.det_type_total[det_type_number].add(obj_id)
            circ_start = 1
            for cords in check:
                circ = circ_start + 3
                cv2.circle(img, cords, 2, color, circ)
            else:
                cv2.rectangle(img, pt1, pt2, color, 1)
                
                
                
def lotsofdetectionstuff():
    videothingie = cv2.videothingie()
    while videothingie isOpened:
        #lots of detection stuff
        image = getSortCoordinates(detections)
        
    #and so on
