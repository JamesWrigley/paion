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

Item {
    anchors.fill: parent

    property string labelText
    readonly property string text: input.text

    ColumnLayout {
        anchors.fill: parent

        Text {
            id: label

            anchors.leftMargin: 10
            anchors.left: parent.left
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignTop

            text: labelText
        }

        Rectangle {
            height: input.height + 10

            anchors.left: label.left
            anchors.topMargin: 5
            anchors.top: label.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            Layout.alignment: Qt.AlignTop
            Layout.preferredHeight: height
            Layout.preferredWidth: parent.width

            color: ma.containsMouse || input.cursorVisible ? "#F1F1F1" : "lightgrey"

            MouseArea {
                id: ma
                hoverEnabled: true
                anchors.fill: input
            }

            TextInput {
                id: input

                anchors.leftMargin: 5
                anchors.rightMargin: 5
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.verticalCenter: parent.verticalCenter

                selectByMouse: true
                wrapMode: TextInput.Wrap 
                selectionColor: "steelblue"

                onEditingFinished: { parent.forceActiveFocus() }
            }
        }
    }
}