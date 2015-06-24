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

    signal forward()
    signal backward()

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

    toolBar: Rectangle {
        height: 40
        color: "#FFA49B"
        anchors.fill: parent

        RowLayout {
            spacing: 100
            anchors.centerIn: parent

            Image {
                source: "icons/previous.svg"

                MouseArea {
                    anchors.fill: parent
                    onClicked: { backward() }
                }
            }

            Rectangle {
                anchors.centerIn: parent

                Text {
                    anchors.centerIn: parent
                    text: currentMonth
                }
            }

            Image {
                source: "icons/next.svg"

                MouseArea {
                    anchors.fill: parent
                    onClicked: { forward() }
                }
            }
        }
    }

    SplitView {
        anchors.fill: parent
        orientation: Qt.Horizontal

        Rectangle {
            id: calendarPanel
            color: "grey"
            width: Screen.desktopAvailableWidth / 1.3
            Layout.minimumWidth: Screen.desktopAvailableWidth / 2

            ListView {
                id: daysView
                height: 30
                model: daysModel
                z: 1 // Force this to be drawn on top

                interactive: false
                orientation: "Horizontal"
                anchors.left: parent.left
                anchors.right: parent.right
                Layout.alignment: Qt.AlignTop

                delegate: Rectangle {
                    color: "#E68B77"
                    height: parent.height
                    width: calendarPanel.width / 7

                    Text {
                        anchors.centerIn: parent

                        text: modelData
                        color: "white"
                    }
                }
            }

            Flickable {
                anchors.margins: 5
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: daysView.bottom
                anchors.bottom: parent.bottom

                contentWidth: calendarGrid.width
                contentHeight: calendarGrid.height

                flickableDirection: Flickable.VerticalFlick

                Grid {
                    id: calendarGrid
                    columns: 7
                    spacing: 5

                    Repeater {
                        model: calendarModel

                        delegate: Rectangle {
                            color: modelData === 0 ? "#39B286" : "#84FFD2"
                            height: calendarPanel.height / 5
                            width: (calendarPanel.width / 7) - calendarGrid.spacing - .5

                            Text {
                                anchors.centerIn: parent
                                text: modelData === 0 ? "" : modelData
                            }
                        }
                    }
                }
            }
        }

        Rectangle {
            id: propertiesPanel
            color: "#B25945"

            Layout.maximumWidth: Screen.desktopAvailableWidth / 2
            Layout.minimumWidth: Screen.desktopAvailableWidth / 6
            Layout.fillWidth: true
        }
    }
}