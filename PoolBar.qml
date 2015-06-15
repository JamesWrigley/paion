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
import QtQuick.Controls 1.3

ToolBar {
    RowLayout {
        spacing: 100
        anchors.centerIn: parent

        Image {
            source: "icons/previous.svg"
        }

        Rectangle {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter

            Text {
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                text: "Month"
            }
        }

        Image {
            source: "icons/next.svg"
        }
    }
}