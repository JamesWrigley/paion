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
from datetime import date
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

class Paion():
    dates = []
    month = -1
    year = -1

    def __init__(self, initialMonth, initialYear):
        assert type(initialMonth) == int and type(initialYear) == int

        self.month = initialMonth
        self.year = initialYear
        self.createDatesList()

        app = QApplication(sys.argv)

        self.engine = QQmlApplicationEngine()
        self.resetProperties()
        self.engine.load("MainWindow.qml")

        rootObject = self.engine.rootObjects()[0]
        rootObject.forward.connect(self.forward)
        rootObject.backward.connect(self.backward)

        app.exec()

    def createDatesList(self):
        self.dates = [day for week in calendar.monthcalendar(self.year, self.month) for day in week]

    def resetProperties(self):
        self.engine.rootContext().setContextProperty("calendarModel", self.dates)
        self.engine.rootContext().setContextProperty("currentMonth", calendar.month_name[self.month] + ", " + str(self.year))        

    def forward(self):
        # Rollover to the next year if necessary
        if self.month + 1 > 12:
            self.month = 1
            self.year += 1
        else:
            self.month += 1

        self.createDatesList()
        self.resetProperties()

    def backward(self):
        if self.month - 1 < 1:
            self.month = 12
            self.year -= 1
        else:
            self.month -= 1

        self.createDatesList()
        self.resetProperties()


if __name__ == "__main__":
    window = Paion(date.today().month, date.today().year)
