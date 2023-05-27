# Data


## General Info

 
| <div style="width:80px">Name</div> | <div style="width:80px">Description</div> | <div style="width:80px">Value</div> |
| ----- |:---------------------|:----------------|
| ```slotMachineDrawCount``` | Bought bikes           | 35 |
| ```currency```             | Amount of current gems | -  |
| ```currentChallengeRuns```             | Amount of runs completed  | -  |
| ```lastCompletedChallengeIndex```             | Last completed challenge  | -  |
| ```currentCompleteRunsValue```             | for multipart challanges this is the value that keeps track of how many are completed (setting to max does not just complete challange next load) (there are 3 different values) | 0 |
| ```valueX``` and ```valueY```             | The 2nd value (like ```valueX```) in the challange (eg ```Collect between x and x gems in 1 run```, the first  ```x``` is ```valueX```, the second ```x``` is ```valueY```) (there are 3 different places where these values are found in the save file) | -  |
|              |  | -  |






<br>

## Specific Save Info

### Challenges (challengeTaskTimesCompleted)

fixed  
 
| <div style="width:150px">Challange number?</div> | <div style="width:80px">Name</div> | <div style="width:80px">Type</div> |<div style="width:200px">Description</div> |
| ----- |:---------------------|:---------------------|:----------------|
| 3 | ```ch3``` | fixed : 1 | Win a new bike |
| 4 | ```ch4``` | fixed : 1 | Win a new bike |
| 5 | ```ch5``` | fixed : 1 | Score x+ 2 times in a row |
| 6 | ```ch6``` | fixed : 1 | Collect x+ gems 2x |
| 7 | ```ch1``` | infinitive : 0 -> 1 | Collect between x and x gems in 1 run |
| 8 | ```ch2``` | infinitive : 1 | Score between x and x points 2x in a row |
| 9 | ```ch3``` | infinitive : 1 | Make x+ perfect flips in 2 runs |
| 10 | ```ch4``` | infinitive : 1 | Score x+ points in 1 run |
| 11 | ```ch5``` | infinitive : 1 | Collect x gems in 1 run |
| 12 | ```ch6``` | infinitive : 1 | Make x+ flips in 2 runs |
| 13 | ```ch7``` | infinitive : 1 | Score exactly x points in 1 run |
| 14 | ```ch8``` | infinitive : 1 | Collect x+ gems x games in a row |
| 15 | ```ch9``` | infinitive : 1 | Makes x+ perfect flips in 1 run |
| 16 | ```ch10``` | infinitive : 1 | Score between x and x points in 1 run |
| 17 | ```ch11``` | infinitive : 1 | Score x+ points 3x in a row |
| 18 | ```ch12``` | infinitive : 1 | Collect exactly x gems 3x |
| 19 | ```ch13``` | infinitive : 1 | Score x+ points 3x |
| 20 | ```ch14``` | infinitive : 1 | Collect x+ gems 1x |
| 21 | ```ch15``` | infinitive : 1 | Make x+ flips in 1 run |
| 22 | ```ch16``` | infinitive : 1 | Collect between x and x gems in 1 run |
| 23 | ```ch17``` | infinitive : 1 | Make x double flips in total |
| 24 | ```ch18``` | infinitive : 1 | Collect axactly x gems in 1 run |
| 25 | ```ch19``` | infinitive : 1 | Score x+ points 2x in a row |
| 26 | ```ch20``` | infinitive : 1 | Collect exactly x gems 2x |
| 27 | ```ch1``` | infinitive : 1 -> 2 | Collect between x and x gems in 1 run |
| 28 | ```ch2``` | infinitive : 1 -> 2 | Score between x and x points 3x in a row |
| 29 | ```ch3``` | infinitive : 1 -> 2 | Make x+ perfect flips in 3 runs |
| 29 | ```ch4``` | infinitive : 1 -> 2 | Score x+ points in 1 run |
| 30 | ```ch5``` | infinitive : 1 -> 2 | Collect x gems in 1 run |
| 31 | ```ch6``` | infinitive : 1 -> 2 | Makes x+ flips in 3 runs |
| 31 | ```--``` | infinitive : 1 -> 2 | Score exactly x points in 1 run |

### Unlocked Bikes (charactersTable)

| <div style="width:80px">Index</div> | <div style="width:80px">Rarity</div> | <div style="width:80px">Name/Info</div> |
|:----- |:---------------------|:----------------|
| 1     | common               | bike            |
| 2     | common               | racer           |
| 3     | epic                 | skeleton        |
| 4     | rare                 | fit             |
| 5     | epic                 | rider           |
| 6     | common               | suki            |
| 7     | epic                 | smooth          |
| 8     | rare                 | thrust          |
| 9     | rare                 | fox             |
| 10    | epic                 | claw            |
| 11    | common               | bmx             |
| 12    | epic                 | hood            |
| 13    | -                    | -               |
| 14    | rare                 | neon            |
| 15    | play 500             | derp            |
| 16    | -                    | -               |
| 17    | -                    | -               |
| 18    | common               | swift           |
| 19    | -                    | -               |
| 20    | common               | max             |
| 21    | play 50              | spoily          |
| 22    | common               | derby           |
| 23    | score 25             | blitz           |
| 24    | epic                 | batt            |
| 25    | common               | drift           |
| 26    | rare                 | airo            |
| 27    | rare                 | rally           |
| 28    | common               | moped           |
| 29    | -                    | -               |
| 30    | -                    | -               |
| 31    | challenge 25         | skate           |
| 32    | score 75             | golf            |
| 33    | score 100            | robin           |
| 34    | score 50             | outback         |
| 35    | -                    | -               |
| 36    | challenge 100        | tank            |
| 37    | secret               | rocket          |
| 38    | common               | trice           |
| 39    | -                    | -               |
| 40    | challenge 50         | cart            |
| 41    | rare                 | digi            |
| 42    | secret               | bullet          |
| 43    | secret               | hyper           |
| 44    | challenge 10         | jigawatt        |
| 45    | play 50000           | stripes         |
| 46    | -                    | -               |
| 47    | rare                 | buzzard         |
| 48    | secret               | spitfire        |
| 49    | common               | tokyo           |
| 50    | common               | harley          |
| 51    | rare                 | hawk            |
| 52    | rare                 | horus           |
| 53    | -                    | -               |
| 54    | rare                 | muscle          |
| 55    | common               | chopper         |
| 56    | common               | wire            |
| 57    | common               | flint           |
| 58    | epic                 | prime           |
| 59    | 10 Stars             | shell           |
| 60    | 20 Stars             | decall          |
| 61    | 40 Stars             | skull           |
| 62    | 75 Stars             | solar           |
| 63    | 125 Stars            | freedom         |
| 64    | epic                 | node            |
| 65    | epic                 | cyber           |
| 66    | rare                 | flow            |
| 67    | race                 | sprint          |
| 68    | race                 | dash            |
| 69    | race                 | surge           |
| 70    | race                 | rush            |

### Unlocked Themes (activeScapes)

| <div style="width:80px">Index</div> | <div style="width:120px">Background Color</div> | <div style="width:120px">Foreground Color</div> |
|:----- |:---------------------|:----------------|
| 1  | Dark Blue    | Pink/Purple   |
| 2  | Cyan         | Lime Green    |
| 3  | Purple       | Pink          |
| 4  | Red          | Yellow        |
| 5  | Gray         | Green         | 
| 6  | Dark Blue    | Green         |
| 7  | Merlot       | Light Blue    |
| 8  | Gray         | Yellow        |
| 9  | Cyan         | Yellow        |
| 10 | Cyan         | Green         |

