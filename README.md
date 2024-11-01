<h1>README</h1>

<h3>Description</h3>
This is a python script written with <a href=https://docs.python.org/3/library/tkinter.htmlr>Tkinter</a> designed to depict electric fields and equipotential lines, written as a bonus assignment for Physics C: Electricity & Magnetism. 

<h3>User Guide</h3>
The UI for this program should hopefully feel intuitive, but in case it is not: <br>
-Click to add a charge <br>
-Clicking on an exsisting charge will select it<br>
-Dragging a charge will um... drag it <br>
-Shift + Click to add a negative charge <br>
-Delete to delete the selected charge <br>
-Cmd(alt) + Click to draw an equipotential line <br>
<br>
Sliders:<br>
&nbsp; &nbsp; &nbsp; Field Densiity - the amount of field lines originating from each charge, (this should not be interpreted as the strength of the field)<br>
&nbsp; &nbsp; &nbsp; Magnitue - the relative magnitude of the charges<br>
&nbsp; &nbsp; &nbsp; Precision - the percision at which field lines are drawn (higher is more precise) (lower values can produce unintended results)<br>
<!-- Im so good at html -->

<h3>Screenshots</h3>
A single charge with maximum field density:
<img width="1235" alt="Screenshot 2024-10-31 at 7 33 04 PM" src="https://github.com/user-attachments/assets/930d4bd5-cbd3-4f89-945c-810e32292a3d">
A simple diople:
<img width="1235" alt="Screenshot 2024-10-31 at 7 17 37 PM" src="https://github.com/user-attachments/assets/d4bcd083-6161-44fe-8ae5-c259ce236bdc">
My attempt to draw a ghost using equipotential lines:
<img width="1237" alt="Screenshot 2024-10-31 at 7 20 11 PM" src="https://github.com/user-attachments/assets/fedf0843-cad1-4a8f-b551-b066bfa55ffc">

<h3>Know Issues</h3>
-Equipotential lines will sometimes fail to draw completely<br>
-Using the Magnitude slider without a charge selected will produce unitented results<br>
-Tkinter does not scale its pixels properly to (at least with my computer) the maximum aspect ratio available<br>
-This script has only been tested on a M2 Macbook, if you experience issues on your device file a ticket or smthn idunno<br>
-There are probably copious spelling errors in this README<br>

<h3>Potential Features</h3>
-Equipotential line permenace (currently they are cleared on any screen refresh, even though not all would require them to be redrawn)<br>
-An electric potential heatmap (the beginings of which can be seen under the <a href=https://github.com/dq1Mango/Electric-Fields/tree/experimental> expiremental branch</a>)<br>
-Whatever will get me more bonus points ;)
