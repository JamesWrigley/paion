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

from Event import Event
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QFrame, QLabel, QWidget, QGridLayout, QScrollArea, QVBoxLayout

"""
A class that represents each cell of CalendarGrid.
Methods of note:
 - Day(str/int), the constructor, which takes in either a string or int to display
"""
class Day(QFrame):
    isNull = False
    isSelected = False
    defaultStylesheet = ""
    enteredStylesheet = ""
    selectedStylesheet = ""
    selected = pyqtSignal(QFrame)
    scrollArea = None

    def __init__(self, day):
        assert type(day) == int or type(day) == str
        super().__init__()

        self.isNull = str(day) == "0"
        dayLabel = QLabel("" if self.isNull else str(day))

        mainLayout = QVBoxLayout()
        mainLayout.setAlignment(Qt.AlignCenter)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.addWidget(dayLabel)

        eventsWidget = QWidget()
        eventsLayout = QVBoxLayout()
        eventsLayout.addWidget(Event("The Great Quux"))
        eventsLayout.addWidget(Event("Fedora 15 ate my dingoes baby"))
        eventsWidget.setLayout(eventsLayout)

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidget(eventsWidget)
        self.scrollArea.setWidgetResizable(True)

        mainLayout.addWidget(self.scrollArea)

        backgroundColor = "#319973" if self.isNull else "#6ED5AF"
        scrollBarStyle = ("QScrollBar { background: #333333 }"
                          "QScrollBar::handle { background: #636363 }"
                          "QScrollBar::handle:hover { background: #737373 }"
                          "QScrollBar::up-arrow, QScrollBar::down-arrow, "
                          "QScrollBar::left-arrow, QScrollBar::right-arrow, "
                          "QScrollBar::sub-line, QScrollBar::add-line { background: transparent }")

        self.defaultStylesheet = ("QWidget {{ background: {0}; font-size: 18px }}".format(backgroundColor) +
                                  scrollBarStyle)
        self.enteredStylesheet = "QWidget { background: #84FFD2; font-size: 18px }" + scrollBarStyle
        self.selectedStylesheet = "QWidget { background: #FFAAAA; font-size: 18px }" + scrollBarStyle
        self.setStyleSheet(self.defaultStylesheet)

        self.setLayout(mainLayout)

    def enterEvent(self, event):
        if not self.isNull and not self.isSelected:
            self.setStyleSheet(self.enteredStylesheet)

    def leaveEvent(self, event):
        if not self.isNull and not self.isSelected:
            self.setStyleSheet(self.defaultStylesheet)

    def mousePressEvent(self, event):
        if not self.isNull:
            self.isSelected = not self.isSelected

            if self.isSelected:
                self.setStyleSheet(self.selectedStylesheet)
                self.selected.emit(self)

    def mouseReleaseEvent(self, event):
        if not self.isNull and not self.isSelected:
            self.enterEvent(None)


"""
A class that contains the QGridLayout holding all the Day's.
Methods of note:
 - CalendarGrid(), the constructor
 - setMonth(), takes in a list of weeks and applies it to the grid
"""
class CalendarGrid(QWidget):
    currentDay = -1
    monthModel = []
    mainLayout = None

    def __init__(self):
        super().__init__()

        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)

    def onSelectionChanged(self, day):
        dayIndex = self.mainLayout.indexOf(day)
        if self.currentDay != -1 and dayIndex != self.currentDay:
            self.monthModel[self.currentDay].isSelected = False
            self.monthModel[self.currentDay].leaveEvent(None)

        self.currentDay = dayIndex

    def setMonth(self, month):
        assert all(type(week) == list for week in month)

        # Clear the grid and the month model
        while self.mainLayout.count():
            self.mainLayout.itemAt(self.mainLayout.count() - 1).widget().setParent(None)
        self.monthModel.clear()

        for i, week in enumerate(month):
            for j, day in enumerate(week):
                cell = Day(day)
                self.monthModel.append(cell)
                cell.selected.connect(self.onSelectionChanged)
                self.mainLayout.addWidget(cell, i, j)
