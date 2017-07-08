# Visualize your Google location history in one map
This tool converts your Google location history data for use in a Google Fusion Table. This allows you to see your complete location history in a zoomable and interactive Google map. You can customize the visualization to your own preference in the map settings. In order to hide artifacts in the GPS data the code splits movement when locations are too far apart. The code was tested to work with six years of location history containing 1.4 million points.

![example](https://raw.githubusercontent.com/bouncer/locationhistory/master/example.png)


# Instructions

* Download your location history in JSON format via Google Takeout: https://www.google.com/settings/takeout
* Extract the JSON file and configure its location in generate.py
* Run generate.py using Python 2.7 and your location history will be transformed into a CSV file with connected coordinates
* Create a new Fusion Table in Google Drive and upload your history.csv file
* Go to the map tab to view your location history. Change the feature styles such as Line Color to an opacity of 5% to 10%
* Change the map to terrain view to improve visibility. You can share the map via Tools -> Publish

