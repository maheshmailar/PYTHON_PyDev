Pytest -s -v -m "regression" --html=./Reports/rpreg.html --capture sys -rP --capture sys -rF TestCases\ --browser chrome
Pytest -s -v -m "sanity" --html=./Reports/rpsanity.html --capture sys -rP --capture sys -rF TestCases\ --browser chrome