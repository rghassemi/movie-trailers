import jinja2
import webbrowser
import os


templateLoader = jinja2.FileSystemLoader( searchpath="" )
templateEnv = jinja2.Environment( loader=templateLoader )

movies = [
          {"title": "The Girl with the Dragon Tattoo",
           "storyline": "A journalist is aided in his search for a woman who has been missing -- or dead -- for forty years by a young female hacker.",
           "poster_image_url": "http://upload.wikimedia.org/wikipedia/en/a/ae/Men_Who_Hate_Women.jpg",
           "trailer_youtube_url": "RL8LI-h2WFc"
          },

          {"title": "The Girl who Played with Fire",
           "storyline": "As computer hacker Lisbeth and journalist Mikael investigate a sex-trafficking ring, Lisbeth is accused of three murders, causing her to go on the run while Mikael works to clear her name.",
           "poster_image_url": "http://upload.wikimedia.org/wikipedia/en/a/ae/The_Girl_Who_Played_with_Fire.jpg",
           "trailer_youtube_url": "VdwvAvXUxc4"
          },

          {"title": "The Girl who Kicked the Hornet's Nest",
           "storyline": "Lisbeth is recovering in a hospital and awaiting trial for three murders when she is released. Mikael must prove her innocence, but Lisbeth must be willing to share the details of her sordid experiences with the court.",
           "poster_image_url": "http://upload.wikimedia.org/wikipedia/en/7/70/The_Girl_Who_Kicked_the_Hornets%27_Nest_%28film%29.jpg",
           "trailer_youtube_url": "8fccRlpFuLo"
          }
        ]

class Movie(object):
    def __init__(self, data):
        self.title = data['title']
        self.storyline = data['storyline']
        self.poster_image_url = data['poster_image_url']
        self.trailer_youtube_url = data['trailer_youtube_url']


class MovieTrailers(object):
    def __init__(self,
                 data,
                 output_file="output.html",
                 output_path=None,
                 template_file="fresh_tomatoes_template.html",
                 template_path=""):

        #  If no path is provided, assume the current working directory
        self.path = output_path
        if not self.path:
            self.path = os.getcwd()
        # set the output file
        self.output_file = os.path.join(self.path, output_file)

        # Load the template
        self.template_path = template_path
        self.template_file = template_file
        self.template_loader = jinja2.FileSystemLoader(searchpath=self.template_path)
        self.template_environment = jinja2.Environment(loader=self.template_loader)
        self.template = self.template_environment.get_template(self.template_file)

        self.movies = []

        for entry in data:
            self.movies.append(Movie(entry))

    def create_page(self):
        with open(self.output_file, "w") as out:
            out.write(self.template.render(movies=self.movies))

    def open_page(self):
        webbrowser.open('file://%s' % self.output_file)


if __name__ == "__main__":
    fresh_tomatoes = MovieTrailers(movies)
    fresh_tomatoes.create_page()
    fresh_tomatoes.open_page()


