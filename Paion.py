#! /bin/python3

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

import sys
import calendar
import EventPanel
import CalendarGrid
from datetime import date
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter

class Paion(QMainWindow):
    dates = []
    month = -1
    year = -1

    def __init__(self, initialMonth, initialYear):
        assert type(initialMonth) == int and type(initialYear) == int
        super().__init__()

        self.month = initialMonth
        self.year = initialYear
        self.createDatesList()

        # Create UI
        gridWidget = CalendarGrid.CalendarGrid(self.dates)
        eventWidget = EventPanel.EventPanel()
        eventWidget.setMaximumWidth(self.width() / 1.2)

        splitter = QSplitter()
        splitter.setChildrenCollapsible(False)
        splitter.addWidget(gridWidget)
        splitter.addWidget(eventWidget)
        splitter.moveSplitter(self.width() / 1.3, 0)

        self.setCentralWidget(splitter)
        self.setWindowState(Qt.WindowMaximized)
        self.setStyleSheet("QMainWindow { background: #333333 }")

        self.show()

    def backward(self):
        if self.month - 1 < 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1

        self.createDatesList()

    def createDatesList(self):
        self.dates = calendar.monthcalendar(self.year, self.month)

    def forward(self):
        # Rollover to the next year if necessary
        if self.month + 1 > 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1

        self.createDatesList()
        self.resetProperties()


if __name__ == "__main__":
    app = QApplication(sys.argv)
#    app.setFont(QFont("Comfortaa", 13))
    window = Paion(date.today().month, date.today().year)
    sys.exit(app.exec_())
