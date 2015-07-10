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
from PyQt5.QtWidgets import QLabel, QScrollArea, QTextEdit, QVBoxLayout, QWidget, QLayout, QSizePolicy

"""
A subclass of QTextEdit that dynamically resizes its height to the
height of its contents.
Methods of note:
 - EventField(), the constructor
"""
class EventField(QTextEdit):
    def __init__(self):
        super().__init__()

        self.document().contentsChanged.connect(self.resize)
        self.setMaximumHeight(self.fontMetrics().height() + 8)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def resize(self):
        currentHeight = self.document().size().height()
        self.setMinimumHeight(currentHeight)
        self.setMaximumHeight(currentHeight)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resize()


"""
The widget that contains/displays all fields for events.
Methods of note:
 - EventPanel(), the constructor
 - clear(), clear all the fields
"""
class EventPanel(QScrollArea):
    nameField = None
    locationField = None
    descriptionField = None

    def __init__(self):
        super().__init__()

        nameLabel = QLabel("Name")
        self.nameField = EventField()

        locationLabel = QLabel("Location")
        self.locationField = EventField()

        descriptionLabel = QLabel("Description")
        self.descriptionField = EventField()

        mainVbox = QVBoxLayout()
        mainVbox.setSizeConstraint(QLayout.SetMinAndMaxSize)
        mainVbox.addWidget(nameLabel)
        mainVbox.addWidget(self.nameField)
        mainVbox.addSpacing(20)
        mainVbox.addWidget(locationLabel)
        mainVbox.addWidget(self.locationField)
        mainVbox.addSpacing(20)
        mainVbox.addWidget(descriptionLabel)
        mainVbox.addWidget(self.descriptionField)
        mainVbox.addStretch()

        mainWidget = QWidget()
        mainWidget.setLayout(mainVbox)
        mainWidget.setObjectName("eventPanelWidget")
        self.setStyleSheet("QTextEdit { background: #DBDBDB }"
                           "QLabel { color: #DBDBDB; font-size: 17px }"
                           "QScrollBar { background: #333333 }"
                           "QScrollBar::handle { background: #636363 }"
                           "QScrollBar::handle:hover { background: #737373 }"
                           "QScrollBar::up-arrow, QScrollBar::down-arrow, "
                           "QScrollBar::left-arrow, QScrollBar::right-arrow, "
                           "QScrollBar::sub-line, QScrollBar::add-line { background: transparent }")

        self.setWidget(mainWidget)
        self.setWidgetResizable(True)

    def clear(self):
        self.nameField.clear()
        self.locationField.clear()
        self.descriptionField.clear()
