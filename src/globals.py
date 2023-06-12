import numpy as np

import company
import inspector
import report

COMPANIES_PATH = "input/companies.txt"
companies = list[company.Company]

INSPECTORS_PATH = "input/inspectors.txt"
inspectors = list[inspector.Inspector]

REPORTS_PATH = "input/reports.txt"
reports = list[report.Report]

loaded_measurement: None | np.ndarray = None
