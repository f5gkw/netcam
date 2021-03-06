from NetCam import *

if __name__ == "__main__":
    # netCam = NetCam(display='VGA', ip='135.12.187.203', port='52549')
    # netCam = NetCam(display='VGA', ip='135.19.113.126', port='5557')
    # netCam = NetCam(display='VGA', ip='192.168.1.89', port='5557')
    netCam = NetCam(display='VGA', ip='192.168.1.247', port='5557', isStereoCam=True)
    netCam.invertVertical()
    # netCam2 = NetCam(display='VGA', ip='135.12.187.203', port='5557')

    # netCam.invertVertical()

    try:
        while netCam.isRunning():
            netCam.display()
            # netCam2.display()

    except KeyboardInterrupt:
        netCam.clearAll()
        # netCam2.clearAll()

    except Exception as err:
        netCam.clearAll()
        # netCam2.clearAll()

    exit()
