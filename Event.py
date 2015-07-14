############################ Copyrights and License ##############################
#                                                                                #
# This file is part of Paion. http://github.com/JamesWrigley/paion/              #
#                                                                                #
# Paion is free software: you can redistribute it and/or modify it under         #
# the terms of the GNU General Public License as published by the Free Software  #
# Foundation, either version 3 of the License, or (at your option) any later     #
# version.                                                                       #
#                                                                                #
# Paion is distributed in the hope that it will be useful, but WITHOUT ANY       #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS      #
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. #
#                                                                                #
# You should have received a copy of the GNU General Public License along with   #
# Paion. If not, see <http://www.gnu.org/licenses/>.                             #
#                                                                                #
##################################################################################

from PyQt5.QtWidgets import QLabel, QVBoxLayout

class Event(QVBoxLayout):
    nameLabel = None
    location = ""
    notes = ""
    allDay = False

    def __init__(self, Name="", Location="", Notes="", AllDay=False):
        assert (type(Name) == str and type(Location) == str and
                type(Notes) == str and type(AllDay) == bool)
        super().__init__()

        self.nameLabel = QLabel(Name)
        self.location = Location
        self.notes = Notes
        self.allDay = AllDay

        self.nameLabel.setStyleSheet("QLabel { border: 1px solid black;"
                                     "border-left: 0px;"
                                     "border-right: 0px;"
                                     "font-size: 10px }")
        self.nameLabel.setWordWrap(True)
        self.addWidget(self.nameLabel)
