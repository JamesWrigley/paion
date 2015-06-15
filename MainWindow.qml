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
import QtQuick.Window 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.3

ApplicationWindow {
    id: window
    visible: true
    visibility: "Maximized"

    toolBar: PoolBar { }

    SplitView {
        anchors.fill: parent
        orientation: Qt.Horizontal

        Rectangle {
            id: calendarPanel
            width: Screen.desktopAvailableWidth / 1.3
            Layout.minimumWidth: Screen.desktopAvailableWidth / 2
            color: "gray"
        }

        Rectangle {
            id: propertiesPanel
            Layout.maximumWidth: Screen.desktopAvailableWidth / 2
            Layout.minimumWidth: Screen.desktopAvailableWidth / 6
            Layout.fillWidth: true
            color: "lightgray"
        }
    }
}