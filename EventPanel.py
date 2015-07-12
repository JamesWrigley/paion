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

from PyQt5.QtCore import Qt, QTime
from PyQt5.QtWidgets import (QLabel, QScrollArea, QTextEdit, QVBoxLayout, QWidget,
                             QLayout, QSizePolicy, QGroupBox, QTimeEdit,
                             QHBoxLayout, QPushButton)

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
 - delete(), deletes the current event
"""
class EventPanel(QScrollArea):
    nameField = None
    locationField = None
    notesField = None
    durationGroupBox = None
    fromField = None
    toField = None

    def __init__(self):
        super().__init__()

        addButton = QPushButton("Add")
        deleteButton = QPushButton("Delete")
        deleteButton.clicked.connect(self.delete)
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(addButton)
        buttonLayout.addWidget(deleteButton)

        nameLabel = QLabel("Name")
        self.nameField = EventField()

        locationLabel = QLabel("Location")
        self.locationField = EventField()

        notesLabel = QLabel("Notes")
        self.notesField = EventField()

        self.durationGroupBox = QGroupBox("All Day")
        self.fromField = QTimeEdit(QTime(12, 0))
        toLabel = QLabel("to")
        self.toField = QTimeEdit(QTime(13, 0))
        durationGroupBoxLayout = QHBoxLayout()
        durationGroupBoxLayout.addWidget(self.fromField, 0, Qt.AlignLeft)
        durationGroupBoxLayout.addWidget(toLabel, 0, Qt.AlignHCenter)
        durationGroupBoxLayout.addWidget(self.toField, 0, Qt.AlignRight)
        self.durationGroupBox.setLayout(durationGroupBoxLayout)
        self.durationGroupBox.setCheckable(True)
        self.durationGroupBox.setChecked(True)

        spacing = 20
        mainVbox = QVBoxLayout()
        mainVbox.setSizeConstraint(QLayout.SetMinAndMaxSize)
        mainVbox.addLayout(buttonLayout)
        mainVbox.addSpacing(spacing)
        mainVbox.addWidget(nameLabel)
        mainVbox.addWidget(self.nameField)
        mainVbox.addSpacing(spacing)
        mainVbox.addWidget(locationLabel)
        mainVbox.addWidget(self.locationField)
        mainVbox.addSpacing(spacing)
        mainVbox.addWidget(notesLabel)
        mainVbox.addWidget(self.notesField)
        mainVbox.addSpacing(spacing)
        mainVbox.addWidget(self.durationGroupBox)
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
                           "QScrollBar::sub-line, QScrollBar::add-line { background: transparent }"

                           "QGroupBox { background-color: #3C3C3C; font-size: 17px; padding-top: 3ex; outline: 0 }"
                           "QGroupBox::title { color: #DBDBDB }"
                           "QGroupBox::indicator { background-color: grey }"
                           "QGroupBox::indicator:unchecked { image: url(icons/check.svg) }"

                           "QTimeEdit { background-color: #DBDBDB; border: 7 solid #DBDBDB }"
                           "QTimeEdit::up-button, QTimeEdit::down-button { margin-right: 5px }"
                           "QTimeEdit::up-button { image: url(icons/up-arrow.svg) }"
                           "QTimeEdit::down-button { image: url(icons/down-arrow.svg) }"
                           "QTimeEdit::up-button:disabled { image: url(icons/up-arrow-disabled.svg) }"
                           "QTimeEdit::down-button:disabled { image: url(icons/down-arrow-disabled.svg) }"

                           "QPushButton { border: 1px solid #424242; color: #DBDBDB; font-size: 20px }")

        self.setWidget(mainWidget)
        self.setWidgetResizable(True)

    def clear(self):
        self.nameField.clear()
        self.locationField.clear()
        self.notesField.clear()
        self.durationGroupBox.setChecked(True)
        self.fromField.setTime(QTime(12, 0))
        self.toField.setTime(QTime(13, 0))

    # Unfinished
    def delete(self):
        self.clear()
