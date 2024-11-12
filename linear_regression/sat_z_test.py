import pandas as pd
import sys
import logging
import math
from colorama import Fore, Style

if len(sys.argv) != 2:
    raise Exception("File path not provided")

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_path = sys.argv[1]
data_frame = pd.read_csv(file_path)
sat_series = data_frame["SAT"]

logging.info(f"Data describe: {data_frame.describe()}")
sat_actual_mean = 1845.273810
sat_std = 104.530661
sat_standard_error = sat_std/math.sqrt(sat_series.size)

# Null Hypothesis: SAT mean is 1843
sat_hypothesis_mean = 1825

z_test_result = (sat_actual_mean - sat_hypothesis_mean)/sat_standard_error
logging.info(f"Z Test result: {z_test_result}")

# With significance level of 0.01 (alpha=0.01) (alpha/2=0.005) (t-value=2.5758)
if z_test_result <= 2.5758 and  z_test_result >= -2.5758:
    logging.info(f"Z test {Fore.LIGHTGREEN_EX}pass{Style.RESET_ALL} with significance level of 0.01")
else:
    logging.info(f"Z test {Fore.LIGHTRED_EX}fail{Style.RESET_ALL} with significance level of 0.1")

# With significance level of 0.05 (alpha=0.05) (alpha/2=0.025) (t-value=1.96)
if z_test_result <= 1.96 and  z_test_result >= -1.96:
    logging.info(f"Z test {Fore.LIGHTGREEN_EX}pass{Style.RESET_ALL} with significance level of 0.05")
else:
    logging.info(f"Z test {Fore.LIGHTRED_EX}fail{Style.RESET_ALL} with significance level of 0.05")

# With significance level of 0.1 (alpha=0.1) (alpha/2=0.05) (t-value=1.6449)
if z_test_result <= 1.6449 and z_test_result >= -1.6449:
    logging.info(f"Z test {Fore.LIGHTGREEN_EX}pass{Style.RESET_ALL} with significance level of 0.1")
else:
    logging.info(f"Z test {Fore.LIGHTRED_EX}fail{Style.RESET_ALL} with significance level of 0.1")
