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
import QtQml.Models 2.1
import QtQuick.Window 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.3

ApplicationWindow {
    id: window
    visible: true
    width: Screen.desktopAvailableWidth
    height: Screen.desktopAvailableHeight

    ListModel {
        id: daysModel

        ListElement { name: "Monday" }
        ListElement { name: "Tuesday" }
        ListElement { name: "Wednesday" }
        ListElement { name: "Thursday" }
        ListElement { name: "Friday" }
        ListElement { name: "Saturday" }
        ListElement { name: "Sunday" }
    }

    toolBar: PoolBar { }

    SplitView {
        anchors.fill: parent
        orientation: Qt.Horizontal

        Rectangle {
            id: calendarPanel
            width: Screen.desktopAvailableWidth / 1.3
            Layout.minimumWidth: Screen.desktopAvailableWidth / 2
            color: "grey"

            ColumnLayout {
                anchors.fill: parent
                spacing: 5

                ListView {
                    z: 1 // Force this to be drawn on top
                    id: daysView
                    anchors.left: parent.left
                    anchors.right: parent.right
                    height: 30
                    model: daysModel
                    Layout.alignment: Qt.AlignTop
                    orientation: "Horizontal"

                    delegate: Rectangle {
                        width: (calendarPanel.width / 7)
                        height: parent.height
                        border.width: 1
                        color: "#FF9A84"

                        Text {
                            anchors.centerIn: parent
                            text: modelData
                            color: "white"
                        }
                    }
                }

                GridView {
                    id: calendarView
                    anchors.top: daysView.bottom
                    anchors.topMargin: 5
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.bottom: parent.bottom
                    model: calendarModel

                    cellWidth: calendarPanel.width / 7
                    cellHeight: calendarPanel.height / 5

                    delegate: Rectangle {
                        width: calendarView.cellWidth - 2
                        height: calendarView.cellHeight - 2
                        border.width: modelData === 0 ? 1 : 2
                        color: modelData === 0 ? "#39B286" : "#84FFD2"

                        Text {
                            anchors.centerIn: parent
                            text: modelData === 0 ? "" : modelData
                        }
                    }
                }
            }
        }

        Rectangle {
            id: propertiesPanel
            Layout.maximumWidth: Screen.desktopAvailableWidth / 2
            Layout.minimumWidth: Screen.desktopAvailableWidth / 6
            Layout.fillWidth: true
            color: "#B25945"
        }
    }
}