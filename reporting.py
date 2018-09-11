from entrolib import *
from os import walk, path
"""
reporting.py: A set of functions to create entropy reports.
"""
__author__    = "Pavel Chikul"
__copyright__ = "Copyright 2018, REGLabs"


class report:
    def __init__(self, quite = False):
        self.mute_console = quite

    def console_out(self, message):
        if not self.mute_console:
            print(message)

    def process_directory(self, in_path, out_file_name):
        """
        Creates an entropy report for a list of filesin directory and saves it in a CSV spreadsheet.
        """
        (_, _, file_list) = next(walk(in_path), (None, None, []))
        if out_file_name != "":
            with open(out_file_name, "w") as file_out:
                file_out.write("File Name;File Size (B);Entropy;Pi;Pi Deviation (%);Chi-Squared\r")

        self.console_out("%30s %15s %15s %15s %15s %15s" % ("File Name", "File Size (B)", "Entropy", "Pi", "Pi Deviation (%)", "Chi-Squared"))

        for file_name in file_list:
            byte_array = []
            with open(path.join(in_path, file_name), "rb") as f:
                byte_array = f.read()

            file_size = len(byte_array)
            entropy = compute_entropy(byte_array)
            new_pi = compute_monte_carlo_pi(byte_array)
            pi_deviation = get_pi_deviation(new_pi)
            chi_squared = compute_chi_squared(byte_array)

            if out_file_name != "":
                with open(out_file_name, "a") as file_out:
                    file_out.write("%s;%d;%f;%f;%f;%f\r" % (file_name, file_size, entropy, new_pi, pi_deviation, chi_squared))

            self.console_out("%30s %15d %15f %15f %15f %15f" % (file_name, file_size, entropy, new_pi, pi_deviation, chi_squared))
        