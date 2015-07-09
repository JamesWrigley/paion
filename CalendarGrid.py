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

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QLabel, QWidget, QGridLayout, QVBoxLayout

# A class for each cell of CalendarGrid
class Day(QFrame):
    isSelected = False
    isNull = False
    backgroundColor = "pink"
    defaultStylesheet = ""

    def __init__(self, day):
        assert type(day) == int or type(day) == str
        super().__init__()

        self.isNull = str(day) == "0"

        dayLabel = QLabel("" if self.isNull else str(day))

        mainVbox = QVBoxLayout()
        mainVbox.setAlignment(Qt.AlignCenter)
        mainVbox.addWidget(dayLabel)

        self.backgroundColor = "#319973" if self.isNull else "#6ED5AF"
        self.defaultStylesheet = "QFrame {{ background: {0}; font-size: 18px }}".format(self.backgroundColor)
        self.setStyleSheet(self.defaultStylesheet)
        self.setLayout(mainVbox)

    def enterEvent(self, event):
        if not self.isNull and not self.isSelected:
            self.setStyleSheet("QFrame { background: #84FFD2; font-size: 20px }")

    def leaveEvent(self, event):
        if not self.isNull and not self.isSelected:
            self.setStyleSheet(self.defaultStylesheet)

    def mousePressEvent(self, event):
        if not self.isNull:
            self.isSelected = not self.isSelected

            if self.isSelected:
                self.setStyleSheet("QFrame { background: #FFAAAA; font-size: 20px }")

    def mouseReleaseEvent(self, event):
        if not self.isNull and not self.isSelected:
            self.enterEvent(None)

class CalendarGrid(QWidget):
    def __init__(self, month):
        assert all(type(element) == list for element in month)
        super().__init__()

        mainLayout = QGridLayout()
        for i, week in enumerate(month):
            for j, day in enumerate(week):
                mainLayout.addWidget(Day(day), i, j)

        self.setLayout(mainLayout)
