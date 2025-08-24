# Lap-time-simulations-
Data created when doing lap time simulations for the VUB Racing vehicle of 2025. Openlap en Optimumlap are used.


For openlap: 
  - in the a__Cars file the 2025 VUBRacing car is set as the file 'car'. This has to be changed following the simulation you want to do
  - In the a__Tracks file acceleration, skidpad, 2012 endurance and 2012 autocross can be vieuwed. There where problems with the autocross track when the power was too high.
  - To use OPenlap see videos from Michael: https://youtube.com/playlist?list=PLQiPsAzoaLqUtdVImOM4WjzoYrNUy7fve&si=8RVPn69e_F-R67Ug . And his projects github: https://github.com/mc12027

For optimumlap:
  - For optimumlap its best to see its manuel and play with it.
  - In results is a template, when you open this template it will open an excel. This excel has on the first sheet a comparing template. The second sheet is called "Optimumlap code" and this is the one that is interesting. After having exported the data in CSV (only one vehicle one track) add the data in this excel file. Change all the "." with "," and then insert 2 columns before all the data. Then copy and paste the 2 columns that are visible in the second sheet making sure that the "FS Event score" is at the same place. Now you have all simulated data in the same format as Openlap. 

Python:
  - In the python folder there are 4 scripts:
  -   - Gui matlab file reader --> reads the exported matlab files in a GUI, from which they can be exported. Make sure that you select to correct event type for the point calculation.
      - GUI punten --> This is a point scored calculator. Set the reference time (fastest time to go in the formula) to the desired value and then in the set the simulated times.
      - Matlab visualiser --> takes the raw CSV file from matlab and plots them, it is possible to plot more than one simulation to compare. It is best that you read the code to understand how it works like it should.
      - Battery capacity calculator --> takes raw CSV files from matlab and calculates the battery size and possible regen. This is very most likely wrong so yeah...

The optimisation route that I took was too optimise a parameter in Optimumlap with for example the "batch" run option. Then use that value in the Openlap software. 

If you are a VUB Racing student you may contact me (Tom Paquet) for more information or my simulated data.


