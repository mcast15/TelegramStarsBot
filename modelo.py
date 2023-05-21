from matplotlib import pyplot as plt
import PIL


class Modelo:

    def __init__(self):
        self.starcoords = dict()
        self.starlight = dict()
        self.starnames = dict()
        self.constellations = dict()
        self.__read_coords('files/stars.txt')
        self.__read_constellations()

    def __read_coords(self, filepath):
        file = open(filepath, 'r', encoding='utf-8')
        for star in file:
            starinfo = star.rstrip('\n').split(' ', maxsplit=6)
            x = float(starinfo[0])
            y = float(starinfo[1])
            henrydraper = starinfo[3]
            magnitude = float(starinfo[4])
            names = []
            if len(starinfo) > 6:  # En caso de que la estrella tenga nombre(s)
                names = starinfo[6].split("; ")
            self.starcoords[henrydraper] = (x, y)
            self.starlight[henrydraper] = magnitude
            for name in names:
                self.starnames[name] = henrydraper
        file.close()

    def __read_constellation(self, filepath, constellation_name):
        file = open(filepath, 'r', encoding='utf-8')
        self.constellations[constellation_name] = []
        for constellation in file:
            cons = constellation.rstrip('\n').split(',')  # Removemos el salto de línea
            self.constellations[constellation_name].append((cons[0], cons[1]))
        file.close()

    def __read_constellations(self):
        self.__read_constellation('files/constellations/Boyero.txt', 'BOYERO')
        self.__read_constellation('files/constellations/Casiopea.txt', 'CASIOPEA')
        self.__read_constellation('files/constellations/Cygnet.txt', 'CYGNET')
        self.__read_constellation('files/constellations/Geminis.txt', 'GEMINIS')
        self.__read_constellation('files/constellations/Hydra.txt', 'HYDRA')
        self.__read_constellation('files/constellations/OsaMayor.txt', 'OSA MAYOR')
        self.__read_constellation('files/constellations/OsaMenor.txt', 'OSA MENOR')
        self.__read_constellation('files/constellations/Cazo.txt', 'CAZO')

    def __plot_stars(self):
        x, y, s = [], [], []
        for star in self.starcoords:
            xi, yi = self.starcoords[star]
            x.append(xi)
            y.append(yi)
            s.append((5 / (self.starlight[star] + 2)) ** 2)

        fig = plt.figure(figsize=(12, 12))
        fig.patch.set_facecolor('#000000')

        ax = fig.add_subplot(1, 1, 1)
        ax.scatter(x, y, s=s, marker='s', c='white')
        ax.patch.set_facecolor('#000000')
        ax.patch.set_alpha(0.5)
        return fig, ax

    def __plot_constellation(self, name, fig, ax, color):
        for union in self.constellations[name]:
            p1, p2 = union
            x1, y1 = self.starcoords[self.starnames[p1]]
            x2, y2 = self.starcoords[self.starnames[p2]]
            line, = ax.plot([x1, x2], [y1, y2], c=color)
        line.set_label(name)
        ax.legend()
        return fig, ax

    def plot_stars_and_constellations(self):
        fig, ax = self.__plot_stars()
        colors = ['red', 'yellow', 'green', 'blue', 'cyan', 'magenta', 'white', '#FF5733']
        i = 0
        for constellation_name in self.constellations:
            fig, ax = self.__plot_constellation(constellation_name, fig, ax, colors[i])
            i += 1
        self.__save(fig, 'all.png')

    def plot_stars_and_constellation(self, constellation_name):
        fig, ax = self.__plot_stars()
        fig, ax = self.__plot_constellation(constellation_name, fig, ax, 'yellow')
        self.__save(fig, constellation_name + '.png')

    def plot_stars(self):
        fig, ax = self.__plot_stars()
        self.__save(fig, 'stars.png')

    def __save(self, fig, filename):
        path = 'generated/%s' % filename
        fig.savefig(path, facecolor=fig.get_facecolor(), edgecolor='none')
        im = PIL.Image.open(path)
        im = im.crop((150, 150, 1070, 1070))
        im.save(path, 'png')
