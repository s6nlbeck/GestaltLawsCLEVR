def check_center_valid_similarity(centers, pos):
  return True
  #TODO Implemtnt


import random


def get_positions(num_objects,minx,maxx,miny,maxy):
  centers = []
  tries = 0
  x = random.uniform(minx, maxx)
  y = random.uniform(miny, maxy)
  for group in range(num_objects):
    x = random.uniform(minx, maxx)
    y = random.uniform(miny, maxy)
    while not check_center_valid_similarity(centers, (x, y)):
      x = random.uniform(minx, maxx)
      y = random.uniform(miny, maxy)
      tries = tries + 1
      if tries > 1000:
        print(
          "Number of groups and margin does not match. Please lower the number of groups or the margin of the groups")
        return get_positions(num_objects)
    centers.append((x, y))
  print("Centers", centers)
  return centers

print(get_positions(2,-3,3,-3,3))