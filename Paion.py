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
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
                             QToolBar, QSplitter, QWidget, QSizePolicy)

class Paion(QMainWindow):
    year = -1
    month = -1
    dates = []

    def __init__(self, initialMonth, initialYear):
        assert type(initialMonth) == int and type(initialYear) == int
        super().__init__()

        self.month = initialMonth
        self.year = initialYear
        self.createDatesList()

        # Create UI
        leftSpacer = QWidget()
        leftSpacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        rightSpacer = QWidget()
        rightSpacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        monthLabel = QLabel(calendar.month_name[self.month])
        monthLabel.setObjectName("monthLabel")

        toolbar = QToolBar()
        toolbar.addWidget(leftSpacer)
        toolbar.addWidget(QPushButton(QIcon("icons/previous.svg"), ""))
        toolbar.addWidget(monthLabel)
        toolbar.addWidget(QPushButton(QIcon("icons/next.svg"), ""))
        toolbar.addWidget(rightSpacer)
        toolbar.setMovable(False)

        gridWidget = CalendarGrid.CalendarGrid(self.dates)
        eventWidget = EventPanel.EventPanel()
        eventWidget.setMaximumWidth(self.width() / 1.2)

        splitter = QSplitter()
        splitter.addWidget(gridWidget)
        splitter.addWidget(eventWidget)
        splitter.setChildrenCollapsible(False)
        splitter.moveSplitter(self.width() / 1.3, 0)

        self.addToolBar(toolbar)
        self.setCentralWidget(splitter)
        self.setWindowState(Qt.WindowMaximized)
        self.setStyleSheet("QMainWindow { background: #333333 }"
                           "QToolBar { background: #444444; border: 1px solid black; padding: 3px; spacing: 30px }"
                           "QLabel#monthLabel { font-size: 25px; color: #DBDBDB }"
                           "QPushButton { border: none; outline: none; icon-size: 35px}"
                           "QPushButton:hover { background-color: #393939 }"
                           "QPushButton:pressed { background-color: #303030 }")

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
