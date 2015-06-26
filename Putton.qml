/*************************** Copyrights and License ******************************
*                                                                                *
* This file is part of Paion. http://github.com/JamesWrigley/paion/              *
*                                                                                *
* Paion is free software: you can redistribute it and/or modify it under         *
* the terms of the GNU General Public License as published by the Free Software  *
* Foundation, either version 3 of the License, or (at your option) any later     *
* version.                                                                       *
*                                                                                *
* Paion is distributed in the hope that it will be useful, but WITHOUT ANY       *
* WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS      *
* FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. *
*                                                                                *
* You should have received a copy of the GNU General Public License along with   *
* Paion. If not, see <http://www.gnu.org/licenses/>.                             *
*                                                                                *
*********************************************************************************/

import QtQuick 2.4
import QtQuick.Layouts 1.1

Rectangle {
    width: 30
    height: 30
    color: baseColor
    Layout.fillWidth: true

    property string iconPath
    property color baseColor: "grey"

    signal mouseReleased()

    Image {
        z: 1
        anchors.centerIn: parent
        source: iconPath
    }

    MouseArea {
        hoverEnabled: true
        anchors.fill: parent

        property color hoveredColor: Qt.darker(baseColor, 1.1)

        onExited: { parent.color = parent.baseColor }
        onEntered: { parent.color = hoveredColor }
        onReleased: { mouseReleased(); parent.color = hoveredColor }
        onPressed: { parent.color = Qt.darker(parent.color, 1.2) }
    }
}
