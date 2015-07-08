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

from PyQt5.QtWidgets import QLabel, QWidget, QTextEdit, QVBoxLayout

class EventPanel(QWidget):
    def __init__(self):
        super().__init__()

        nameLabel = QLabel("Name")
        nameField = QTextEdit()

        locationLabel = QLabel("Location")
        locationField = QTextEdit()

        descriptionLabel = QLabel("Description")
        descriptionField = QTextEdit()

        self.setStyleSheet("QLabel { color: #DBDBDB; font-size: 17px } QTextEdit { background: #DBDBDB }")

        mainVbox = QVBoxLayout()
        mainVbox.addWidget(nameLabel)
        mainVbox.addWidget(nameField)
        mainVbox.addStretch()
        mainVbox.addWidget(locationLabel)
        mainVbox.addWidget(locationField)
        mainVbox.addStretch()
        mainVbox.addWidget(descriptionLabel)
        mainVbox.addWidget(descriptionField)
        mainVbox.addStretch()

        self.setLayout(mainVbox)
