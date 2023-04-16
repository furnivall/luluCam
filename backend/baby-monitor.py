import asyncio
import cv2
import numpy as np
from aiortc import RTCPeerConnection, RTCSessionDescription, VideoStreamTrack
from aiortc.contrib.media import MediaPlayer
from picamera import PiCamera
from picamera.array import PiRGBArray

class CameraVideoStreamTrack(VideoStreamTrack):
    def __init__(self):
        super().__init__()  # Don't forget to call the superclass constructor
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 30
        self.raw_capture = PiRGBArray(self.camera, size=(640, 480))

    async def recv(self):
        self.camera.capture(self.raw_capture, format="bgr", use_video_port=True)
        frame = self.raw_capture.array
        self.raw_capture.truncate(0)

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = cv2.Canny(img, 100, 200)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        return img

async def run(pc):
    # Set up a video track using the camera
    local_video = CameraVideoStreamTrack()
    pc.addTrack(local_video)

    # Connect to the signaling server
    async with websockets.connect("ws://localhost:8765") as websocket:
        # Wait for remote SDP
        remote_sdp = await websocket.recv()
        remote_sdp = json.loads(remote_sdp)
        remote_sdp = RTCSessionDescription(sdp=remote_sdp["sdp"], type=remote_sdp["type"])
        await pc.setRemoteDescription(remote_sdp)

        # Create and send local SDP
        answer = await pc.createAnswer()
        await pc.setLocalDescription(answer)
        await websocket.send(json.dumps({"sdp": answer.sdp, "type": answer.type}))

        # Wait for connection to close
        await pc.waitTransportsClosed()

async def main():
    pc = RTCPeerConnection()
    try:
        await run(pc)
    finally:
        await pc.close()

if __name__ == "__main__":
    asyncio.run(main())

