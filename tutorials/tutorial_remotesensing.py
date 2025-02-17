"""
    msui.tutorials.tutorial_remotesensing
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This python script generates an automatic demonstration of how to work with remote sensing tool in topview.
    This file is part of MSS.

    :copyright: Copyright 2021 Hrithik Kumar Verma
    :copyright: Copyright 2021-2022 by the MSS team, see AUTHORS.
    :license: APACHE-2.0, see LICENSE for details.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import pyautogui as pag

from sys import platform
from pyscreeze import ImageNotFoundException
from tutorials.utils import platform_keys, start, finish
from tutorials.pictures import picture


def automate_rs():
    """
    This is the main automating script of the MSS remote sensing tutorial which will be recorded and saved
    to a file having dateframe nomenclature with a .mp4 extension(codec).
    """
    # Giving time for loading of the MSS GUI.
    pag.sleep(10)

    ctrl, enter, win, alt = platform_keys()

    # Maximizing the window
    try:
        pag.hotkey('ctrl', 'command', 'f') if platform == 'darwin' else pag.hotkey(win, 'up')
    except Exception:
        print("\nException : Enable Shortcuts for your system or try again!")
    pag.sleep(2)
    pag.hotkey('ctrl', 'h')
    pag.sleep(3)

    # Opening Remote Sensing dockwidget
    try:
        x, y = pag.locateCenterOnScreen(picture('wms', 'selecttoopencontrol.png'))
        pag.click(x, y, interval=2)
        pag.sleep(1)
        pag.press('down', presses=3, interval=1)
        pag.sleep(1)
        pag.press(enter)
        pag.sleep(2)
    except (ImageNotFoundException, OSError, Exception):
        print("\nException :\'select to open control\' button/option not found on the screen.")
        raise

    # Adding waypoints for demonstrating remote sensing
    try:
        x, y = pag.locateCenterOnScreen(picture('wms', 'add_waypoint.png'))
        pag.click(x, y, interval=2)
        pag.move(-50, 150, duration=1)
        pag.click(interval=2)
        pag.sleep(1)
        pag.move(65, 65, duration=1)
        pag.click(interval=2)
        pag.sleep(1)

        pag.move(-150, 30, duration=1)
        pag.click(interval=2)
        pag.sleep(1)
        pag.move(200, 150, duration=1)
        pag.click(interval=2)
        pag.sleep(2)
    except (ImageNotFoundException, OSError, Exception):
        print("\nException : Add waypoint button in topview not found on the screen.")
        raise

    # Showing Solar Angle Colors
    try:
        x, y = pag.locateCenterOnScreen(picture('remotesensing', 'showangle.png'))
        pag.sleep(1)
        pag.click(x, y, duration=2)
        pag.sleep(1)

        for _ in range(2):
            pag.click(x + 100, y, duration=1)
            pag.press('down', interval=1)
            pag.sleep(1)
            pag.press(enter, interval=1)
            pag.sleep(2)

        for _ in range(3):
            pag.click(x + 200, y, duration=1)
            pag.press('down', interval=1)
            pag.sleep(1)
            pag.press(enter, interval=1)
            pag.sleep(2)

        pag.click(x + 200, y, duration=1)
        pag.press('up', presses=3, interval=1)
        pag.sleep(1)
        pag.press(enter, interval=1)
        pag.sleep(2)
    except (ImageNotFoundException, OSError, Exception):
        print("\nException :\'Show angle\' checkbox not found on the screen.")
        raise

    # Changing azimuth angles
    try:
        x, y = pag.locateCenterOnScreen(picture('remotesensing', 'azimuth.png'))
        pag.click(x + 70, y, duration=1)
        azimuth_x, azimuth_y = pag.position()
        pag.sleep(2)
        pag.hotkey(ctrl, 'a')
        pag.sleep(2)
        pag.typewrite('45', interval=1)
        pag.press(enter)
        pag.sleep(3)
        pag.click(duration=1)
        pag.hotkey(ctrl, 'a')
        pag.typewrite('90', interval=1)
        pag.press(enter)
        pag.sleep(3)
    except (ImageNotFoundException, OSError, Exception):
        print("\nException :\'Azimuth\' spinbox not found on the screen.")
        raise

    # Changing elevation angles
    try:
        x, y = pag.locateCenterOnScreen(picture('remotesensing', 'elevation.png'))
        pag.click(x + 70, y, duration=1)
        pag.sleep(2)
        pag.hotkey(ctrl, 'a')
        pag.sleep(2)
        pag.typewrite('-1', interval=1)
        pag.press(enter)
        pag.sleep(3)
        pag.click(duration=1)
        pag.hotkey(ctrl, 'a')
        pag.typewrite('-3', interval=1)
        pag.press(enter)
        pag.sleep(3)
    except (ImageNotFoundException, OSError, Exception):
        print("\nException :\'Elevation\' spinbox not found on the screen.")
        raise

    # Drawing tangents to the waypoints and path
    try:
        x, y = pag.locateCenterOnScreen(picture('remotesensing', 'drawtangent.png'))
        pag.click(x, y, duration=1)
        pag.sleep(2)
        # Changing color of tangents
        pag.click(x + 160, y, duration=1)
        pag.sleep(1)
        pag.press(enter)
        pag.sleep(1)

        # Changing Kilometers of the tangent distance
        pag.click(x + 250, y, duration=1)
        pag.sleep(1)
        pag.hotkey(ctrl, 'a')
        pag.sleep(1)
        pag.typewrite('20', interval=1)
        pag.press(enter)
        pag.sleep(3)

        # Zooming into the map
        try:
            x, y = pag.locateCenterOnScreen(picture('wms', 'zoom.png'))
            pag.click(x, y, interval=2)
            pag.move(0, 150, duration=1)
            pag.dragRel(230, 150, duration=2)
            pag.sleep(5)
        except ImageNotFoundException:
            print("\n Exception : Zoom button could not be located on the screen")
            raise

        # Rotating the tangent through various angles
        try:
            pag.click(azimuth_x, azimuth_y, duration=1)
            pag.sleep(1)
            pag.hotkey(ctrl, 'a')
            pag.sleep(1)
            pag.typewrite('120', interval=0.5)
            pag.sleep(2)
            for _ in range(10):
                pag.press('down')
                pag.sleep(2)
            pag.sleep(1)
            pag.click(azimuth_x + 500, y, duration=1)
            pag.sleep(1)
        except UnboundLocalError:
            print('Azimuth spinbox coordinates are not stored. Hence cannot change values.')
            raise
    except (ImageNotFoundException, OSError, Exception):
        print("\nException :\'Tangent\' checkbox not found on the screen.")
        raise

    print("\nAutomation is over for this tutorial. Watch next tutorial for other functions.")
    finish()


if __name__ == '__main__':
    start(target=automate_rs, duration=198)
