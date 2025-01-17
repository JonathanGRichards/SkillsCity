class Room():
  def __init__(self, room_name):
    self._name = room_name
    self._description = None
  @property
  def description(self):
    return self._description
  @description.setter
  def set_description(self, room_description):
    self._description = room_description
