# Traffic-Signal-Optimization

Aim : <br>
Our aim is to develop a program which will modifiy traffic signal timer according to live density of traffic.

Uniquness : <br>
We are using Python, OpenCV to track density of vehicles and after appling some calculation it will produce best suitable time to manage road traffic.
It help to manage road traffic and people don't need to wait unnecessary.

Working : <br>
by using camera program will capture and process every frame by using background Substraction method (Gaussian Mixture-based Background/Foreground Segmentation Algorithm) and to remove frame noise by MOG it will able to track vehicle and road density....


# Setup
<h3>Use <a href="https://github.com/Aman-Khan/Traffic-Signal-Optimization/blob/main/setup.py">setup.py</a> file to set coordinates of road</h3>
&nbsp&nbsp&nbsp&nbsp -- Run Program capture any frame(to capture frame press s) to mark coordinates. <a href="https://github.com/Aman-Khan/Traffic-Signal-Optimization/blob/main/data/1.1_setup.png">Setup Image 1.01</a> <br>
&nbsp&nbsp&nbsp&nbsp  -- Captured frame will open automatically start marking coordinate(can only mark 4 coodinates) <a href="https://github.com/Aman-Khan/Traffic-Signal-Optimization/blob/main/data/1.2_setup.png">Setup Image 1.02</a> <br>
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp [Left bottom, Left Top, Right Top, Right bottom]

<h3><a href="https://github.com/Aman-Khan/Traffic-Signal-Optimization/blob/main/signalOptimize.py">signalOptimize.py</a></h3>
&nbsp&nbsp&nbsp&nbsp -- <a href="https://github.com/Aman-Khan/Traffic-Signal-Optimization/blob/main/data/1.3_setup.png">Red Signal</a><br>
&nbsp&nbsp&nbsp&nbsp -- <a href="https://github.com/Aman-Khan/Traffic-Signal-Optimization/blob/main/data/2.1_setup.png">Green Signal</a>
<br><br>
contributor <br>
ig - @_.demon0804._ <br>
ig - @eww.dex <br>
<br>
special thanks <br>
ig - @codewithkiran_
