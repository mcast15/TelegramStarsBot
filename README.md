<p> Astronomers collect lots of data about stars and there are many
catalogs that identify the locations of stars. In this assignment, you
will use data from a <a href="http://webviz.u-strasbg.fr/viz-bin/VizieR">star catalog</a> to
create a picture that plots the locations of stars. </p>

<p> Since a real data set often has some incorrect data and the
occasional field missing, a cleaned up catalog has been prepared for your
use in this assignment. The file <a href="https://github.com/miguelnietoa/StarsConstellations-Bot/blob/master/files/stars.txt"> stars.txt</a> contains one line for each
star that is represented in the catalog. The meaning of each field
(column) is described below.</p>

<ul> 

<li>The first three fields are the x, y and z coordinates for the
star. We will ignore the z coordinate, and use only the x and y
coordinates. Each axis in the coordinate system goes from -1 to +1,
and the centre point is 0,0. (See the figure below.)</li>

<li>The fourth field is the <a href="http://en.wikipedia.org/wiki/Henry_Draper_catalogue"> Henry
Draper</a> number, which is simply a unique identifier for the
star.</li>

<li>The fifth field is the <a href="http://en.wikipedia.org/wiki/Apparent_magnitude"> magnitude</a> (or brightness) of the star.</li>

<li>The sixth field is Harvard Revised number, another identifier. </li>

<li>The seventh field exists only for a small number of stars and is a
semicolon-separated list of names for a star. A star may have several
names.</li>

</ul>

<p>Two unique identifiers appear in the data because the star data has been
collected from different sources, and the catalogs have several different ways
to uniquely identify stars. The fields that you will need for this assignment
include the x and y coordinates, the magnitude, the Henry Draper number, and
the name (or names) of each star.</p>

<b>This problem is an adaptation of <a href="http://nifty.stanford.edu/2009/reid-starmap/starmap.html">[1]</a>.</b>