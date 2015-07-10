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

"""
The main window.
Methods of note:
 - Paion(int, int), the constructor, which takes a month and a year to start with
 - backward(), goes back one month
 - forward(), goes forward one month
 - refresh(), refreshes the grid and date label in the toolbar (called by backward() and forward())
 - resetMonth(), resets the program to the current month and year
"""
class Paion(QMainWindow):
    year = -1
    month = -1
    dates = []
    gridWidget = None
    monthLabel = None

    def __init__(self, initialMonth, initialYear):
        assert type(initialMonth) == int and type(initialYear) == int
        super().__init__()

        self.month = initialMonth
        self.year = initialYear

        # Create UI
        leftSpacer = QWidget()
        leftSpacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        rightSpacer = QWidget()
        rightSpacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.monthLabel = QPushButton(calendar.month_name[self.month])
        self.monthLabel.setObjectName("monthLabel")
        self.monthLabel.clicked.connect(self.resetMonth)

        previousButton = QPushButton(QIcon("icons/previous.svg"), "")
        nextButton = QPushButton(QIcon("icons/next.svg"), "")
        previousButton.clicked.connect(self.backward)
        nextButton.clicked.connect(self.forward)
        toolbar = QToolBar()
        toolbar.addWidget(leftSpacer)
        toolbar.addWidget(previousButton)
        toolbar.addWidget(self.monthLabel)
        toolbar.addWidget(nextButton)
        toolbar.addWidget(rightSpacer)
        toolbar.setMovable(False)
        toolbar.setContextMenuPolicy(Qt.PreventContextMenu) # Disable the toolbar context menu (which hides the toolbar)

        self.gridWidget = CalendarGrid.CalendarGrid()
        self.refresh()

        eventWidget = EventPanel.EventPanel()
        eventWidget.setMaximumWidth(self.width() / 1.2)

        splitter = QSplitter()
        splitter.addWidget(self.gridWidget)
        splitter.addWidget(eventWidget)
        splitter.setChildrenCollapsible(False)
        splitter.setSizes([self.width() / 4 * 3, self.width() / 4])

        self.addToolBar(toolbar)
        self.setCentralWidget(splitter)
        self.setWindowState(Qt.WindowMaximized)
        self.setStyleSheet("QMainWindow { background: #333333 }"
                           "QScrollArea { border: 0px solid black; }"
                           "QWidget#eventPanelWidget { background: #333333 }"
                           "QToolBar { background: #444444; border: 1px solid black; spacing: 30px }"
                           "QPushButton { border: none; outline: none; icon-size: 35px}"
                           "QPushButton:hover { background-color: #393939 }"
                           "QPushButton:pressed { background-color: #303030 }"
                           "QPushButton#monthLabel { font-size: 25px; color: #DBDBDB; padding: 10px }")

        self.show()

    def backward(self):
        # Rollover to the previous year if necessary
        if self.month - 1 < 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1

        self.refresh()

    def forward(self):
        # Rollover to the next year if necessary
        if self.month + 1 > 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1

        self.refresh()

    def refresh(self):
        self.gridWidget.setMonth(calendar.monthcalendar(self.year, self.month))
        self.monthLabel.setText(calendar.month_name[self.month] + ", " + str(self.year))

    def resetMonth(self):
        if self.month != date.today().month or self.year != date.today().year:
            self.month = date.today().month
            self.year = date.today().year
            self.refresh()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Paion(date.today().month, date.today().year)
    sys.exit(app.exec_())
