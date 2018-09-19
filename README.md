# Satellite-Aerial-Image-Retrieval

A program using Bing maps tile system to automatically download aerial imagery (maximum resolution available) given a lat/lon bounding box.

## Group Members 
* * *

## Algorithm
Convert the Bing Tile System. 
Iteratively paste a higher quality tile to the previous image until the Bing server could not provide better data.
1. The base canvas is created.
2. Find starting 4 tiles, as below:
<table>
  <tr>
    <td colspan=4 style="background: white; border: none">lat1</td>
  </tr>
  <tr>
    <td rowspan=2>lon1</td>
    <td >Tile</td>
    <td>Tile</td>
    <td rowspan=2>lon2</td>
  </tr>
  <tr>
    <td>Tile</td>
    <td>Tile</td>
  </tr>
  <tr>
    <td colspan=4 style="background: white; border: none">lat2</td>
  </tr>
</table>
<ul> 
  <li>the lat, lon cells represent the lat/lon border line</li>
  <li>the tile cells represent the staellite image tile</li>
</ul>
3. Increase the resolusion, iterate through all the tiles from the Bing Map server, and paste the better one to the correct position in the big canvas.
4. Repeat Step 3 until resolution of some data is null returned by the Server.

## Usage
```
python main.py lat1 lon1 lat2 lon2
```
* Result will be saved as "THENAMEYOUCHOOSE.jpg" in the same directory.
* lat1 lon1 lat2 lon2 will be saved as "THENAMEYOUCHOOSE" in the same directory.

## Caveat 
If the selected bonding box is too tiny, for example, the location is in the same tile even when the resolution is 23 (maximum), but Bing Map Tile System does not have data with 23 resolution for it, then the code does not generate the tile.

## Reference
[Bing Tile System](https://msdn.microsoft.com/en-us/library/bb259689.aspx#Anchor_0)
