
stars
=====

Nasa: Astronomy Picture of the Day

Idea:

Scrape the images and metadata from NASA’s “Astronomy Picture of the Day” archive, and create a more visually appealing/functional website to display them.

Image Copyright:

From http://apod.nasa.gov/apod/lib/about_apod.html#srapply
“You may use NASA imagery, video, audio, and data files used for the rendition of 3-dimensional models for educational or informational purposes, including photo collections, textbooks, public exhibits, computer graphical simulations and Internet Web pages. This general permission extends to personal Web pages.”
“NASA should be acknowledged as the source of the material”

Developement Plan:

1. Scrape <a>s from http://apod.nasa.gov/apod/archivepix.html
2. Scrape images, timestamp and text for each page
3. wget images?
4. Create DB - Images (image_url, text, time)
5. Ruby rails web app?
6. Page design
