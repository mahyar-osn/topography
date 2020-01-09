import os
import argparse

import pandas as pd
import numpy as np
import open3d as o3d

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class ProgramArguments(object):
    pass


class PointCloudResampling(object):

    def __init__(self, input_filename, output_filename, factor):
        self._input_filename = input_filename
        self._output_filename = output_filename
        self._factor = factor

        self._pcd = None
        self._pcd_array_temp = None
        self._pcd_array_unique = None
        self._pcd_array_resampled = None
        self._pcd_resampled = None

        self._load_file()
        self._check_duplicate_rows()

    def _check_duplicate_rows(self):
        print("Removing duplicate rows and saving the new txt file.")
        print("This may take a while...")
        self._pcd_array_unique = np.unique(self._pcd_array_temp.get_values(), axis=0)
        filename, file_extension = os.path.splitext(self._input_filename)
        output_unique_file = filename + "_unique" + file_extension
        np.savetxt(output_unique_file, self._pcd_array_unique, delimiter=" ", fmt="%5f")
        print("")

    def _plot_regional_density(self):
        hist, edges = np.histogramdd(self._pcd_array_resampled[0:10000, :], normed=False)
        X, Y = np.meshgrid(edges[0][:-1], edges[1][:-1])
        fig = plt.figure()
        ax1 = fig.add_subplot(111, projection='3d')
        ax1.plot(self._pcd_array_resampled[0:10000, 0], self._pcd_array_resampled[0:10000, 1],
                 self._pcd_array_resampled[0:10000, 2], 'k.', alpha=0.3)
        for ct in [0, 2, 5, 7, 9]:
            cs = ax1.contourf(X, Y, hist[:, :, ct],
                              zdir='z',
                              offset=edges[2][ct],
                              level=100,
                              cmap=plt.cm.RdYlBu_r,
                              alpha=0.5)
        plt.colorbar(cs)
        plt.show()

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

    def resample(self):
        print("Saving the resampled file. This may take a while...")
        self._pcd_array_resampled = self._pcd_array_unique[0::self._factor]
        self._plot_regional_density()

    def save_resampled_file(self):
        np.savetxt(self._output_filename, self._pcd_array_resampled, delimiter=" ", fmt="%5f")

    def visualize(self):
        self._pcd_resampled = o3d.io.read_point_cloud(self._output_filename, format="xyz")
        o3d.visualization.draw_geometries([self._pcd_resampled])


def main():
    args = parse_args()
    if os.path.exists(args.input_file):
        if args.output_file is None:
            filename, file_extension = os.path.splitext(args.input_file)
            output_file = filename + "_resampled" + file_extension
        else:
            output_file = args.output_file

        if args.downsampling_factor is None:
            downsample_factor = 2
        else:
            downsample_factor = int(args.downsampling_factor)

        """ Resampling """
        PCR = PointCloudResampling(args.input_file, output_file, downsample_factor)
        PCR.resample()
        """ Saving the new file """
        PCR.save_resampled_file()
        """ Visualizing the new file """
        PCR.visualize()


def parse_args():
    parser = argparse.ArgumentParser(description="Downsampling of point cloud data.")
    parser.add_argument("input_file", help="Location of the input txt file.")
    parser.add_argument("--output_file", help="Location of the output downsampled txt file. "
                                              "[defaults to the location of the input file if not set.]")
    parser.add_argument("--downsampling_factor", help="A downsample factor to reduce the data file. "
                                                      "[default is 2.]")

    program_arguments = ProgramArguments()
    parser.parse_args(namespace=program_arguments)

    return program_arguments


if __name__ == '__main__':
    main()
