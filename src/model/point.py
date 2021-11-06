class Point:
    def __init__(self, x, y, z = 0):
        self.coordinates = [[x, y, z]]
    
    def get_x(self):
        return self.coordinates[0][0]

    def get_y(self):
        return self.coordinates[0][1]

    def get_z(self):
        return self.coordinates[0][2]