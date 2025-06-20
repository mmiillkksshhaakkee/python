import matplotlib.pyplot as plt

class Circle(object):

    def __init__(self, radius=1, color='pink'):
        self.radius = radius
        self.color = color

    def add_radius(self, radius):
        self.radius += radius
        return self.radius

    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

class Rectangle(object):

    def __init__(self, width=2, height=3, color='r'):
        self.width = width
        self.height = height
        self.color = color

    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()

if __name__ == '__main__':
    DefCircle = Circle()
    GreenCircle = Circle(8, 'green')

    DefCircle.drawCircle()
    GreenCircle.drawCircle()

    DefRect = Rectangle()
    YellowRect = Rectangle(8, 9, 'yellow')

    DefRect.drawRectangle()
    YellowRect.drawRectangle()