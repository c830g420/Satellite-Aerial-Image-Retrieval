# Satellite-Aerial-Image-Retrieval

A program using Bing maps tile system to automatically download aerial imagery (maximum resolution available) given a lat/lon bounding box.

##Group Members Ziyu Liu (zliu102), Chen Gong (cgong2), Jing Chen

##Algorithm
Convert the Bing Tile System. Reference: https://msdn.microsoft.com/en-us/library/bb259689.aspx#Anchor_0
Iteratively paste a higher quality tile to the previous image until the Bing server could not provide better data.
The base canvas is created.
Choose the highest resoluation with which image have at least one side has only one tile as the starting point.
Increase the resolusion, iterate through all the tiles from the Bing Map server, and paste the better one to the correct position in the big canvas.
Repeat Step 3 until resolution of some data is null returned by the Server.

##Usage
python main.py lat1 lon1 lat2 lon2
Result will be saved as "THENAMEYOUCHOOSE.jpg" in the same directory.
lat1 lon1 lat2 lon2 will be saved as "THENAMEYOUCHOOSE" in the same directory.

##Caveat If the selected bonding box is too tiny, for example, the location is in the same tile even when the resolution is 23 (maximum), but Bing Map Tile System does not have data with 23 resolution for it, then the code does not generate the tile.
