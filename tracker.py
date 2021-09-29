from collections import defaultdict, deque


class DetObject:
    def __init__(self):
        self.track = deque(maxlen=30)
        self.counted = False

    def add_coord(self, coord):
        if not self.counted:
            self.track.append(coord)

    def set_counted(self):
        self.counted = True

    def is_counted(self):
        return self.counted


class ObjectTracker:
    def __init__(self):
        self.dict_tracks = defaultdict(dict)

    def set_trajectory(self, center, track_id, class_name):
        track_id_str = str(track_id)
        # This function stores all tracked objects and their moving patterns
        if track_id_str not in self.dict_tracks[class_name]:
            self.dict_tracks[class_name][track_id_str] = DetObject()
        # append
        self.dict_tracks[class_name][track_id_str].add_coord(center)

        return self.dict_tracks[class_name][track_id_str].track

    def get_trajectory(self, track_id, class_name):
        track_id_str = str(track_id)
        return list(self.dict_tracks[class_name][track_id_str].track)

    def get_all_trajectories(self):
        return self.dict_tracks

    def get_class_trajectories(self, class_name):
        """returns a dict of {track_id_str: track} for given class_name"""
        return {
            track_id_str: self.get_trajectory(track_id_str, class_name)
            for track_id_str in self.dict_tracks[class_name]
        }

    def get_class_trajectory_ids(self, class_name):
        return list(self.dict_tracks[class_name].keys())

    def set_counted(self, track_id, class_name):
        """set counted for a given track_id of a given class_name"""
        track_id_str = str(track_id)
        self.dict_tracks[class_name][track_id_str].set_counted()

    def get_counted_for_class(self, class_name):
        """get a list of all track_id_str for all objects which are counted
        for a given class_name, using a list comprehension, and return the
        length of that list"""
        return len(
            [
                track_id_str
                for track_id_str, detobj in self.dict_tracks[class_name].items()
                if detobj.is_counted()
            ]
        )
