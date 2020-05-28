import os

import pandas as pd
import numpy as np
import math
import rtree
import open3d as o3d


class PointCloudResampling(object):

    def __init__(self):
        self._input_filename = None
        self._output_filename = None
        self._factor = None
        self._output_directory = None

        self._pcd = None
        self._pcd_array_temp = None
        self._pcd_array_unique = None
        self._pcd_array_resampled = None
        self._pcd_resampled = None

        self._original_max = None
        self._original_min = None
        self._original_size = None
        self._resampled_max = None
        self._resampled_min = None
        self._resampled_size = None

    def set_input_file(self, input_file):
        self._input_filename = input_file

    def set_output_location(self, output_location):
        self._output_directory = output_location

    def set_factor(self, factor):
        self._factor = int(factor)

    def get_original_size(self):
        return self._original_size

    def get_original_max(self):
        return self._original_max

    def get_original_min(self):
        return self._original_min

    def get_resampled_size(self):
        return self._resampled_size

    def get_resampled_max(self):
        return self._resampled_max

    def get_resampled_min(self):
        return self._resampled_min

    def get_result_report(self):
        index = ['Original', 'Resampled']
        column = ['Size', 'Min', 'Max']
        data = np.asarray([
            [self._original_size, self._original_min, self._original_max],
            [self._resampled_size, self._resampled_min, self._resampled_max]
        ])
        result_array = pd.DataFrame(data, index=index, columns=column)
        result_array.to_csv(os.path.join(self._output_directory, 'Resampled_Report.csv'), sep=',')

    def _check_duplicate_rows(self):
        print("Removing duplicate rows and saving the new txt file...")
        self._pcd_array_unique = np.unique(self._pcd_array_temp.values, axis=0)
        filename, file_extension = os.path.basename(self._input_filename).split('.')
        output_unique_file = filename + "_unique." + file_extension
        np.savetxt(os.path.join(self._output_directory, output_unique_file),
                   self._pcd_array_unique,
                   delimiter=" ",
                   fmt="%5f")
        self._pcd_unique = o3d.io.read_point_cloud(os.path.join(self._output_directory, output_unique_file),
                                                   format="xyz")

        self._original_size = self._pcd_array_unique.shape[0]
        self._original_min = self._pcd_array_unique[:, 2].min()
        self._original_max = self._pcd_array_unique[:, 2].max()
        print("")

    @staticmethod
    def dist(p, q):
        """
        Return the Euclidean distance between points p and q.
        """
        return math.hypot(p[0] - q[0], p[1] - q[1])

    def _local_resample(self):

        print("")
        print("Local resampling. This may take a while...")

        r = self._factor

        data = self._pcd_array_unique

        result = []
        index = rtree.index.Index()

        for i, p in enumerate(data):
            px, py, pz = p
            nearby = index.intersection((px - r, py - r, px + r, py + r))
            if all(self.dist(p, data[j]) >= r for j in nearby):
                result.append(p)
                index.insert(i, (px, py, px, py))

        resampled_array = np.asarray(result)
        self._resampled_size = resampled_array.shape[0]
        self._resampled_min = resampled_array[:, 2].min()
        self._resampled_max = resampled_array[:, 2].max()

        return resampled_array

    def _load_file(self):
        if os.path.exists(self._input_filename):
            print("")
            print("Loading txt file...")
            self._pcd = o3d.io.read_point_cloud(self._input_filename, format="xyz")
            self._pcd_array_temp = pd.read_csv(self._input_filename, header=None, sep=" ")
        else:
            raise FileNotFoundError("Input txt file not found! Please check the path and try again.")
        print("Txt file loaded! ")
        print("")
        self._check_duplicate_rows()

    def resample(self):
        self._load_file()
        self._pcd_array_resampled = self._local_resample()
        self._save_resampled_file()

    def _save_resampled_file(self):
        print("Saving the resampled file. This may take a while...")
        filename, file_extension = os.path.basename(self._input_filename).split('.')
        output_unique_file = filename + "_resampled_at_{}_factor.".format(str(self._factor)) + file_extension
        np.savetxt(os.path.join(self._output_directory, output_unique_file),
                   self._pcd_array_resampled,
                   delimiter=" ",
                   fmt="%5f")

        self._pcd_resampled = o3d.io.read_point_cloud(os.path.join(self._output_directory, output_unique_file),
                                                      format="xyz")

        print("Saved!")

    def view_original(self):
        o3d.visualization.draw_geometries([self._pcd_unique])

    def view_resampled(self):
        o3d.visualization.draw_geometries([self._pcd_resampled])
