# movie-trailers
movie trailers project for udacity

I've modified the project a bit.
1.) I use jinja for the templating (it's seems inherently cleaner this way).
2.) I use a python list of dictionaries for storing all the movies.  This way the whole thing can
    be edited as JSON (also makes it more flexible for using as a json file in the future perhaps).
3.) To conform to the project guidelines, I iterate over each entry in the list and create a Movie
    object from it.
4.) I also added the storyline underneath the video of the trailer.

