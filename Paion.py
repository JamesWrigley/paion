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
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlEngine, QQmlComponent

if __name__ == "__main__":
    currentMonth = calendar.monthcalendar(date.today().year, date.today().month)

    app = QApplication(sys.argv)
    engine = QQmlEngine()
    windowComponent = QQmlComponent(engine)
    windowComponent.loadUrl(QUrl("MainWindow.qml"))

    window = windowComponent.create()
    window.show()
    app.exec()
